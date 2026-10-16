(define (problem prob-1-3-3-5-2)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	instrument1 - instrument
	instrument2 - instrument
	image1 - mode
	image0 - mode
	image2 - mode
	GroundStation2 - direction
	Star3 - direction
	GroundStation0 - direction
	GroundStation4 - direction
	Star1 - direction
	Phenomenon5 - direction
	Star6 - direction
)
(:init
	(supports instrument0 image2)
	(calibration_target instrument0 GroundStation0)
	(supports instrument1 image0)
	(calibration_target instrument1 GroundStation4)
	(supports instrument2 image2)
	(supports instrument2 image1)
	(supports instrument2 image0)
	(calibration_target instrument2 Star1)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(on_board instrument2 satellite0)
	(power_avail satellite0)
	(pointing satellite0 GroundStation2)
)
(:goal (and
	(have_image Phenomenon5 image0)
	(have_image Star6 image1)
))

)
