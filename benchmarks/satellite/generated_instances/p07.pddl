(define (problem prob-5-3-3-5-2)
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
	satellite3 - satellite
	instrument7 - instrument
	instrument8 - instrument
	satellite4 - satellite
	instrument9 - instrument
	instrument10 - instrument
	instrument11 - instrument
	image2 - mode
	image0 - mode
	image1 - mode
	Star1 - direction
	GroundStation2 - direction
	GroundStation0 - direction
	GroundStation4 - direction
	Star3 - direction
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
	(supports instrument7 image1)
	(supports instrument7 image0)
	(calibration_target instrument7 Star3)
	(supports instrument8 image0)
	(supports instrument8 image2)
	(supports instrument8 image1)
	(calibration_target instrument8 GroundStation0)
	(on_board instrument7 satellite3)
	(on_board instrument8 satellite3)
	(power_avail satellite3)
	(pointing satellite3 Star6)
	(supports instrument9 image1)
	(calibration_target instrument9 Star3)
	(supports instrument10 image2)
	(supports instrument10 image0)
	(calibration_target instrument10 GroundStation4)
	(supports instrument11 image1)
	(supports instrument11 image2)
	(calibration_target instrument11 Star3)
	(on_board instrument9 satellite4)
	(on_board instrument10 satellite4)
	(on_board instrument11 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Star1)
)
(:goal (and
	(pointing satellite1 Phenomenon5)
	(pointing satellite4 Star1)
	(have_image Phenomenon5 image0)
	(have_image Star6 image1)
))

)
