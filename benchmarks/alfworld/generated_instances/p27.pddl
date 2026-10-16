
(define (problem plan_trial_t20190907_083429_887065)
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
        bowl2 - object
        bowl3 - object
        bread1 - object
        butterknife1 - object
        butterknife2 - object
        cellphone1 - object
        cellphone2 - object
        cellphone3 - object
        chair1 - object
        chair2 - object
        creditcard1 - object
        cup1 - object
        cup2 - object
        cup3 - object
        dishsponge1 - object
        egg1 - object
        faucet1 - object
        fork1 - object
        glassbottle1 - object
        glassbottle2 - object
        houseplant1 - object
        knife1 - object
        lettuce1 - object
        lettuce2 - object
        lettuce3 - object
        lightswitch1 - object
        mug1 - object
        mug2 - object
        mug3 - object
        pan1 - object
        papertowelroll1 - object
        peppershaker1 - object
        peppershaker2 - object
        plate1 - object
        potato1 - object
        potato2 - object
        pot1 - object
        pot2 - object
        saltshaker1 - object
        sink1 - object
        soapbottle1 - object
        soapbottle2 - object
        soapbottle3 - object
        spatula1 - object
        spatula2 - object
        spoon1 - object
        statue1 - object
        stoveknob1 - object
        stoveknob2 - object
        stoveknob3 - object
        stoveknob4 - object
        tomato1 - object
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
        (objecttype bowl2 bowltype)
        (objecttype houseplant1 houseplanttype)
        (objecttype potato1 potatotype)
        (objecttype cup1 cuptype)
        (objecttype spoon1 spoontype)
        (objecttype plate1 platetype)
        (objecttype window1 windowtype)
        (objecttype vase1 vasetype)
        (objecttype peppershaker2 peppershakertype)
        (objecttype mug3 mugtype)
        (objecttype mug1 mugtype)
        (objecttype tomato1 tomatotype)
        (objecttype vase2 vasetype)
        (objecttype cellphone1 cellphonetype)
        (objecttype chair1 chairtype)
        (objecttype creditcard1 creditcardtype)
        (objecttype glassbottle2 glassbottletype)
        (objecttype pot1 pottype)
        (objecttype soapbottle2 soapbottletype)
        (objecttype dishsponge1 dishspongetype)
        (objecttype soapbottle3 soapbottletype)
        (objecttype saltshaker1 saltshakertype)
        (objecttype butterknife2 butterknifetype)
        (objecttype stoveknob4 stoveknobtype)
        (objecttype bowl1 bowltype)
        (objecttype pan1 pantype)
        (objecttype potato2 potatotype)
        (objecttype lettuce3 lettucetype)
        (objecttype cup2 cuptype)
        (objecttype spatula1 spatulatype)
        (objecttype lightswitch1 lightswitchtype)
        (objecttype stoveknob3 stoveknobtype)
        (objecttype fork1 forktype)
        (objecttype pot2 pottype)
        (objecttype lettuce1 lettucetype)
        (objecttype sink1 sinktype)
        (objecttype bread1 breadtype)
        (objecttype cup3 cuptype)
        (objecttype papertowelroll1 papertowelrolltype)
        (objecttype chair2 chairtype)
        (objecttype soapbottle1 soapbottletype)
        (objecttype mug2 mugtype)
        (objecttype cellphone3 cellphonetype)
        (objecttype knife1 knifetype)
        (objecttype glassbottle1 glassbottletype)
        (objecttype stoveknob1 stoveknobtype)
        (objecttype lettuce2 lettucetype)
        (objecttype bowl3 bowltype)
        (objecttype vase3 vasetype)
        (objecttype stoveknob2 stoveknobtype)
        (objecttype egg1 eggtype)
        (objecttype apple1 appletype)
        (objecttype peppershaker1 peppershakertype)
        (objecttype butterknife1 butterknifetype)
        (objecttype cellphone2 cellphonetype)
        (objecttype window2 windowtype)
        (objecttype spatula2 spatulatype)
        (objecttype statue1 statuetype)
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
        (pickupable bowl2)
        (pickupable potato1)
        (pickupable cup1)
        (pickupable spoon1)
        (pickupable plate1)
        (pickupable vase1)
        (pickupable peppershaker2)
        (pickupable mug3)
        (pickupable mug1)
        (pickupable tomato1)
        (pickupable vase2)
        (pickupable cellphone1)
        (pickupable creditcard1)
        (pickupable glassbottle2)
        (pickupable pot1)
        (pickupable soapbottle2)
        (pickupable dishsponge1)
        (pickupable soapbottle3)
        (pickupable saltshaker1)
        (pickupable butterknife2)
        (pickupable bowl1)
        (pickupable pan1)
        (pickupable potato2)
        (pickupable lettuce3)
        (pickupable cup2)
        (pickupable spatula1)
        (pickupable fork1)
        (pickupable pot2)
        (pickupable lettuce1)
        (pickupable bread1)
        (pickupable cup3)
        (pickupable papertowelroll1)
        (pickupable soapbottle1)
        (pickupable mug2)
        (pickupable cellphone3)
        (pickupable knife1)
        (pickupable glassbottle1)
        (pickupable lettuce2)
        (pickupable bowl3)
        (pickupable vase3)
        (pickupable egg1)
        (pickupable apple1)
        (pickupable peppershaker1)
        (pickupable butterknife1)
        (pickupable cellphone2)
        (pickupable spatula2)
        (pickupable statue1)
        
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
        
        (cleanable bowl2)
        (cleanable potato1)
        (cleanable cup1)
        (cleanable spoon1)
        (cleanable plate1)
        (cleanable mug3)
        (cleanable mug1)
        (cleanable tomato1)
        (cleanable pot1)
        (cleanable dishsponge1)
        (cleanable butterknife2)
        (cleanable bowl1)
        (cleanable pan1)
        (cleanable potato2)
        (cleanable lettuce3)
        (cleanable cup2)
        (cleanable spatula1)
        (cleanable fork1)
        (cleanable pot2)
        (cleanable lettuce1)
        (cleanable cup3)
        (cleanable mug2)
        (cleanable knife1)
        (cleanable lettuce2)
        (cleanable bowl3)
        (cleanable egg1)
        (cleanable apple1)
        (cleanable butterknife1)
        (cleanable spatula2)
        
        (heatable potato1)
        (heatable cup1)
        (heatable plate1)
        (heatable mug3)
        (heatable mug1)
        (heatable tomato1)
        (heatable potato2)
        (heatable cup2)
        (heatable bread1)
        (heatable cup3)
        (heatable mug2)
        (heatable egg1)
        (heatable apple1)
        (coolable bowl2)
        (coolable potato1)
        (coolable cup1)
        (coolable plate1)
        (coolable mug3)
        (coolable mug1)
        (coolable tomato1)
        (coolable pot1)
        (coolable bowl1)
        (coolable pan1)
        (coolable potato2)
        (coolable lettuce3)
        (coolable cup2)
        (coolable pot2)
        (coolable lettuce1)
        (coolable bread1)
        (coolable cup3)
        (coolable mug2)
        (coolable lettuce2)
        (coolable bowl3)
        (coolable egg1)
        (coolable apple1)
        
        
        
        
        
        (sliceable potato1)
        (sliceable tomato1)
        (sliceable potato2)
        (sliceable lettuce3)
        (sliceable lettuce1)
        (sliceable bread1)
        (sliceable lettuce2)
        (sliceable egg1)
        (sliceable apple1)
        
        (inreceptacle soapbottle2 cabinet1)
        (inreceptacle pot2 stoveburner4)
        (inreceptacle pot2 stoveburner2)
        (inreceptacle houseplant1 countertop3)
        (inreceptacle spoon1 countertop3)
        (inreceptacle butterknife2 countertop3)
        (inreceptacle vase1 countertop3)
        (inreceptacle bread1 countertop3)
        (inreceptacle cup3 countertop3)
        (inreceptacle vase2 countertop3)
        (inreceptacle statue1 countertop3)
        (inreceptacle lettuce2 countertop1)
        (inreceptacle glassbottle2 countertop1)
        (inreceptacle pot1 countertop1)
        (inreceptacle lettuce1 countertop1)
        (inreceptacle butterknife1 countertop1)
        (inreceptacle cellphone2 countertop1)
        (inreceptacle cellphone3 countertop1)
        (inreceptacle cellphone1 drawer2)
        (inreceptacle glassbottle1 cabinet2)
        (inreceptacle soapbottle1 cabinet2)
        (inreceptacle egg1 countertop2)
        (inreceptacle knife1 countertop2)
        (inreceptacle apple1 countertop2)
        (inreceptacle mug1 countertop2)
        (inreceptacle pan1 cabinet6)
        (inreceptacle bowl2 cabinet3)
        (inreceptacle bowl3 cabinet3)
        (inreceptacle peppershaker1 cabinet4)
        (inreceptacle cup1 cabinet4)
        (inreceptacle dishsponge1 shelf3)
        (inreceptacle creditcard1 shelf2)
        (inreceptacle saltshaker1 shelf2)
        (inreceptacle peppershaker2 shelf2)
        (inreceptacle vase3 shelf2)
        (inreceptacle soapbottle3 garbagecan1)
        (inreceptacle papertowelroll1 garbagecan1)
        (inreceptacle cup2 sinkbasin1)
        (inreceptacle spatula1 sinkbasin1)
        (inreceptacle fork1 sinkbasin1)
        (inreceptacle potato2 sinkbasin1)
        (inreceptacle lettuce3 sinkbasin1)
        (inreceptacle spatula2 sinkbasin1)
        (inreceptacle mug3 microwave1)
        (inreceptacle potato1 fridge1)
        (inreceptacle plate1 fridge1)
        (inreceptacle bowl1 fridge1)
        (inreceptacle tomato1 fridge1)
        (inreceptacle mug2 fridge1)
        
        
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
        (objectatlocation cup2 location6)
        (objectatlocation bowl1 location10)
        (objectatlocation vase3 location29)
        (objectatlocation soapbottle1 location22)
        (objectatlocation butterknife1 location2)
        (objectatlocation peppershaker2 location29)
        (objectatlocation spatula2 location6)
        (objectatlocation pot1 location2)
        (objectatlocation lettuce1 location2)
        (objectatlocation potato2 location6)
        (objectatlocation cellphone2 location2)
        (objectatlocation glassbottle1 location22)
        (objectatlocation mug3 location24)
        (objectatlocation lettuce3 location6)
        (objectatlocation bowl3 location16)
        (objectatlocation soapbottle3 location8)
        (objectatlocation cup3 location3)
        (objectatlocation cellphone3 location2)
        (objectatlocation sink1 location6)
        (objectatlocation statue1 location3)
        (objectatlocation glassbottle2 location2)
        (objectatlocation bread1 location3)
        (objectatlocation creditcard1 location29)
        (objectatlocation cellphone1 location15)
        (objectatlocation lightswitch1 location25)
        (objectatlocation potato1 location10)
        (objectatlocation knife1 location11)
        (objectatlocation stoveknob3 location12)
        (objectatlocation stoveknob4 location7)
        (objectatlocation stoveknob1 location18)
        (objectatlocation stoveknob2 location12)
        (objectatlocation fork1 location6)
        (objectatlocation pan1 location4)
        (objectatlocation lettuce2 location2)
        (objectatlocation plate1 location10)
        (objectatlocation apple1 location11)
        (objectatlocation pot2 location21)
        (objectatlocation window1 location30)
        (objectatlocation window2 location28)
        (objectatlocation spatula1 location6)
        (objectatlocation papertowelroll1 location8)
        (objectatlocation tomato1 location10)
        (objectatlocation egg1 location11)
        (objectatlocation saltshaker1 location29)
        (objectatlocation peppershaker1 location14)
        (objectatlocation vase2 location3)
        (objectatlocation butterknife2 location3)
        (objectatlocation soapbottle2 location19)
        (objectatlocation vase1 location3)
        (objectatlocation bowl2 location16)
        (objectatlocation dishsponge1 location26)
        (objectatlocation chair2 location1)
        (objectatlocation chair1 location23)
        (objectatlocation spoon1 location3)
        (objectatlocation cup1 location14)
        (objectatlocation houseplant1 location3)
        (objectatlocation mug2 location10)
        )
    

        (:goal
            (and
                (validateheatandplace cuptype cabinettype)

                ;;(exists (?r - receptacle)
                ;;    (exists (?o - object)
                ;;        (and
                ;;            (heatable ?o)
                ;;            (objecttype ?o cuptype)
                ;;            (receptacletype ?r cabinettype)
                ;;            (ishot ?o)
                ;;            (inreceptacle ?o ?r)
                ;;        )
                ;;    )
                ;;)
            )
        )
         
    )
    
