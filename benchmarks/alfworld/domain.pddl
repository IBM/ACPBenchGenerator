;; Specification in PDDL of the Alfred domain
;; Intended to be used with Fast Downward which supports PDDL 2.2 level 1 plus the :action-costs requirement from PDDL 3.1.
;; Modified and simplified version

(define (domain alfred)
 (:requirements
    :adl
    :action-costs
    :typing
 ) 
 (:types
  agent
  location
  objectorreceptacle
  rtype
  otype - object
  receptacle - objectorreceptacle
  )

 (:constants 
	knifetype - otype
        sinktype - otype
        butterknifetype - otype
	sinkbasintype - rtype
        microwavetype - rtype
        fridgetype - rtype
 )

 (:predicates
    (atlocation ?a - agent ?l - location)                     ; true if the agent is at the location
    (receptacleatlocation ?r - receptacle ?l - location)      ; true if the receptacle is at the location (constant)
    (objectatlocation ?o - object ?l - location)              ; true if the object is at the location
    (openable ?r - receptacle)                                ; true if a receptacle is openable
    (opened ?r - receptacle)                                  ; true if a receptacle is opened
    (inreceptacle ?o - object ?r - objectorreceptacle)                ; object ?o is in receptacle ?r
    (checked ?r - receptacle)                                 ; whether the receptacle has been looked inside/visited
    (receptacletype ?r - receptacle ?t - rtype)               ; the type of receptacle (cabinet vs cabinet|01|2...)
    (cancontain ?rt - rtype ?ot - otype)                      ; true if receptacle can hold object
    (objecttype ?o - object ?t - otype)                       ; the type of object (apple vs apple|01|2...)
    (holds ?a - agent ?o - object)                            ; object ?o is held by agent ?a
    (handempty ?a - agent)                                    ;;; (holdsany ?a - agent)        ; agent ?a holds an object
    (isclean ?o - object)                                     ; true if the object has been clean in sink
    (cleanable ?o - object)                                   ; true if the object can be placed in a sink
    (ishot ?o - object)                                       ; true if the object has been heated up
    (heatable ?o - object)                                    ; true if the object can be heated up in a microwave
    (iscool ?o - object)                                      ; true if the object has been cooled
    (coolable ?o - object)                                    ; true if the object can be cooled in the fridge
    (pickupable ?o - object)                                   ; true if the object can be picked up
    (toggleable ?o - object)                                  ; true if the object can be turned on/off
    (ison ?o - object)                                        ; true if the object is on
    (istoggled ?o - object)                                   ; true if the object has been toggled
    (sliceable ?o - object)                                   ; true if the object can be sliced
    (issliced ?o - object)                                    ; true if the object is sliced


    (validatepickandplace ?ot - otype ?rt - rtype)
    (validateexamineinlight ?otogglet - otype ?ot - otype ) 
    (validatecleanandplace ?ot - otype ?rt - rtype) 
    (validateheatandplace ?ot - otype ?rt - rtype)
    (validatecoolandplace ?ot - otype ?rt - rtype)
    (validatepicktwoandplace  ?ot - otype  ?rt - rtype)
    (notvalidated)

    (closed ?r - receptacle)
    (isoff ?o - object)                                        ; true if the object is off
    (notopenable ?r - receptacle)
 )

;   (:functions
;    )

;; all actions are specified such that the final arguments are the ones used
;; for performing actions in unity.


;; agent goes to receptacle
 (:action go_to_location
    :parameters (?a - agent ?lstart - location ?lend - location ?r - receptacle)
    :precondition (and
                    (atlocation ?a ?lstart)
                    (receptacleatlocation ?r ?lend)
                    (not (= ?lstart ?lend))
                    (notvalidated)
                  )
    :effect (and    
                (not (atlocation ?a ?lstart))
                (atlocation ?a ?lend)
                
            )
 )

;; agent opens receptacle
 (:action open_receptacle
    :parameters (?a - agent ?l - location ?r - receptacle)
    :precondition (and
            (openable ?r)
            (atlocation ?a ?l)
            (receptacleatlocation ?r ?l)
            (closed ?r)   ;; (not (opened ?r))
            (notvalidated)
            )
    :effect (and    
                (opened ?r) (not (closed ?r))
                (checked ?r)
                
            )
 )
;; agent closes receptacle
 (:action close_receptacle
    :parameters (?a - agent ?l - location ?r - receptacle)
    :precondition (and
            (openable ?r)
            (atlocation ?a ?l)
            (receptacleatlocation ?r ?l)
            (opened ?r)
            (notvalidated)
            )
    :effect (and    
                (not (opened ?r)) (closed ?r)
            )

 )

 ;; agent picks up object from a receptacle
 (:action pickup_object_from_not_openable_receptacle
    :parameters (?a - agent ?l - location ?o - object ?r - receptacle)
    :precondition
        (and
            (pickupable ?o)
            (atlocation ?a ?l)
            (receptacleatlocation ?r ?l)
            (inreceptacle ?o ?r)
            (handempty ?a)    ;; (not (holdsany ?a))  ; agent's hands are empty.
            (notopenable ?r)  ;; (or (not (openable ?r)) (opened ?r))  ; receptacle is opened if it is openable.
            (notvalidated)
        )
    :effect
        (and
            (not (inreceptacle ?o ?r))
            (holds ?a ?o)
            (not  (handempty ?a))    ;;(holdsany ?a)
            (not (objectatlocation ?o ?l))
        )
 )

(:action pickup_object_from_openable_receptacle
    :parameters (?a - agent ?l - location ?o - object ?r - receptacle)
    :precondition
        (and
            (pickupable ?o)
            (atlocation ?a ?l)
            (receptacleatlocation ?r ?l)
            (inreceptacle ?o ?r)
            (handempty ?a)    ;; (not (holdsany ?a))  ; agent's hands are empty.
            (openable ?r) (opened ?r)    ;; (or (not (openable ?r)) (opened ?r))  ; receptacle is opened if it is openable.
            (notvalidated)
        )
    :effect
        (and
            (not (inreceptacle ?o ?r))
            (holds ?a ?o)
            (not  (handempty ?a))    ;;(holdsany ?a)
            (not (objectatlocation ?o ?l))
        )
 )



;; agent puts down an object
 (:action put_object_on_not_openable_receptacle
    :parameters (?a - agent ?l - location ?o - object ?r - receptacle ?ot - otype ?rt - rtype)
    :precondition (and
            (holds ?a ?o)
            (atlocation ?a ?l)
            (receptacleatlocation ?r ?l)
            (notopenable ?r)  ;; (or (not (openable ?r)) (opened ?r))    ; receptacle is opened if it is openable
            (objecttype ?o ?ot)
            (receptacletype ?r ?rt)
            (cancontain ?rt ?ot)
            (notvalidated)
            )
    :effect (and    
                (inreceptacle ?o ?r)
                (objectatlocation ?o ?l)
                (not (holds ?a ?o))
                (handempty ?a) ;; (not (holdsany ?a))
                
            )
 )

 ;; agent puts down an object
 (:action put_object_in_openable_receptacle
    :parameters (?a - agent ?l - location ?o - object ?r - receptacle ?ot - otype ?rt - rtype)
    :precondition (and
            (holds ?a ?o)
            (atlocation ?a ?l)
            (receptacleatlocation ?r ?l)
            (openable ?r) (opened ?r)  ;; (or (not (openable ?r)) (opened ?r))    ; receptacle is opened if it is openable
            (objecttype ?o ?ot)
            (receptacletype ?r ?rt)
            (cancontain ?rt ?ot)
            (notvalidated)
            )
    :effect (and    
                (inreceptacle ?o ?r)
                (objectatlocation ?o ?l)
                (not (holds ?a ?o))
                (handempty ?a) ;; (not (holdsany ?a))
                
            )
 )


;; agent cleans some object
 (:action clean_object
    :parameters (?a - agent ?l - location ?r - receptacle ?o - object)
    :precondition (and
            (cleanable ?o)
            (receptacletype ?r sinkbasintype)
            (atlocation ?a ?l)
            (receptacleatlocation ?r ?l)
            (holds ?a ?o)
            (notvalidated)
            )
    :effect (and    
                (isclean ?o)
            )
 )


;; agent heats-up some object
 (:action heat_object
    :parameters (?a - agent ?l - location ?r - receptacle ?o - object)
    :precondition (and
            (heatable ?o)
            (receptacletype ?r microwavetype)
            (atlocation ?a ?l)
            (receptacleatlocation ?r ?l)
            (holds ?a ?o)
            (notvalidated)
            )
    :effect (and    
                (ishot ?o)
                (not (iscool ?o))
            )
 )

;; agent cools some object
 (:action cool_object
    :parameters (?a - agent ?l - location ?r - receptacle ?o - object)
    :precondition (and
            (coolable ?o)
            (receptacletype ?r fridgetype)
            (atlocation ?a ?l)
            (receptacleatlocation ?r ?l)
            (holds ?a ?o)
            (notvalidated)
            )
    :effect (and    
                (iscool ?o)
                (not (ishot ?o))
            )
 )


;; agent toggle object
 (:action toggle_object_off
    :parameters (?a - agent ?l - location ?o - object ?r - receptacle)
    :precondition (and
            (toggleable ?o)
            (atlocation ?a ?l)
            (receptacleatlocation ?r ?l)
            (inreceptacle ?o ?r)
            (ison ?o)
            (notvalidated)
            )
    :effect (and    
                ;;(when (ison ?o)
                (not (ison ?o)) (isoff ?o)
                ;;(when (not (ison ?o))
                ;;    (ison ?o))
                (istoggled ?o)
            )
 )

;; agent toggle object
 (:action toggle_object_on
    :parameters (?a - agent ?l - location ?o - object ?r - receptacle)
    :precondition (and
            (toggleable ?o)
            (atlocation ?a ?l)
            (receptacleatlocation ?r ?l)
            (inreceptacle ?o ?r)
            (isoff ?o)
            (notvalidated)
            )
    :effect (and    
                ;;(when (ison ?o)
                ;;    (not (ison ?o)))
                ;;(when (not (ison ?o))
                (ison ?o) (not (isoff ?o))
                (istoggled ?o)
            )
 )


;; agent slices some object with a knife
 (:action slice_object
    :parameters (?a - agent ?l - location ?co - object ?ko - object)
    :precondition
            (and
                (sliceable ?co)
                (or
                    (objecttype ?ko knifetype)
                    (objecttype ?ko butterknifetype)
                )
                (atlocation ?a ?l)
                (objectatlocation ?co ?l)
                (holds ?a ?ko)
                (notvalidated)
            )
    :effect (and    
                (issliced ?co)
            )
 )



 (:action validate_pick_and_place_in_receptacle
    :parameters           (?o - object
                          ?ot - otype
                          ?r - receptacle
                          ?rt - rtype)
    :precondition
            (and
                        (inreceptacle ?o ?r)
                        (objecttype ?o ?ot)
                        (receptacletype ?r ?rt)
                        (notvalidated)
            )
    :effect (and
                (validatepickandplace ?ot ?rt)
                (not (notvalidated))
            )
  )


  (:action validate_examine_in_light
    :parameters           (?otoggle - object
                           ?otogglet - otype
                           ?o - object
                           ?ot - otype
                           ?r - receptacle
                           ?a - agent
                           ?l - location)
    :precondition
            (and
                         (objecttype ?otoggle ?otogglet)  
                         (toggleable ?otoggle)
                         (istoggled ?otoggle)
                         (inreceptacle ?otoggle ?r)
                         (receptacleatlocation ?r ?l)

                         (holds ?a ?o)
                         (objecttype ?o ?ot)
                         (atlocation ?a ?l)

                         (notvalidated)
            )
    :effect (and
                (validateexamineinlight ?otogglet ?ot)
                (not (notvalidated))
            )
  )


 (:action validate_clean_and_place_in_receptacle
    :parameters           (?o - object
                          ?ot - otype
                          ?r - receptacle
                          ?rt - rtype)
    :precondition
            (and
                        (cleanable ?o)
                        (objecttype ?o ?ot)
                        (receptacletype ?r ?rt)
                        (isclean ?o)
                        (inreceptacle ?o ?r)
                        (notvalidated)
            )
    :effect (and
                (validatecleanandplace ?ot ?rt)
                (not (notvalidated))
            )
  )


 (:action validate_heat_and_place_in_receptacle
    :parameters           (?o - object
                          ?ot - otype
                          ?r - receptacle
                          ?rt - rtype)
    :precondition
            (and
                        (heatable ?o)
                        (objecttype ?o ?ot)
                        (receptacletype ?r ?rt)
                        (ishot ?o)
                        (inreceptacle ?o ?r)
                        (notvalidated)
            )
    :effect (and
                (validateheatandplace ?ot ?rt)
                (not (notvalidated))
            )
  )


 (:action validate_cool_and_place_in_receptacle 
    :parameters          (?o - object
                          ?ot - otype
                          ?r - receptacle
                          ?rt - rtype)
    :precondition
            (and
                        (coolable ?o)
                        (objecttype ?o ?ot)
                        (receptacletype ?r ?rt)
                        (iscool ?o)
                        (inreceptacle ?o ?r)
                        (notvalidated)
            )
    :effect (and
                (validatecoolandplace  ?ot ?rt)
                (not (notvalidated))
            )
  )


 (:action validate_pick_two_and_place_in_receptacle
    :parameters          (?o1 - object
                          ?o2 - object
                          ?ot - otype
                          ?r - receptacle
                          ?rt - rtype)
    :precondition
            (and
                        (objecttype ?o1 ?ot)
                        (objecttype ?o2 ?ot)

                        (inreceptacle ?o1 ?r)
                        (inreceptacle ?o2 ?r)

                        (not (= ?o1 ?o2))
                        
                        (receptacletype ?r ?rt)
                        (notvalidated)
            )
    :effect (and
                (validatepicktwoandplace  ?ot ?rt)
                (not (notvalidated))
            )
  )

       

)
