(define (domain depots)
(:requirements :strips :typing)
(:types place locatable - object
	Depot Distributor - place
        Truck Hoist Surface - locatable
        Pallet Crate - Surface)

(:predicates (at ?x - locatable ?y - place)
             (on ?x - Crate ?y - Surface)
             (in ?x - Crate ?y - Truck)
             (lifting ?x - Hoist ?y - Crate)
             (available ?x - Hoist)
             (clear ?x - Surface))

(:action drive
  :parameters (?x - Truck ?y - place ?z - place)
  :precondition (and (at ?x ?y))
  :effect (and (not (at ?x ?y)) (at ?x ?z)))

(:action lift
  :parameters (?x - Hoist ?y - Crate ?z - Surface ?p - place)
  :precondition (and (at ?x ?p) (available ?x) (at ?y ?p) (on ?y ?z) (clear ?y))
  :effect (and (not (at ?y ?p)) (lifting ?x ?y) (not (clear ?y)) (not (available ?x)) (clear ?z) (not (on ?y ?z))))

(:action drop
  :parameters (?x - Hoist ?y - Crate ?z - Surface ?p - place)
  :precondition (and (at ?x ?p) (at ?z ?p) (clear ?z) (lifting ?x ?y))
  :effect (and (available ?x) (not (lifting ?x ?y)) (at ?y ?p) (not (clear ?z)) (clear ?y)(on ?y ?z)))

(:action load
  :parameters (?x - Hoist ?y - Crate ?z - Truck ?p - place)
  :precondition (and (at ?x ?p) (at ?z ?p) (lifting ?x ?y))
  :effect (and (not (lifting ?x ?y)) (in ?y ?z) (available ?x)))

(:action unload
  :parameters (?x - Hoist ?y - Crate ?z - Truck ?p - place)
  :precondition (and (at ?x ?p) (at ?z ?p) (available ?x) (in ?y ?z))
  :effect (and (not (in ?y ?z)) (not (available ?x)) (lifting ?x ?y)))
)