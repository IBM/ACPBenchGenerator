(define (problem prob-6-3-3-7-4)
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
	satellite4 - satellite
	instrument7 - instrument
	instrument8 - instrument
	satellite5 - satellite
	instrument9 - instrument
	instrument10 - instrument
	spectrograph0 - mode
	thermograph2 - mode
	infrared1 - mode
	GroundStation5 - direction
	Star0 - direction
	Star2 - direction
	GroundStation3 - direction
	GroundStation1 - direction
	GroundStation6 - direction
	GroundStation4 - direction
	Planet7 - direction
	Planet8 - direction
	Star9 - direction
	Star10 - direction
)
(:init
	(supports instrument0 thermograph2)
	(supports instrument0 infrared1)
	(supports instrument0 spectrograph0)
	(calibration_target instrument0 Star0)
	(supports instrument1 spectrograph0)
	(supports instrument1 thermograph2)
	(supports instrument1 infrared1)
	(calibration_target instrument1 GroundStation5)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Star10)
	(supports instrument2 infrared1)
	(supports instrument2 thermograph2)
	(calibration_target instrument2 Star2)
	(on_board instrument2 satellite1)
	(power_avail satellite1)
	(pointing satellite1 Star0)
	(supports instrument3 spectrograph0)
	(supports instrument3 infrared1)
	(supports instrument3 thermograph2)
	(calibration_target instrument3 GroundStation3)
	(calibration_target instrument3 GroundStation1)
	(supports instrument4 infrared1)
	(supports instrument4 spectrograph0)
	(supports instrument4 thermograph2)
	(calibration_target instrument4 GroundStation5)
	(supports instrument5 infrared1)
	(calibration_target instrument5 Star2)
	(on_board instrument3 satellite2)
	(on_board instrument4 satellite2)
	(on_board instrument5 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Star0)
	(supports instrument6 infrared1)
	(supports instrument6 thermograph2)
	(supports instrument6 spectrograph0)
	(calibration_target instrument6 GroundStation4)
	(calibration_target instrument6 Star0)
	(on_board instrument6 satellite3)
	(power_avail satellite3)
	(pointing satellite3 Star9)
	(supports instrument7 spectrograph0)
	(calibration_target instrument7 GroundStation3)
	(supports instrument8 spectrograph0)
	(calibration_target instrument8 GroundStation3)
	(calibration_target instrument8 Star2)
	(on_board instrument7 satellite4)
	(on_board instrument8 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Star0)
	(supports instrument9 infrared1)
	(supports instrument9 spectrograph0)
	(supports instrument9 thermograph2)
	(calibration_target instrument9 GroundStation6)
	(calibration_target instrument9 GroundStation1)
	(supports instrument10 thermograph2)
	(calibration_target instrument10 GroundStation4)
	(on_board instrument9 satellite5)
	(on_board instrument10 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Planet8)
)
(:goal (and
	(pointing satellite1 Star9)
	(pointing satellite4 Star10)
	(pointing satellite5 Star2)
	(have_image Planet7 thermograph2)
	(have_image Planet8 infrared1)
	(have_image Star9 infrared1)
	(have_image Star10 infrared1)
))

)
