(define (problem gripper-1-3-7)
(:domain gripper-strips)
(:objects robot1 - robot
right1 left1 - gripper
room1 room2 room3 - room
ball1 ball2 ball3 ball4 ball5 ball6 ball7 - ball)
(:init
(at-robby robot1 room3)
(free robot1 right1)
(free robot1 left1)
(at ball1 room1)
(at ball2 room1)
(at ball3 room3)
(at ball4 room1)
(at ball5 room3)
(at ball6 room2)
(at ball7 room3)
)
(:goal
(and
(at ball1 room3)
(at ball2 room1)
(at ball3 room1)
(at ball4 room1)
(at ball5 room2)
(at ball6 room2)
(at ball7 room1)
)
)
)
