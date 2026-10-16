
(define (problem plan_trial_t20190908_125200_737896)
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


        alarmclock1 - object
        alarmclock2 - object
        baseballbat1 - object
        basketball1 - object
        blinds1 - object
        blinds2 - object
        book1 - object
        bowl1 - object
        bowl2 - object
        cd1 - object
        cellphone1 - object
        cellphone2 - object
        chair1 - object
        chair2 - object
        creditcard1 - object
        desklamp1 - object
        keychain1 - object
        keychain2 - object
        keychain3 - object
        laptop1 - object
        laundryhamperlid1 - object
        lightswitch1 - object
        mirror1 - object
        mug1 - object
        pencil1 - object
        pen1 - object
        pen2 - object
        pillow1 - object
        window1 - object
        window2 - object
        bed1 - receptacle
        desk1 - receptacle
        desk2 - receptacle
        drawer1 - receptacle
        drawer2 - receptacle
        drawer3 - receptacle
        drawer4 - receptacle
        drawer5 - receptacle
        drawer6 - receptacle
        garbagecan1 - receptacle
        laundryhamper1 - receptacle
        safe1 - receptacle
        shelf1 - receptacle
        shelf2 - receptacle
        shelf3 - receptacle
        shelf4 - receptacle
        shelf5 - receptacle
        shelf6 - receptacle
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
        location20 - location
        location21 - location
        location22 - location
        location23 - location
        location24 - location
        location25 - location
        location26 - location
        location27 - location
        )
    

(:init

         


        (receptacletype drawer2 drawertype)
        (receptacletype laundryhamper1 laundryhampertype)
        (receptacletype drawer1 drawertype)
        (receptacletype drawer4 drawertype)
        (receptacletype drawer5 drawertype)
        (receptacletype desk2 desktype)
        (receptacletype shelf3 shelftype)
        (receptacletype drawer6 drawertype)
        (receptacletype shelf6 shelftype)
        (receptacletype shelf5 shelftype)
        (receptacletype drawer3 drawertype)
        (receptacletype shelf1 shelftype)
        (receptacletype safe1 safetype)
        (receptacletype shelf2 shelftype)
        (receptacletype garbagecan1 garbagecantype)
        (receptacletype bed1 bedtype)
        (receptacletype shelf4 shelftype)
        (receptacletype desk1 desktype)
        (objecttype pen1 pentype)
        (objecttype lightswitch1 lightswitchtype)
        (objecttype cellphone2 cellphonetype)
        (objecttype alarmclock1 alarmclocktype)
        (objecttype mirror1 mirrortype)
        (objecttype bowl1 bowltype)
        (objecttype desklamp1 desklamptype)
        (objecttype bowl2 bowltype)
        (objecttype book1 booktype)
        (objecttype blinds2 blindstype)
        (objecttype window2 windowtype)
        (objecttype window1 windowtype)
        (objecttype alarmclock2 alarmclocktype)
        (objecttype laptop1 laptoptype)
        (objecttype keychain1 keychaintype)
        (objecttype pillow1 pillowtype)
        (objecttype baseballbat1 baseballbattype)
        (objecttype laundryhamperlid1 laundryhamperlidtype)
        (objecttype pencil1 penciltype)
        (objecttype cellphone1 cellphonetype)
        (objecttype chair1 chairtype)
        (objecttype cd1 cdtype)
        (objecttype keychain2 keychaintype)
        (objecttype keychain3 keychaintype)
        (objecttype blinds1 blindstype)
        (objecttype chair2 chairtype)
        (objecttype mug1 mugtype)
        (objecttype creditcard1 creditcardtype)
        (objecttype basketball1 basketballtype)
        (objecttype pen2 pentype)
        (cancontain drawertype pentype)
        (cancontain drawertype cellphonetype)
        (cancontain drawertype creditcardtype)
        (cancontain drawertype cdtype)
        (cancontain drawertype penciltype)
        (cancontain drawertype keychaintype)
        (cancontain drawertype booktype)
        (cancontain drawertype pentype)
        (cancontain drawertype cellphonetype)
        (cancontain drawertype creditcardtype)
        (cancontain drawertype cdtype)
        (cancontain drawertype penciltype)
        (cancontain drawertype keychaintype)
        (cancontain drawertype booktype)
        (cancontain drawertype pentype)
        (cancontain drawertype cellphonetype)
        (cancontain drawertype creditcardtype)
        (cancontain drawertype cdtype)
        (cancontain drawertype penciltype)
        (cancontain drawertype keychaintype)
        (cancontain drawertype booktype)
        (cancontain drawertype pentype)
        (cancontain drawertype cellphonetype)
        (cancontain drawertype creditcardtype)
        (cancontain drawertype cdtype)
        (cancontain drawertype penciltype)
        (cancontain drawertype keychaintype)
        (cancontain drawertype booktype)
        (cancontain desktype laptoptype)
        (cancontain desktype alarmclocktype)
        (cancontain desktype pentype)
        (cancontain desktype cellphonetype)
        (cancontain desktype bowltype)
        (cancontain desktype creditcardtype)
        (cancontain desktype cdtype)
        (cancontain desktype penciltype)
        (cancontain desktype keychaintype)
        (cancontain desktype mugtype)
        (cancontain desktype basketballtype)
        (cancontain desktype booktype)
        (cancontain shelftype alarmclocktype)
        (cancontain shelftype pentype)
        (cancontain shelftype cellphonetype)
        (cancontain shelftype bowltype)
        (cancontain shelftype creditcardtype)
        (cancontain shelftype cdtype)
        (cancontain shelftype penciltype)
        (cancontain shelftype keychaintype)
        (cancontain shelftype mugtype)
        (cancontain shelftype booktype)
        (cancontain drawertype pentype)
        (cancontain drawertype cellphonetype)
        (cancontain drawertype creditcardtype)
        (cancontain drawertype cdtype)
        (cancontain drawertype penciltype)
        (cancontain drawertype keychaintype)
        (cancontain drawertype booktype)
        (cancontain shelftype alarmclocktype)
        (cancontain shelftype pentype)
        (cancontain shelftype cellphonetype)
        (cancontain shelftype bowltype)
        (cancontain shelftype creditcardtype)
        (cancontain shelftype cdtype)
        (cancontain shelftype penciltype)
        (cancontain shelftype keychaintype)
        (cancontain shelftype mugtype)
        (cancontain shelftype booktype)
        (cancontain shelftype alarmclocktype)
        (cancontain shelftype pentype)
        (cancontain shelftype cellphonetype)
        (cancontain shelftype bowltype)
        (cancontain shelftype creditcardtype)
        (cancontain shelftype cdtype)
        (cancontain shelftype penciltype)
        (cancontain shelftype keychaintype)
        (cancontain shelftype mugtype)
        (cancontain shelftype booktype)
        (cancontain drawertype pentype)
        (cancontain drawertype cellphonetype)
        (cancontain drawertype creditcardtype)
        (cancontain drawertype cdtype)
        (cancontain drawertype penciltype)
        (cancontain drawertype keychaintype)
        (cancontain drawertype booktype)
        (cancontain shelftype alarmclocktype)
        (cancontain shelftype pentype)
        (cancontain shelftype cellphonetype)
        (cancontain shelftype bowltype)
        (cancontain shelftype creditcardtype)
        (cancontain shelftype cdtype)
        (cancontain shelftype penciltype)
        (cancontain shelftype keychaintype)
        (cancontain shelftype mugtype)
        (cancontain shelftype booktype)
        (cancontain safetype cellphonetype)
        (cancontain safetype keychaintype)
        (cancontain safetype creditcardtype)
        (cancontain safetype cdtype)
        (cancontain shelftype alarmclocktype)
        (cancontain shelftype pentype)
        (cancontain shelftype cellphonetype)
        (cancontain shelftype bowltype)
        (cancontain shelftype creditcardtype)
        (cancontain shelftype cdtype)
        (cancontain shelftype penciltype)
        (cancontain shelftype keychaintype)
        (cancontain shelftype mugtype)
        (cancontain shelftype booktype)
        (cancontain garbagecantype pentype)
        (cancontain garbagecantype cdtype)
        (cancontain garbagecantype penciltype)
        (cancontain bedtype cellphonetype)
        (cancontain bedtype baseballbattype)
        (cancontain bedtype pillowtype)
        (cancontain bedtype laptoptype)
        (cancontain bedtype basketballtype)
        (cancontain bedtype booktype)
        (cancontain shelftype alarmclocktype)
        (cancontain shelftype pentype)
        (cancontain shelftype cellphonetype)
        (cancontain shelftype bowltype)
        (cancontain shelftype creditcardtype)
        (cancontain shelftype cdtype)
        (cancontain shelftype penciltype)
        (cancontain shelftype keychaintype)
        (cancontain shelftype mugtype)
        (cancontain shelftype booktype)
        (cancontain desktype laptoptype)
        (cancontain desktype alarmclocktype)
        (cancontain desktype pentype)
        (cancontain desktype cellphonetype)
        (cancontain desktype bowltype)
        (cancontain desktype creditcardtype)
        (cancontain desktype cdtype)
        (cancontain desktype penciltype)
        (cancontain desktype keychaintype)
        (cancontain desktype mugtype)
        (cancontain desktype basketballtype)
        (cancontain desktype booktype)
        (pickupable pen1)
        (pickupable cellphone2)
        (pickupable alarmclock1)
        (pickupable bowl1)
        (pickupable bowl2)
        (pickupable book1)
        (pickupable alarmclock2)
        (pickupable laptop1)
        (pickupable keychain1)
        (pickupable pillow1)
        (pickupable baseballbat1)
        (pickupable pencil1)
        (pickupable cellphone1)
        (pickupable cd1)
        (pickupable keychain2)
        (pickupable keychain3)
        (pickupable mug1)
        (pickupable creditcard1)
        (pickupable basketball1)
        (pickupable pen2)
        
        (openable drawer1)
        (openable drawer6)
        (openable drawer3)
        (openable safe1)
        
        (notopenable bed1)
        (notopenable desk1)
        (notopenable desk2)
        (notopenable drawer2)
        (notopenable drawer4)
        (notopenable drawer5)
        (notopenable garbagecan1)
        (notopenable laundryhamper1)
        (notopenable shelf1)
        (notopenable shelf2)
        (notopenable shelf3)
        (notopenable shelf4)
        (notopenable shelf5)
        (notopenable shelf6)

        (closed drawer1)
        (closed drawer6)
        (closed drawer3)
        (closed safe1)

        (handempty agent1)
        (notvalidated)

        (atlocation agent1 location27)
        
        (cleanable bowl1)
        (cleanable bowl2)
        (cleanable mug1)
        
        (heatable mug1)
        (coolable bowl1)
        (coolable bowl2)
        (coolable mug1)
        
        
        (toggleable desklamp1)
        (isoff desklamp1)
        
        
        
        (inreceptacle bowl2 desk2)
        (inreceptacle alarmclock2 desk2)
        (inreceptacle cd1 desk2)
        (inreceptacle desklamp1 desk2)
        (inreceptacle laptop1 desk2)
        (inreceptacle creditcard1 drawer2)
        (inreceptacle pen2 drawer5)
        (inreceptacle keychain1 drawer5)
        (inreceptacle cellphone1 desk1)
        (inreceptacle pen1 desk1)
        (inreceptacle bowl1 desk1)
        (inreceptacle pillow1 bed1)
        (inreceptacle book1 bed1)
        (inreceptacle pencil1 drawer3)
        (inreceptacle alarmclock1 shelf3)
        (inreceptacle cellphone2 shelf6)
        (inreceptacle mug1 shelf5)
        (inreceptacle alarmclock2 shelf4)
        (inreceptacle desklamp1 shelf4)
        (inreceptacle bowl2 shelf4)
        (inreceptacle keychain2 safe1)
        (inreceptacle keychain3 safe1)
        
        
        (receptacleatlocation bed1 location13)
        (receptacleatlocation desk1 location3)
        (receptacleatlocation desk2 location10)
        (receptacleatlocation drawer1 location21)
        (receptacleatlocation drawer2 location18)
        (receptacleatlocation drawer3 location17)
        (receptacleatlocation drawer4 location12)
        (receptacleatlocation drawer5 location12)
        (receptacleatlocation drawer6 location1)
        (receptacleatlocation garbagecan1 location2)
        (receptacleatlocation laundryhamper1 location8)
        (receptacleatlocation safe1 location6)
        (receptacleatlocation shelf1 location20)
        (receptacleatlocation shelf2 location25)
        (receptacleatlocation shelf3 location11)
        (receptacleatlocation shelf4 location23)
        (receptacleatlocation shelf5 location22)
        (receptacleatlocation shelf6 location24)
        (objectatlocation cellphone1 location3)
        (objectatlocation keychain2 location6)
        (objectatlocation bowl2 location23)
        (objectatlocation pen2 location12)
        (objectatlocation alarmclock1 location11)
        (objectatlocation keychain3 location6)
        (objectatlocation chair2 location26)
        (objectatlocation book1 location13)
        (objectatlocation laundryhamperlid1 location8)
        (objectatlocation chair1 location21)
        (objectatlocation lightswitch1 location14)
        (objectatlocation alarmclock2 location23)
        (objectatlocation basketball1 location7)
        (objectatlocation pen1 location3)
        (objectatlocation laptop1 location10)
        (objectatlocation baseballbat1 location9)
        (objectatlocation bowl1 location3)
        (objectatlocation pillow1 location13)
        (objectatlocation keychain1 location12)
        (objectatlocation creditcard1 location18)
        (objectatlocation cellphone2 location24)
        (objectatlocation mirror1 location19)
        (objectatlocation desklamp1 location23)
        (objectatlocation cd1 location10)
        (objectatlocation window2 location4)
        (objectatlocation window1 location5)
        (objectatlocation pencil1 location17)
        (objectatlocation mug1 location22)
        (objectatlocation blinds1 location16)
        (objectatlocation blinds2 location15)
        )
    

        (:goal
            (and
                (validatepickandplace mugtype desktype)
                
                ;;(exists (?r - receptacle)
                ;;    (exists (?o - object)
                ;;        (and
                ;;            (inreceptacle ?o ?r)
                ;;            (objecttype ?o mugtype)
                ;;            (receptacletype ?r desktype)
                ;;        )
                ;;    )
                ;;)
            )
        )
         
    )
    

