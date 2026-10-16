

(define (problem BW-rand-5)
(:domain blocksworld-4ops)
(:objects block_1 block_2 block_3 block_4 block_5 )
(:init
(handempty)
(ontable block_1)
(on block_2 block_1)
(on block_3 block_5)
(ontable block_4)
(ontable block_5)
(clear block_2)
(clear block_3)
(clear block_4)
)
(:goal
(and
(on block_3 block_5)
(on block_4 block_1)
(on block_5 block_4))
)
)


