(define (problem prob-6-3-3-7-4)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	satellite1 - satellite
	instrument1 - instrument
	satellite2 - satellite
	instrument2 - instrument
	satellite3 - satellite
	instrument3 - instrument
	instrument4 - instrument
	instrument5 - instrument
	satellite4 - satellite
	instrument6 - instrument
	instrument7 - instrument
	satellite5 - satellite
	instrument8 - instrument
	instrument9 - instrument
	image0 - mode
	image1 - mode
	image2 - mode
	GroundStation4 - direction
	GroundStation0 - direction
	Star1 - direction
	GroundStation2 - direction
	GroundStation6 - direction
	Star3 - direction
	GroundStation5 - direction
	Phenomenon7 - direction
	Planet8 - direction
	Star9 - direction
	Phenomenon10 - direction
)
(:init
	(supports instrument0 image0)
	(calibration_target instrument0 GroundStation2)
	(on_board instrument0 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Star1)
	(supports instrument1 image2)
	(calibration_target instrument1 GroundStation4)
	(on_board instrument1 satellite1)
	(power_avail satellite1)
	(pointing satellite1 Phenomenon7)
	(supports instrument2 image2)
	(supports instrument2 image1)
	(supports instrument2 image0)
	(calibration_target instrument2 Star3)
	(on_board instrument2 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Phenomenon7)
	(supports instrument3 image1)
	(calibration_target instrument3 GroundStation6)
	(supports instrument4 image0)
	(calibration_target instrument4 GroundStation6)
	(calibration_target instrument4 GroundStation0)
	(supports instrument5 image0)
	(supports instrument5 image2)
	(supports instrument5 image1)
	(calibration_target instrument5 GroundStation5)
	(calibration_target instrument5 GroundStation2)
	(on_board instrument3 satellite3)
	(on_board instrument4 satellite3)
	(on_board instrument5 satellite3)
	(power_avail satellite3)
	(pointing satellite3 GroundStation0)
	(supports instrument6 image2)
	(supports instrument6 image1)
	(calibration_target instrument6 Star1)
	(calibration_target instrument6 GroundStation2)
	(supports instrument7 image1)
	(calibration_target instrument7 Star1)
	(on_board instrument6 satellite4)
	(on_board instrument7 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Star3)
	(supports instrument8 image1)
	(supports instrument8 image0)
	(calibration_target instrument8 GroundStation6)
	(calibration_target instrument8 GroundStation2)
	(supports instrument9 image1)
	(supports instrument9 image0)
	(calibration_target instrument9 GroundStation5)
	(calibration_target instrument9 Star3)
	(on_board instrument8 satellite5)
	(on_board instrument9 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Phenomenon10)
)
(:goal (and
	(pointing satellite1 Star3)
	(pointing satellite5 GroundStation6)
	(have_image Phenomenon7 image2)
	(have_image Planet8 image0)
	(have_image Star9 image2)
	(have_image Phenomenon10 image0)
))

)
