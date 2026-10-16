(define (domain Rover)
(:requirements :strips :typing)
(:types Rover Waypoint Store Camera Mode Lander Objective)

(:predicates (at ?x - Rover ?y - Waypoint) 
             (at_lander ?x - Lander ?y - Waypoint)
             (can_traverse ?r - Rover ?x - Waypoint ?y - Waypoint)
	     (equipped_for_soil_analysis ?r - Rover)
             (equipped_for_rock_analysis ?r - Rover)
             (equipped_for_imaging ?r - Rover)
             (empty ?s - Store)
             (have_rock_analysis ?r - Rover ?w - Waypoint)
             (have_soil_analysis ?r - Rover ?w - Waypoint)
             (full ?s - Store)
	     (calibrated ?c - Camera ?r - Rover) 
	     (supports ?c - Camera ?m - Mode)
             (available ?r - Rover)
             (visible ?w - Waypoint ?p - Waypoint)
             (have_image ?r - Rover ?o - Objective ?m - Mode)
             (communicated_soil_data ?w - Waypoint)
             (communicated_rock_data ?w - Waypoint)
             (communicated_image_data ?o - Objective ?m - Mode)
	     (at_soil_sample ?w - Waypoint)
	     (at_rock_sample ?w - Waypoint)
             (visible_from ?o - Objective ?w - Waypoint)
	     (store_of ?s - Store ?r - Rover)
	     (calibration_target ?i - Camera ?o - Objective)
	     (on_board ?i - Camera ?r - Rover)
	     (channel_free ?l - Lander))

(:action navigate
:parameters (?x - Rover ?y - Waypoint ?z - Waypoint) 
:precondition (and (can_traverse ?x ?y ?z) (available ?x) (at ?x ?y) 
                (visible ?y ?z))
:effect (and (not (at ?x ?y)) (at ?x ?z)))

(:action sample_soil
:parameters (?x - Rover ?s - Store ?p - Waypoint)
:precondition (and (at ?x ?p) (at_soil_sample ?p) 
		   (equipped_for_soil_analysis ?x) (store_of ?s ?x) (empty ?s))
:effect (and (not (empty ?s)) (full ?s) (have_soil_analysis ?x ?p) 
	     (not (at_soil_sample ?p))))

(:action sample_rock
:parameters (?x - Rover ?s - Store ?p - Waypoint)
:precondition (and (at ?x ?p) (at_rock_sample ?p) 
	           (equipped_for_rock_analysis ?x) (store_of ?s ?x)(empty ?s))
:effect (and (not (empty ?s)) (full ?s) (have_rock_analysis ?x ?p) 
	     (not (at_rock_sample ?p))))

(:action drop
:parameters (?x - Rover ?y - Store)
:precondition (and (store_of ?y ?x) (full ?y))
:effect (and (not (full ?y)) (empty ?y)))



(:action calibrate
 :parameters (?r - Rover ?i - Camera ?t - Objective ?w - Waypoint)
 :precondition (and (equipped_for_imaging ?r) (calibration_target ?i ?t) 
	            (at ?r ?w) (visible_from ?t ?w)(on_board ?i ?r))
 :effect (calibrated ?i ?r))

(:action take_image
 :parameters (?r - Rover ?p - Waypoint ?o - Objective ?i - Camera ?m - Mode)
 :precondition (and (calibrated ?i ?r) (on_board ?i ?r) (equipped_for_imaging ?r)
                      (supports ?i ?m) (visible_from ?o ?p) (at ?r ?p))
 :effect (and (have_image ?r ?o ?m)(not (calibrated ?i ?r))))

(:action communicate_soil_data
 :parameters (?r - Rover ?l - Lander ?p - Waypoint ?x - Waypoint ?y - Waypoint)
 :precondition (and (at ?r ?x)(at_lander ?l ?y)(have_soil_analysis ?r ?p) 
                   (visible ?x ?y)(available ?r)(channel_free ?l))
 :effect (and (not (available ?r))(not (channel_free ?l))(channel_free ?l)
		(communicated_soil_data ?p)(available ?r)))

(:action communicate_rock_data
 :parameters (?r - Rover ?l - Lander ?p - Waypoint ?x - Waypoint ?y - Waypoint)
 :precondition (and (at ?r ?x)(at_lander ?l ?y)(have_rock_analysis ?r ?p)
                   (visible ?x ?y)(available ?r)(channel_free ?l))
 :effect (and (not (available ?r))(not (channel_free ?l))
	      (channel_free ?l)(communicated_rock_data ?p)(available ?r)))


(:action communicate_image_data
 :parameters (?r - Rover ?l - Lander ?o - Objective ?m - Mode 
	      ?x - Waypoint ?y - Waypoint)
 :precondition (and (at ?r ?x)(at_lander ?l ?y)(have_image ?r ?o ?m)
	            (visible ?x ?y)(available ?r)(channel_free ?l))
 :effect (and (not (available ?r))(not (channel_free ?l))(channel_free ?l)
	      (communicated_image_data ?o ?m)(available ?r)))
)
