(define (problem prob-6-3-3-8-5)
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
	instrument8 - instrument
	satellite5 - satellite
	instrument9 - instrument
	instrument10 - instrument
	spectrograph0 - mode
	infrared1 - mode
	thermograph2 - mode
	GroundStation4 - direction
	GroundStation6 - direction
	Star2 - direction
	Star0 - direction
	GroundStation5 - direction
	GroundStation7 - direction
	GroundStation3 - direction
	GroundStation1 - direction
	Star8 - direction
	Star9 - direction
	Phenomenon10 - direction
	Phenomenon11 - direction
	Star12 - direction
)
(:init
	(supports instrument0 thermograph2)
	(supports instrument0 infrared1)
	(calibration_target instrument0 GroundStation4)
	(calibration_target instrument0 GroundStation1)
	(on_board instrument0 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Star0)
	(supports instrument1 infrared1)
	(calibration_target instrument1 Star2)
	(on_board instrument1 satellite1)
	(power_avail satellite1)
	(pointing satellite1 GroundStation1)
	(supports instrument2 thermograph2)
	(calibration_target instrument2 GroundStation5)
	(calibration_target instrument2 Star2)
	(on_board instrument2 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Star12)
	(supports instrument3 infrared1)
	(calibration_target instrument3 Star2)
	(calibration_target instrument3 GroundStation7)
	(supports instrument4 spectrograph0)
	(supports instrument4 thermograph2)
	(supports instrument4 infrared1)
	(calibration_target instrument4 GroundStation3)
	(calibration_target instrument4 GroundStation6)
	(supports instrument5 thermograph2)
	(supports instrument5 spectrograph0)
	(calibration_target instrument5 Star2)
	(on_board instrument3 satellite3)
	(on_board instrument4 satellite3)
	(on_board instrument5 satellite3)
	(power_avail satellite3)
	(pointing satellite3 GroundStation7)
	(supports instrument6 infrared1)
	(calibration_target instrument6 GroundStation6)
	(calibration_target instrument6 GroundStation7)
	(supports instrument7 spectrograph0)
	(supports instrument7 thermograph2)
	(calibration_target instrument7 Star0)
	(calibration_target instrument7 Star2)
	(supports instrument8 spectrograph0)
	(supports instrument8 thermograph2)
	(supports instrument8 infrared1)
	(calibration_target instrument8 GroundStation5)
	(on_board instrument6 satellite4)
	(on_board instrument7 satellite4)
	(on_board instrument8 satellite4)
	(power_avail satellite4)
	(pointing satellite4 GroundStation6)
	(supports instrument9 thermograph2)
	(calibration_target instrument9 GroundStation3)
	(calibration_target instrument9 GroundStation7)
	(supports instrument10 thermograph2)
	(calibration_target instrument10 GroundStation1)
	(on_board instrument9 satellite5)
	(on_board instrument10 satellite5)
	(power_avail satellite5)
	(pointing satellite5 GroundStation5)
)
(:goal (and
	(pointing satellite0 GroundStation4)
	(pointing satellite3 GroundStation5)
	(pointing satellite5 Star12)
	(have_image Star8 spectrograph0)
	(have_image Star9 thermograph2)
	(have_image Phenomenon10 infrared1)
	(have_image Phenomenon11 infrared1)
	(have_image Star12 thermograph2)
))

)
