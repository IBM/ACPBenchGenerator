(define (problem prob-6-3-3-10-7)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	instrument1 - instrument
	satellite1 - satellite
	instrument2 - instrument
	instrument3 - instrument
	satellite2 - satellite
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
	instrument12 - instrument
	instrument13 - instrument
	infrared1 - mode
	thermograph2 - mode
	spectrograph0 - mode
	GroundStation6 - direction
	GroundStation3 - direction
	GroundStation4 - direction
	GroundStation9 - direction
	GroundStation7 - direction
	Star0 - direction
	GroundStation1 - direction
	GroundStation5 - direction
	Star8 - direction
	Star2 - direction
	Planet10 - direction
	Planet11 - direction
	Star12 - direction
	Planet13 - direction
	Phenomenon14 - direction
	Star15 - direction
	Phenomenon16 - direction
)
(:init
	(supports instrument0 spectrograph0)
	(supports instrument0 infrared1)
	(supports instrument0 thermograph2)
	(calibration_target instrument0 GroundStation7)
	(calibration_target instrument0 Star0)
	(supports instrument1 infrared1)
	(supports instrument1 thermograph2)
	(calibration_target instrument1 Star8)
	(calibration_target instrument1 GroundStation9)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Star2)
	(supports instrument2 thermograph2)
	(supports instrument2 infrared1)
	(calibration_target instrument2 GroundStation1)
	(calibration_target instrument2 GroundStation5)
	(supports instrument3 spectrograph0)
	(supports instrument3 thermograph2)
	(calibration_target instrument3 GroundStation1)
	(calibration_target instrument3 Star8)
	(calibration_target instrument3 GroundStation3)
	(on_board instrument2 satellite1)
	(on_board instrument3 satellite1)
	(power_avail satellite1)
	(pointing satellite1 GroundStation4)
	(supports instrument4 thermograph2)
	(calibration_target instrument4 Star0)
	(calibration_target instrument4 GroundStation1)
	(supports instrument5 spectrograph0)
	(supports instrument5 infrared1)
	(calibration_target instrument5 Star2)
	(calibration_target instrument5 GroundStation4)
	(on_board instrument4 satellite2)
	(on_board instrument5 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Star15)
	(supports instrument6 thermograph2)
	(supports instrument6 infrared1)
	(calibration_target instrument6 GroundStation1)
	(supports instrument7 spectrograph0)
	(supports instrument7 infrared1)
	(supports instrument7 thermograph2)
	(calibration_target instrument7 Star8)
	(calibration_target instrument7 GroundStation9)
	(calibration_target instrument7 Star0)
	(on_board instrument6 satellite3)
	(on_board instrument7 satellite3)
	(power_avail satellite3)
	(pointing satellite3 GroundStation9)
	(supports instrument8 infrared1)
	(supports instrument8 thermograph2)
	(calibration_target instrument8 Star2)
	(calibration_target instrument8 GroundStation1)
	(calibration_target instrument8 GroundStation5)
	(supports instrument9 thermograph2)
	(calibration_target instrument9 GroundStation7)
	(supports instrument10 spectrograph0)
	(calibration_target instrument10 GroundStation1)
	(calibration_target instrument10 Star0)
	(on_board instrument8 satellite4)
	(on_board instrument9 satellite4)
	(on_board instrument10 satellite4)
	(power_avail satellite4)
	(pointing satellite4 GroundStation7)
	(supports instrument11 thermograph2)
	(calibration_target instrument11 Star8)
	(calibration_target instrument11 GroundStation5)
	(supports instrument12 spectrograph0)
	(calibration_target instrument12 Star8)
	(supports instrument13 thermograph2)
	(calibration_target instrument13 Star2)
	(on_board instrument11 satellite5)
	(on_board instrument12 satellite5)
	(on_board instrument13 satellite5)
	(power_avail satellite5)
	(pointing satellite5 GroundStation3)
)
(:goal (and
	(pointing satellite1 Star8)
	(pointing satellite3 GroundStation9)
	(pointing satellite4 Planet11)
	(have_image Planet10 infrared1)
	(have_image Planet11 infrared1)
	(have_image Star12 infrared1)
	(have_image Planet13 spectrograph0)
	(have_image Phenomenon14 infrared1)
	(have_image Star15 thermograph2)
	(have_image Phenomenon16 thermograph2)
))

)
