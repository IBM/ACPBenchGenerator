(define (problem prob-6-3-3-10-7)
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
	instrument7 - instrument
	satellite3 - satellite
	instrument8 - instrument
	satellite4 - satellite
	instrument9 - instrument
	instrument10 - instrument
	satellite5 - satellite
	instrument11 - instrument
	instrument12 - instrument
	instrument13 - instrument
	image2 - mode
	image0 - mode
	image1 - mode
	GroundStation4 - direction
	GroundStation6 - direction
	Star3 - direction
	Star8 - direction
	Star1 - direction
	GroundStation5 - direction
	GroundStation2 - direction
	GroundStation0 - direction
	GroundStation9 - direction
	GroundStation7 - direction
	Star10 - direction
	Star11 - direction
	Phenomenon12 - direction
	Planet13 - direction
	Planet14 - direction
	Phenomenon15 - direction
	Star16 - direction
)
(:init
	(supports instrument0 image2)
	(supports instrument0 image0)
	(supports instrument0 image1)
	(calibration_target instrument0 Star8)
	(supports instrument1 image1)
	(supports instrument1 image0)
	(calibration_target instrument1 GroundStation9)
	(calibration_target instrument1 GroundStation5)
	(supports instrument2 image1)
	(supports instrument2 image0)
	(supports instrument2 image2)
	(calibration_target instrument2 Star1)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(on_board instrument2 satellite0)
	(power_avail satellite0)
	(pointing satellite0 GroundStation2)
	(supports instrument3 image2)
	(supports instrument3 image1)
	(supports instrument3 image0)
	(calibration_target instrument3 GroundStation7)
	(supports instrument4 image2)
	(calibration_target instrument4 Star3)
	(supports instrument5 image0)
	(supports instrument5 image1)
	(supports instrument5 image2)
	(calibration_target instrument5 Star8)
	(on_board instrument3 satellite1)
	(on_board instrument4 satellite1)
	(on_board instrument5 satellite1)
	(power_avail satellite1)
	(pointing satellite1 Star3)
	(supports instrument6 image2)
	(calibration_target instrument6 GroundStation6)
	(supports instrument7 image0)
	(supports instrument7 image2)
	(supports instrument7 image1)
	(calibration_target instrument7 Star1)
	(calibration_target instrument7 Star3)
	(calibration_target instrument7 Star8)
	(on_board instrument6 satellite2)
	(on_board instrument7 satellite2)
	(power_avail satellite2)
	(pointing satellite2 GroundStation5)
	(supports instrument8 image2)
	(supports instrument8 image1)
	(supports instrument8 image0)
	(calibration_target instrument8 Star8)
	(calibration_target instrument8 GroundStation2)
	(calibration_target instrument8 GroundStation9)
	(on_board instrument8 satellite3)
	(power_avail satellite3)
	(pointing satellite3 Star3)
	(supports instrument9 image2)
	(calibration_target instrument9 Star1)
	(supports instrument10 image2)
	(supports instrument10 image1)
	(calibration_target instrument10 GroundStation7)
	(calibration_target instrument10 GroundStation5)
	(on_board instrument9 satellite4)
	(on_board instrument10 satellite4)
	(power_avail satellite4)
	(pointing satellite4 GroundStation9)
	(supports instrument11 image2)
	(calibration_target instrument11 GroundStation9)
	(supports instrument12 image1)
	(supports instrument12 image2)
	(supports instrument12 image0)
	(calibration_target instrument12 GroundStation2)
	(calibration_target instrument12 GroundStation9)
	(calibration_target instrument12 GroundStation5)
	(supports instrument13 image2)
	(calibration_target instrument13 GroundStation7)
	(calibration_target instrument13 GroundStation9)
	(calibration_target instrument13 GroundStation0)
	(on_board instrument11 satellite5)
	(on_board instrument12 satellite5)
	(on_board instrument13 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Star1)
)
(:goal (and
	(pointing satellite2 Star11)
	(have_image Star10 image1)
	(have_image Star11 image0)
	(have_image Phenomenon12 image2)
	(have_image Planet13 image1)
	(have_image Planet14 image2)
	(have_image Phenomenon15 image1)
	(have_image Star16 image2)
))

)
