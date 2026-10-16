
(define (problem plan_trial_t20190909_121710_650938)
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
        bowl1 - object
        bread1 - object
        butterknife1 - object
        butterknife2 - object
        butterknife3 - object
        cellphone1 - object
        cellphone2 - object
        cellphone3 - object
        chair1 - object
        chair2 - object
        creditcard1 - object
        creditcard2 - object
        creditcard3 - object
        cup1 - object
        cup2 - object
        dishsponge1 - object
        dishsponge2 - object
        dishsponge3 - object
        egg1 - object
        egg2 - object
        egg3 - object
        faucet1 - object
        fork1 - object
        fork2 - object
        fork3 - object
        glassbottle1 - object
        houseplant1 - object
        knife1 - object
        knife2 - object
        lettuce1 - object
        lightswitch1 - object
        mug1 - object
        mug2 - object
        pan1 - object
        papertowelroll1 - object
        peppershaker1 - object
        plate1 - object
        plate2 - object
        plate3 - object
        potato1 - object
        potato2 - object
        potato3 - object
        pot1 - object
        pot2 - object
        saltshaker1 - object
        saltshaker2 - object
        saltshaker3 - object
        sink1 - object
        soapbottle1 - object
        spatula1 - object
        spatula2 - object
        spoon1 - object
        statue1 - object
        statue2 - object
        stoveknob1 - object
        stoveknob2 - object
        stoveknob3 - object
        stoveknob4 - object
        tomato1 - object
        tomato2 - object
        vase1 - object
        vase2 - object
        vase3 - object
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
        location32 - location
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
        (objecttype cellphone1 cellphonetype)
        (objecttype pan1 pantype)
        (objecttype bowl1 bowltype)
        (objecttype creditcard2 creditcardtype)
        (objecttype creditcard1 creditcardtype)
        (objecttype lettuce1 lettucetype)
        (objecttype houseplant1 houseplanttype)
        (objecttype saltshaker2 saltshakertype)
        (objecttype vase2 vasetype)
        (objecttype tomato2 tomatotype)
        (objecttype plate1 platetype)
        (objecttype window1 windowtype)
        (objecttype papertowelroll1 papertowelrolltype)
        (objecttype dishsponge2 dishspongetype)
        (objecttype cellphone3 cellphonetype)
        (objecttype tomato1 tomatotype)
        (objecttype chair1 chairtype)
        (objecttype cellphone2 cellphonetype)
        (objecttype apple1 appletype)
        (objecttype fork2 forktype)
        (objecttype butterknife1 butterknifetype)
        (objecttype potato1 potatotype)
        (objecttype vase3 vasetype)
        (objecttype dishsponge1 dishspongetype)
        (objecttype stoveknob4 stoveknobtype)
        (objecttype saltshaker3 saltshakertype)
        (objecttype potato3 potatotype)
        (objecttype glassbottle1 glassbottletype)
        (objecttype cup2 cuptype)
        (objecttype knife2 knifetype)
        (objecttype butterknife3 butterknifetype)
        (objecttype peppershaker1 peppershakertype)
        (objecttype bread1 breadtype)
        (objecttype fork3 forktype)
        (objecttype spatula2 spatulatype)
        (objecttype saltshaker1 saltshakertype)
        (objecttype pot2 pottype)
        (objecttype egg2 eggtype)
        (objecttype spatula1 spatulatype)
        (objecttype fork1 forktype)
        (objecttype pot1 pottype)
        (objecttype lightswitch1 lightswitchtype)
        (objecttype stoveknob3 stoveknobtype)
        (objecttype vase1 vasetype)
        (objecttype sink1 sinktype)
        (objecttype soapbottle1 soapbottletype)
        (objecttype chair2 chairtype)
        (objecttype spoon1 spoontype)
        (objecttype egg3 eggtype)
        (objecttype stoveknob1 stoveknobtype)
        (objecttype mug2 mugtype)
        (objecttype creditcard3 creditcardtype)
        (objecttype plate3 platetype)
        (objecttype cup1 cuptype)
        (objecttype knife1 knifetype)
        (objecttype mug1 mugtype)
        (objecttype statue1 statuetype)
        (objecttype stoveknob2 stoveknobtype)
        (objecttype egg1 eggtype)
        (objecttype window2 windowtype)
        (objecttype statue2 statuetype)
        (objecttype dishsponge3 dishspongetype)
        (objecttype potato2 potatotype)
        (objecttype butterknife2 butterknifetype)
        (objecttype plate2 platetype)
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
        (pickupable cellphone1)
        (pickupable pan1)
        (pickupable bowl1)
        (pickupable creditcard2)
        (pickupable creditcard1)
        (pickupable lettuce1)
        (pickupable saltshaker2)
        (pickupable vase2)
        (pickupable tomato2)
        (pickupable plate1)
        (pickupable papertowelroll1)
        (pickupable dishsponge2)
        (pickupable cellphone3)
        (pickupable tomato1)
        (pickupable cellphone2)
        (pickupable apple1)
        (pickupable fork2)
        (pickupable butterknife1)
        (pickupable potato1)
        (pickupable vase3)
        (pickupable dishsponge1)
        (pickupable saltshaker3)
        (pickupable potato3)
        (pickupable glassbottle1)
        (pickupable cup2)
        (pickupable knife2)
        (pickupable butterknife3)
        (pickupable peppershaker1)
        (pickupable bread1)
        (pickupable fork3)
        (pickupable spatula2)
        (pickupable saltshaker1)
        (pickupable pot2)
        (pickupable egg2)
        (pickupable spatula1)
        (pickupable fork1)
        (pickupable pot1)
        (pickupable vase1)
        (pickupable soapbottle1)
        (pickupable spoon1)
        (pickupable egg3)
        (pickupable mug2)
        (pickupable creditcard3)
        (pickupable plate3)
        (pickupable cup1)
        (pickupable knife1)
        (pickupable mug1)
        (pickupable statue1)
        (pickupable egg1)
        (pickupable statue2)
        (pickupable dishsponge3)
        (pickupable potato2)
        (pickupable butterknife2)
        (pickupable plate2)
        
        
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


        (atlocation agent1 location32)
        
        (cleanable pan1)
        (cleanable bowl1)
        (cleanable lettuce1)
        (cleanable tomato2)
        (cleanable plate1)
        (cleanable dishsponge2)
        (cleanable tomato1)
        (cleanable apple1)
        (cleanable fork2)
        (cleanable butterknife1)
        (cleanable potato1)
        (cleanable dishsponge1)
        (cleanable potato3)
        (cleanable cup2)
        (cleanable knife2)
        (cleanable butterknife3)
        (cleanable fork3)
        (cleanable spatula2)
        (cleanable pot2)
        (cleanable egg2)
        (cleanable spatula1)
        (cleanable fork1)
        (cleanable pot1)
        (cleanable spoon1)
        (cleanable egg3)
        (cleanable mug2)
        (cleanable plate3)
        (cleanable cup1)
        (cleanable knife1)
        (cleanable mug1)
        (cleanable egg1)
        (cleanable dishsponge3)
        (cleanable potato2)
        (cleanable butterknife2)
        (cleanable plate2)
        
        (heatable tomato2)
        (heatable plate1)
        (heatable tomato1)
        (heatable apple1)
        (heatable potato1)
        (heatable potato3)
        (heatable cup2)
        (heatable bread1)
        (heatable egg2)
        (heatable egg3)
        (heatable mug2)
        (heatable plate3)
        (heatable cup1)
        (heatable mug1)
        (heatable egg1)
        (heatable potato2)
        (heatable plate2)
        (coolable pan1)
        (coolable bowl1)
        (coolable lettuce1)
        (coolable tomato2)
        (coolable plate1)
        (coolable tomato1)
        (coolable apple1)
        (coolable potato1)
        (coolable potato3)
        (coolable cup2)
        (coolable bread1)
        (coolable pot2)
        (coolable egg2)
        (coolable pot1)
        (coolable egg3)
        (coolable mug2)
        (coolable plate3)
        (coolable cup1)
        (coolable mug1)
        (coolable egg1)
        (coolable potato2)
        (coolable plate2)
        
        
        
        
        
        (sliceable lettuce1)
        (sliceable tomato2)
        (sliceable tomato1)
        (sliceable apple1)
        (sliceable potato1)
        (sliceable potato3)
        (sliceable bread1)
        (sliceable egg2)
        (sliceable egg3)
        (sliceable egg1)
        (sliceable potato2)
        
        (inreceptacle pan1 stoveburner1)
        (inreceptacle pot1 stoveburner4)
        (inreceptacle pot1 stoveburner2)
        (inreceptacle fork3 drawer3)
        (inreceptacle fork2 drawer3)
        (inreceptacle mug2 cabinet5)
        (inreceptacle saltshaker2 cabinet5)
        (inreceptacle houseplant1 countertop3)
        (inreceptacle knife2 countertop3)
        (inreceptacle peppershaker1 countertop3)
        (inreceptacle spatula2 countertop3)
        (inreceptacle plate3 countertop3)
        (inreceptacle pot2 countertop3)
        (inreceptacle knife1 countertop3)
        (inreceptacle statue1 countertop3)
        (inreceptacle statue2 countertop3)
        (inreceptacle cellphone2 countertop3)
        (inreceptacle dishsponge3 countertop3)
        (inreceptacle butterknife2 countertop3)
        (inreceptacle butterknife3 countertop3)
        (inreceptacle butterknife1 countertop1)
        (inreceptacle potato1 countertop1)
        (inreceptacle creditcard2 countertop1)
        (inreceptacle lettuce1 countertop1)
        (inreceptacle creditcard3 countertop1)
        (inreceptacle vase2 countertop1)
        (inreceptacle dishsponge2 countertop1)
        (inreceptacle dishsponge1 countertop1)
        (inreceptacle tomato1 countertop1)
        (inreceptacle pan1 stoveburner3)
        (inreceptacle spoon1 drawer1)
        (inreceptacle cellphone1 drawer2)
        (inreceptacle spatula1 drawer2)
        (inreceptacle creditcard1 drawer2)
        (inreceptacle saltshaker1 drawer2)
        (inreceptacle vase1 cabinet2)
        (inreceptacle mug1 countertop2)
        (inreceptacle papertowelroll1 countertop2)
        (inreceptacle bowl1 cabinet3)
        (inreceptacle vase3 cabinet4)
        (inreceptacle soapbottle1 shelf3)
        (inreceptacle saltshaker3 shelf2)
        (inreceptacle cellphone3 shelf2)
        (inreceptacle glassbottle1 shelf2)
        (inreceptacle mug1 coffeemachine1)
        (inreceptacle egg3 garbagecan1)
        (inreceptacle potato3 garbagecan1)
        (inreceptacle egg2 sinkbasin1)
        (inreceptacle cup2 sinkbasin1)
        (inreceptacle cup1 sinkbasin1)
        (inreceptacle potato2 sinkbasin1)
        (inreceptacle bread1 fridge1)
        (inreceptacle tomato2 fridge1)
        (inreceptacle plate1 fridge1)
        (inreceptacle egg1 fridge1)
        (inreceptacle apple1 fridge1)
        (inreceptacle plate2 fridge1)
        
        
        (receptacleatlocation cabinet1 location20)
        (receptacleatlocation cabinet2 location23)
        (receptacleatlocation cabinet3 location17)
        (receptacleatlocation cabinet4 location15)
        (receptacleatlocation cabinet5 location14)
        (receptacleatlocation cabinet6 location5)
        (receptacleatlocation coffeemachine1 location12)
        (receptacleatlocation countertop1 location3)
        (receptacleatlocation countertop2 location12)
        (receptacleatlocation countertop3 location4)
        (receptacleatlocation drawer1 location21)
        (receptacleatlocation drawer2 location16)
        (receptacleatlocation drawer3 location28)
        (receptacleatlocation fridge1 location11)
        (receptacleatlocation garbagecan1 location9)
        (receptacleatlocation microwave1 location25)
        (receptacleatlocation shelf1 location18)
        (receptacleatlocation shelf2 location30)
        (receptacleatlocation shelf3 location27)
        (receptacleatlocation sinkbasin1 location7)
        (receptacleatlocation stoveburner1 location6)
        (receptacleatlocation stoveburner2 location22)
        (receptacleatlocation stoveburner3 location6)
        (receptacleatlocation stoveburner4 location22)
        (receptacleatlocation toaster1 location10)
        (objectatlocation mug1 location12)
        (objectatlocation cup2 location7)
        (objectatlocation dishsponge2 location3)
        (objectatlocation vase2 location3)
        (objectatlocation butterknife2 location4)
        (objectatlocation saltshaker3 location30)
        (objectatlocation egg2 location7)
        (objectatlocation tomato2 location11)
        (objectatlocation spatula1 location16)
        (objectatlocation pot1 location22)
        (objectatlocation plate3 location4)
        (objectatlocation fork2 location28)
        (objectatlocation knife1 location4)
        (objectatlocation potato3 location9)
        (objectatlocation cellphone2 location4)
        (objectatlocation creditcard1 location16)
        (objectatlocation statue2 location4)
        (objectatlocation saltshaker2 location14)
        (objectatlocation plate2 location11)
        (objectatlocation egg1 location11)
        (objectatlocation fork1 location1)
        (objectatlocation butterknife1 location3)
        (objectatlocation dishsponge3 location4)
        (objectatlocation cellphone1 location16)
        (objectatlocation creditcard3 location3)
        (objectatlocation potato1 location3)
        (objectatlocation sink1 location7)
        (objectatlocation statue1 location4)
        (objectatlocation glassbottle1 location30)
        (objectatlocation bread1 location11)
        (objectatlocation creditcard2 location3)
        (objectatlocation cellphone3 location30)
        (objectatlocation lightswitch1 location26)
        (objectatlocation potato2 location7)
        (objectatlocation knife2 location4)
        (objectatlocation stoveknob3 location13)
        (objectatlocation stoveknob4 location8)
        (objectatlocation stoveknob1 location19)
        (objectatlocation stoveknob2 location13)
        (objectatlocation fork3 location28)
        (objectatlocation pan1 location6)
        (objectatlocation lettuce1 location3)
        (objectatlocation plate1 location11)
        (objectatlocation apple1 location11)
        (objectatlocation pot2 location4)
        (objectatlocation window1 location31)
        (objectatlocation window2 location29)
        (objectatlocation spatula2 location4)
        (objectatlocation papertowelroll1 location12)
        (objectatlocation tomato1 location3)
        (objectatlocation egg3 location9)
        (objectatlocation saltshaker1 location16)
        (objectatlocation peppershaker1 location4)
        (objectatlocation vase1 location23)
        (objectatlocation butterknife3 location4)
        (objectatlocation soapbottle1 location27)
        (objectatlocation vase3 location15)
        (objectatlocation bowl1 location17)
        (objectatlocation dishsponge1 location3)
        (objectatlocation chair2 location2)
        (objectatlocation chair1 location24)
        (objectatlocation spoon1 location21)
        (objectatlocation cup1 location7)
        (objectatlocation houseplant1 location4)
        (objectatlocation mug2 location14)
        )
    

        (:goal
            (and
                (validatecoolandplace mugtype cabinettype)

                ;;(exists (?r - receptacle)
                ;;    (exists (?o - object)
                ;;        (and
                ;;            (coolable ?o)
                ;;            (objecttype ?o mugtype)
                ;;            (receptacletype ?r cabinettype)
                ;;            (iscool ?o)
                ;;            (inreceptacle ?o ?r)
                ;;        )
                ;;    )
                ;;)
            )
        )
         
    )
    
