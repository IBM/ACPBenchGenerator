;; Created by Michael Katz
;; Domain for swapping the roles of agents

(define (domain swap)
(:requirements :typing)
(:types agent role - object)

(:predicates
    (not-eq ?x ?y - object)
		(assigned ?a - agent ?r - role)
    ; (unassigned ?x - object)
)

(:action swap
  :parameters (?a1 ?a2 - agent ?r1 ?r2 - role)
  :precondition (and (assigned ?a1 ?r1) (assigned ?a2 ?r2)
                (not-eq ?a1 ?a2) (not-eq ?r1 ?r2))
  :effect (and (not (assigned ?a1 ?r1))
               (not (assigned ?a2 ?r2))
               (assigned ?a1 ?r2)
               (assigned ?a2 ?r1)
               )
)

; (:action assign-role
;   :parameters (?a - agent ?r - role)
;   :precondition (and (unassigned ?r) (unassigned ?a))
;   :effect (and (assigned ?a ?r)
;                 (not (unassigned ?r))
;                 (not (unassigned ?a))
;           )
; )

)
