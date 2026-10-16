(define (problem prob-6-3-3-8-5)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	instrument1 - instrument
	satellite1 - satellite
	instrument2 - instrument
	instrument3 - instrument
	instrument4 - instrument
	satellite2 - satellite
	instrument5 - instrument
	instrument6 - instrument
	satellite3 - satellite
	instrument7 - instrument
	instrument8 - instrument
	instrument9 - instrument
	satellite4 - satellite
	instrument10 - instrument
	satellite5 - satellite
	instrument11 - instrument
	instrument12 - instrument
	instrument13 - instrument
	image2 - mode
	image1 - mode
	image0 - mode
	GroundStation6 - direction
	GroundStation2 - direction
	GroundStation7 - direction
	Star1 - direction
	GroundStation4 - direction
	GroundStation0 - direction
	Star3 - direction
	GroundStation5 - direction
	Phenomenon8 - direction
	Star9 - direction
	Phenomenon10 - direction
	Star11 - direction
	Star12 - direction
)
(:init
	(supports instrument0 image1)
	(supports instrument0 image2)
	(calibration_target instrument0 GroundStation7)
	(supports instrument1 image2)
	(supports instrument1 image1)
	(calibration_target instrument1 GroundStation4)
	(calibration_target instrument1 GroundStation2)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Phenomenon8)
	(supports instrument2 image1)
	(calibration_target instrument2 GroundStation4)
	(supports instrument3 image1)
	(supports instrument3 image0)
	(supports instrument3 image2)
	(calibration_target instrument3 GroundStation2)
	(supports instrument4 image1)
	(supports instrument4 image2)
	(calibration_target instrument4 GroundStation5)
	(calibration_target instrument4 GroundStation4)
	(on_board instrument2 satellite1)
	(on_board instrument3 satellite1)
	(on_board instrument4 satellite1)
	(power_avail satellite1)
	(pointing satellite1 GroundStation5)
	(supports instrument5 image0)
	(supports instrument5 image1)
	(calibration_target instrument5 GroundStation0)
	(supports instrument6 image2)
	(supports instrument6 image0)
	(calibration_target instrument6 Star1)
	(on_board instrument5 satellite2)
	(on_board instrument6 satellite2)
	(power_avail satellite2)
	(pointing satellite2 GroundStation5)
	(supports instrument7 image1)
	(supports instrument7 image2)
	(supports instrument7 image0)
	(calibration_target instrument7 Star1)
	(calibration_target instrument7 GroundStation7)
	(supports instrument8 image2)
	(supports instrument8 image1)
	(supports instrument8 image0)
	(calibration_target instrument8 GroundStation4)
	(calibration_target instrument8 GroundStation0)
	(supports instrument9 image2)
	(calibration_target instrument9 GroundStation0)
	(on_board instrument7 satellite3)
	(on_board instrument8 satellite3)
	(on_board instrument9 satellite3)
	(power_avail satellite3)
	(pointing satellite3 GroundStation7)
	(supports instrument10 image2)
	(supports instrument10 image0)
	(supports instrument10 image1)
	(calibration_target instrument10 GroundStation0)
	(on_board instrument10 satellite4)
	(power_avail satellite4)
	(pointing satellite4 GroundStation4)
	(supports instrument11 image1)
	(supports instrument11 image0)
	(calibration_target instrument11 Star3)
	(supports instrument12 image0)
	(calibration_target instrument12 Star3)
	(supports instrument13 image2)
	(calibration_target instrument13 GroundStation5)
	(on_board instrument11 satellite5)
	(on_board instrument12 satellite5)
	(on_board instrument13 satellite5)
	(power_avail satellite5)
	(pointing satellite5 GroundStation2)
)
(:goal (and
	(pointing satellite4 GroundStation2)
	(have_image Phenomenon8 image2)
	(have_image Star9 image2)
	(have_image Phenomenon10 image1)
	(have_image Star11 image0)
	(have_image Star12 image1)
))

)
