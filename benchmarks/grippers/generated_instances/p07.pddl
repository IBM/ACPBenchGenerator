(define (problem gripper-1-7-4)
(:domain gripper-strips)
(:objects robot1 - robot
right1 left1 - gripper
room1 room2 room3 room4 room5 room6 room7 - room
ball1 ball2 ball3 ball4 - ball)
(:init
(at-robby robot1 room3)
(free robot1 right1)
(free robot1 left1)
(at ball1 room3)
(at ball2 room3)
(at ball3 room5)
(at ball4 room6)
)
(:goal
(and
(at ball1 room1)
(at ball2 room2)
(at ball3 room3)
(at ball4 room1)
)
)
)
