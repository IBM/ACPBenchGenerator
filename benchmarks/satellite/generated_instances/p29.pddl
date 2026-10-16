(define (problem prob-6-3-3-15-12)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	satellite1 - satellite
	instrument1 - instrument
	instrument2 - instrument
	satellite2 - satellite
	instrument3 - instrument
	instrument4 - instrument
	satellite3 - satellite
	instrument5 - instrument
	satellite4 - satellite
	instrument6 - instrument
	instrument7 - instrument
	instrument8 - instrument
	satellite5 - satellite
	instrument9 - instrument
	infrared2 - mode
	image1 - mode
	thermograph0 - mode
	Star13 - direction
	GroundStation11 - direction
	GroundStation14 - direction
	GroundStation0 - direction
	GroundStation6 - direction
	GroundStation7 - direction
	Star4 - direction
	GroundStation1 - direction
	Star9 - direction
	GroundStation3 - direction
	GroundStation12 - direction
	GroundStation5 - direction
	GroundStation8 - direction
	Star2 - direction
	GroundStation10 - direction
	Planet15 - direction
	Star16 - direction
	Planet17 - direction
	Phenomenon18 - direction
	Phenomenon19 - direction
	Star20 - direction
	Planet21 - direction
	Phenomenon22 - direction
	Star23 - direction
	Star24 - direction
	Star25 - direction
	Phenomenon26 - direction
)
(:init
	(supports instrument0 thermograph0)
	(supports instrument0 infrared2)
	(calibration_target instrument0 GroundStation3)
	(calibration_target instrument0 GroundStation8)
	(calibration_target instrument0 GroundStation5)
	(on_board instrument0 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Star24)
	(supports instrument1 thermograph0)
	(supports instrument1 image1)
	(supports instrument1 infrared2)
	(calibration_target instrument1 GroundStation11)
	(calibration_target instrument1 Star4)
	(calibration_target instrument1 GroundStation8)
	(calibration_target instrument1 GroundStation7)
	(calibration_target instrument1 GroundStation6)
	(supports instrument2 infrared2)
	(supports instrument2 image1)
	(supports instrument2 thermograph0)
	(calibration_target instrument2 GroundStation5)
	(calibration_target instrument2 Star4)
	(calibration_target instrument2 GroundStation10)
	(calibration_target instrument2 GroundStation14)
	(on_board instrument1 satellite1)
	(on_board instrument2 satellite1)
	(power_avail satellite1)
	(pointing satellite1 Phenomenon22)
	(supports instrument3 thermograph0)
	(supports instrument3 infrared2)
	(supports instrument3 image1)
	(calibration_target instrument3 GroundStation0)
	(calibration_target instrument3 GroundStation1)
	(calibration_target instrument3 GroundStation8)
	(supports instrument4 infrared2)
	(supports instrument4 image1)
	(calibration_target instrument4 GroundStation3)
	(calibration_target instrument4 GroundStation0)
	(on_board instrument3 satellite2)
	(on_board instrument4 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Phenomenon26)
	(supports instrument5 thermograph0)
	(supports instrument5 infrared2)
	(calibration_target instrument5 Star4)
	(calibration_target instrument5 GroundStation5)
	(calibration_target instrument5 GroundStation12)
	(calibration_target instrument5 GroundStation7)
	(calibration_target instrument5 GroundStation6)
	(on_board instrument5 satellite3)
	(power_avail satellite3)
	(pointing satellite3 GroundStation5)
	(supports instrument6 image1)
	(calibration_target instrument6 GroundStation1)
	(calibration_target instrument6 GroundStation12)
	(calibration_target instrument6 Star2)
	(supports instrument7 image1)
	(supports instrument7 thermograph0)
	(supports instrument7 infrared2)
	(calibration_target instrument7 GroundStation10)
	(calibration_target instrument7 GroundStation3)
	(calibration_target instrument7 Star9)
	(calibration_target instrument7 GroundStation5)
	(calibration_target instrument7 Star2)
	(supports instrument8 image1)
	(supports instrument8 thermograph0)
	(supports instrument8 infrared2)
	(calibration_target instrument8 Star2)
	(calibration_target instrument8 GroundStation8)
	(calibration_target instrument8 GroundStation10)
	(calibration_target instrument8 GroundStation5)
	(calibration_target instrument8 GroundStation12)
	(on_board instrument6 satellite4)
	(on_board instrument7 satellite4)
	(on_board instrument8 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Phenomenon22)
	(supports instrument9 infrared2)
	(supports instrument9 image1)
	(calibration_target instrument9 GroundStation10)
	(on_board instrument9 satellite5)
	(power_avail satellite5)
	(pointing satellite5 GroundStation11)
)
(:goal (and
	(pointing satellite4 Planet21)
	(have_image Planet15 infrared2)
	(have_image Star16 image1)
	(have_image Planet17 infrared2)
	(have_image Phenomenon18 image1)
	(have_image Phenomenon19 infrared2)
	(have_image Star20 infrared2)
	(have_image Planet21 thermograph0)
	(have_image Phenomenon22 thermograph0)
	(have_image Star23 image1)
	(have_image Star24 infrared2)
	(have_image Star25 thermograph0)
	(have_image Phenomenon26 thermograph0)
))

)
