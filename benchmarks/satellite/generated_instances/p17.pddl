(define (problem prob-6-3-3-7-4)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	satellite1 - satellite
	instrument1 - instrument
	instrument2 - instrument
	instrument3 - instrument
	satellite2 - satellite
	instrument4 - instrument
	satellite3 - satellite
	instrument5 - instrument
	instrument6 - instrument
	satellite4 - satellite
	instrument7 - instrument
	instrument8 - instrument
	satellite5 - satellite
	instrument9 - instrument
	instrument10 - instrument
	thermograph0 - mode
	infrared2 - mode
	image1 - mode
	Star2 - direction
	GroundStation6 - direction
	GroundStation5 - direction
	Star4 - direction
	GroundStation1 - direction
	GroundStation0 - direction
	GroundStation3 - direction
	Phenomenon7 - direction
	Star8 - direction
	Phenomenon9 - direction
	Phenomenon10 - direction
)
(:init
	(supports instrument0 thermograph0)
	(supports instrument0 image1)
	(calibration_target instrument0 GroundStation1)
	(calibration_target instrument0 GroundStation3)
	(on_board instrument0 satellite0)
	(power_avail satellite0)
	(pointing satellite0 GroundStation3)
	(supports instrument1 infrared2)
	(supports instrument1 thermograph0)
	(supports instrument1 image1)
	(calibration_target instrument1 GroundStation6)
	(supports instrument2 image1)
	(supports instrument2 infrared2)
	(supports instrument2 thermograph0)
	(calibration_target instrument2 GroundStation0)
	(calibration_target instrument2 GroundStation3)
	(supports instrument3 thermograph0)
	(calibration_target instrument3 GroundStation3)
	(on_board instrument1 satellite1)
	(on_board instrument2 satellite1)
	(on_board instrument3 satellite1)
	(power_avail satellite1)
	(pointing satellite1 Phenomenon9)
	(supports instrument4 thermograph0)
	(supports instrument4 infrared2)
	(supports instrument4 image1)
	(calibration_target instrument4 GroundStation3)
	(on_board instrument4 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Phenomenon7)
	(supports instrument5 image1)
	(supports instrument5 infrared2)
	(calibration_target instrument5 GroundStation5)
	(supports instrument6 image1)
	(supports instrument6 thermograph0)
	(calibration_target instrument6 GroundStation1)
	(calibration_target instrument6 Star4)
	(on_board instrument5 satellite3)
	(on_board instrument6 satellite3)
	(power_avail satellite3)
	(pointing satellite3 GroundStation1)
	(supports instrument7 thermograph0)
	(supports instrument7 infrared2)
	(supports instrument7 image1)
	(calibration_target instrument7 GroundStation1)
	(calibration_target instrument7 GroundStation0)
	(supports instrument8 image1)
	(supports instrument8 infrared2)
	(supports instrument8 thermograph0)
	(calibration_target instrument8 GroundStation0)
	(on_board instrument7 satellite4)
	(on_board instrument8 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Phenomenon9)
	(supports instrument9 infrared2)
	(supports instrument9 thermograph0)
	(supports instrument9 image1)
	(calibration_target instrument9 GroundStation0)
	(supports instrument10 infrared2)
	(supports instrument10 image1)
	(supports instrument10 thermograph0)
	(calibration_target instrument10 GroundStation3)
	(on_board instrument9 satellite5)
	(on_board instrument10 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Star8)
)
(:goal (and
	(pointing satellite0 Star8)
	(pointing satellite1 GroundStation6)
	(have_image Phenomenon7 thermograph0)
	(have_image Star8 infrared2)
	(have_image Phenomenon9 infrared2)
	(have_image Phenomenon10 infrared2)
))

)
