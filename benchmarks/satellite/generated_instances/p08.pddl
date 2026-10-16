(define (problem prob-5-3-3-5-2)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	satellite1 - satellite
	instrument1 - instrument
	instrument2 - instrument
	satellite2 - satellite
	instrument3 - instrument
	satellite3 - satellite
	instrument4 - instrument
	instrument5 - instrument
	satellite4 - satellite
	instrument6 - instrument
	instrument7 - instrument
	infrared2 - mode
	thermograph0 - mode
	image1 - mode
	Star4 - direction
	GroundStation3 - direction
	GroundStation1 - direction
	GroundStation0 - direction
	Star2 - direction
	Planet5 - direction
	Planet6 - direction
)
(:init
	(supports instrument0 thermograph0)
	(supports instrument0 image1)
	(calibration_target instrument0 Star4)
	(on_board instrument0 satellite0)
	(power_avail satellite0)
	(pointing satellite0 GroundStation1)
	(supports instrument1 thermograph0)
	(calibration_target instrument1 GroundStation3)
	(supports instrument2 infrared2)
	(supports instrument2 thermograph0)
	(supports instrument2 image1)
	(calibration_target instrument2 Star2)
	(on_board instrument1 satellite1)
	(on_board instrument2 satellite1)
	(power_avail satellite1)
	(pointing satellite1 GroundStation0)
	(supports instrument3 image1)
	(calibration_target instrument3 GroundStation0)
	(on_board instrument3 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Planet6)
	(supports instrument4 image1)
	(supports instrument4 thermograph0)
	(supports instrument4 infrared2)
	(calibration_target instrument4 GroundStation1)
	(supports instrument5 thermograph0)
	(supports instrument5 infrared2)
	(calibration_target instrument5 GroundStation1)
	(on_board instrument4 satellite3)
	(on_board instrument5 satellite3)
	(power_avail satellite3)
	(pointing satellite3 GroundStation1)
	(supports instrument6 image1)
	(supports instrument6 thermograph0)
	(supports instrument6 infrared2)
	(calibration_target instrument6 GroundStation0)
	(supports instrument7 infrared2)
	(supports instrument7 image1)
	(supports instrument7 thermograph0)
	(calibration_target instrument7 Star2)
	(on_board instrument6 satellite4)
	(on_board instrument7 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Planet6)
)
(:goal (and
	(have_image Planet5 thermograph0)
	(have_image Planet6 infrared2)
))

)
