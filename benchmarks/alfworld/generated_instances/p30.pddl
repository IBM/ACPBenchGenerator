
(define (problem plan_trial_t20190908_010306_215435)
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


        apple1 - object
        apple2 - object
        bowl1 - object
        bread1 - object
        butterknife1 - object
        cellphone1 - object
        cellphone2 - object
        cellphone3 - object
        chair1 - object
        chair2 - object
        creditcard1 - object
        cup1 - object
        dishsponge1 - object
        dishsponge2 - object
        egg1 - object
        egg2 - object
        egg3 - object
        faucet1 - object
        fork1 - object
        fork2 - object
        fork3 - object
        glassbottle1 - object
        glassbottle2 - object
        houseplant1 - object
        knife1 - object
        knife2 - object
        lettuce1 - object
        lettuce2 - object
        lightswitch1 - object
        mug1 - object
        mug2 - object
        mug3 - object
        pan1 - object
        papertowelroll1 - object
        peppershaker1 - object
        peppershaker2 - object
        peppershaker3 - object
        plate1 - object
        plate2 - object
        potato1 - object
        potato2 - object
        pot1 - object
        pot2 - object
        saltshaker1 - object
        saltshaker2 - object
        sink1 - object
        soapbottle1 - object
        soapbottle2 - object
        soapbottle3 - object
        spatula1 - object
        spatula2 - object
        spatula3 - object
        spoon1 - object
        spoon2 - object
        spoon3 - object
        statue1 - object
        stoveknob1 - object
        stoveknob2 - object
        stoveknob3 - object
        stoveknob4 - object
        tomato1 - object
        tomato2 - object
        vase1 - object
        vase2 - object
        window1 - object
        window2 - object
        cabinet1 - receptacle
        cabinet2 - receptacle
        cabinet3 - receptacle
        cabinet4 - receptacle
        cabinet5 - receptacle
        cabinet6 - receptacle
        coffeemachine1 - receptacle
        countertop1 - receptacle
        countertop2 - receptacle
        countertop3 - receptacle
        drawer1 - receptacle
        drawer2 - receptacle
        drawer3 - receptacle
        fridge1 - receptacle
        garbagecan1 - receptacle
        microwave1 - receptacle
        shelf1 - receptacle
        shelf2 - receptacle
        shelf3 - receptacle
        sinkbasin1 - receptacle
        stoveburner1 - receptacle
        stoveburner2 - receptacle
        stoveburner3 - receptacle
        stoveburner4 - receptacle
        toaster1 - receptacle
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
        location28 - location
        location29 - location
        location30 - location
        location31 - location
        )
    

(:init

         


        (receptacletype microwave1 microwavetype)
        (receptacletype drawer1 drawertype)
        (receptacletype shelf2 shelftype)
        (receptacletype cabinet4 cabinettype)
        (receptacletype shelf1 shelftype)
        (receptacletype cabinet1 cabinettype)
        (receptacletype stoveburner3 stoveburnertype)
        (receptacletype countertop1 countertoptype)
        (receptacletype cabinet3 cabinettype)
        (receptacletype cabinet2 cabinettype)
        (receptacletype stoveburner1 stoveburnertype)
        (receptacletype cabinet6 cabinettype)
        (receptacletype drawer3 drawertype)
        (receptacletype countertop3 countertoptype)
        (receptacletype coffeemachine1 coffeemachinetype)
        (receptacletype stoveburner4 stoveburnertype)
        (receptacletype cabinet5 cabinettype)
        (receptacletype sinkbasin1 sinkbasintype)
        (receptacletype garbagecan1 garbagecantype)
        (receptacletype countertop2 countertoptype)
        (receptacletype stoveburner2 stoveburnertype)
        (receptacletype fridge1 fridgetype)
        (receptacletype toaster1 toastertype)
        (receptacletype shelf3 shelftype)
        (receptacletype drawer2 drawertype)
        (objecttype cellphone2 cellphonetype)
        (objecttype pan1 pantype)
        (objecttype saltshaker1 saltshakertype)
        (objecttype butterknife1 butterknifetype)
        (objecttype houseplant1 houseplanttype)
        (objecttype apple1 appletype)
        (objecttype glassbottle1 glassbottletype)
        (objecttype spoon1 spoontype)
        (objecttype window1 windowtype)
        (objecttype spatula3 spatulatype)
        (objecttype apple2 appletype)
        (objecttype peppershaker1 peppershakertype)
        (objecttype glassbottle2 glassbottletype)
        (objecttype lettuce1 lettucetype)
        (objecttype tomato2 tomatotype)
        (objecttype chair1 chairtype)
        (objecttype plate1 platetype)
        (objecttype spoon2 spoontype)
        (objecttype bowl1 bowltype)
        (objecttype peppershaker3 peppershakertype)
        (objecttype bread1 breadtype)
        (objecttype soapbottle1 soapbottletype)
        (objecttype egg2 eggtype)
        (objecttype creditcard1 creditcardtype)
        (objecttype vase2 vasetype)
        (objecttype fork1 forktype)
        (objecttype cup1 cuptype)
        (objecttype peppershaker2 peppershakertype)
        (objecttype spoon3 spoontype)
        (objecttype stoveknob4 stoveknobtype)
        (objecttype potato2 potatotype)
        (objecttype plate2 platetype)
        (objecttype soapbottle3 soapbottletype)
        (objecttype mug2 mugtype)
        (objecttype knife1 knifetype)
        (objecttype cellphone1 cellphonetype)
        (objecttype statue1 statuetype)
        (objecttype saltshaker2 saltshakertype)
        (objecttype vase1 vasetype)
        (objecttype lightswitch1 lightswitchtype)
        (objecttype stoveknob3 stoveknobtype)
        (objecttype soapbottle2 soapbottletype)
        (objecttype pot1 pottype)
        (objecttype papertowelroll1 papertowelrolltype)
        (objecttype mug3 mugtype)
        (objecttype sink1 sinktype)
        (objecttype dishsponge2 dishspongetype)
        (objecttype spatula1 spatulatype)
        (objecttype knife2 knifetype)
        (objecttype chair2 chairtype)
        (objecttype dishsponge1 dishspongetype)
        (objecttype stoveknob1 stoveknobtype)
        (objecttype fork2 forktype)
        (objecttype fork3 forktype)
        (objecttype stoveknob2 stoveknobtype)
        (objecttype mug1 mugtype)
        (objecttype spatula2 spatulatype)
        (objecttype potato1 potatotype)
        (objecttype window2 windowtype)
        (objecttype egg3 eggtype)
        (objecttype lettuce2 lettucetype)
        (objecttype egg1 eggtype)
        (objecttype cellphone3 cellphonetype)
        (objecttype tomato1 tomatotype)
        (objecttype pot2 pottype)
        (cancontain microwavetype appletype)
        (cancontain microwavetype glassbottletype)
        (cancontain microwavetype mugtype)
        (cancontain microwavetype tomatotype)
        (cancontain microwavetype bowltype)
        (cancontain microwavetype cuptype)
        (cancontain microwavetype platetype)
        (cancontain microwavetype eggtype)
        (cancontain microwavetype potatotype)
        (cancontain microwavetype breadtype)
        (cancontain drawertype peppershakertype)
        (cancontain drawertype forktype)
        (cancontain drawertype cellphonetype)
        (cancontain drawertype knifetype)
        (cancontain drawertype spatulatype)
        (cancontain drawertype soapbottletype)
        (cancontain drawertype creditcardtype)
        (cancontain drawertype saltshakertype)
        (cancontain drawertype spoontype)
        (cancontain drawertype butterknifetype)
        (cancontain drawertype dishspongetype)
        (cancontain shelftype peppershakertype)
        (cancontain shelftype cellphonetype)
        (cancontain shelftype bowltype)
        (cancontain shelftype soapbottletype)
        (cancontain shelftype cuptype)
        (cancontain shelftype creditcardtype)
        (cancontain shelftype statuetype)
        (cancontain shelftype saltshakertype)
        (cancontain shelftype vasetype)
        (cancontain shelftype glassbottletype)
        (cancontain shelftype mugtype)
        (cancontain shelftype platetype)
        (cancontain shelftype dishspongetype)
        (cancontain shelftype pottype)
        (cancontain cabinettype peppershakertype)
        (cancontain cabinettype bowltype)
        (cancontain cabinettype soapbottletype)
        (cancontain cabinettype cuptype)
        (cancontain cabinettype pantype)
        (cancontain cabinettype saltshakertype)
        (cancontain cabinettype vasetype)
        (cancontain cabinettype mugtype)
        (cancontain cabinettype glassbottletype)
        (cancontain cabinettype platetype)
        (cancontain cabinettype dishspongetype)
        (cancontain cabinettype pottype)
        (cancontain shelftype peppershakertype)
        (cancontain shelftype cellphonetype)
        (cancontain shelftype bowltype)
        (cancontain shelftype soapbottletype)
        (cancontain shelftype cuptype)
        (cancontain shelftype creditcardtype)
        (cancontain shelftype statuetype)
        (cancontain shelftype saltshakertype)
        (cancontain shelftype vasetype)
        (cancontain shelftype glassbottletype)
        (cancontain shelftype mugtype)
        (cancontain shelftype platetype)
        (cancontain shelftype dishspongetype)
        (cancontain shelftype pottype)
        (cancontain cabinettype peppershakertype)
        (cancontain cabinettype bowltype)
        (cancontain cabinettype soapbottletype)
        (cancontain cabinettype cuptype)
        (cancontain cabinettype pantype)
        (cancontain cabinettype saltshakertype)
        (cancontain cabinettype vasetype)
        (cancontain cabinettype mugtype)
        (cancontain cabinettype glassbottletype)
        (cancontain cabinettype platetype)
        (cancontain cabinettype dishspongetype)
        (cancontain cabinettype pottype)
        (cancontain stoveburnertype pantype)
        (cancontain stoveburnertype pottype)
        (cancontain countertoptype peppershakertype)
        (cancontain countertoptype forktype)
        (cancontain countertoptype cellphonetype)
        (cancontain countertoptype knifetype)
        (cancontain countertoptype bowltype)
        (cancontain countertoptype spatulatype)
        (cancontain countertoptype soapbottletype)
        (cancontain countertoptype cuptype)
        (cancontain countertoptype creditcardtype)
        (cancontain countertoptype pantype)
        (cancontain countertoptype tomatotype)
        (cancontain countertoptype statuetype)
        (cancontain countertoptype saltshakertype)
        (cancontain countertoptype potatotype)
        (cancontain countertoptype vasetype)
        (cancontain countertoptype spoontype)
        (cancontain countertoptype appletype)
        (cancontain countertoptype glassbottletype)
        (cancontain countertoptype mugtype)
        (cancontain countertoptype butterknifetype)
        (cancontain countertoptype platetype)
        (cancontain countertoptype dishspongetype)
        (cancontain countertoptype eggtype)
        (cancontain countertoptype pottype)
        (cancontain countertoptype lettucetype)
        (cancontain countertoptype breadtype)
        (cancontain cabinettype peppershakertype)
        (cancontain cabinettype bowltype)
        (cancontain cabinettype soapbottletype)
        (cancontain cabinettype cuptype)
        (cancontain cabinettype pantype)
        (cancontain cabinettype saltshakertype)
        (cancontain cabinettype vasetype)
        (cancontain cabinettype mugtype)
        (cancontain cabinettype glassbottletype)
        (cancontain cabinettype platetype)
        (cancontain cabinettype dishspongetype)
        (cancontain cabinettype pottype)
        (cancontain cabinettype peppershakertype)
        (cancontain cabinettype bowltype)
        (cancontain cabinettype soapbottletype)
        (cancontain cabinettype cuptype)
        (cancontain cabinettype pantype)
        (cancontain cabinettype saltshakertype)
        (cancontain cabinettype vasetype)
        (cancontain cabinettype mugtype)
        (cancontain cabinettype glassbottletype)
        (cancontain cabinettype platetype)
        (cancontain cabinettype dishspongetype)
        (cancontain cabinettype pottype)
        (cancontain stoveburnertype pantype)
        (cancontain stoveburnertype pottype)
        (cancontain cabinettype peppershakertype)
        (cancontain cabinettype bowltype)
        (cancontain cabinettype soapbottletype)
        (cancontain cabinettype cuptype)
        (cancontain cabinettype pantype)
        (cancontain cabinettype saltshakertype)
        (cancontain cabinettype vasetype)
        (cancontain cabinettype mugtype)
        (cancontain cabinettype glassbottletype)
        (cancontain cabinettype platetype)
        (cancontain cabinettype dishspongetype)
        (cancontain cabinettype pottype)
        (cancontain drawertype peppershakertype)
        (cancontain drawertype forktype)
        (cancontain drawertype cellphonetype)
        (cancontain drawertype knifetype)
        (cancontain drawertype spatulatype)
        (cancontain drawertype soapbottletype)
        (cancontain drawertype creditcardtype)
        (cancontain drawertype saltshakertype)
        (cancontain drawertype spoontype)
        (cancontain drawertype butterknifetype)
        (cancontain drawertype dishspongetype)
        (cancontain countertoptype peppershakertype)
        (cancontain countertoptype forktype)
        (cancontain countertoptype cellphonetype)
        (cancontain countertoptype knifetype)
        (cancontain countertoptype bowltype)
        (cancontain countertoptype spatulatype)
        (cancontain countertoptype soapbottletype)
        (cancontain countertoptype cuptype)
        (cancontain countertoptype creditcardtype)
        (cancontain countertoptype pantype)
        (cancontain countertoptype tomatotype)
        (cancontain countertoptype statuetype)
        (cancontain countertoptype saltshakertype)
        (cancontain countertoptype potatotype)
        (cancontain countertoptype vasetype)
        (cancontain countertoptype spoontype)
        (cancontain countertoptype appletype)
        (cancontain countertoptype glassbottletype)
        (cancontain countertoptype mugtype)
        (cancontain countertoptype butterknifetype)
        (cancontain countertoptype platetype)
        (cancontain countertoptype dishspongetype)
        (cancontain countertoptype eggtype)
        (cancontain countertoptype pottype)
        (cancontain countertoptype lettucetype)
        (cancontain countertoptype breadtype)
        (cancontain coffeemachinetype mugtype)
        (cancontain stoveburnertype pantype)
        (cancontain stoveburnertype pottype)
        (cancontain cabinettype peppershakertype)
        (cancontain cabinettype bowltype)
        (cancontain cabinettype soapbottletype)
        (cancontain cabinettype cuptype)
        (cancontain cabinettype pantype)
        (cancontain cabinettype saltshakertype)
        (cancontain cabinettype vasetype)
        (cancontain cabinettype mugtype)
        (cancontain cabinettype glassbottletype)
        (cancontain cabinettype platetype)
        (cancontain cabinettype dishspongetype)
        (cancontain cabinettype pottype)
        (cancontain sinkbasintype forktype)
        (cancontain sinkbasintype knifetype)
        (cancontain sinkbasintype bowltype)
        (cancontain sinkbasintype spatulatype)
        (cancontain sinkbasintype cuptype)
        (cancontain sinkbasintype tomatotype)
        (cancontain sinkbasintype pantype)
        (cancontain sinkbasintype potatotype)
        (cancontain sinkbasintype spoontype)
        (cancontain sinkbasintype appletype)
        (cancontain sinkbasintype glassbottletype)
        (cancontain sinkbasintype mugtype)
        (cancontain sinkbasintype butterknifetype)
        (cancontain sinkbasintype platetype)
        (cancontain sinkbasintype dishspongetype)
        (cancontain sinkbasintype eggtype)
        (cancontain sinkbasintype pottype)
        (cancontain sinkbasintype lettucetype)
        (cancontain garbagecantype soapbottletype)
        (cancontain garbagecantype tomatotype)
        (cancontain garbagecantype potatotype)
        (cancontain garbagecantype appletype)
        (cancontain garbagecantype breadtype)
        (cancontain garbagecantype dishspongetype)
        (cancontain garbagecantype eggtype)
        (cancontain garbagecantype lettucetype)
        (cancontain countertoptype peppershakertype)
        (cancontain countertoptype forktype)
        (cancontain countertoptype cellphonetype)
        (cancontain countertoptype knifetype)
        (cancontain countertoptype bowltype)
        (cancontain countertoptype spatulatype)
        (cancontain countertoptype soapbottletype)
        (cancontain countertoptype cuptype)
        (cancontain countertoptype creditcardtype)
        (cancontain countertoptype pantype)
        (cancontain countertoptype tomatotype)
        (cancontain countertoptype statuetype)
        (cancontain countertoptype saltshakertype)
        (cancontain countertoptype potatotype)
        (cancontain countertoptype vasetype)
        (cancontain countertoptype spoontype)
        (cancontain countertoptype appletype)
        (cancontain countertoptype glassbottletype)
        (cancontain countertoptype mugtype)
        (cancontain countertoptype butterknifetype)
        (cancontain countertoptype platetype)
        (cancontain countertoptype dishspongetype)
        (cancontain countertoptype eggtype)
        (cancontain countertoptype pottype)
        (cancontain countertoptype lettucetype)
        (cancontain countertoptype breadtype)
        (cancontain stoveburnertype pantype)
        (cancontain stoveburnertype pottype)
        (cancontain fridgetype bowltype)
        (cancontain fridgetype cuptype)
        (cancontain fridgetype tomatotype)
        (cancontain fridgetype pantype)
        (cancontain fridgetype potatotype)
        (cancontain fridgetype appletype)
        (cancontain fridgetype glassbottletype)
        (cancontain fridgetype mugtype)
        (cancontain fridgetype platetype)
        (cancontain fridgetype breadtype)
        (cancontain fridgetype eggtype)
        (cancontain fridgetype pottype)
        (cancontain fridgetype lettucetype)
        (cancontain shelftype peppershakertype)
        (cancontain shelftype cellphonetype)
        (cancontain shelftype bowltype)
        (cancontain shelftype soapbottletype)
        (cancontain shelftype cuptype)
        (cancontain shelftype creditcardtype)
        (cancontain shelftype statuetype)
        (cancontain shelftype saltshakertype)
        (cancontain shelftype vasetype)
        (cancontain shelftype glassbottletype)
        (cancontain shelftype mugtype)
        (cancontain shelftype platetype)
        (cancontain shelftype dishspongetype)
        (cancontain shelftype pottype)
        (cancontain drawertype peppershakertype)
        (cancontain drawertype forktype)
        (cancontain drawertype cellphonetype)
        (cancontain drawertype knifetype)
        (cancontain drawertype spatulatype)
        (cancontain drawertype soapbottletype)
        (cancontain drawertype creditcardtype)
        (cancontain drawertype saltshakertype)
        (cancontain drawertype spoontype)
        (cancontain drawertype butterknifetype)
        (cancontain drawertype dishspongetype)
        (pickupable cellphone2)
        (pickupable pan1)
        (pickupable saltshaker1)
        (pickupable butterknife1)
        (pickupable apple1)
        (pickupable glassbottle1)
        (pickupable spoon1)
        (pickupable spatula3)
        (pickupable apple2)
        (pickupable peppershaker1)
        (pickupable glassbottle2)
        (pickupable lettuce1)
        (pickupable tomato2)
        (pickupable plate1)
        (pickupable spoon2)
        (pickupable bowl1)
        (pickupable peppershaker3)
        (pickupable bread1)
        (pickupable soapbottle1)
        (pickupable egg2)
        (pickupable creditcard1)
        (pickupable vase2)
        (pickupable fork1)
        (pickupable cup1)
        (pickupable peppershaker2)
        (pickupable spoon3)
        (pickupable potato2)
        (pickupable plate2)
        (pickupable soapbottle3)
        (pickupable mug2)
        (pickupable knife1)
        (pickupable cellphone1)
        (pickupable statue1)
        (pickupable saltshaker2)
        (pickupable vase1)
        (pickupable soapbottle2)
        (pickupable pot1)
        (pickupable papertowelroll1)
        (pickupable mug3)
        (pickupable dishsponge2)
        (pickupable spatula1)
        (pickupable knife2)
        (pickupable dishsponge1)
        (pickupable fork2)
        (pickupable fork3)
        (pickupable mug1)
        (pickupable spatula2)
        (pickupable potato1)
        (pickupable egg3)
        (pickupable lettuce2)
        (pickupable egg1)
        (pickupable cellphone3)
        (pickupable tomato1)
        (pickupable pot2)
        
        (openable microwave1)
        (openable drawer1)
        (openable cabinet1)
        (openable cabinet2)
        (openable drawer3)
        (openable cabinet5)
        (openable fridge1)
        (openable drawer2)

        (notopenable cabinet3)
        (notopenable cabinet4)
        (notopenable cabinet6)
        (notopenable coffeemachine1)
        (notopenable countertop1)
        (notopenable countertop2)
        (notopenable countertop3)
        (notopenable garbagecan1)
        (notopenable shelf1)
        (notopenable shelf2)
        (notopenable shelf3)
        (notopenable sinkbasin1)
        (notopenable stoveburner1)
        (notopenable stoveburner2)
        (notopenable stoveburner3)
        (notopenable stoveburner4)
        (notopenable toaster1)
 

        (closed microwave1)
        (closed drawer1)
        (closed cabinet1)
        (closed cabinet2)
        (closed drawer3)
        (closed cabinet5)
        (closed fridge1)
        (closed drawer2)

        (handempty agent1)
        (notvalidated)


        
        (atlocation agent1 location31)
        
        (cleanable pan1)
        (cleanable butterknife1)
        (cleanable apple1)
        (cleanable spoon1)
        (cleanable spatula3)
        (cleanable apple2)
        (cleanable lettuce1)
        (cleanable tomato2)
        (cleanable plate1)
        (cleanable spoon2)
        (cleanable bowl1)
        (cleanable egg2)
        (cleanable fork1)
        (cleanable cup1)
        (cleanable spoon3)
        (cleanable potato2)
        (cleanable plate2)
        (cleanable mug2)
        (cleanable knife1)
        (cleanable pot1)
        (cleanable mug3)
        (cleanable dishsponge2)
        (cleanable spatula1)
        (cleanable knife2)
        (cleanable dishsponge1)
        (cleanable fork2)
        (cleanable fork3)
        (cleanable mug1)
        (cleanable spatula2)
        (cleanable potato1)
        (cleanable egg3)
        (cleanable lettuce2)
        (cleanable egg1)
        (cleanable tomato1)
        (cleanable pot2)
        
        (heatable apple1)
        (heatable apple2)
        (heatable tomato2)
        (heatable plate1)
        (heatable bread1)
        (heatable egg2)
        (heatable cup1)
        (heatable potato2)
        (heatable plate2)
        (heatable mug2)
        (heatable mug3)
        (heatable mug1)
        (heatable potato1)
        (heatable egg3)
        (heatable egg1)
        (heatable tomato1)
        (coolable pan1)
        (coolable apple1)
        (coolable apple2)
        (coolable lettuce1)
        (coolable tomato2)
        (coolable plate1)
        (coolable bowl1)
        (coolable bread1)
        (coolable egg2)
        (coolable cup1)
        (coolable potato2)
        (coolable plate2)
        (coolable mug2)
        (coolable pot1)
        (coolable mug3)
        (coolable mug1)
        (coolable potato1)
        (coolable egg3)
        (coolable lettuce2)
        (coolable egg1)
        (coolable tomato1)
        (coolable pot2)
        
        
        
        
        
        (sliceable apple1)
        (sliceable apple2)
        (sliceable lettuce1)
        (sliceable tomato2)
        (sliceable bread1)
        (sliceable egg2)
        (sliceable potato2)
        (sliceable potato1)
        (sliceable egg3)
        (sliceable lettuce2)
        (sliceable egg1)
        (sliceable tomato1)
        
        (inreceptacle pan1 stoveburner1)
        (inreceptacle saltshaker1 cabinet1)
        (inreceptacle pot1 stoveburner4)
        (inreceptacle pot1 stoveburner2)
        (inreceptacle fork2 drawer3)
        (inreceptacle cellphone1 drawer3)
        (inreceptacle peppershaker3 cabinet5)
        (inreceptacle creditcard1 countertop3)
        (inreceptacle cellphone2 countertop3)
        (inreceptacle houseplant1 countertop3)
        (inreceptacle pot2 countertop3)
        (inreceptacle spoon3 countertop3)
        (inreceptacle apple2 countertop3)
        (inreceptacle spatula3 countertop3)
        (inreceptacle glassbottle2 countertop3)
        (inreceptacle plate2 countertop3)
        (inreceptacle spoon2 countertop3)
        (inreceptacle cellphone3 countertop3)
        (inreceptacle bread1 countertop3)
        (inreceptacle statue1 countertop3)
        (inreceptacle knife1 countertop1)
        (inreceptacle butterknife1 countertop1)
        (inreceptacle mug3 countertop1)
        (inreceptacle peppershaker1 countertop1)
        (inreceptacle tomato1 countertop1)
        (inreceptacle pan1 stoveburner3)
        (inreceptacle spatula1 drawer1)
        (inreceptacle dishsponge1 cabinet2)
        (inreceptacle soapbottle1 countertop2)
        (inreceptacle fork1 countertop2)
        (inreceptacle cup1 countertop2)
        (inreceptacle spoon1 countertop2)
        (inreceptacle mug1 countertop2)
        (inreceptacle soapbottle2 countertop2)
        (inreceptacle spatula2 countertop2)
        (inreceptacle peppershaker2 cabinet6)
        (inreceptacle mug2 cabinet6)
        (inreceptacle vase1 cabinet3)
        (inreceptacle soapbottle3 cabinet4)
        (inreceptacle glassbottle1 cabinet4)
        (inreceptacle bowl1 shelf2)
        (inreceptacle saltshaker2 shelf2)
        (inreceptacle mug1 coffeemachine1)
        (inreceptacle vase2 shelf1)
        (inreceptacle papertowelroll1 garbagecan1)
        (inreceptacle lettuce2 garbagecan1)
        (inreceptacle fork3 sinkbasin1)
        (inreceptacle knife2 sinkbasin1)
        (inreceptacle lettuce1 sinkbasin1)
        (inreceptacle dishsponge2 sinkbasin1)
        (inreceptacle egg3 sinkbasin1)
        (inreceptacle tomato2 sinkbasin1)
        (inreceptacle potato2 sinkbasin1)
        (inreceptacle egg2 microwave1)
        (inreceptacle egg1 fridge1)
        (inreceptacle potato1 fridge1)
        (inreceptacle apple1 fridge1)
        (inreceptacle plate1 fridge1)
        
        
        (receptacleatlocation cabinet1 location19)
        (receptacleatlocation cabinet2 location22)
        (receptacleatlocation cabinet3 location16)
        (receptacleatlocation cabinet4 location14)
        (receptacleatlocation cabinet5 location13)
        (receptacleatlocation cabinet6 location4)
        (receptacleatlocation coffeemachine1 location11)
        (receptacleatlocation countertop1 location2)
        (receptacleatlocation countertop2 location11)
        (receptacleatlocation countertop3 location3)
        (receptacleatlocation drawer1 location20)
        (receptacleatlocation drawer2 location15)
        (receptacleatlocation drawer3 location27)
        (receptacleatlocation fridge1 location10)
        (receptacleatlocation garbagecan1 location8)
        (receptacleatlocation microwave1 location24)
        (receptacleatlocation shelf1 location17)
        (receptacleatlocation shelf2 location29)
        (receptacleatlocation shelf3 location26)
        (receptacleatlocation sinkbasin1 location6)
        (receptacleatlocation stoveburner1 location5)
        (receptacleatlocation stoveburner2 location21)
        (receptacleatlocation stoveburner3 location5)
        (receptacleatlocation stoveburner4 location21)
        (receptacleatlocation toaster1 location9)
        (objectatlocation mug1 location11)
        (objectatlocation spoon3 location3)
        (objectatlocation dishsponge2 location6)
        (objectatlocation soapbottle2 location11)
        (objectatlocation peppershaker3 location13)
        (objectatlocation saltshaker1 location19)
        (objectatlocation egg3 location6)
        (objectatlocation tomato2 location6)
        (objectatlocation spatula3 location3)
        (objectatlocation pot1 location21)
        (objectatlocation apple2 location3)
        (objectatlocation plate1 location10)
        (objectatlocation lettuce2 location8)
        (objectatlocation fork3 location6)
        (objectatlocation knife1 location2)
        (objectatlocation potato2 location6)
        (objectatlocation cellphone2 location3)
        (objectatlocation glassbottle1 location14)
        (objectatlocation mug2 location4)
        (objectatlocation peppershaker1 location2)
        (objectatlocation soapbottle1 location11)
        (objectatlocation egg2 location24)
        (objectatlocation spatula2 location11)
        (objectatlocation spoon2 location3)
        (objectatlocation fork2 location27)
        (objectatlocation cellphone1 location27)
        (objectatlocation sink1 location6)
        (objectatlocation statue1 location3)
        (objectatlocation glassbottle2 location3)
        (objectatlocation bread1 location3)
        (objectatlocation creditcard1 location3)
        (objectatlocation cellphone3 location3)
        (objectatlocation lightswitch1 location25)
        (objectatlocation potato1 location10)
        (objectatlocation knife2 location6)
        (objectatlocation stoveknob3 location12)
        (objectatlocation stoveknob4 location7)
        (objectatlocation stoveknob1 location18)
        (objectatlocation stoveknob2 location12)
        (objectatlocation fork1 location11)
        (objectatlocation pan1 location5)
        (objectatlocation lettuce1 location6)
        (objectatlocation plate2 location3)
        (objectatlocation apple1 location10)
        (objectatlocation pot2 location3)
        (objectatlocation window1 location30)
        (objectatlocation window2 location28)
        (objectatlocation spatula1 location20)
        (objectatlocation papertowelroll1 location8)
        (objectatlocation tomato1 location2)
        (objectatlocation egg1 location10)
        (objectatlocation saltshaker2 location29)
        (objectatlocation peppershaker2 location4)
        (objectatlocation vase2 location17)
        (objectatlocation butterknife1 location2)
        (objectatlocation soapbottle3 location14)
        (objectatlocation vase1 location16)
        (objectatlocation bowl1 location29)
        (objectatlocation dishsponge1 location22)
        (objectatlocation chair2 location1)
        (objectatlocation chair1 location23)
        (objectatlocation spoon1 location11)
        (objectatlocation cup1 location11)
        (objectatlocation houseplant1 location3)
        (objectatlocation mug3 location2)
        )
    

                (:goal
                    (and
                        (validatepicktwoandplace  peppershakertype drawertype)

                        ;;(exists (?r - receptacle)
                        ;;    (exists (?o1 - object)
                        ;;        (and
                        ;;            (objecttype ?o1 peppershakertype)
                        ;;            (receptacletype ?r drawertype)
                        ;;            (inreceptacle ?o1 ?r)
                        ;;           (exists (?o2 - object)
                        ;;                (and
                        ;;                    (not (= ?o1 ?o2))
                        ;;                    (objecttype ?o2 peppershakertype)
                        ;;                    (receptacletype ?r drawertype)
                        ;;                    (inreceptacle ?o2 ?r)
                        ;;                )
                        ;;            )
                        ;;        )
                        ;;    )
                        ;;)
                    )
                )
                 
            )
            

