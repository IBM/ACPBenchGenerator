(define (problem prob-6-3-3-10-7)
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
	satellite4 - satellite
	instrument4 - instrument
	instrument5 - instrument
	instrument6 - instrument
	satellite5 - satellite
	instrument7 - instrument
	instrument8 - instrument
	thermograph0 - mode
	image1 - mode
	infrared2 - mode
	GroundStation7 - direction
	Star4 - direction
	GroundStation5 - direction
	Star2 - direction
	Star9 - direction
	GroundStation1 - direction
	GroundStation3 - direction
	GroundStation0 - direction
	GroundStation8 - direction
	GroundStation6 - direction
	Planet10 - direction
	Phenomenon11 - direction
	Star12 - direction
	Phenomenon13 - direction
	Phenomenon14 - direction
	Star15 - direction
	Star16 - direction
)
(:init
	(supports instrument0 infrared2)
	(calibration_target instrument0 Star4)
	(calibration_target instrument0 GroundStation5)
	(calibration_target instrument0 GroundStation8)
	(on_board instrument0 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Star12)
	(supports instrument1 thermograph0)
	(calibration_target instrument1 Star9)
	(calibration_target instrument1 GroundStation3)
	(on_board instrument1 satellite1)
	(power_avail satellite1)
	(pointing satellite1 GroundStation5)
	(supports instrument2 image1)
	(calibration_target instrument2 Star9)
	(calibration_target instrument2 GroundStation5)
	(on_board instrument2 satellite2)
	(power_avail satellite2)
	(pointing satellite2 GroundStation6)
	(supports instrument3 infrared2)
	(supports instrument3 thermograph0)
	(calibration_target instrument3 GroundStation6)
	(calibration_target instrument3 Star9)
	(on_board instrument3 satellite3)
	(power_avail satellite3)
	(pointing satellite3 Star4)
	(supports instrument4 thermograph0)
	(supports instrument4 infrared2)
	(calibration_target instrument4 Star2)
	(calibration_target instrument4 GroundStation5)
	(calibration_target instrument4 GroundStation8)
	(supports instrument5 thermograph0)
	(calibration_target instrument5 GroundStation3)
	(calibration_target instrument5 Star9)
	(calibration_target instrument5 GroundStation0)
	(supports instrument6 image1)
	(supports instrument6 infrared2)
	(calibration_target instrument6 GroundStation3)
	(calibration_target instrument6 GroundStation1)
	(on_board instrument4 satellite4)
	(on_board instrument5 satellite4)
	(on_board instrument6 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Planet10)
	(supports instrument7 thermograph0)
	(calibration_target instrument7 GroundStation0)
	(supports instrument8 image1)
	(supports instrument8 thermograph0)
	(calibration_target instrument8 GroundStation6)
	(calibration_target instrument8 GroundStation8)
	(on_board instrument7 satellite5)
	(on_board instrument8 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Star4)
)
(:goal (and
	(pointing satellite1 GroundStation6)
	(pointing satellite4 GroundStation6)
	(have_image Planet10 thermograph0)
	(have_image Phenomenon11 image1)
	(have_image Star12 infrared2)
	(have_image Phenomenon13 infrared2)
	(have_image Phenomenon14 infrared2)
	(have_image Star15 infrared2)
	(have_image Star16 image1)
))

)
