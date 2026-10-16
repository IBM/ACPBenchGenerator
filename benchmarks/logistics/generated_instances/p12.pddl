


(define (problem logistics-c5-s3-p4-a1)
(:domain logistics-strips)
(:objects a0 - airplane
          c0 c1 c2 c3 c4 - city 
          t0 t1 t2 t3 t4 - truck
          l0-0 - airport
          l0-1 - location
          l0-2 - location
          l1-0 - airport 
          l1-1 - location
          l1-2 - location
          l2-0 - airport 
          l2-1 - location
          l2-2 - location
          l3-0 - airport 
          l3-1 - location
          l3-2 - location
          l4-0 - airport 
          l4-1 - location
          l4-2 - location
          p0 p1 p2 p3 - package
)
(:init
    ; (AIRPLANE a0)
    ; (CITY c0)
    ; (CITY c1)
    ; (CITY c2)
    ; (CITY c3)
    ; (CITY c4)
    ; (TRUCK t0)
    ; (TRUCK t1)
    ; (TRUCK t2)
    ; (TRUCK t3)
    ; (TRUCK t4)
    ; (LOCATION l0-0)
    (in-city  l0-0 c0)
    ; (LOCATION l0-1)
    (in-city  l0-1 c0)
    ; (LOCATION l0-2)
    (in-city  l0-2 c0)
    ; (LOCATION l1-0)
    (in-city  l1-0 c1)
    ; (LOCATION l1-1)
    (in-city  l1-1 c1)
    ; (LOCATION l1-2)
    (in-city  l1-2 c1)
    ; (LOCATION l2-0)
    (in-city  l2-0 c2)
    ; (LOCATION l2-1)
    (in-city  l2-1 c2)
    ; (LOCATION l2-2)
    (in-city  l2-2 c2)
    ; (LOCATION l3-0)
    (in-city  l3-0 c3)
    ; (LOCATION l3-1)
    (in-city  l3-1 c3)
    ; (LOCATION l3-2)
    (in-city  l3-2 c3)
    ; (LOCATION l4-0)
    (in-city  l4-0 c4)
    ; (LOCATION l4-1)
    (in-city  l4-1 c4)
    ; (LOCATION l4-2)
    (in-city  l4-2 c4)
    ; (AIRPORT l0-0)
    ; (AIRPORT l1-0)
    ; (AIRPORT l2-0)
    ; (AIRPORT l3-0)
    ; (AIRPORT l4-0)
    ; (OBJ p0)
    ; (OBJ p1)
    ; (OBJ p2)
    ; (OBJ p3)
    (at t0 l0-0)
    (at t1 l1-1)
    (at t2 l2-1)
    (at t3 l3-0)
    (at t4 l4-0)
    (at p0 l2-0)
    (at p1 l0-1)
    (at p2 l1-0)
    (at p3 l2-0)
    (at a0 l0-0)
)
(:goal
    (and
        (at p0 l4-2)
        (at p1 l4-0)
        (at p2 l2-2)
        (at p3 l1-2)
    )
)
)


