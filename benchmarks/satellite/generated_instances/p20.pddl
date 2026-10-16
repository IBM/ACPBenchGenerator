(define (problem prob-6-3-3-8-5)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	instrument1 - instrument
	satellite1 - satellite
	instrument2 - instrument
	satellite2 - satellite
	instrument3 - instrument
	instrument4 - instrument
	instrument5 - instrument
	satellite3 - satellite
	instrument6 - instrument
	instrument7 - instrument
	satellite4 - satellite
	instrument8 - instrument
	instrument9 - instrument
	instrument10 - instrument
	satellite5 - satellite
	instrument11 - instrument
	thermograph0 - mode
	image1 - mode
	infrared2 - mode
	GroundStation3 - direction
	GroundStation5 - direction
	GroundStation0 - direction
	GroundStation6 - direction
	GroundStation1 - direction
	GroundStation7 - direction
	Star4 - direction
	Star2 - direction
	Planet8 - direction
	Star9 - direction
	Planet10 - direction
	Phenomenon11 - direction
	Planet12 - direction
)
(:init
	(supports instrument0 image1)
	(calibration_target instrument0 Star4)
	(supports instrument1 infrared2)
	(calibration_target instrument1 Star2)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Star2)
	(supports instrument2 infrared2)
	(calibration_target instrument2 GroundStation5)
	(calibration_target instrument2 Star2)
	(on_board instrument2 satellite1)
	(power_avail satellite1)
	(pointing satellite1 GroundStation7)
	(supports instrument3 image1)
	(supports instrument3 thermograph0)
	(calibration_target instrument3 GroundStation0)
	(calibration_target instrument3 GroundStation7)
	(supports instrument4 thermograph0)
	(supports instrument4 image1)
	(supports instrument4 infrared2)
	(calibration_target instrument4 GroundStation5)
	(supports instrument5 image1)
	(supports instrument5 thermograph0)
	(calibration_target instrument5 GroundStation6)
	(calibration_target instrument5 Star4)
	(on_board instrument3 satellite2)
	(on_board instrument4 satellite2)
	(on_board instrument5 satellite2)
	(power_avail satellite2)
	(pointing satellite2 GroundStation5)
	(supports instrument6 thermograph0)
	(supports instrument6 image1)
	(calibration_target instrument6 Star2)
	(calibration_target instrument6 GroundStation1)
	(supports instrument7 thermograph0)
	(supports instrument7 image1)
	(calibration_target instrument7 GroundStation0)
	(on_board instrument6 satellite3)
	(on_board instrument7 satellite3)
	(power_avail satellite3)
	(pointing satellite3 Planet12)
	(supports instrument8 image1)
	(supports instrument8 thermograph0)
	(calibration_target instrument8 GroundStation6)
	(calibration_target instrument8 GroundStation1)
	(supports instrument9 thermograph0)
	(supports instrument9 infrared2)
	(supports instrument9 image1)
	(calibration_target instrument9 GroundStation1)
	(supports instrument10 thermograph0)
	(supports instrument10 infrared2)
	(calibration_target instrument10 Star2)
	(calibration_target instrument10 GroundStation7)
	(on_board instrument8 satellite4)
	(on_board instrument9 satellite4)
	(on_board instrument10 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Planet8)
	(supports instrument11 thermograph0)
	(calibration_target instrument11 Star2)
	(calibration_target instrument11 Star4)
	(on_board instrument11 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Star2)
)
(:goal (and
	(pointing satellite0 Planet12)
	(pointing satellite2 GroundStation6)
	(pointing satellite3 Planet10)
	(pointing satellite4 Planet10)
	(pointing satellite5 GroundStation7)
	(have_image Planet8 infrared2)
	(have_image Star9 thermograph0)
	(have_image Planet10 infrared2)
	(have_image Phenomenon11 image1)
	(have_image Planet12 thermograph0)
))

)
