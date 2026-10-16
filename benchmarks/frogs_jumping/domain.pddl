
(define (domain frogs-jumping)
  (:requirements :strips :typing)

  (:types
    frog lilypad - object
    leftfrog rightfrog - frog
  )

  ;; p2 is immediately to the right of p1
  (:predicates
    (at ?f - frog ?p - lilypad)
    (empty ?p - lilypad)
    (next ?p1 - lilypad ?p2 - lilypad)
  )

  ;; Left frogs move only to the right 
  (:action slide-right
    :parameters (?lf - leftfrog ?from - lilypad ?to - lilypad)
    :precondition (and (at ?lf ?from) (next ?from ?to) (empty ?to))
    :effect (and (not (at ?lf ?from)) (at ?lf ?to) (empty ?from) (not (empty ?to)))
  )

  (:action jump-right
    :parameters (?lf - leftfrog ?from - lilypad ?mid - lilypad ?to - lilypad ?rf - rightfrog)
    :precondition (and
      (at ?lf ?from) (next ?from ?mid) (next ?mid ?to) 
      (at ?rf ?mid) (empty ?to))
    :effect (and (not (at ?lf ?from)) (at ?lf ?to) (empty ?from) (not (empty ?to)))
  )

  ;; Right frogs move only to the left 
  (:action slide-left
    :parameters (?rf - rightfrog ?from - lilypad ?to - lilypad)
    :precondition (and (at ?rf ?from) (next ?to ?from) (empty ?to))
    :effect (and (not (at ?rf ?from)) (at ?rf ?to) (empty ?from) (not (empty ?to)))
  )

  (:action jump-left
    :parameters (?rf - rightfrog ?from - lilypad ?mid - lilypad ?to - lilypad ?lf - leftfrog)
    :precondition (and
      (at ?rf ?from) (next ?to ?mid) (next ?mid ?from)
      (at ?lf ?mid) (empty ?to))
    :effect (and (not (at ?rf ?from)) (at ?rf ?to) (empty ?from) (not (empty ?to)))
  )
)
