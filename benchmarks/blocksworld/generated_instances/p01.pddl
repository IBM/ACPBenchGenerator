

(define (problem BW-rand-3)
(:domain blocksworld-4ops)
(:objects block_1 block_2 block_3 )
(:init
(handempty)
(ontable block_1)
(on block_2 block_1)
(ontable block_3)
(clear block_2)
(clear block_3)
)
(:goal
(and
(on block_1 block_3)
(on block_2 block_1))
)
)


