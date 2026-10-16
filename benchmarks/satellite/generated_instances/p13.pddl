(define (problem prob-10-3-3-5-2)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	instrument1 - instrument
	instrument2 - instrument
	satellite1 - satellite
	instrument3 - instrument
	instrument4 - instrument
	instrument5 - instrument
	satellite2 - satellite
	instrument6 - instrument
	satellite3 - satellite
	instrument7 - instrument
	instrument8 - instrument
	satellite4 - satellite
	instrument9 - instrument
	instrument10 - instrument
	instrument11 - instrument
	satellite5 - satellite
	instrument12 - instrument
	instrument13 - instrument
	instrument14 - instrument
	satellite6 - satellite
	instrument15 - instrument
	instrument16 - instrument
	instrument17 - instrument
	satellite7 - satellite
	instrument18 - instrument
	instrument19 - instrument
	satellite8 - satellite
	instrument20 - instrument
	instrument21 - instrument
	satellite9 - satellite
	instrument22 - instrument
	image0 - mode
	image1 - mode
	image2 - mode
	Star3 - direction
	GroundStation2 - direction
	GroundStation4 - direction
	GroundStation0 - direction
	Star1 - direction
	Phenomenon5 - direction
	Star6 - direction
)
(:init
	(supports instrument0 image2)
	(calibration_target instrument0 GroundStation0)
	(supports instrument1 image0)
	(calibration_target instrument1 GroundStation4)
	(supports instrument2 image2)
	(supports instrument2 image1)
	(supports instrument2 image0)
	(calibration_target instrument2 Star1)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(on_board instrument2 satellite0)
	(power_avail satellite0)
	(pointing satellite0 GroundStation2)
	(supports instrument3 image1)
	(supports instrument3 image2)
	(supports instrument3 image0)
	(calibration_target instrument3 Star3)
	(supports instrument4 image2)
	(calibration_target instrument4 GroundStation0)
	(supports instrument5 image1)
	(supports instrument5 image0)
	(supports instrument5 image2)
	(calibration_target instrument5 Star3)
	(on_board instrument3 satellite1)
	(on_board instrument4 satellite1)
	(on_board instrument5 satellite1)
	(power_avail satellite1)
	(pointing satellite1 Phenomenon5)
	(supports instrument6 image0)
	(supports instrument6 image2)
	(supports instrument6 image1)
	(calibration_target instrument6 GroundStation2)
	(on_board instrument6 satellite2)
	(power_avail satellite2)
	(pointing satellite2 GroundStation2)
	(supports instrument7 image1)
	(supports instrument7 image0)
	(calibration_target instrument7 Star3)
	(supports instrument8 image0)
	(supports instrument8 image2)
	(supports instrument8 image1)
	(calibration_target instrument8 GroundStation0)
	(on_board instrument7 satellite3)
	(on_board instrument8 satellite3)
	(power_avail satellite3)
	(pointing satellite3 Star6)
	(supports instrument9 image1)
	(calibration_target instrument9 Star3)
	(supports instrument10 image2)
	(supports instrument10 image0)
	(calibration_target instrument10 GroundStation4)
	(supports instrument11 image1)
	(supports instrument11 image2)
	(calibration_target instrument11 Star3)
	(on_board instrument9 satellite4)
	(on_board instrument10 satellite4)
	(on_board instrument11 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Star1)
	(supports instrument12 image0)
	(calibration_target instrument12 GroundStation0)
	(supports instrument13 image2)
	(supports instrument13 image0)
	(calibration_target instrument13 GroundStation0)
	(supports instrument14 image1)
	(supports instrument14 image2)
	(supports instrument14 image0)
	(calibration_target instrument14 GroundStation4)
	(on_board instrument12 satellite5)
	(on_board instrument13 satellite5)
	(on_board instrument14 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Phenomenon5)
	(supports instrument15 image2)
	(supports instrument15 image0)
	(supports instrument15 image1)
	(calibration_target instrument15 GroundStation2)
	(supports instrument16 image0)
	(supports instrument16 image1)
	(calibration_target instrument16 GroundStation2)
	(supports instrument17 image1)
	(calibration_target instrument17 GroundStation0)
	(on_board instrument15 satellite6)
	(on_board instrument16 satellite6)
	(on_board instrument17 satellite6)
	(power_avail satellite6)
	(pointing satellite6 GroundStation0)
	(supports instrument18 image1)
	(supports instrument18 image2)
	(calibration_target instrument18 GroundStation0)
	(supports instrument19 image2)
	(supports instrument19 image1)
	(calibration_target instrument19 GroundStation4)
	(on_board instrument18 satellite7)
	(on_board instrument19 satellite7)
	(power_avail satellite7)
	(pointing satellite7 Phenomenon5)
	(supports instrument20 image2)
	(supports instrument20 image1)
	(supports instrument20 image0)
	(calibration_target instrument20 GroundStation0)
	(supports instrument21 image2)
	(calibration_target instrument21 Star1)
	(on_board instrument20 satellite8)
	(on_board instrument21 satellite8)
	(power_avail satellite8)
	(pointing satellite8 GroundStation4)
	(supports instrument22 image2)
	(supports instrument22 image0)
	(calibration_target instrument22 Star1)
	(on_board instrument22 satellite9)
	(power_avail satellite9)
	(pointing satellite9 Star3)
)
(:goal (and
	(pointing satellite1 Phenomenon5)
	(pointing satellite4 Star1)
	(pointing satellite5 GroundStation0)
	(pointing satellite9 Phenomenon5)
	(have_image Phenomenon5 image0)
	(have_image Star6 image1)
))

)
