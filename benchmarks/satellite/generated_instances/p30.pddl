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
	instrument5 - instrument
	satellite3 - satellite
	instrument6 - instrument
	satellite4 - satellite
	instrument7 - instrument
	satellite5 - satellite
	instrument8 - instrument
	instrument9 - instrument
	instrument10 - instrument
	thermograph2 - mode
	spectrograph0 - mode
	infrared1 - mode
	GroundStation10 - direction
	GroundStation1 - direction
	GroundStation11 - direction
	Star0 - direction
	GroundStation5 - direction
	GroundStation14 - direction
	Star12 - direction
	Star13 - direction
	GroundStation6 - direction
	GroundStation7 - direction
	Star8 - direction
	Star2 - direction
	GroundStation9 - direction
	GroundStation4 - direction
	GroundStation3 - direction
	Star15 - direction
	Star16 - direction
	Star17 - direction
	Phenomenon18 - direction
	Star19 - direction
	Planet20 - direction
	Planet21 - direction
	Phenomenon22 - direction
	Star23 - direction
	Phenomenon24 - direction
	Planet25 - direction
	Planet26 - direction
)
(:init
	(supports instrument0 infrared1)
	(calibration_target instrument0 GroundStation14)
	(calibration_target instrument0 GroundStation7)
	(calibration_target instrument0 GroundStation10)
	(on_board instrument0 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Star12)
	(supports instrument1 spectrograph0)
	(supports instrument1 thermograph2)
	(calibration_target instrument1 GroundStation3)
	(calibration_target instrument1 Star12)
	(calibration_target instrument1 GroundStation4)
	(calibration_target instrument1 Star13)
	(calibration_target instrument1 GroundStation14)
	(supports instrument2 thermograph2)
	(calibration_target instrument2 GroundStation7)
	(calibration_target instrument2 GroundStation11)
	(calibration_target instrument2 Star2)
	(calibration_target instrument2 Star8)
	(on_board instrument1 satellite1)
	(on_board instrument2 satellite1)
	(power_avail satellite1)
	(pointing satellite1 Planet21)
	(supports instrument3 infrared1)
	(supports instrument3 thermograph2)
	(supports instrument3 spectrograph0)
	(calibration_target instrument3 Star0)
	(calibration_target instrument3 Star2)
	(calibration_target instrument3 GroundStation11)
	(calibration_target instrument3 GroundStation1)
	(calibration_target instrument3 GroundStation9)
	(supports instrument4 infrared1)
	(calibration_target instrument4 Star12)
	(calibration_target instrument4 GroundStation14)
	(calibration_target instrument4 GroundStation9)
	(calibration_target instrument4 Star8)
	(supports instrument5 thermograph2)
	(supports instrument5 infrared1)
	(supports instrument5 spectrograph0)
	(calibration_target instrument5 GroundStation14)
	(calibration_target instrument5 GroundStation4)
	(calibration_target instrument5 GroundStation7)
	(calibration_target instrument5 GroundStation5)
	(on_board instrument3 satellite2)
	(on_board instrument4 satellite2)
	(on_board instrument5 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Star15)
	(supports instrument6 spectrograph0)
	(supports instrument6 thermograph2)
	(supports instrument6 infrared1)
	(calibration_target instrument6 Star2)
	(calibration_target instrument6 GroundStation14)
	(calibration_target instrument6 GroundStation9)
	(on_board instrument6 satellite3)
	(power_avail satellite3)
	(pointing satellite3 GroundStation10)
	(supports instrument7 spectrograph0)
	(supports instrument7 infrared1)
	(supports instrument7 thermograph2)
	(calibration_target instrument7 Star12)
	(calibration_target instrument7 GroundStation9)
	(calibration_target instrument7 GroundStation14)
	(calibration_target instrument7 GroundStation7)
	(on_board instrument7 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Planet25)
	(supports instrument8 thermograph2)
	(supports instrument8 infrared1)
	(calibration_target instrument8 GroundStation6)
	(calibration_target instrument8 Star13)
	(calibration_target instrument8 Star8)
	(supports instrument9 infrared1)
	(calibration_target instrument9 Star2)
	(calibration_target instrument9 Star8)
	(calibration_target instrument9 GroundStation9)
	(calibration_target instrument9 GroundStation3)
	(calibration_target instrument9 GroundStation7)
	(supports instrument10 infrared1)
	(supports instrument10 spectrograph0)
	(calibration_target instrument10 GroundStation3)
	(calibration_target instrument10 GroundStation4)
	(calibration_target instrument10 GroundStation9)
	(on_board instrument8 satellite5)
	(on_board instrument9 satellite5)
	(on_board instrument10 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Planet20)
)
(:goal (and
	(have_image Star15 infrared1)
	(have_image Star16 infrared1)
	(have_image Star17 thermograph2)
	(have_image Phenomenon18 thermograph2)
	(have_image Star19 thermograph2)
	(have_image Planet20 spectrograph0)
	(have_image Planet21 thermograph2)
	(have_image Phenomenon22 infrared1)
	(have_image Star23 infrared1)
	(have_image Phenomenon24 infrared1)
	(have_image Planet25 spectrograph0)
	(have_image Planet26 thermograph2)
))

)
