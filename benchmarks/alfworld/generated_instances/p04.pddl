
(define (problem plan_trial_t20190909_102644_926781)
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
        bread2 - object
        butterknife1 - object
        butterknife2 - object
        cellphone1 - object
        cellphone2 - object
        chair1 - object
        chair2 - object
        creditcard1 - object
        cup1 - object
        cup2 - object
        cup3 - object
        dishsponge1 - object
        dishsponge2 - object
        egg1 - object
        faucet1 - object
        fork1 - object
        glassbottle1 - object
        glassbottle2 - object
        houseplant1 - object
        knife1 - object
        knife2 - object
        knife3 - object
        lettuce1 - object
        lightswitch1 - object
        mug1 - object
        mug2 - object
        mug3 - object
        pan1 - object
        pan2 - object
        papertowelroll1 - object
        peppershaker1 - object
        peppershaker2 - object
        peppershaker3 - object
        plate1 - object
        plate2 - object
        plate3 - object
        potato1 - object
        pot1 - object
        saltshaker1 - object
        saltshaker2 - object
        saltshaker3 - object
        sink1 - object
        soapbottle1 - object
        spatula1 - object
        spatula2 - object
        spatula3 - object
        spoon1 - object
        spoon2 - object
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
        (objecttype dishsponge1 dishspongetype)
        (objecttype houseplant1 houseplanttype)
        (objecttype mug1 mugtype)
        (objecttype glassbottle2 glassbottletype)
        (objecttype tomato1 tomatotype)
        (objecttype butterknife2 butterknifetype)
        (objecttype plate3 platetype)
        (objecttype spoon1 spoontype)
        (objecttype dishsponge2 dishspongetype)
        (objecttype fork1 forktype)
        (objecttype window1 windowtype)
        (objecttype spatula3 spatulatype)
        (objecttype saltshaker1 saltshakertype)
        (objecttype chair1 chairtype)
        (objecttype cup3 cuptype)
        (objecttype cellphone1 cellphonetype)
        (objecttype egg1 eggtype)
        (objecttype cellphone2 cellphonetype)
        (objecttype bread2 breadtype)
        (objecttype spoon2 spoontype)
        (objecttype apple1 appletype)
        (objecttype soapbottle1 soapbottletype)
        (objecttype vase1 vasetype)
        (objecttype cup2 cuptype)
        (objecttype stoveknob4 stoveknobtype)
        (objecttype saltshaker2 saltshakertype)
        (objecttype peppershaker1 peppershakertype)
        (objecttype butterknife1 butterknifetype)
        (objecttype knife2 knifetype)
        (objecttype tomato2 tomatotype)
        (objecttype plate1 platetype)
        (objecttype lightswitch1 lightswitchtype)
        (objecttype potato1 potatotype)
        (objecttype stoveknob3 stoveknobtype)
        (objecttype pot1 pottype)
        (objecttype sink1 sinktype)
        (objecttype creditcard1 creditcardtype)
        (objecttype chair2 chairtype)
        (objecttype statue1 statuetype)
        (objecttype spatula1 spatulatype)
        (objecttype peppershaker3 peppershakertype)
        (objecttype papertowelroll1 papertowelrolltype)
        (objecttype vase2 vasetype)
        (objecttype stoveknob1 stoveknobtype)
        (objecttype knife3 knifetype)
        (objecttype lettuce1 lettucetype)
        (objecttype cup1 cuptype)
        (objecttype peppershaker2 peppershakertype)
        (objecttype pan1 pantype)
        (objecttype mug3 mugtype)
        (objecttype knife1 knifetype)
        (objecttype mug2 mugtype)
        (objecttype stoveknob2 stoveknobtype)
        (objecttype bowl1 bowltype)
        (objecttype spatula2 spatulatype)
        (objecttype pan2 pantype)
        (objecttype window2 windowtype)
        (objecttype saltshaker3 saltshakertype)
        (objecttype glassbottle1 glassbottletype)
        (objecttype plate2 platetype)
        (objecttype bread1 breadtype)
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
        (pickupable dishsponge1)
        (pickupable mug1)
        (pickupable glassbottle2)
        (pickupable tomato1)
        (pickupable butterknife2)
        (pickupable plate3)
        (pickupable spoon1)
        (pickupable dishsponge2)
        (pickupable fork1)
        (pickupable spatula3)
        (pickupable saltshaker1)
        (pickupable cup3)
        (pickupable cellphone1)
        (pickupable egg1)
        (pickupable cellphone2)
        (pickupable bread2)
        (pickupable spoon2)
        (pickupable apple1)
        (pickupable soapbottle1)
        (pickupable vase1)
        (pickupable cup2)
        (pickupable saltshaker2)
        (pickupable peppershaker1)
        (pickupable butterknife1)
        (pickupable knife2)
        (pickupable tomato2)
        (pickupable plate1)
        (pickupable potato1)
        (pickupable pot1)
        (pickupable creditcard1)
        (pickupable statue1)
        (pickupable spatula1)
        (pickupable peppershaker3)
        (pickupable papertowelroll1)
        (pickupable vase2)
        (pickupable knife3)
        (pickupable lettuce1)
        (pickupable cup1)
        (pickupable peppershaker2)
        (pickupable pan1)
        (pickupable mug3)
        (pickupable knife1)
        (pickupable mug2)
        (pickupable bowl1)
        (pickupable spatula2)
        (pickupable pan2)
        (pickupable saltshaker3)
        (pickupable glassbottle1)
        (pickupable plate2)
        (pickupable bread1)

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
        
        (cleanable dishsponge1)
        (cleanable mug1)
        (cleanable tomato1)
        (cleanable butterknife2)
        (cleanable plate3)
        (cleanable spoon1)
        (cleanable dishsponge2)
        (cleanable fork1)
        (cleanable spatula3)
        (cleanable cup3)
        (cleanable egg1)
        (cleanable spoon2)
        (cleanable apple1)
        (cleanable cup2)
        (cleanable butterknife1)
        (cleanable knife2)
        (cleanable tomato2)
        (cleanable plate1)
        (cleanable potato1)
        (cleanable pot1)
        (cleanable spatula1)
        (cleanable knife3)
        (cleanable lettuce1)
        (cleanable cup1)
        (cleanable pan1)
        (cleanable mug3)
        (cleanable knife1)
        (cleanable mug2)
        (cleanable bowl1)
        (cleanable spatula2)
        (cleanable pan2)
        (cleanable plate2)
        
        (heatable mug1)
        (heatable tomato1)
        (heatable plate3)
        (heatable cup3)
        (heatable egg1)
        (heatable bread2)
        (heatable apple1)
        (heatable cup2)
        (heatable tomato2)
        (heatable plate1)
        (heatable potato1)
        (heatable cup1)
        (heatable mug3)
        (heatable mug2)
        (heatable plate2)
        (heatable bread1)
        (coolable mug1)
        (coolable tomato1)
        (coolable plate3)
        (coolable cup3)
        (coolable egg1)
        (coolable bread2)
        (coolable apple1)
        (coolable cup2)
        (coolable tomato2)
        (coolable plate1)
        (coolable potato1)
        (coolable pot1)
        (coolable lettuce1)
        (coolable cup1)
        (coolable pan1)
        (coolable mug3)
        (coolable mug2)
        (coolable bowl1)
        (coolable pan2)
        (coolable plate2)
        (coolable bread1)
        
        
        
        
        
        (sliceable tomato1)
        (sliceable egg1)
        (sliceable bread2)
        (sliceable apple1)
        (sliceable tomato2)
        (sliceable potato1)
        (sliceable lettuce1)
        (sliceable bread1)
        
        (inreceptacle pot1 stoveburner4)
        (inreceptacle pot1 stoveburner2)
        (inreceptacle peppershaker1 drawer3)
        (inreceptacle plate3 cabinet5)
        (inreceptacle knife2 countertop3)
        (inreceptacle houseplant1 countertop3)
        (inreceptacle glassbottle2 countertop3)
        (inreceptacle butterknife2 countertop3)
        (inreceptacle potato1 countertop3)
        (inreceptacle bread2 countertop3)
        (inreceptacle pan2 countertop3)
        (inreceptacle cup3 countertop3)
        (inreceptacle spoon2 countertop3)
        (inreceptacle knife3 countertop3)
        (inreceptacle soapbottle1 countertop3)
        (inreceptacle lettuce1 countertop1)
        (inreceptacle tomato1 countertop1)
        (inreceptacle knife1 countertop1)
        (inreceptacle saltshaker1 countertop1)
        (inreceptacle saltshaker2 countertop1)
        (inreceptacle creditcard1 countertop1)
        (inreceptacle cellphone1 countertop1)
        (inreceptacle butterknife1 countertop1)
        (inreceptacle statue1 countertop1)
        (inreceptacle spatula1 drawer1)
        (inreceptacle peppershaker2 drawer1)
        (inreceptacle spoon1 drawer2)
        (inreceptacle dishsponge1 countertop2)
        (inreceptacle mug2 countertop2)
        (inreceptacle glassbottle1 cabinet3)
        (inreceptacle mug3 cabinet3)
        (inreceptacle bowl1 cabinet3)
        (inreceptacle plate2 cabinet4)
        (inreceptacle cup1 cabinet4)
        (inreceptacle saltshaker3 shelf3)
        (inreceptacle cellphone2 shelf2)
        (inreceptacle vase2 shelf2)
        (inreceptacle peppershaker3 shelf2)
        (inreceptacle mug2 coffeemachine1)
        (inreceptacle vase1 shelf1)
        (inreceptacle dishsponge2 garbagecan1)
        (inreceptacle papertowelroll1 garbagecan1)
        (inreceptacle tomato2 sinkbasin1)
        (inreceptacle fork1 sinkbasin1)
        (inreceptacle spatula3 sinkbasin1)
        (inreceptacle cup2 sinkbasin1)
        (inreceptacle spatula2 sinkbasin1)
        (inreceptacle apple1 sinkbasin1)
        (inreceptacle egg1 microwave1)
        (inreceptacle pan1 fridge1)
        (inreceptacle plate1 fridge1)
        (inreceptacle bread1 fridge1)
        (inreceptacle mug1 fridge1)
        
        
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
        (objectatlocation mug3 location16)
        (objectatlocation cup2 location6)
        (objectatlocation spoon2 location3)
        (objectatlocation dishsponge1 location11)
        (objectatlocation butterknife2 location3)
        (objectatlocation peppershaker3 location29)
        (objectatlocation saltshaker1 location2)
        (objectatlocation tomato2 location6)
        (objectatlocation spatula1 location20)
        (objectatlocation plate1 location10)
        (objectatlocation pan1 location10)
        (objectatlocation knife3 location3)
        (objectatlocation cellphone2 location29)
        (objectatlocation bread2 location3)
        (objectatlocation glassbottle2 location3)
        (objectatlocation mug2 location11)
        (objectatlocation peppershaker1 location27)
        (objectatlocation saltshaker3 location26)
        (objectatlocation plate2 location14)
        (objectatlocation cup3 location3)
        (objectatlocation knife1 location2)
        (objectatlocation spatula3 location6)
        (objectatlocation sink1 location6)
        (objectatlocation statue1 location2)
        (objectatlocation glassbottle1 location16)
        (objectatlocation bread1 location10)
        (objectatlocation creditcard1 location2)
        (objectatlocation cellphone1 location2)
        (objectatlocation lightswitch1 location25)
        (objectatlocation potato1 location3)
        (objectatlocation knife2 location3)
        (objectatlocation stoveknob3 location12)
        (objectatlocation stoveknob4 location7)
        (objectatlocation stoveknob1 location18)
        (objectatlocation stoveknob2 location12)
        (objectatlocation fork1 location6)
        (objectatlocation pan2 location3)
        (objectatlocation lettuce1 location2)
        (objectatlocation plate3 location13)
        (objectatlocation apple1 location6)
        (objectatlocation pot1 location21)
        (objectatlocation window1 location30)
        (objectatlocation window2 location28)
        (objectatlocation spatula2 location6)
        (objectatlocation papertowelroll1 location8)
        (objectatlocation tomato1 location2)
        (objectatlocation egg1 location24)
        (objectatlocation saltshaker2 location2)
        (objectatlocation peppershaker2 location20)
        (objectatlocation vase1 location17)
        (objectatlocation butterknife1 location2)
        (objectatlocation soapbottle1 location3)
        (objectatlocation vase2 location29)
        (objectatlocation bowl1 location16)
        (objectatlocation dishsponge2 location8)
        (objectatlocation chair2 location1)
        (objectatlocation chair1 location23)
        (objectatlocation spoon1 location15)
        (objectatlocation cup1 location14)
        (objectatlocation houseplant1 location3)
        (objectatlocation mug1 location10)
        )
    

        (:goal
            (and
                (validatecoolandplace tomatotype microwavetype)
                ;;(exists (?r - receptacle)
                ;;    (exists (?o - object)
                ;;        (and
                ;;            (coolable ?o)
                ;;            (objecttype ?o tomatotype)
                ;;            (receptacletype ?r microwavetype)
                ;;            (iscool ?o)
                ;;            (inreceptacle ?o ?r)
                ;;        )
                ;;    )
                ;;)
            )
        )
         
    )
    

