

(define (domain hanoi)
(:requirements :strips)
(:predicates (clear ?x)
             (on ?x ?y)
             (smaller ?x ?y))

(:action move
:parameters (?disk ?from ?to)
:precondition (and (smaller ?to ?disk) 
                   (on ?disk ?from) 
                   (clear ?disk) 
                   (clear ?to))
:effect  (and (clear ?from) 
              (on ?disk ?to) 
              (not (on ?disk ?from))  
              (not (clear ?to)))
 )) 