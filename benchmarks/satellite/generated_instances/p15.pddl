(define (problem prob-10-3-3-5-2)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	instrument1 - instrument
	instrument2 - instrument
	satellite1 - satellite
	instrument3 - instrument
	satellite2 - satellite
	instrument4 - instrument
	satellite3 - satellite
	instrument5 - instrument
	satellite4 - satellite
	instrument6 - instrument
	instrument7 - instrument
	instrument8 - instrument
	satellite5 - satellite
	instrument9 - instrument
	instrument10 - instrument
	instrument11 - instrument
	satellite6 - satellite
	instrument12 - instrument
	instrument13 - instrument
	instrument14 - instrument
	satellite7 - satellite
	instrument15 - instrument
	instrument16 - instrument
	instrument17 - instrument
	satellite8 - satellite
	instrument18 - instrument
	instrument19 - instrument
	satellite9 - satellite
	instrument20 - instrument
	infrared1 - mode
	thermograph2 - mode
	spectrograph0 - mode
	GroundStation1 - direction
	Star2 - direction
	GroundStation3 - direction
	Star0 - direction
	GroundStation4 - direction
	Planet5 - direction
	Phenomenon6 - direction
)
(:init
	(supports instrument0 spectrograph0)
	(supports instrument0 thermograph2)
	(supports instrument0 infrared1)
	(calibration_target instrument0 Star0)
	(supports instrument1 spectrograph0)
	(calibration_target instrument1 Star2)
	(supports instrument2 spectrograph0)
	(supports instrument2 infrared1)
	(calibration_target instrument2 GroundStation3)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(on_board instrument2 satellite0)
	(power_avail satellite0)
	(pointing satellite0 GroundStation4)
	(supports instrument3 infrared1)
	(calibration_target instrument3 GroundStation3)
	(on_board instrument3 satellite1)
	(power_avail satellite1)
	(pointing satellite1 GroundStation3)
	(supports instrument4 thermograph2)
	(supports instrument4 infrared1)
	(supports instrument4 spectrograph0)
	(calibration_target instrument4 Star2)
	(on_board instrument4 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Star2)
	(supports instrument5 thermograph2)
	(calibration_target instrument5 GroundStation3)
	(on_board instrument5 satellite3)
	(power_avail satellite3)
	(pointing satellite3 Star2)
	(supports instrument6 infrared1)
	(calibration_target instrument6 GroundStation1)
	(supports instrument7 spectrograph0)
	(calibration_target instrument7 GroundStation3)
	(supports instrument8 spectrograph0)
	(calibration_target instrument8 GroundStation3)
	(on_board instrument6 satellite4)
	(on_board instrument7 satellite4)
	(on_board instrument8 satellite4)
	(power_avail satellite4)
	(pointing satellite4 GroundStation1)
	(supports instrument9 thermograph2)
	(supports instrument9 infrared1)
	(calibration_target instrument9 GroundStation1)
	(supports instrument10 infrared1)
	(supports instrument10 spectrograph0)
	(calibration_target instrument10 GroundStation4)
	(supports instrument11 infrared1)
	(supports instrument11 spectrograph0)
	(supports instrument11 thermograph2)
	(calibration_target instrument11 Star2)
	(on_board instrument9 satellite5)
	(on_board instrument10 satellite5)
	(on_board instrument11 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Star2)
	(supports instrument12 thermograph2)
	(supports instrument12 spectrograph0)
	(calibration_target instrument12 Star2)
	(supports instrument13 thermograph2)
	(calibration_target instrument13 GroundStation4)
	(supports instrument14 infrared1)
	(calibration_target instrument14 Star2)
	(on_board instrument12 satellite6)
	(on_board instrument13 satellite6)
	(on_board instrument14 satellite6)
	(power_avail satellite6)
	(pointing satellite6 Star0)
	(supports instrument15 thermograph2)
	(calibration_target instrument15 GroundStation4)
	(supports instrument16 spectrograph0)
	(supports instrument16 infrared1)
	(calibration_target instrument16 GroundStation3)
	(supports instrument17 thermograph2)
	(supports instrument17 spectrograph0)
	(supports instrument17 infrared1)
	(calibration_target instrument17 Star0)
	(on_board instrument15 satellite7)
	(on_board instrument16 satellite7)
	(on_board instrument17 satellite7)
	(power_avail satellite7)
	(pointing satellite7 Phenomenon6)
	(supports instrument18 infrared1)
	(supports instrument18 spectrograph0)
	(calibration_target instrument18 GroundStation4)
	(supports instrument19 infrared1)
	(calibration_target instrument19 GroundStation4)
	(on_board instrument18 satellite8)
	(on_board instrument19 satellite8)
	(power_avail satellite8)
	(pointing satellite8 Star2)
	(supports instrument20 spectrograph0)
	(supports instrument20 infrared1)
	(calibration_target instrument20 GroundStation4)
	(on_board instrument20 satellite9)
	(power_avail satellite9)
	(pointing satellite9 GroundStation1)
)
(:goal (and
	(pointing satellite1 Phenomenon6)
	(pointing satellite4 GroundStation4)
	(have_image Planet5 thermograph2)
	(have_image Phenomenon6 spectrograph0)
))

)
