(define (problem prob-6-3-3-12-9)
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
	instrument5 - instrument
	instrument6 - instrument
	satellite3 - satellite
	instrument7 - instrument
	instrument8 - instrument
	satellite4 - satellite
	instrument9 - instrument
	satellite5 - satellite
	instrument10 - instrument
	spectrograph0 - mode
	thermograph2 - mode
	infrared1 - mode
	GroundStation6 - direction
	Star8 - direction
	GroundStation4 - direction
	GroundStation3 - direction
	GroundStation5 - direction
	GroundStation7 - direction
	Star0 - direction
	GroundStation9 - direction
	GroundStation10 - direction
	Star2 - direction
	GroundStation1 - direction
	GroundStation11 - direction
	Star12 - direction
	Star13 - direction
	Planet14 - direction
	Planet15 - direction
	Planet16 - direction
	Star17 - direction
	Phenomenon18 - direction
	Planet19 - direction
	Phenomenon20 - direction
)
(:init
	(supports instrument0 thermograph2)
	(supports instrument0 infrared1)
	(calibration_target instrument0 GroundStation9)
	(calibration_target instrument0 GroundStation5)
	(calibration_target instrument0 GroundStation11)
	(on_board instrument0 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Star12)
	(supports instrument1 thermograph2)
	(supports instrument1 infrared1)
	(supports instrument1 spectrograph0)
	(calibration_target instrument1 GroundStation7)
	(calibration_target instrument1 GroundStation5)
	(supports instrument2 spectrograph0)
	(calibration_target instrument2 GroundStation4)
	(supports instrument3 infrared1)
	(supports instrument3 thermograph2)
	(supports instrument3 spectrograph0)
	(calibration_target instrument3 Star0)
	(on_board instrument1 satellite1)
	(on_board instrument2 satellite1)
	(on_board instrument3 satellite1)
	(power_avail satellite1)
	(pointing satellite1 GroundStation7)
	(supports instrument4 infrared1)
	(calibration_target instrument4 Star2)
	(calibration_target instrument4 GroundStation10)
	(calibration_target instrument4 GroundStation5)
	(calibration_target instrument4 GroundStation3)
	(supports instrument5 spectrograph0)
	(supports instrument5 infrared1)
	(supports instrument5 thermograph2)
	(calibration_target instrument5 Star2)
	(calibration_target instrument5 Star0)
	(supports instrument6 spectrograph0)
	(supports instrument6 thermograph2)
	(supports instrument6 infrared1)
	(calibration_target instrument6 GroundStation7)
	(calibration_target instrument6 GroundStation9)
	(calibration_target instrument6 GroundStation1)
	(on_board instrument4 satellite2)
	(on_board instrument5 satellite2)
	(on_board instrument6 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Star12)
	(supports instrument7 thermograph2)
	(calibration_target instrument7 Star0)
	(calibration_target instrument7 GroundStation11)
	(supports instrument8 infrared1)
	(calibration_target instrument8 GroundStation11)
	(calibration_target instrument8 GroundStation9)
	(on_board instrument7 satellite3)
	(on_board instrument8 satellite3)
	(power_avail satellite3)
	(pointing satellite3 GroundStation9)
	(supports instrument9 thermograph2)
	(supports instrument9 spectrograph0)
	(supports instrument9 infrared1)
	(calibration_target instrument9 GroundStation1)
	(calibration_target instrument9 GroundStation10)
	(on_board instrument9 satellite4)
	(power_avail satellite4)
	(pointing satellite4 GroundStation3)
	(supports instrument10 thermograph2)
	(supports instrument10 infrared1)
	(supports instrument10 spectrograph0)
	(calibration_target instrument10 GroundStation11)
	(calibration_target instrument10 GroundStation1)
	(calibration_target instrument10 Star2)
	(on_board instrument10 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Planet19)
)
(:goal (and
	(pointing satellite3 Planet15)
	(have_image Star12 spectrograph0)
	(have_image Star13 spectrograph0)
	(have_image Planet14 thermograph2)
	(have_image Planet15 infrared1)
	(have_image Planet16 spectrograph0)
	(have_image Star17 thermograph2)
	(have_image Phenomenon18 infrared1)
	(have_image Planet19 spectrograph0)
	(have_image Phenomenon20 thermograph2)
))

)
