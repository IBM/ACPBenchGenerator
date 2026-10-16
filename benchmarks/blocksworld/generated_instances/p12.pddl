

(define (problem BW-rand-10)
(:domain blocksworld-4ops)
(:objects block_1 block_2 block_3 block_4 block_5 block_6 block_7 block_8 block_9 block_10 )
(:init
(handempty)
(on block_1 block_6)
(on block_2 block_3)
(on block_3 block_8)
(on block_4 block_9)
(ontable block_5)
(on block_6 block_5)
(ontable block_7)
(ontable block_8)
(on block_9 block_10)
(on block_10 block_1)
(clear block_2)
(clear block_4)
(clear block_7)
)
(:goal
(and
(on block_2 block_7)
(on block_4 block_3)
(on block_5 block_1)
(on block_6 block_8)
(on block_8 block_4)
(on block_9 block_6)
(on block_10 block_5))
)
)


