(define (domain ferry)
  (:requirements :strips :typing) 
  (:types 
    car location - object     
  )		

   (:predicates (not-eq ?x ?y)
		; (car ?c)
		; (location ?l)
		(at-ferry ?l - location)
		(at ?c - car ?l - location)
		(empty-ferry)
		(on ?c - car))

   (:action sail
       :parameters  (?from - location ?to - location)
       :precondition (and (not-eq ?from ?to) 
                        ;   (location ?from) (location ?to) 
                          (at-ferry ?from))
       :effect (and  (at-ferry ?to)
		     (not (at-ferry ?from))))


   (:action board
       :parameters (?car - car ?loc - location)
       :precondition  (and  
    ;    (car ?car) (location ?loc)
			    (at ?car ?loc) (at-ferry ?loc) (empty-ferry))
       :effect (and (on ?car)
		    (not (at ?car ?loc)) 
		    (not (empty-ferry))))

   (:action debark
       :parameters  (?car - car  ?loc - location)
       :precondition  (and  
    ;    (car ?car) (location ?loc)
			    (on ?car) (at-ferry ?loc))
       :effect (and (at ?car ?loc)
		    (empty-ferry)
		    (not (on ?car)))))
