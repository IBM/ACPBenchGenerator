(define (problem prob-3-3-3-5-2)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	instrument1 - instrument
	instrument2 - instrument
	satellite1 - satellite
	instrument3 - instrument
	instrument4 - instrument
	instrument5 - instrument
	satellite2 - satellite
	instrument6 - instrument
	image1 - mode
	image2 - mode
	image0 - mode
	GroundStation4 - direction
	Star1 - direction
	GroundStation0 - direction
	Star3 - direction
	GroundStation2 - direction
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
	(supports instrument3 image1)
	(supports instrument3 image2)
	(supports instrument3 image0)
	(calibration_target instrument3 Star3)
	(supports instrument4 image2)
	(calibration_target instrument4 GroundStation0)
	(supports instrument5 image1)
	(supports instrument5 image0)
	(supports instrument5 image2)
	(calibration_target instrument5 Star3)
	(on_board instrument3 satellite1)
	(on_board instrument4 satellite1)
	(on_board instrument5 satellite1)
	(power_avail satellite1)
	(pointing satellite1 Phenomenon5)
	(supports instrument6 image0)
	(supports instrument6 image2)
	(supports instrument6 image1)
	(calibration_target instrument6 GroundStation2)
	(on_board instrument6 satellite2)
	(power_avail satellite2)
	(pointing satellite2 GroundStation2)
)
(:goal (and
	(pointing satellite1 Phenomenon5)
	(have_image Phenomenon5 image0)
	(have_image Star6 image1)
))

)
