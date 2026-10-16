
(define (problem plan_trial_t20190906_202926_527010)
(:domain alfred)
(:objects
agent1 - agent
remotecontrol - object
        laptop - object
        kettle - object
        pen - object
        fork - object
        cloth - object
        houseplant - object
        plunger - object
        soapbottle - object
        cup - object
        candle - object
        tomato - object
        television - object
        tennisracket - object
        towel - object
        saltshaker - object
        spoon - object
        apple - object
        poster - object
        curtains - object
        footstool - object
        alarmclock - object
        ladle - object
        papertowelroll - object
        baseballbat - object
        knife - object
        spatula - object
        soapbar - object
        creditcard - object
        sink - object
        newspaper - object
        laundryhamperlid - object
        keychain - object
        glassbottle - object
        butterknife - object
        chair - object
        handtowel - object
        toiletpaperroll - object
        plate - object
        pot - object
        winebottle - object
        boots - object
        peppershaker - object
        papertowel - object
        bowl - object
        spraybottle - object
        scrubbrush - object
        box - object
        cd - object
        pan - object
        statue - object
        vase - object
        showerglass - object
        dishsponge - object
        egg - object
        lettuce - object
        book - object
        teddybear - object
        toiletpaper - object
        showerdoor - object
        window - object
        blinds - object
        cellphone - object
        floorlamp - object
        pillow - object
        mirror - object
        painting - object
        tissuebox - object
        pencil - object
        potato - object
        lightswitch - object
        stoveknob - object
        mug - object
        bathtub - object
        desklamp - object
        watch - object
        wateringcan - object
        basketball - object
        bread - object
remotecontroltype - otype
        laptoptype - otype
        kettletype - otype
        pentype - otype
        forktype - otype
        clothtype - otype
        houseplanttype - otype
        plungertype - otype
        soapbottletype - otype
        cuptype - otype
        candletype - otype
        tomatotype - otype
        televisiontype - otype
        tennisrackettype - otype
        toweltype - otype
        saltshakertype - otype
        spoontype - otype
        appletype - otype
        postertype - otype
        curtainstype - otype
        footstooltype - otype
        alarmclocktype - otype
        ladletype - otype
        papertowelrolltype - otype
        baseballbattype - otype
        spatulatype - otype
        soapbartype - otype
        creditcardtype - otype
        newspapertype - otype
        laundryhamperlidtype - otype
        keychaintype - otype
        glassbottletype - otype
        chairtype - otype
        handtoweltype - otype
        toiletpaperrolltype - otype
        platetype - otype
        pottype - otype
        winebottletype - otype
        bootstype - otype
        peppershakertype - otype
        papertoweltype - otype
        bowltype - otype
        spraybottletype - otype
        scrubbrushtype - otype
        boxtype - otype
        cdtype - otype
        pantype - otype
        statuetype - otype
        vasetype - otype
        showerglasstype - otype
        dishspongetype - otype
        eggtype - otype
        lettucetype - otype
        booktype - otype
        teddybeartype - otype
        toiletpapertype - otype
        showerdoortype - otype
        windowtype - otype
        blindstype - otype
        cellphonetype - otype
        floorlamptype - otype
        pillowtype - otype
        mirrortype - otype
        paintingtype - otype
        tissueboxtype - otype
        penciltype - otype
        potatotype - otype
        lightswitchtype - otype
        stoveknobtype - otype
        mugtype - otype
        bathtubtype - otype
        desklamptype - otype
        watchtype - otype
        wateringcantype - otype
        basketballtype - otype
        breadtype - otype
        garbagecantype - rtype
        stoveburnertype - rtype
        ottomantype - rtype
        cabinettype - rtype
        sidetabletype - rtype
        diningtabletype - rtype
        coffeetabletype - rtype
        safetype - rtype
        dressertype - rtype
        desktype - rtype
        bedtype - rtype
        towelholdertype - rtype
        toiletpaperhangertype - rtype
        sofatype - rtype
        carttype - rtype
        armchairtype - rtype
        handtowelholdertype - rtype
        tvstandtype - rtype
        bathtubbasintype - rtype
        coffeemachinetype - rtype
        toastertype - rtype
        laundryhampertype - rtype
        drawertype - rtype
        toilettype - rtype
        shelftype - rtype
        paintinghangertype - rtype
        countertoptype - rtype


        candle1 - object
        candle2 - object
        candle3 - object
        cloth1 - object
        cloth2 - object
        faucet1 - object
        faucet2 - object
        faucet3 - object
        handtowel1 - object
        lightswitch1 - object
        mirror1 - object
        plunger1 - object
        scrubbrush1 - object
        showerdoor1 - object
        showerglass1 - object
        sink1 - object
        sink2 - object
        soapbar1 - object
        soapbar2 - object
        soapbar3 - object
        soapbottle1 - object
        soapbottle2 - object
        soapbottle3 - object
        spraybottle1 - object
        spraybottle2 - object
        toiletpaper1 - object
        toiletpaper2 - object
        toiletpaper3 - object
        towel1 - object
        cabinet1 - receptacle
        cabinet2 - receptacle
        cabinet3 - receptacle
        cabinet4 - receptacle
        countertop1 - receptacle
        garbagecan1 - receptacle
        handtowelholder1 - receptacle
        handtowelholder2 - receptacle
        sinkbasin1 - receptacle
        sinkbasin2 - receptacle
        toiletpaperhanger1 - receptacle
        toilet1 - receptacle
        towelholder1 - receptacle
        location1 - location
        location2 - location
        location3 - location
        location4 - location
        location5 - location
        location6 - location
        location7 - location
        location8 - location
        location9 - location
        location10 - location
        location11 - location
        location12 - location
        location13 - location
        location14 - location
        location15 - location
        location16 - location
        location17 - location
        location18 - location
        location19 - location
        )
    

(:init

         


        (receptacletype toilet1 toilettype)
        (receptacletype garbagecan1 garbagecantype)
        (receptacletype handtowelholder1 handtowelholdertype)
        (receptacletype towelholder1 towelholdertype)
        (receptacletype sinkbasin1 sinkbasintype)
        (receptacletype cabinet1 cabinettype)
        (receptacletype countertop1 countertoptype)
        (receptacletype toiletpaperhanger1 toiletpaperhangertype)
        (receptacletype cabinet4 cabinettype)
        (receptacletype cabinet2 cabinettype)
        (receptacletype cabinet3 cabinettype)
        (receptacletype handtowelholder2 handtowelholdertype)
        (receptacletype sinkbasin2 sinkbasintype)
        (objecttype candle3 candletype)
        (objecttype candle2 candletype)
        (objecttype lightswitch1 lightswitchtype)
        (objecttype scrubbrush1 scrubbrushtype)
        (objecttype sink1 sinktype)
        (objecttype sink2 sinktype)
        (objecttype soapbar1 soapbartype)
        (objecttype spraybottle1 spraybottletype)
        (objecttype candle1 candletype)
        (objecttype soapbar2 soapbartype)
        (objecttype spraybottle2 spraybottletype)
        (objecttype towel1 toweltype)
        (objecttype soapbar3 soapbartype)
        (objecttype cloth1 clothtype)
        (objecttype soapbottle1 soapbottletype)
        (objecttype soapbottle3 soapbottletype)
        (objecttype showerglass1 showerglasstype)
        (objecttype showerdoor1 showerdoortype)
        (objecttype toiletpaper2 toiletpapertype)
        (objecttype plunger1 plungertype)
        (objecttype cloth2 clothtype)
        (objecttype mirror1 mirrortype)
        (objecttype toiletpaper1 toiletpapertype)
        (objecttype handtowel1 handtoweltype)
        (objecttype toiletpaper3 toiletpapertype)
        (objecttype soapbottle2 soapbottletype)
        (cancontain toilettype handtoweltype)
        (cancontain toilettype toiletpapertype)
        (cancontain toilettype clothtype)
        (cancontain toilettype soapbottletype)
        (cancontain toilettype spraybottletype)
        (cancontain toilettype soapbartype)
        (cancontain toilettype candletype)
        (cancontain garbagecantype toiletpapertype)
        (cancontain garbagecantype clothtype)
        (cancontain garbagecantype spraybottletype)
        (cancontain garbagecantype soapbartype)
        (cancontain garbagecantype soapbottletype)
        (cancontain garbagecantype handtoweltype)
        (cancontain handtowelholdertype handtoweltype)
        (cancontain towelholdertype toweltype)
        (cancontain sinkbasintype clothtype)
        (cancontain sinkbasintype soapbartype)
        (cancontain sinkbasintype handtoweltype)
        (cancontain cabinettype toiletpapertype)
        (cancontain cabinettype clothtype)
        (cancontain cabinettype plungertype)
        (cancontain cabinettype spraybottletype)
        (cancontain cabinettype soapbartype)
        (cancontain cabinettype soapbottletype)
        (cancontain cabinettype candletype)
        (cancontain cabinettype handtoweltype)
        (cancontain countertoptype toiletpapertype)
        (cancontain countertoptype clothtype)
        (cancontain countertoptype spraybottletype)
        (cancontain countertoptype soapbartype)
        (cancontain countertoptype soapbottletype)
        (cancontain countertoptype candletype)
        (cancontain countertoptype handtoweltype)
        (cancontain toiletpaperhangertype toiletpapertype)
        (cancontain cabinettype toiletpapertype)
        (cancontain cabinettype clothtype)
        (cancontain cabinettype plungertype)
        (cancontain cabinettype spraybottletype)
        (cancontain cabinettype soapbartype)
        (cancontain cabinettype soapbottletype)
        (cancontain cabinettype candletype)
        (cancontain cabinettype handtoweltype)
        (cancontain cabinettype toiletpapertype)
        (cancontain cabinettype clothtype)
        (cancontain cabinettype plungertype)
        (cancontain cabinettype spraybottletype)
        (cancontain cabinettype soapbartype)
        (cancontain cabinettype soapbottletype)
        (cancontain cabinettype candletype)
        (cancontain cabinettype handtoweltype)
        (cancontain cabinettype toiletpapertype)
        (cancontain cabinettype clothtype)
        (cancontain cabinettype plungertype)
        (cancontain cabinettype spraybottletype)
        (cancontain cabinettype soapbartype)
        (cancontain cabinettype soapbottletype)
        (cancontain cabinettype candletype)
        (cancontain cabinettype handtoweltype)
        (cancontain handtowelholdertype handtoweltype)
        (cancontain sinkbasintype clothtype)
        (cancontain sinkbasintype soapbartype)
        (cancontain sinkbasintype handtoweltype)
        (pickupable candle3)
        (pickupable candle2)
        (pickupable scrubbrush1)
        (pickupable soapbar1)
        (pickupable spraybottle1)
        (pickupable candle1)
        (pickupable soapbar2)
        (pickupable spraybottle2)
        (pickupable towel1)
        (pickupable soapbar3)
        (pickupable cloth1)
        (pickupable soapbottle1)
        (pickupable soapbottle3)
        (pickupable toiletpaper2)
        (pickupable plunger1)
        (pickupable cloth2)
        (pickupable toiletpaper1)
        (pickupable handtowel1)
        (pickupable toiletpaper3)
        (pickupable soapbottle2)
        
        (openable cabinet1)
        (openable cabinet4)
        (openable cabinet2)
        (openable cabinet3)
        
        (notopenable countertop1)
        (notopenable garbagecan1)
        (notopenable handtowelholder1)
        (notopenable handtowelholder2)
        (notopenable sinkbasin1)
        (notopenable sinkbasin2)
        (notopenable toiletpaperhanger1)
        (notopenable toilet1)
        (notopenable towelholder1)


        (closed cabinet1)
        (closed cabinet4)
        (closed cabinet2)
        (closed cabinet3)

        (handempty agent1)
        (notvalidated)

        (atlocation agent1 location19)
        
        (cleanable soapbar1)
        (cleanable soapbar2)
        (cleanable soapbar3)
        (cleanable cloth1)
        (cleanable cloth2)
        
        
        
        
        
        
        
        
        
        
        (inreceptacle spraybottle2 cabinet2)
        (inreceptacle soapbottle2 cabinet3)
        (inreceptacle candle3 countertop1)
        (inreceptacle spraybottle1 countertop1)
        (inreceptacle candle1 countertop1)
        (inreceptacle soapbottle3 countertop1)
        (inreceptacle toiletpaper3 countertop1)
        (inreceptacle cloth2 cabinet4)
        (inreceptacle candle2 cabinet4)
        (inreceptacle cloth1 cabinet1)
        (inreceptacle soapbottle1 cabinet1)
        (inreceptacle towel1 towelholder1)
        (inreceptacle handtowel1 handtowelholder1)
        (inreceptacle toiletpaper1 toilet1)
        (inreceptacle soapbar2 toilet1)
        (inreceptacle soapbar1 toilet1)
        (inreceptacle soapbar3 sinkbasin1)
        
        
        (receptacleatlocation cabinet1 location4)
        (receptacleatlocation cabinet2 location11)
        (receptacleatlocation cabinet3 location8)
        (receptacleatlocation cabinet4 location15)
        (receptacleatlocation countertop1 location3)
        (receptacleatlocation garbagecan1 location2)
        (receptacleatlocation handtowelholder1 location18)
        (receptacleatlocation handtowelholder2 location17)
        (receptacleatlocation sinkbasin1 location16)
        (receptacleatlocation sinkbasin2 location6)
        (receptacleatlocation toiletpaperhanger1 location10)
        (receptacleatlocation toilet1 location7)
        (receptacleatlocation towelholder1 location5)
        (objectatlocation soapbottle3 location3)
        (objectatlocation cloth2 location15)
        (objectatlocation spraybottle1 location3)
        (objectatlocation toiletpaper2 location10)
        (objectatlocation candle1 location3)
        (objectatlocation soapbar3 location16)
        (objectatlocation soapbottle2 location8)
        (objectatlocation soapbar1 location7)
        (objectatlocation candle3 location3)
        (objectatlocation mirror1 location9)
        (objectatlocation sink2 location14)
        (objectatlocation showerdoor1 location1)
        (objectatlocation showerglass1 location5)
        (objectatlocation sink1 location12)
        (objectatlocation handtowel1 location18)
        (objectatlocation towel1 location5)
        (objectatlocation soapbar2 location7)
        (objectatlocation toiletpaper1 location7)
        (objectatlocation plunger1 location10)
        (objectatlocation candle2 location15)
        (objectatlocation lightswitch1 location13)
        (objectatlocation toiletpaper3 location3)
        (objectatlocation spraybottle2 location11)
        (objectatlocation cloth1 location4)
        (objectatlocation scrubbrush1 location10)
        (objectatlocation soapbottle1 location4)
        )
    

                (:goal
                    (and
                        (validatepicktwoandplace  toiletpapertype cabinettype)

                        ;;(exists (?r - receptacle)
                        ;;    (exists (?o1 - object)
                        ;;        (and
                        ;;            (objecttype ?o1 toiletpapertype)
                        ;;            (receptacletype ?r cabinettype)
                        ;;            (inreceptacle ?o1 ?r)
                        ;;            (exists (?o2 - object)
                        ;;                (and
                        ;;                    (not (= ?o1 ?o2))
                        ;;                    (objecttype ?o2 toiletpapertype)
                        ;;                   (receptacletype ?r cabinettype)
                        ;;                   (inreceptacle ?o2 ?r)
                        ;;                )
                        ;;            )
                        ;;        )
                        ;;    )
                        ;;)
                    )
                )

                 
            )
            

