(define (problem prob-6-3-3-12-9)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	instrument1 - instrument
	satellite1 - satellite
	instrument2 - instrument
	satellite2 - satellite
	instrument3 - instrument
	satellite3 - satellite
	instrument4 - instrument
	instrument5 - instrument
	satellite4 - satellite
	instrument6 - instrument
	instrument7 - instrument
	satellite5 - satellite
	instrument8 - instrument
	instrument9 - instrument
	instrument10 - instrument
	image1 - mode
	image0 - mode
	image2 - mode
	Star10 - direction
	Star8 - direction
	GroundStation0 - direction
	Star3 - direction
	Star11 - direction
	GroundStation2 - direction
	GroundStation9 - direction
	GroundStation7 - direction
	GroundStation5 - direction
	GroundStation6 - direction
	Star1 - direction
	GroundStation4 - direction
	Star12 - direction
	Phenomenon13 - direction
	Phenomenon14 - direction
	Phenomenon15 - direction
	Phenomenon16 - direction
	Planet17 - direction
	Star18 - direction
	Planet19 - direction
	Phenomenon20 - direction
)
(:init
	(supports instrument0 image0)
	(supports instrument0 image1)
	(calibration_target instrument0 GroundStation2)
	(calibration_target instrument0 Star8)
	(supports instrument1 image1)
	(supports instrument1 image2)
	(supports instrument1 image0)
	(calibration_target instrument1 GroundStation6)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Star12)
	(supports instrument2 image0)
	(supports instrument2 image2)
	(calibration_target instrument2 GroundStation2)
	(calibration_target instrument2 GroundStation6)
	(calibration_target instrument2 GroundStation4)
	(on_board instrument2 satellite1)
	(power_avail satellite1)
	(pointing satellite1 Star10)
	(supports instrument3 image1)
	(calibration_target instrument3 GroundStation0)
	(calibration_target instrument3 GroundStation9)
	(calibration_target instrument3 Star3)
	(on_board instrument3 satellite2)
	(power_avail satellite2)
	(pointing satellite2 GroundStation7)
	(supports instrument4 image2)
	(supports instrument4 image0)
	(calibration_target instrument4 GroundStation4)
	(calibration_target instrument4 GroundStation2)
	(calibration_target instrument4 Star1)
	(supports instrument5 image1)
	(supports instrument5 image2)
	(supports instrument5 image0)
	(calibration_target instrument5 Star3)
	(calibration_target instrument5 GroundStation5)
	(on_board instrument4 satellite3)
	(on_board instrument5 satellite3)
	(power_avail satellite3)
	(pointing satellite3 Phenomenon16)
	(supports instrument6 image2)
	(calibration_target instrument6 Star1)
	(supports instrument7 image2)
	(supports instrument7 image1)
	(supports instrument7 image0)
	(calibration_target instrument7 GroundStation2)
	(calibration_target instrument7 Star11)
	(on_board instrument6 satellite4)
	(on_board instrument7 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Star10)
	(supports instrument8 image2)
	(supports instrument8 image0)
	(supports instrument8 image1)
	(calibration_target instrument8 GroundStation4)
	(calibration_target instrument8 GroundStation9)
	(calibration_target instrument8 Star1)
	(calibration_target instrument8 GroundStation5)
	(supports instrument9 image2)
	(supports instrument9 image0)
	(calibration_target instrument9 GroundStation5)
	(calibration_target instrument9 GroundStation7)
	(supports instrument10 image2)
	(calibration_target instrument10 GroundStation4)
	(calibration_target instrument10 Star1)
	(calibration_target instrument10 GroundStation6)
	(calibration_target instrument10 GroundStation5)
	(on_board instrument8 satellite5)
	(on_board instrument9 satellite5)
	(on_board instrument10 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Phenomenon20)
)
(:goal (and
	(pointing satellite1 Star11)
	(pointing satellite2 GroundStation5)
	(have_image Star12 image1)
	(have_image Phenomenon13 image1)
	(have_image Phenomenon14 image2)
	(have_image Phenomenon15 image1)
	(have_image Phenomenon16 image1)
	(have_image Planet17 image0)
	(have_image Star18 image1)
	(have_image Planet19 image0)
	(have_image Phenomenon20 image1)
))

)
