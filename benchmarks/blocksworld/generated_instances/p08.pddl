

(define (problem BW-rand-5)
(:domain blocksworld-4ops)
(:objects block_1 block_2 block_3 block_4 block_5 )
(:init
(handempty)
(on block_1 block_4)
(ontable block_2)
(on block_3 block_1)
(ontable block_4)
(on block_5 block_3)
(clear block_2)
(clear block_5)
)
(:goal
(and
(on block_1 block_3)
(on block_3 block_2))
)
)


