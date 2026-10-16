(define (domain grid)
(:requirements :strips :typing)
  (:types 
    place key shape - object     
  )		

(:predicates (conn ?x - place ?y - place)
             (key-shape ?k - key ?s - shape)
             (lock-shape ?x - place ?s - shape)
             (at ?r - key ?x - place )
	     (at-robot ?x - place)
        ;      (place ?p)
        ;      (key ?k)
        ;      (shape ?s)
             (locked ?x - place)
             (holding ?k - key)
             (open ?x - place)
             (arm-empty ))



(:action unlock
:parameters (?curpos - place ?lockpos - place ?key - key ?shape - shape)
:precondition (and 
; (place ?curpos) (place ?lockpos) (key ?key) (shape ?shape)
          (conn ?curpos ?lockpos) (key-shape ?key ?shape)
                   (lock-shape ?lockpos ?shape) (at-robot ?curpos) 
                   (locked ?lockpos) (holding ?key))
:effect (and  (open ?lockpos) (not (locked ?lockpos))))


(:action move
:parameters (?curpos - place ?nextpos - place)
:precondition (and 
; (place ?curpos) (place ?nextpos)
               (at-robot ?curpos) (conn ?curpos ?nextpos) (open ?nextpos))
:effect (and (at-robot ?nextpos) (not (at-robot ?curpos))))

(:action pickup
:parameters (?curpos - place ?key - key)
:precondition (and 
; (place ?curpos) (key ?key) 
                  (at-robot ?curpos) (at ?key ?curpos) (arm-empty ))
:effect (and (holding ?key)
   (not (at ?key ?curpos)) (not (arm-empty ))))


(:action pickup-and-loose
:parameters (?curpos - place ?newkey - key ?oldkey - key)
:precondition (and 
; (place ?curpos) (key ?newkey) (key ?oldkey)
                  (at-robot ?curpos) (holding ?oldkey) (at ?newkey ?curpos))
:effect (and (holding ?newkey) (at ?oldkey ?curpos)
        (not (holding ?oldkey)) (not (at ?newkey ?curpos))))

(:action putdown
:parameters (?curpos - place ?key - key)
:precondition (and 
; (place ?curpos) (key ?key) 
                  (at-robot ?curpos) (holding ?key))
:effect (and (arm-empty ) (at ?key ?curpos) (not (holding ?key)))))


	
