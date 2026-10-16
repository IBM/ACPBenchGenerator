(define (problem prob-6-3-3-12-9)
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
	instrument5 - instrument
	instrument6 - instrument
	satellite3 - satellite
	instrument7 - instrument
	satellite4 - satellite
	instrument8 - instrument
	instrument9 - instrument
	instrument10 - instrument
	satellite5 - satellite
	instrument11 - instrument
	instrument12 - instrument
	instrument13 - instrument
	image1 - mode
	thermograph0 - mode
	infrared2 - mode
	GroundStation8 - direction
	GroundStation10 - direction
	GroundStation7 - direction
	GroundStation5 - direction
	GroundStation1 - direction
	GroundStation0 - direction
	Star4 - direction
	GroundStation11 - direction
	Star9 - direction
	GroundStation6 - direction
	Star2 - direction
	GroundStation3 - direction
	Phenomenon12 - direction
	Phenomenon13 - direction
	Star14 - direction
	Phenomenon15 - direction
	Star16 - direction
	Star17 - direction
	Phenomenon18 - direction
	Star19 - direction
	Planet20 - direction
)
(:init
	(supports instrument0 infrared2)
	(supports instrument0 thermograph0)
	(calibration_target instrument0 GroundStation0)
	(calibration_target instrument0 GroundStation3)
	(calibration_target instrument0 GroundStation1)
	(supports instrument1 image1)
	(supports instrument1 infrared2)
	(calibration_target instrument1 Star2)
	(supports instrument2 thermograph0)
	(calibration_target instrument2 GroundStation11)
	(calibration_target instrument2 GroundStation0)
	(calibration_target instrument2 GroundStation7)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(on_board instrument2 satellite0)
	(power_avail satellite0)
	(pointing satellite0 Phenomenon13)
	(supports instrument3 image1)
	(supports instrument3 thermograph0)
	(supports instrument3 infrared2)
	(calibration_target instrument3 Star2)
	(calibration_target instrument3 GroundStation11)
	(calibration_target instrument3 GroundStation8)
	(on_board instrument3 satellite1)
	(power_avail satellite1)
	(pointing satellite1 GroundStation3)
	(supports instrument4 thermograph0)
	(supports instrument4 infrared2)
	(calibration_target instrument4 GroundStation7)
	(calibration_target instrument4 GroundStation10)
	(calibration_target instrument4 Star4)
	(supports instrument5 image1)
	(calibration_target instrument5 Star9)
	(calibration_target instrument5 GroundStation0)
	(calibration_target instrument5 GroundStation1)
	(supports instrument6 thermograph0)
	(calibration_target instrument6 GroundStation1)
	(calibration_target instrument6 Star9)
	(calibration_target instrument6 Star4)
	(calibration_target instrument6 GroundStation11)
	(on_board instrument4 satellite2)
	(on_board instrument5 satellite2)
	(on_board instrument6 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Phenomenon18)
	(supports instrument7 thermograph0)
	(supports instrument7 image1)
	(supports instrument7 infrared2)
	(calibration_target instrument7 GroundStation11)
	(on_board instrument7 satellite3)
	(power_avail satellite3)
	(pointing satellite3 Planet20)
	(supports instrument8 infrared2)
	(supports instrument8 thermograph0)
	(calibration_target instrument8 GroundStation1)
	(calibration_target instrument8 GroundStation5)
	(supports instrument9 thermograph0)
	(supports instrument9 infrared2)
	(calibration_target instrument9 GroundStation0)
	(calibration_target instrument9 Star4)
	(supports instrument10 thermograph0)
	(supports instrument10 image1)
	(supports instrument10 infrared2)
	(calibration_target instrument10 Star2)
	(on_board instrument8 satellite4)
	(on_board instrument9 satellite4)
	(on_board instrument10 satellite4)
	(power_avail satellite4)
	(pointing satellite4 GroundStation6)
	(supports instrument11 thermograph0)
	(calibration_target instrument11 Star4)
	(supports instrument12 thermograph0)
	(supports instrument12 image1)
	(supports instrument12 infrared2)
	(calibration_target instrument12 GroundStation3)
	(calibration_target instrument12 GroundStation11)
	(supports instrument13 thermograph0)
	(calibration_target instrument13 GroundStation3)
	(calibration_target instrument13 Star2)
	(calibration_target instrument13 GroundStation6)
	(calibration_target instrument13 Star9)
	(on_board instrument11 satellite5)
	(on_board instrument12 satellite5)
	(on_board instrument13 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Star4)
)
(:goal (and
	(pointing satellite0 GroundStation7)
	(pointing satellite1 Star17)
	(pointing satellite4 GroundStation0)
	(have_image Phenomenon12 infrared2)
	(have_image Phenomenon13 image1)
	(have_image Star14 thermograph0)
	(have_image Phenomenon15 image1)
	(have_image Star16 thermograph0)
	(have_image Star17 image1)
	(have_image Phenomenon18 image1)
	(have_image Star19 infrared2)
	(have_image Planet20 infrared2)
))

)
