label donbirthday:
    python:
        B_Name = "Brittney"
        C_Name = "Christeena"
        M_Name = "Mrs. Truman"
        P_Name = "???"
        K_Name = "Kelly"
        cutoff = False
        b_partial = False
        b_hat = 1
        c_blush = False
        outfit_b = "a"
        outfit_c = "b"
        outfit_d = "a"
        outfit_k = "b"
        outfit_m = "b"
    show text "{size=+50}June, 2013{/size}":
        xalign 0.5 yalign 0.05
    show screen calendarOs
    show calendar june june_31:
        xalign 0.5 yalign 0.6
    show full_circle:
        xalign 0.31 yalign 0.88
    with dissolve
    pause 1
    $currentmonth = "July"
    scene bg fade
    show text "{size=+50}July, 2013{/size}":
        xalign 0.5 yalign 0.05
    show screen calendarOs
    show calendar july july_04:
        xalign 0.5 yalign 0.67
    with pushdown
    show calendar_circle:
        xalign 0.56 yalign 0.39
    if replay == False:
        $ persistent.todays_date = "July 4th, 2013"
        $ renpy.notify("Game saved!")
        $ renpy.save("1-1")
    pause 4
    hide text
    hide screen calendarOs
    hide calendar
    hide calendar_circle
    with dissolve
    pause 1
    scene bg living_w with dissolve
    window show dissolve
    pause 0.1
    $d_blink = True
    $ renpy.block_rollback()
    a "Hellooo?"
    with Pause(.1)
    $ current_track = "\"Brotato Chips\""
    play music donald
    show don p1 straight casual smile at middle with dissolve
    pause 0.1
    d "Hey, man! Thanks for coming!"
    a "No problem! Happy birthday!"
    $d_blink = False
    d closed grin sad "Thanks!"
    show don at twoleft
    show ginger p2 straight sad grin at tworight
    with easeinright
    pause 0.1
    g "Happy birthday, Donald!"
    $d_blink = True
    d straight casual "Thanks, Mrs. Sprouse."
    hide ginger with easeoutright
    show fred p1 straight casual glasses grin at tworight with easeinright
    pause 0.1
    f "Happy birthday, Don."
    d smile "Thanks, Mr. Sprouse."
    hide fred with easeoutright
    show harry p1 straight mad closed_smile at tworight with easeinright
    pause 0.1
    h "Happy anniversary of the day you exited your mom's vagina!"
    g_o "Harold!"
    h casual "What? It is!"
    $d_blink = False
    d closed sad "Hahaha! Thanks, big guy."
    show harry mad blank
    "Donald then rustled Harry's hair, which my brother didn't seem to be a big fan of."
    hide harry with easeoutright
    show ginger p2 sad grin straight at tworight with easeinright
    g "Gosh, 17 years old... Where does time go?"
    $d_blink = True
    d raised smile straight "Shouldn't you be saving that speech for when your son turns 17 next year?"
    g blank "And make myself feel even older?"
    d level right grin "I mean, you're how old right now? 24? 25?"
    g level grin "Oh, stop it, you."
    show fred glasses p1 straight raised grin at threeleft
    show don at middle
    show ginger at threeright
    with easeinleft
    pause 0.1
    f "If you're done flirting with my wife, Donald..."
    f "If you're done flirting with my wife, Donald{fast}, where can we put your presents?"
    d straight casual "There's a table over there by the TV."
    scene bg living_w with dissolve
    pause 0.1
    "Getting the mental image of my mother cheating on my father with Donald out of my head, I walked over to the table with my family, where we each placed our gifts on the table."
    "By the time they were on the table, two more people had entered the living room."
    pause 0.1
    show janice p1 straight casual grin at twoleft
    show latrell p1 straight casual grin at l_tworight
    with dissolve
    pause 0.1
    j "Well, hello there, Sprouses!"
    show ginger p2 straight casual grin at threeleft
    show janice at middle
    show latrell at l_threeright
    with easeinleft
    pause 0.1
    g "Good morning, you two! Sorry for just bursting into your house like this."
    l level "Ah, no worries. You guys are always welcome."
    g sad "It looks like we're the first ones here. I hope we're not too early."
    j sad "Aw, y'all are fine. We're just relaxing in the backyard if you wanna come out."
    g casual "That would be lovely."
    $ current_track = "None"
    stop music fadeout(1)
    scene bg living_w with dissolve
    pause 0.5
    scene bg backyard_w with dissolve
    pause 0.5
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    "The Waters' backyard was hardly 'decorated', as you'd call it, but for a 17th birthday party for a guy, you can't be too surprised, especially for a simple guy like Donald."
    "There were coolers alongside the back of the house, a grill that was waiting to do its job, a bag toss game near the back of the property, and several lawn chairs spread around."
    "My parents and Donald's parents all sat near each other by the grill while Donald and I gathered near the middle of the yard."
    "Harry, meanwhile, stayed in the house to play on his TS. Turns out he hadn't given up on that Doctor Letton deal after all..."
    show don p1 straight casual grin at close_d with dissolve
    pause 0.1
    a "Man, you know you're a big deal when everyone here seems to forget that it's America's birthday, too."
    $d_blink = False
    d closed sad smile "Ahahaha. I wouldn't call myself a 'big deal'..."
    $d_blink = True
    d straight raised grin "BUUUUT I can't say I'm shocked people forgot."
    $ brit_dare = False
    $ chris_dare = False
    $ don_dare = False
    if persistent.choices["18"] == 1:
        if persistent.choices["20"]== 1 or persistent.choices["20"] == 3:
            $ brit_dare = True
            jump bad_dare_discussion
        elif persistent.choices["20"] == 2 and persistent.choices["21"] == 1:
            $ brit_dare = True
            jump good_dare_discussion
        else:
            jump no_dare_discussion
    if persistent.choices["18"] == 2:
        if persistent.choices["19"] == 3:
            $ chris_dare = True
            jump bad_dare_discussion
        else:
            jump no_dare_discussion
    if persistent.choices["18"] == 3:
        if persistent.choices["20"] == 2:
            $ don_dare = True
            jump bad_dare_discussion
        else:
            jump no_dare_discussion
    label bad_dare_discussion:
        a "Hey, while we've got a minute alone..."
        a "I wanted to talk about that night at the cabin..."
        d blank "Yeah?"
        a "Look, about that dare..."
        d level grin "Hey, man. It's alright."
        d right "I'll be honest; I had it coming."
        if brit_dare == True:
            if persistent.choices["20"] == 1:
                a "Yeah, but having your crush kiss me in front of you was kinda harsh."
                d straight "Well, I can't blame you for wanting to make that dare in the first place."
                d left "I would've done the same thing if I had the chance..."
                a "So, you're not mad...?"
                d raised straight blank "Why would I be? It's not like she's my girlfriend."
                "The way he said that made him sound a little...{w=.5} heartbroken."
                d level grin "Besides, she certainly seemed happy, and if she's happy, I'm happy."
                a "Well, alright, then, if you're not upset..."
                jump no_dare_discussion
            else:
                a "Yeah, but getting punched like that must've hurt worse than normal."
                d straight raised "Eh. She's not THAT strong."
                d level blank "But, uh..."
                d left "...don't tell her I said that."
                a "So, no hard feelings?"
                d straight grin "No hard feelings, I promise."
                a "Alright, if you say so..."
                "I kinda wanted to believe he was serious, but something about the way he was saying all this made me feel like he was just trying to be nice and forget about that night."
                jump no_dare_discussion
        elif chris_dare == True:
            a "Yeah, but getting slapped like that must've hurt."
            d straight raised smile "Well, I'll certainly admit it caught me off guard, but nothing I couldn't handle."
            a "Well, you certainly didn't seem too happy with me afterwards."
            d level blank "Yeah, well..."
            d right "...I was just in the moment."
            d straight raised grin "After some time had passed, and I looked back on it, it really was pretty funny."
            a "So no hard feelings, then?"
            d straight casual grin "Yeah, no hard feelings."
            $d_blink = False
            d closed sad smile "Besides, it is pretty funny to know I actually got slapped in the face by her."
            $d_blink = True
            d straight raised grin "With as often as she threatens to hit me, it's actually kinda interesting to finally see it happen."
            a "We're still talking about Christeena, right?"
            d level "Don't let her fool you. That girl is more violent than she lets on."
            d right "It's mostly empty threats, but I'm sure with enough rage in her tank, she could do some serious hurting."
            d straight casual smile "I suppose you're always welcome to find out how hard she can hit."
            a "Nah, I'll just take your word on it."
            $d_blink = False
            show don closed sad grin
            "Donald just gave a light chuckle in response."
            jump no_dare_discussion
        elif don_dare == True:
                a "Yeah, but jumping in the pond was a pretty stupid idea."
                if persistent.choices["21"] == 1:
                    d straight "Well, credit where it's due, you at least changed your mind and apologized, so no harm, no foul, right?"
                    a "I guess. I still feel bad, though."
                    d raised "Don't, man. It's cool."
                elif persistent.choices["21"] == 2:
                    d straight blank "Well, yeah, it was."
                    d right grin "But I didn't have to do it. I could've been a sissy and turned it down."
                    d "So, honestly, it's really my fault at the end of the day."
                    d "I'm just glad I didn't get sick or something."
                    a "Yeah, same here."
                a "So, no beef?"
                d straight casual "As 'no beef' as a vegetarian buffet!"
                $d_blink = False
                show don closed sad smile
                "We both laughed at that, signaling the end of the conversation."
                a "Well, glad that we've got that clarified..."
                jump no_dare_discussion

    label good_dare_discussion:
        a "Hey, while we've got a minute alone, I've been meaning to ask:"
        a "How did it feel to finally kiss her?"
        d_s level blank "..."
        d "...to be honest..."
        a "Oh, no.{w=.5} Don't tell me you didn't enjoy it..."
        d raised "Well, it was too quick to really feel anything, for starters."
        d level "But..."
        d right "...seeing how uninterested she was in doing it..."
        d "...it just felt wrong, you know?"
        a "Yeah, I hear ya. It's like she became a different person."
        d straight casual "Yeah, exactly."
        d mad "I feel like if me and her are going to kiss, it should be because we both want to."
        a "That's fair."
        a "Maybe I should've tried to stop the dare, or not even have suggested it in the first place..."
        d level grin "Hey, don't beat yourself up over it. You were just trying to do me a solid, and I can't get mad at you for that."
        d right "The past is the past, man. Nothing we can do about it, right?"
        a "Yeah, I guess."
        "With the awkwardness increasing quickly, I decided to change the conversation."

label no_dare_discussion:
    a "So, what time do you think other people will get here?"
    $d_blink = True
    d straight casual grin "Well, the Trumans generally get here pretty early."
    d smile "Brittney usually sends me a text when--{w=.5}{nw}"
    play sound phone_vibrate
    show don blank
    "Donald's phone buzzed, prompting him to pull it out of his pocket, look at the screen, and smile."
    d level grin "...when they're on their way."
    "He pointed his screen at me, allowing me to read the text."
    "{font=fonts/LemonMilk.otf}{i}\"We'll be there in a literal minute dum-dum XP\"{/i}{/font}"
    d casual "What do you say we meet them at the door?"
    a "Sounds good."
    hide don with dissolve
    pause 0.1
    scene bg living_w with dissolve
    pause 0.1
    play sound door_knock
    "By the time Donald and I got to the living room, there was a knock on the door."
    "Donald walked over to it and opened it up."
    play sound door_open
    pause 0.3
    show chad p1 straight casual grin at four1 zorder 2
    show chris p1 straight casual grin at four2 zorder 3
    show brit p1 straight casual grin at four3 zorder 3
    show martha p1 straight casual grin at m_four4 zorder 2
    with dissolve
    pause 0.5
    b p2 raised opened_smile "Ah, there's the birthday boy!"
    c p2 smile "Happy birthday, Donald!"
    ct sad "Happy birthday, Don!"
    mu sad smile "Happy birthday, Donnie!"
    $b_blink = False
    b closed closed_smile sad "Happy anniversary of the day you exited--"
    hide chad
    hide chris
    hide martha
    with dissolve
    show brit at twoleft
    show don p1 closed sad smile at tworight
    with easeinright
    pause 0.1
    d "Sorry, Brit; someone already beat you to it!"
    $b_blink = True
    b p1 small level hanging "Wha...? Who?"
    "Donald then pointed to my brother, who was sitting on the couch, oblivious to us."
    hide don with easeoutright
    show harry p1 level blank right at tworight with easeinright
    pause 0.1
    b p2 mad blank straight "What the hell, Harry?"
    h sad small frown "Huh?"
    "He finally seemed to notice that there were other people in the room."
    b raised hanging "The 'exit the vagina' line is MY line!"
    h mad straight closed_smile "Well, I don't see your name on it!"
    b p1 level grin "Heh. Typical 12-year-old response."
    b p2 left huhu "No...{w=0.5} That's a typical 5-year-old response."
    a "And a response you probably would've made if you were in Harry's position."
    b_s straight blank "..."
    b left huhu "Yeah, you're right."
    b p1 straight mad grin "Alright, I'll let it slide this time."
    $ b_partial = True
    b level huhu "Mostly because you're cute."
    h mad small frown "I told you, guys are not 'cute'!!"
    $ b_partial = False
    show brit p2 straight raised grin at twoleft
    b "Except you."
    h blank right "Gr..."
    "Flustered, Harry continued with his game."
    "One thing I've learned quickly about Brittney is when she finds out what makes you tick, she'll abuse the hell out of it."
    "Though, as I've also learned, that can backfire pretty quickly."
    hide brit
    hide harry
    show don p1 straight casual grin at middle
    with dissolve
    with Pause(.1)
    d smile "Well, anyway, thank you all for coming!"
    d grin "We're just hanging out in the backyard right now."
    d level right "Well, MOST of us."
    d straight casual "Once more guests get here, we'll start grillin'."
    d mad "Mr. T, I assume you brought the brats?"
    show don at tworight
    show chad p1 left sad blank at twoleft
    with easeinleft
    pause 0.1
    ct "Oh, shoot! I..."
    ct mad straight grin "...have them right here."
    "He then tapped on a paper bag he had been holding."
    $d_blink = False
    d closed sad grin "Whew. That's a relief."
    a "What, are these special brats or something?"
    if persistent.choices["18"] == 2 and persistent.choices["19"] == 2 and persistent.choices["20"] == 2:
        hide chad
        hide don
        show brit p1 straight casual grin at middle
        with dissolve
        pause 0.1
        b "They're deer brats. Christeena's uncle is a hunter who makes his own meat products."
        a "Deer meat? I don't think I've ever tried that."
    else:
        hide chad
        hide don
        show chris p2 straight smile casual at middle
        with dissolve
        pause 0.1
        c "My uncle likes to hunt deer and turn the meat into burgers, brats, meatballs, etc."
        c raised grin "He normally keeps a good portion to himself, but he does tend to give us some if we ask nicely."
        a "Deer meat? I don't think I've ever tried that."
        hide chris
        show brit p2 straight raised grin at middle
        with dissolve
        pause 0.1
    $d_blink = True
    b p2 straight raised grin "Well, if you're smart, you'll try it today."
    a "Right, because that's the only thing in the world that shows how smart I can be."
    b p1 casual "Yep!"
    hide brit
    show don p1 straight casual grin at tworight
    show chad p1 straight casual grin at twoleft
    with dissolve
    pause 0.1
    d "Anyway, you can put those in the fridge until we're ready."
    ct raised "Roger that!"
    scene bg living_w with dissolve
    pause 0.1
    "Mr. Truman went towards the kitchen while Donald led the rest of us outside."
    scene bg backyard_w with dissolve
    pause 0.1
    show chris p1 straight casual blank at twoleft
    show ginger p2 straight casual grin at tworight
    with dissolve
    pause 0.1
    g "Ah, hello again, Christeena!"
    c p2 grin "Hi, Mrs. Sprouse!"
    g "And this is your sister, Brittney, I take it?"
    hide chris
    show brit p1 straight casual grin at twoleft
    with dissolve
    pause 0.1
    b p2 raised "Yes, Ma'am! Brittney Usher."
    b level huhu left "I'm the one WITHOUT the uniquely-spelled name."
    g sad "Ahaha! Well, I'm Ginger, Alex's mom. And over by the grill is Fred, Alex's dad."
    b p1 straight casual grin "Oh, so HE'S the one Chris thought was, like, 60?"
    g level "Yes, that would be him."
    show chris p1 level straight blank at threeleft
    show brit at middle
    show ginger at threeright
    with easeinleft
    pause 0.1
    c_s "..."
    g sad "Don't worry, Christeena; you're not the first person to ever make that mistake."
    c p2 left "Still... I still feel bad about that."
    b p2 level "Hey, as far as first impressions go, it could've been worse."
    b huhu left "It's not like you called him or his family retarded, right?"
    hide chris
    show don p1 mad grin straight at threeleft
    with dissolve
    pause 0.1
    d "Yeah, yeah..."
    g casual wide "...what?"
    d casual "Inside joke."
    g level blank "{cps=15}O...kay...{/cps}"
    play sound doorbell
    "We could then hear the doorbell ring."
    d casual "I'll get it!"
    hide don with easeoutleft
    show chris p1 straight casual blank at threeleft with dissolve
    pause 0.1
    g casual grin "Well, I suppose I should leave you kids to hang out with each other while us adults talk."
    b p1 straight raised grin "Yeah, that's probably for the best. I don't feel like talking about politics or the weather or whatever you old people talk about."
    show ginger sad
    "Mom just chuckled as she walked towards the other parents. By then, Mr. Truman had already entered the backyard."
    hide ginger
    show brit at tworight
    show chris at twoleft
    with easeoutright
    pause 0.1
    b p2 casual "Anyhoo, I'm thirsty. You guys want anything from the cooler?"
    c sad grin "Can you see if they have any Hilly Dew?"
    b p1 raised "I can, and I will!"
    b "Alex, you want anything?"
    $ b_dare_talk = False
    $ c_dare_talk = False
    if persistent.choices["23"] == 1:
        jump girltalk_b
    elif persistent.choices["23"] == 2:
        jump girltalk_c
    else:
        menu:
            "Walk over with Brittney":
                $ persistent.choices["23"] = 1
                jump girltalk_b
            "Stay with Christeena":
                $ persistent.choices["23"] = 2
                jump girltalk_c

    label girltalk_c:
        $ C_Points += 1
        $ c_dare_talk = True
        a "Nah, I'm good. Thanks, though."
        $ b_partial = True
        b p2 casual grin "Alright, then."
        hide brit with easeoutright
        pause 0.25
        $ b_partial = False
        show chris:
           ease 0.5 close_c
        pause 0.6
        if persistent.choices["18"] == 1:
            if persistent.choices["19"] == 2:
                jump animetalk_c
            elif persistent.choices["20"] == 1:
                jump kisstalk_c
            elif persistent.choices["20"] == 2:
                jump kisstalk_b_d_c
            elif persistent.choices["20"] == 3:
                jump punchtalk_b_c_c
        elif persistent.choices["18"] == 2:
            if persistent.choices["19"] == 1:
                jump kisstalk_c_c_
            elif persistent.choices["19"] == 2:
                jump flashtalk_c_t
            elif persistent.choices["19"] == 3:
                jump punchtalk_c_c
        elif persistent.choices["18"] == 3:
            if persistent.choices["19"] == 2:
                jump tampontalk_c
            elif persistent.choices["20"] == 1:
                jump pushuptalk_c
            elif persistent.choices["20"] == 2:
                jump pondtalk_c
            elif persistent.choices["20"] == 3:
                jump kisstalk_c_d_d

    label girltalk_b:
        $ B_Points += 1
        $ b_dare_talk = True
        a "You know what? Sure. I'll head over there with you and see what they've got."
        $ b_partial = True
        b p2 grin casual "Good deal."
        scene bg backyard_w with dissolve
        pause 0.1
        $ b_partial = False
        "Brittney and I started walking towards the coolers."
        if persistent.choices["18"] == 1:
            if persistent.choices["19"] == 2:
                jump animetalk_b
            elif persistent.choices["20"] == 1:
                jump kisstalk_b
            elif persistent.choices["20"] == 2:
                jump kisstalk_b_d_b
            elif persistent.choices["20"] == 3:
                jump punchtalk_b_b
        elif persistent.choices["18"] == 2:
            if persistent.choices["19"] == 1:
                if C_Kiss == True:
                    jump kisstalk_b_c_t
                if C_Kiss == False:
                    jump kisstalk_b_c_f
            elif persistent.choices["19"] == 2:
                jump flashtalk_b_c
            elif persistent.choices["19"] == 3:
                jump punchtalk_b_c
        elif persistent.choices["18"] == 3:
            if persistent.choices["19"] == 2:
                jump tampontalk_b
            elif persistent.choices["20"] == 1:
                jump pushuptalk_b
            elif persistent.choices["20"] == 2:
                jump pondtalk_b
            elif persistent.choices["20"] == 3:
                jump kisstalk_b_d_d

label britreturns:
    if b_dare_talk:
        "We had almost reached Christeena, who was turned away from us."
        "Brittney then leaned towards me and whispered."
        $b_blink = True
        b p2 level right huhu "I've got an idea. Play along."
        "She then slid the soda into her pocket, but it was sticking out halfway."
        hide brit with dissolve
        pause 0.1
        "We finally made our way back to Christeena, who seemed relieved to see us."
        show chris p1 straight casual blank at twoleft with dissolve
        pause 0.1
        show brit p1 straight casual grin at tworight with easeinright
        pause 0.1
    if b_dare_talk:
        b "Good news, Chris!"
    else:
        b_o "Good news, Chris!"
    if c_dare_talk:
        "I turned and saw that Brittney had returned with a water bottle in her hand."
        $c_blink = True
        show chris casual straight blank:
            ease 0.5 twoleft
        show brit p1 straight casual grin at tworight with easeinright
        pause 0.1
    b "They do have Hilly Dew!"
    c p2 grin "Yeah, I figured as much."
    c_s blank "..."
    c "Where is it?"
    b p2 blank "Oh, you mean you wanted me to get you one?"
    c p2 mad hanging "What the hell did you think I wanted?"
    b level huhu left "You just told me to see if they had any!"
    c blank "Brittney!"
    if b_dare_talk == True:
        "Christeena then turned towards me to try and get a reading off me, I assume."
        if persistent.choices["24"] == 1:
            jump playalong_b
        elif persistent.choices["24"] == 2:
            jump spoilthefun_b
        else:
            menu:
                "Play along with the joke.":
                    $ persistent.choices["24"] = 1
                    jump playalong_b
                "Spoil the fun.":
                    $ persistent.choices["24"] = 2
                    jump spoilthefun_b
        label spoilthefun_b:
            $ C_Points += 1
            "I gave a small grin and looked down at Brittney's pocket."
            show chris casual
            "Christeena then looked down at Brittney's pocket, as well, and a smile arose on her face."
            c raised grin p1 "Brit, what's that in your pocket?"
            jump endofprank
        label playalong_b:
            $ B_Points += 1
            a "Don't look at me. I thought that's what you meant, too!"
            $ c_blush = True
            c hanging "What?!"
            c blank "There is no way you both are that stu--"
            $ c_blush = False
            show chris p2 straight casual blank at twoleft
            "Christeena then looked down at Brittney's pocket, and the gig was up."
            c raised grin p1 "Brit, what's that in your pocket?"
            jump endofprank
    else:
        "Surely Brittney wouldn't be THAT much of a jerk, would she?"
        "..."
        "I then noticed something bright green sticking out of her pocket."
        show brit straight raised grin
        "I looked and saw that she was looking me, clearly now knowing that I know."
        if persistent.choices["24"] == 1:
            jump playalong_c
        elif persistent.choices["24"] == 2:
            jump spoilthefun_c
        else:
            "Hm..."
            window hide
            menu:
                "Play along with the joke.":
                    $ persistent.choices["24"] = 1
                    window show
                    jump playalong_c
                "Spoil the fun.":
                    $ persistent.choices["24"] = 2
                    window show
                    jump spoilthefun_c
    label spoilthefun_c:
        $ C_Points += 1
        "Well, I guess the gig is up."
        a "Brittney, what's that in your pocket?"
        show chris casual
        "Christeena looked down and quickly saw what I had seen."
        jump endofprank
    label playalong_c:
        $ B_Points += 1
        "I suppose it couldn't hurt to play along."
        a "Brittney, I can't believe you didn't grab a soda for her!"
        b p1 level opened_smile "Hey, I was just following her orders!"
        c p1 hanging "Brittney, you--!"
        show chris casual blank
        "That's when she happened to look down, something seeming to catch her attention."
        show chris raised grin p2
        "The gig's officially up."
        c "Brit, what's that in your pocket?"
        jump endofprank

label endofprank:
    b p2 right level grin "Nothing. I'm just happy to see you."
    c level p1 grin "C'mon, Brit. Hand it over."
    $ b_partial = True
    b level huhu straight "Fine."
    "She then pulled the can out of her pocket and handed it to Christeena, who rolled her eyes and accepted the soda."
    $ b_partial = False
    show brit p1 straight level grin at tworight
    "Brittney then looked towards the back door and her eyebrows raised."
    b p2 casual "Hey, look who it is!"
    "I turned towards the back door to see Donald entering the yard with a familiar woman behind him."
    show brit zorder 1:
        ease 0.5 xalign 1.0
    show chris zorder 1:
        ease 0.5 xalign 0.0
    pause 0.5
    show don p1 straight casual grin at four2 zorder 2
    show kelly p1 straight casual grin at k_four3 zorder 2
    with dissolve
    pause 0.1
    b p1 casual opened_smile straight "Hey, Kelly!"
    k raised "Howdy!"
    a "Huh. Didn't expect to see you here, Kelly."
    k level "Well, you won't be seein' me for long; I just came to drop those off."
    "Donald held up a plastic bag with {i}'Kelly's Deli'{/i} plastered all over it."
    c p2 casual dot straight "What is it?"
    k raised "Well, the deli 'accidentally' made too many buns last night, so I figured Don might have use for them for his cookout birthday party."
    a "Since when do you sell hot dogs?"
    k mad "That's the other strange thing! We don't, yet someone somehow made brat buns instead of sandwich buns!"
    $ b_partial = True
    b p2 raised grin "Quite the unusual blunder."
    k level "Indeed."
    k sad "Anyway, I just wanted to come back here to say hi to y'all."
    d sad blank "You sure you can't stay for a little bit?"
    k blank "Love to, but I've got other plans."
    k raised grin "After all, you haven't forgotten what the 4th of July means for the rest of the country, right?"
    d right level grin "Alright, fair enough."
    d straight raised "Just don't go blowing up a finger or 5 on us. Someone has a deli to run."
    k mad "Boy, I've been doin' this for years. I know how to handle a firework."
    d level "And Dale Earnhardt knew how to drive a racecar."
    k level "Alright, alright. No need to go makin' comparisons."
    k casual "Well, I'll catch y'all later!"
    d casual smile "See ya, Kelly!"
    $ b_partial = False
    show brit p1 straight casual opened_smile at four4 zorder 1
    b "Later!"
    c p1 grin "Bye, Kelly!"
    a "See you later!"
    "Kelly waved to us all before entering the house."
    hide kelly
    with dissolve
    pause 0.1
    show don:
        ease 0.5 xalign 0.5
    show brit:
        ease 0.5 xalign 0.9
    show chris:
        ease 0.5 xalign 0.1
    pause 0.6
    a "So why didn't Kelly just say she made those buns for Donald?"
    b p2 raised grin "And risk word getting out that she used deli supplies for personal reasons?"
    a "Right, because THAT'S what would get Kelly in legal trouble."
    b right level huhu "Fair enough."
    c p2 dot "Guys... I just realized something."
    show brit left casual blank
    d left blank "What?"
    c p1 hanging "Deer brats...{w=.5} on fresh Kelly's Deli buns..."
    show don straight dot
    b small hanging "*gasp*"
    b p1 sad opened_smile straight "That sounds like the most perfect food combination to ever exist!"
    c p2 smile "Exactly!"
    d left level grin "Well, what do you say I set the buns on the table, and we test this theory once it's time to eat?"
    b p2 raised grin "Sounds excellent!"
    hide brit
    hide don
    hide chris
    with dissolve
    pause 0.1
    nvl clear
    window hide dissolve
    nvl show dissolve
    narrate """
    With that, we sat down in some lawn chairs and had some casual conversation.

    Occasionally, Donald would have to leave to greet new guests that had arrived, which ranged from his cousins to classmates.

    He introduced us to the guests we didn't recognize, which, in my case, were the classmates, while it was the family for Brittney and Christeena.

    These students seemed very nice, which was honestly to be expected from a friend of Donald's.

    Of course, Donald could be friends with Charles Manson if he really wanted to. He's just that charismatic.

    Anyway, they all said they were happy to meet me, and they looked forward to seeing me at school with them.

    Well, I'm glad I don't have to fully rely on Donald introducing me to everyone come school starting.
    """
    nvl clear
    narrate """

    Eventually, enough guests arrived that it warranted starting up the grill and cooking our lunch.

    The girls were really excited to try the deer brats with the buns, and admittedly, I was pretty curious to how just the deer brat in general would taste.

    Finally, Mr. Waters let everyone know that we could start getting our food.

    Brittney practically teleported to the front of the line, though she did apologize to the people she nearly bumped into.

    Yes.{w=.5} 'People'.{w=.5} Plural.

    After a few minutes, all four of us managed to get our food, and we met back at the chairs.
    """
    nvl clear
    nvl hide dissolve
    window show dissolve
    pause 0.1
    show brit p1 straight raised grin at middle
    show don p1 straight casual grin at threeright
    show chris p2 straight casual blank at threeleft
    with dissolve
    pause 0.1
    b opened_smile "Alright, let's all take a bite at the same time!"
    d raised smile "Alright!"
    "We each held up our brat to our mouths and looked at each other, waiting for a countdown."
    b grin p1 "One...{w=1} Two...{w=1} Three!"
    "Each of us took a bite."
    "We each had the same immediate reaction."
    show brit p1 sad dot
    show don level blank
    c small sad hanging "Ah! Hot!!"
    "I spat my bite onto my plate on reflex and turned to Christeena."
    a "Yet a Grilled Ham n Cheddar is tolerable?"
    c straight level blank "..."
    "Despite how much my mouth was burning, I could feel some of the juices along my teeth."
    "I ran my tongue across and tasted."
    a "Huh."
    a "That tastes pretty good!"
    show chris p1 dot straight casual
    show don raised grin
    b p2 closed_smile raised "Told ya!"
    b p1 mad opened_smile "Though adding the bun is the real test!"
    "I picked up the bite from my plate and blew on it. The steam seemed to die down a bit."
    "Ripping a bit of my bun off, I wrapped it around the bite and put the whole thing in my mouth."
    "Nearly following suit, Brittney took a bite of her brat."
    "..."
    $b_blink = False
    b p2 closed huhu sad "{cps=6}Ohhhhh{/cps} yeah!{w=.5} That's incredible!"
    a "*cough*"
    d sad grin "You alright, dude?"
    a "The brat has a bit of a kick."
    $b_blink = True
    b p1 casual straight opened_smile "I know, right? It's, like, the best part!"
    "I looked and saw that Christeena had finished chewing her bite with a grin."
    c raised p2 grin "I swear we really need to get Mom to steal this bread recipe."
    b raised p2 grin "You think I haven't tried convincing her?"
    c smile "Well, we should try harder!"
    $ m_partial = True
    show brit zorder 2
    show don zorder 2
    show chris zorder 2
    show martha p1 straight raised grin zorder 1 at m_four2 with dissolve
    pause .1
    show chris casual dot
    show brit casual blank
    mu "Not happening."
    "She had seemingly teleported behind her daughters and placed a hand on each of their shoulders."
    $ b_partial = True
    b p2 level blank "You're no fun."
    $ m_partial = False
    show martha p1 level straight grin at m_four2
    mu "It's called 'Not Being Fired', sweetie."
    $ b_partial = False
    show brit p2 straight raised grin at middle zorder 2
    b "Who needs a job when you can have bread?"
    show martha sad
    "Mrs. Truman gave her daughter a pat on the shoulder before chuckling and walking off."
    hide martha with easeoutright
    pause 0.1
    "With no new conversation ideas at the moment, we continued our lunch."
    hide chris
    hide don
    hide brit
    with dissolve
    pause 0.1
    window hide dissolve
    scene bg fade with wipeleft
    pause 1
    scene bg backyard_w with wipeleft
    window show dissolve
    show brit p2 straight raised grin at middle with dissolve
    pause 0.1
    b "Well, as tempted as I am to get seconds, I need to watch my figure."
    show brit:
        ease 0.5 xalign 0.75
    show chris p2 straight raised blank at twoleft with dissolve
    pause 0.1
    c "You mean the thin, blocky figure you've always had despite once eating a 3 pound burger in one sitting?"
    a "Three pounds?!"
    $ b_wink = True
    b p1 tongue raised "Even the best athletes get a cheat day!"
    $ b_wink = False
    show brit p1 straight casual grin
    b "Anyway, I think I'm gonna burn these calories by playing some bags."
    b p2 right level huhu "Or, as Kelly calls it, {i}corn-haul{/i}."
    a "...what?"
    show brit:
        ease 0.5 xalign 0.5
    show chris:
        ease 0.5 xalign 0.1
    show don p1 straight raised grin at threeright with dissolve
    pause 0.1
    d "{i}Cornhole{/i}, as we non-southeners pronounce it."
    b p1 left casual grin "Anyone wanna play?"
    c p2 level blank "I think I'm just gonna go inside for a bit, if that's alright. The heat's getting to me a little."
    "Now that she mentioned it, the temperature certainly did seem to get higher over the past hour."
    b p1 straight mad grin "Yeah, I wasn't expecting you to play, anyway."
    b casual "What about you, Donnie?"
    d left sad "Maybe later. Not in the mood for physical activity right now."
    b level p2 "Scared of getting your ass beat?"
    d raised smile "What if I said 'yes'?"
    b_s blank "..."
    b left huhu "I dunno. Nobody's ever told me that in response."
    b straight casual p1 grin "But, I won't force ya to play."
    b level "Alex? Whaddaya say?"
    if persistent.choices["25"] == 1:
        jump bagswithbrit
    elif persistent.choices["25"] == 2:
        jump chillinsidewithchris
    elif persistent.choices["25"] == 3:
        jump hangoutwithdon
    else:
        menu:
            "Play bags with Brittney.":
                $ persistent.choices["25"] = 1
                jump bagswithbrit
            "Chill inside with Christeena.":
                $ persistent.choices["25"] = 2
                jump chillinsidewithchris
            "Hang out with Donald.":
                $ persistent.choices["25"] = 3
                jump hangoutwithdon

label bagswithbrit:
    a "Yeah, that sounds fun."
    b p2 opened_smile casual "Awesome!"
    scene bg backyard_w with dissolve
    pause 0.1
    "And so, Christeena went inside while Donald stayed sitting."
    "Meanwhile, Brittney and I stood up and walked over towards the bags setup."
    show brit p2 level blank straight at close_b with dissolve
    b "Hey, Alex?"
    a "Yeah?"
    b "Be honest."
    if persistent.choices["26"] == 1:
        b raised hanging p1 "Did you just want to play because you felt bad for me or something?"
        jump feltbad
    if persistent.choices["26"] == 2:
        b raised hanging p1 "Did you just want to play because you felt bad for me or something?"
        jump didntfeelbad
    else:
        b raised hanging p1 "Did you just want to play because you felt bad for me or something?{nw}"
        menu:
            b "Did you just want to play because you felt bad for me or something?{fast}"
            "Yes":
                $ persistent.choices["26"] = 1
                jump feltbad
            "No":
                $ persistent.choices["26"] = 2
                jump didntfeelbad

    label feltbad:
        a "Maybe just a little."
        b p2 right blank "Hm..."
        a "But it's not like I don't want to play. I swear."
        jump bagsgame
    label didntfeelbad:
        $ B_Points += 1
        a "No, of course not!"
        b blank p2 raised "Are you sure?"
        a "Positive."
        jump bagsgame
    label bagsgame:
        b_s straight level blank "..."
        b grin "Alright. I'll believe you."
        a "Why do you ask?"
        b p1 casual "Just curious."
        b p2 raised opened_smile "Alright, let's play!"
        "Brittney and I got behind one of the boards so that we were facing the other one in the distance."
        b casual grin "Who's going first?"
        a "Well, it's always ladies first."
        b level "True."
        $ b_wink = True
        b tongue raised "So, I guess that means you're going first!"
        a "I guess it does!"
        $ b_wink = False
        $b_blink = False
        show brit p2 closed sad opened_smile
        "We both gave a chuckle as I held my bag in front of me and focused."
        hide brit with dissolve
        pause .1
        $b_blink = True
        "I gave a few slow practice underhand swings before letting loose a fast toss."
        "..."
        play sound bag_hit
        "It smacked onto the board and slid off the side."
        $ b_partial = True
        show brit p2 straight level huhu at close_b with dissolve
        pause .1
        b "Awwww, nice try~!"
        "Her belittling tone wasn't helpful."
        a "Let's see you do better!"
        $ b_partial = False
        show brit p1 mad grin straight at close_b
        b "Gladly!"
        "Brittney picked up her bag and stared at the wooden box."
        show brit level blank
        "She got into a lunging position with her legs while her arm was held out in front of her, all while never breaking eye contact with the board."
        "Her goofy and playful expression was long gone and replaced with one of extreme focus."
        "..."
        "She gave a few practice swings."
        "..."
        show brit:
            ease 0.2 xalign 0.6
            ease 0.2 xalign 0.5
        "And in a 'blink-and-you'll-miss-it' move, she seemingly launched the bag!"
        play sound woosh
        "Before I could properly react, I heard a {i}whoosh{/i} sound, followed by a soft {i}thud{/i}."
        "I felt myself pausing, trying to comprehend what just happened."
        "I finally looked at the board and saw that the bean bag had landed perfectly in the hole."
        $b_blink = False
        show brit mad closed closed_smile:
            ease 0.2 yalign 0.3
            ease 0.2 yalign 0.2
            pause 0.1
            repeat 3
        b "{cps=7}BOOOOOM{/cps} Shakalaka!!"
        a "Alright, hold your horses, Usher! That's only the first toss!"
        $b_blink = True
        $ b_partial = True
        b level huhu straight "And I'm already in a 3-point lead!"
        a "It's anyone's game."
        $ b_partial = False
        show brit p2 raised grin straight at close_b
        b "Nah. {w=.5}It's MINE."
        "Alright.{w=.5} Challenge accepted."
        hide brit with dissolve
        $ current_track = "\"Friendly Competition\""
        play music friendly_competition
        window hide dissolve
        nvl show dissolve
        narrate """
        At first, it truly was a more playful competition.

        As you could probably guess, it didn't stay that way for long.

        I eventually got warmed up enough and managed to get some on the board, and even a few into the hole.

        The realization that she might actually lose got Brittney really nervous.

        Of course, she would never admit that she was nervous, but her decrease in witty comments and insults was all the proof I needed.

        Eventually, we were both really quiet as we played, save the occasional 'Yes!' and such.

        Our game even attracted a few of the party guests, though most didn't really stay for long.
        """
        nvl clear
        narrate "Finally, we were at the game point."
        nvl clear
        nvl hide dissolve
        window show dissolve
        pause 0.1
        show brit p2 straight level blank at close_b with dissolve
        pause .1
        b ".{w=1}.{w=1}."
        "She was staring at the board harder than I ever could have imagined."
        "I swear she hasn't moved in minutes."
        "..."
        show brit:
            ease 0.2 xalign 0.6
            ease 0.2 xalign 0.5
        "{i}WHOOSH!{/i}"
        "She quickly tossed the bag."
        show brit sad
        "Everyone was silent for that one second that it flew in the air, not moving a muscle in their bodies apart from their eyes."
        "..."
        play sound bag_hit
        "{i}THUD{/i}"
        "The bag smacked into the board... {w}and bounced right off, into the grass."
        "A moderate groan of disappointment could be heard from the crowd, as well as a few 'Yeah!'s."
        show brit p1 mad frown
        "Brittney, herself, clenched her fists and let out a grunt of anger."
        b "Damn it...!"
        "To say she's a little annoyed is a bit of an understatement."
        "Alright. I'm up."
        hide brit with dissolve
        "Like Brittney, I got into a lunge position, never losing focus on the board."
        "All eyes were on me."
        "No pressure or anything, right?"
        "..."
        window hide dissolve
        pause 2
        window show dissolve
        "I finally threw the bean bag."
        "Once again, nobody said anything as it flew in the air."
        "..."
        "It was coming down."
        "..."
        play sound bag_hit
        "{i}THUD{/i}"
        "The bag hit the board."
        "It slowly slid down."
        "Everyone stared at the bag, half of us wanting it to stop, the other wanting it to keep going."
        "..."
        "Right before it slid off, it stopped."
        "The crowd cheered, and even applauded, as I jumped in excitement."
        a "Yes! I won!"
        show brit p2 straight level grin at close_b with dissolve
        pause 0.1
        "Brittney looked at me with a face that simultaneously said {i}'Good game.'{/i} and {i}'Fuck you.'{/i}."
        hide brit with dissolve
        $ current_track = "None"
        stop music fadeout(3)
        "With that, half of the spectators walked off, while a few said they wanted to play."
        "Brittney and I decided it was time for others to have some fun, and we walked towards the chairs."
        $ b_partial = True
        $ current_track = "\"Relaxation in the Country\""
        play music relaxation_in_the_country
        show brit p2 straight level huhu at close_b with dissolve
        pause .1
        b "Well played, Alexander."
        $ b_partial = False
        show brit p1 straight raised opened_smile at close_b
        b "I guess I underestimated ya."
        a "I guess you did."
        show brit casual blank
        p_o "Nice throwin' out there, Ush!"
        show brit zorder 2:
            ease 0.5 xalign 0.1
        show percy p1 straight casual grin zorder 1:
            alpha 0.0
            middle
            parallel:
                ease 0.5 tworight
            parallel:
                ease 0.5 alpha 1.0
        pause 1
        b opened_smile "Oh, hey, Percy!"
        show brit:
            ease 0.5 twoleft
        pause .6
        $ P_Name = "Percy"
        b p2 raised grin "Alex, you remember Percy, right?"
        a "Kinda hard to forget someone who's the lead singer of a cover band, don't ya think?"
        b left level huhu "Fair enough."
        "Brittney had introduced me to The Reagans properly about a week or so after I moved here."
        "Admittedly, they were quite..."
        "Well, there's really no other way to say it:{w} 80s."
        "Their appearance wasn't just limited to their performances. If you had seen them in public, you'd think they were lost time travelers."
        "Still, they're pretty good at what they do, giving us a small performance to show off their skill."
        b straight p1 casual grin "Where's the rest of the band?"
        p raised "Mike and Karrie are visitin' his family back in New York for the holiday, and James is practicin' for a new song."
        p level "Nicole's just runnin' some errands, though; she said she'd try to be here soon."
        a "{i}'New song'{/i}? I thought you guys were a cover band."
        p "Well, yeah, that's our main gig, but we occasionally perform our own original works for those interested."
        a "No kidding? Well, that's cool to hear!"
        p mad "Anyway, you both put on quite a performance, yourselves!"
        p "Especially you, Al."
        a "Meh. I just got lucky."
        a "I would've lost if Brittney hadn't sucked ass."
        b p2 left level derp "I blame my lack of practice."
        p casual "Nah. You both did great out there!"
        p "Certainly better than I could do."
        b_s straight blank "..."
        b left huhu "Yeah, let's be real."
        $ b_partial = True
        b straight grin "The best thing you can throw is your back."
        p raised "And even then, I suck at doing THAT!"
        $ b_partial = False
        $ b_wink = True
        b tongue raised "I rest my case."
        p casual "Well, I'm still pretty hungry, so I'm gonna grab some more grub."
        $ b_wink = False
        show brit p1 casual right grin at twoleft
        b "Alright, then. Talk to you later, Percy!"
        a "Yeah, see ya!"
        "Percy gave a nod as he walked towards the food line."
        hide percy with easeoutright
        pause 0.1
        show brit straight:
            ease 0.5 close_b
        pause 0.6
        show brit blank
        a "You seem to get along with Percy pretty well."
        b p2 raised opened_smile "Yeah, you could say that."
        b level right huhu "You might not believe it, but I'm a sucker for a good 80's song, so I suppose you could call it a match made in Heaven."
        a "Well, I hate to be THAT guy, but..."
        a "...doesn't it get suspicious to see a 17-year-old girl hanging out with a guy in his mid-20s?"
        $ b_partial = True
        b_s straight level blank "..."
        a "It's an honest question!"
        b_s raised "..."
        a "..."
        b mad "Honestly, I feel like I should be insulted..."
        $ b_partial = False
        show brit level right huhu p2 at close_b
        b "...but you do raise a good outsider's perspective."
        b p1 straight raised hanging "But if you think that either A. Percy is a pedophile or B. I would do anything of the sort with a guy a decade older than me..."
        a "I don't recall accusing anyone of anything. I just asked if it seemed odd."
        b p2 left level blank "Eh."
        b p1 raised straight grin "We're neighbors. Everyone on this street knows enough about each other to know if anyone comes off as suspicious."
        b "And nobody really fits the bill."
        a "We're talking about the same street that houses a mad scientist."
        b p2 right level derp "Oh, yeah."
        b "I keep forgetting about her..."
        b p1 straight raised opened_smile "Anyway, my point is that Percy and rest of the Reagans are clean and harmless."
        $ b_partial = True
        b huhu level "Besides, do you really think they'd let pedophiles live right by this many minors?"
        a "Do you want the honest answer or the one that makes your point?"
        b_s blank "..."
        a "Hey, you'd be surprised."
        b_s raised "..."
        a_s "..."
        $ b_partial = False
        show brit casual left p1 blank at close_b
        "We could then hear some cheering from the bags boards. Sounds like someone scored some points."
        b p2 straight raised grin "Whaddaya say we see who's winning?"
        a "Sounds good to me!"
        jump presenttime

label chillinsidewithchris:
    a "Thanks, but I think I'll follow Chris's lead and head inside."
    $ b_wink = True
    b p2 mad tongue "{cps=15}Laaaaaaame.{/cps}"
    $ b_wink = False
    show brit p1 level grin straight
    b "Well, I'm sure someone out here wouldn't mind playing a round or two."
    b left huhu "Enjoy your time inside, you two~!"
    $ c_blush = True
    c_s mad blank "..."
    scene bg backyard_w with dissolve
    pause 0.1
    $ c_blush = False
    "And so, Brittney walked towards the crowd of people to find someone to play bags with while Donald stayed sitting."
    "Meanwhile, Christeena and I walked inside of the house."
    "Though, it's worth noting she still sported that angry yet embarrassed look."
    $ current_track = "None"
    stop music fadeout(1.5)
    pause 0.5
    scene bg living_w with wipeleft
    pause 0.5
    $ current_track = "\"Chillaxin'\""
    play music chillaxin
    "We made it to the living room, where a familiar sibling of mine could still be found on the couch playing on the TS."
    "Although, this time, he has company sitting next to him, equally as glued to the screens."
    show harry p1 casual straight grin at tworight
    show daniel p1 straight casual grin at twoleft
    with dissolve
    pause 0.5
    a "Oh, hey, Daniel! I didn't know your family was here."
    da "We got here about 10 minutes ago."
    h raised blank "I thought it was 20."
    da level "Ah, whatever. Doesn't matter."
    show chris p2 straight raised grin at close_right_c
    show harry at middle
    show daniel at threeleft
    with easeinright
    pause 0.1
    c "I'm honestly a little shocked that neither of their mothers have forced them outside."
    a "Between the choice of forcing them outside, where they'll do nothing but complain, and letting them stay inside, where they'll be quiet, what would you do?"
    c level left "I guess."
    scene bg living_w with dissolve
    pause 0.1
    "Christeena and I sat on the couch perpendicular to Harry and Daniel's."
    "They seemed to be minding their business with the game, so I don't think they'll be too much of an issue."
    if cutoff:
        "Still, with them here, it would be a little awkward to further talk about the conversation Chris and I had earlier."
        "Then again, even if they weren't here, maybe a party isn't the best place to keep talking about it."
        "We're supposed to have fun, so we should just do that and not worry about anything else, at least right now."
    "But the question now is what to do..."
    show chris p1 straight casual grin at close_c with dissolve
    pause 0.1
    c "Let's see what's on TV."
    a "That'll work."
    hide chris with dissolve
    pause 0.1
    window hide dissolve
    nvl show dissolve
    narrate """
    Christeena turned on the TV.

    The first thing we saw was the local news.

    Well, I say 'local', but it was really a Chicago news station, so I guess it's more of a force of habit to call it such.

    Still, Christeena rightfully wasn't in the mood to watch the news, so she checked and scrolled through the guide.

    While scrolling through the guide, the news could still be seen and heard in the upper corner.

    The reporters were talking about how people across the city were celebrating the Fourth of July, and giving warnings about launching fireworks and such.

    Of course, they would be having a large firework show later that evening, when it got dark enough.

    That got me thinking...
    """
    nvl clear
    nvl hide dissolve
    window show dissolve
    pause 0.1
    show chris p2 straight casual blank at close_c with dissolve
    pause 0.1
    a "Hey, do they have any firework shows around here?"
    c p1 grin "Yeah, there's a farmer in Smalltown who does the honors."
    c "I think they start at around 8 or 9."
    a "Cool! You going?"
    c level blank "Maybe."
    a "What do you mean?"
    c p2 left "Eh. I'm not really into fireworks."
    c straight raised "I mean, yeah, they were cool when I was younger, but now it's just the same old thing."
    c hanging "{i}\'Ooo, look! A large explosion and pretty colors!\'{/i}"
    a "Yeah, I get what you mean; I've picked up on that recently, as well."
    da_o "So?"
    show chris casual dot zorder 2 at close_right_c
    show harry p1 straight casual blank zorder 1 at middle
    show daniel p1 straight casual grin zorder 1 at threeleft
    with easeinleft
    pause .1
    "We turned towards Daniel. Even Harry was looking at him with curiosity."
    da smile "It's still cool to watch things blow up in the sky! Especially when they look like they're about to fall down onto you!"
    show chris sad blank:
        ease 0.1 xalign 0.91
        block:
            ease 0.2 xalign 0.89
            ease 0.2 xalign 0.91
            repeat 2
        ease 0.1 xalign 0.9
    "Christeena shivered."
    c p1 level "To each their own, but that's the thing that freaks me out the most."
    da level grin "Pft. I hope I don't become as lame as you when I grow up."
    show chris mad hanging
    "Christeena stared at the little Hispanic boy with a forced offended look."
    c p2 raised smile "Harry, I think you're being a bad influence on this precious child!"
    h mad frown "Hey! I am not!"
    da mad blank "Yeah, he is not!"
    a "Whatever you boys say..."
    "Harry then got off the couch."
    h level grin left "C'mon, Daniel. Let's play in the kitchen."
    "Daniel got off the couch, as well, and followed my brother into the kitchen."
    hide harry
    hide daniel
    with easeoutright
    pause 0.1
    $c_blink = False
    show chris closed_happy sad smile at close_c with easeinright
    "Christeena and I just laughed quietly."
    a "I guess it's kinda nice to see Harry be the big brother figure for once."
    $c_blink = True
    c p1 raised straight grin "Well, from what I know about him, I hope he doesn't corrupt poor little Daniel Rodriguez."
    a "Hey, every child's innocence is lost soon enough."
    show chris level
    c_s "..."
    a "You know what I meant."
    if C_Points >= 6:
        $ c_blush = True
        show chris sad p2
        "She just chuckled, though she still looked me in the eye with a smile."
        "I looked back at her, sporting my own smile, albeit it being a bit more of a forced, confused one."
        "..."
        "But I can't deny that looking at her emerald eyes certainly was quite incredible."
        "..."
        if C_Kiss == True:
            show chris:
                ease 0.5 zoom 1.1
            pause .6
            "She got a little bit closer to me."
            "I could feel my heart pounding a bit faster."
            "She then spoke in a whisper."
            c "Hey, uh..."
            if persistent.choices["23"] == 2:
                c right "I know I said I hardly knew you and all, but..."
            else:
                c right "I know this might sound a bit weird, but..."
            c straight "Do you think that maybe we could... you know..."
            c p1 left "...do THAT... {w=0.5}again...?"
            a_s "...!"
            "Well, way to be subtle, Chris."
            "But to answer her question..."
            if persistent.choices["26"] == 1:
                jump kissher
            elif persistent.choices["26"] == 2:
                jump dontkissher
            else:
                menu:
                    "Kiss her.":
                        $ persistent.choices["26"] = 1
                        jump kissher
                    "Don't kiss her.":
                        $ persistent.choices["26"] = 2
                        jump dontkissher
            label kissher:
                $ C_Points += 1
                "Well, without any more hesitation, I leaned towards her."
                show chris straight:
                    ease 0.5 zoom 1.2
                pause 1
                show fade zorder 2 with dissolve
                pause 1
                $c_blink = False
                show chris closed_happy p2
                hide fade with dissolve
                pause .1
                c "..."
                "Well, we were both smiling like idiots, but oh well."
                show chris:
                    ease 0.5 zoom 1.1
                pause .6
                $c_blink = True
                c straight "T-Thanks."
                c right "I know that was weird to ask, but..."
                jump kissexplanation
            label dontkissher:
                a "N-Not right now."
                c sad dot "Eh?"
                "I then pointed behind me towards the kitchen doorway."
                a "I'd hate for them to waltz in unexpectedly."
                c grin p2 "O-Oh. Right."
                c right "Sorry. I know that was weird to ask, but..."
                jump kissexplanation
            label kissexplanation:
                c straight "Well, I guess it's just finally nice to know what kissing feels like."
                a "Wait, you mean that kiss at the cabin was...?!"
                c left "Yeah..."
                a "Why didn't you say something? I would've totally had you wait for a more special occasion!"
                c p1 straight "It's okay, Alex. Really."
                $ c_blush = False
                c p1 level blank straight "It gets kinda embarrassing being one of the few girls your age who hasn't even done so much as a kiss."
                c right dot "I mean, yeah, that wasn't exactly the way I planned on doing it, but..."
                c sad straight grin "...I'm glad it was with a gentleman like you."
                a "Gentleman? What do you mean?"
                c level blank p2 "Well, you could've dared me to do something much worse."
                c grin "And you even offered to fake the kiss just so I could feel more comfortable."
                a "But, you haven't really known me for that long..."
                c sad right "Well, yeah, but..."
                c casual straight blank "Wait..."
                extend mad " is there something I should know that you're not telling me?"
                a "Like what?"
                c level blank "I don't know... I just didn't like the way you said that."
                a "I'm sorry."
                c sad dot "No, don't be; I can over think at times."
                c grin "But anyway, even though I haven't known you for that long..."
                c level blank "...and I still wouldn't consider doing anything like dating yet..."
                c p1 sad grin "...it's still nice to get that out of the way."
                "..."
                "Am I crazy, or did I just get used to mark a box on a to-do list?"
                "..."
                "Ah, whatever. I got my first kiss out of the way now, too, so I can't complain too much."
        "Finally, she cleared her throat and turned back to the TV, which was still showing both the TV guide and the news."
        c p1 left sad grin "A-Anyway, we should probably pick something."
        a "Probably."
    else:
        "She just chuckled in response."
        c p1 raised smile "Anyway, we should probably pick something."
        a "Probably."
    hide chris with dissolve
    pause 0.1
    jump presenttime

label hangoutwithdon:
    a "Thanks, but I'll pass."
    $ b_wink = True
    b p2 mad tongue "{cps=15}Laaaaaaame.{/cps}"
    $ b_wink = False
    show brit p1 level grin straight
    b "Well, I'm sure someone out here wouldn't mind playing a round or two."
    b p2 raised opened_smile "Catch you losers later!"
    scene bg backyard_w with dissolve
    pause 0.1
    "And so, Brittney walked towards the crowd of people to find someone to play bags with while Christeena walked into the house."
    "Meanwhile, Donald and I continued to stay sitting at our chairs in silence."
    "I took this moment to actually look around the backyard."
    "There were a decent amount of guests, maybe around 30 or so?"
    show don p1 straight casual blank at close_d with dissolve
    pause 0.1
    a "Man, it must be nice having so many people here."
    d level right "A little."
    d raised straight "But it's a bit cramped at times."
    a "Yeah, tell me about it."
    "While still bigger than the essentially nonexistent yard back in Chicago, Donald's backyard is still not exactly 'big enough' for a crowd of this size."
    d smile "I think I might actually hang out on the front porch for a bit, if I can sneak through."
    d grin "You in?"
    a "Totally."
    hide don with dissolve
    pause 0.1
    "We got up from our seats and walked through the house seemingly unnoticed, where we eventually found ourselves on the front porch."
    scene bg house_w with dissolve
    pause 0.1
    $d_blink = False
    show don p1 closed casual wide at close_d with dissolve
    pause 0.1
    "Donald stretched his arms and yawned when he sat down on the steps."
    a "Long day?"
    $d_blink = True
    d straight raised grin "Heh. Don't get me started."
    d level right "Decorating the house, greeting the guests..."
    $d_blink = False
    d closed sad smile "I've faked so much positivity and optimism today, I might just be a future politician."
    $d_blink = True
    d straight raised grin "Not to say I'm not enjoying myself, mind you."
    a "Sure, sure."
    a "Well, regardless, the party turned out pretty well!"
    d casual smile "Yeah, agreed!"
    a "Though, honestly, it's just nice to finally be at another birthday party of yours after all these years."
    a "We seriously tried to make it those first few years, I swear!"
    d sad grin "Hahaha! I believe you."
    d level left "I get it. Smalltown isn't a quick, casual drive from Chicago, and I now understand that you guys literally weren't able to afford to come."
    d blank "I guess I'm partially to blame, though. After 2 years of you guys not being able to come down, I kinda just gave up a bit too quickly..."
    $ current_track = "None"
    stop music fadeout(5)
    d_s "..."
    a_s "..."
    a "Man, it's weird."
    show don straight
    a "We used to be so close back in Chicago. We were basically brothers."
    d grin "Don't let Harry hear you say that."
    "We both chuckled."
    a "But now..."
    "I continued, getting more serious."
    a "I dunno. It's been so long, it's like we're not as close as we were."
    a "I mean, for crying out loud, I basically had to guess on what I was going to get you for today."
    show don raised blank
    "He raised an eyebrow in what seemed to be both confusion and pain."
    a "I mean, I'm not trying to act like a dick here, but I just feel bad for not trying harder to stay in touch over the years."
    show don level grin
    "He then smiled and gave me a pat on the shoulder."
    $ current_track = "\"Reflection\""
    play music reflection
    d "Yeah, same here, man."
    d sad "But hey, that doesn't matter."
    d casual smile "Now we're neighbors again after all these years, and in a way, it's like we now have the chance to become close friends all over again!"
    a "I guess that's one way of looking at it..."
    a "Hm..."
    a "You know, I wonder..."
    a "...if I HAD came down to Smalltown at least once between our moves, how much different would the move have been for me?"
    a "I mean, I would've known what Smalltown was like, I would've met everyone down here sooner..."
    a "I dunno. Maybe I wouldn't have been so against it when it finally happened."
    d blank "Hm."
    d level left "That's a fair thought process."
    d casual straight "If you had visited when I first came here, you would've had a totally different idea of Smalltown when you moved here."
    a "Was it that different?"
    d "Well, the only neighbors that were here at the time were the Rodriguezes and Anna."
    a "What, were the other houses empty?"
    d raised "Yep."
    a "Is Berry Street just that odd of a place to live or something?"
    d right "Maybe not 'odd', but it's certainly a bit out of the way, as I'm sure you've noticed."
    "He wasn't kidding."
    "Berry Street is so secluded from the rest of Smalltown, that it practically feels like the street is its own little town of 21 residents."
    "That sounds like it would be some sort of world record, actually."
    d straight "Anyway, Anna was here first, then the Rodriguezes, then me."
    d casual "Then it was the Reagans, then Eleanor, then the Trumans, and finally you."
    a "All within 5 years?"
    d "Yup."
    a "Huh."
    "I then looked down the street. Since Donald's house was at the far end, I could get a good view of all 4 houses across from us."
    a "So, I guess the street was built relatively recently?"
    d level right dot "Around 2007, I believe."
    d raised blank "Why, though, I'm not sure. It certainly does seem very out of the way."
    d casual straight "But honestly, I don't really care."
    d grin "At the end of the day, I'm in a good town with good neighbors."
    d raised left "Especially the one in that house."
    "As he said that, he pointed to the house next door."
    a "Yeah, that Martha certainly is something."
    $d_blink = False
    show don sad closed
    "Clearly not expecting that response, Donald closed his eyes and gave a large grin and chuckle."
    a "But her daughter's not bad, either."
    $d_blink = True
    d straight raised smile "Yeah, you don't gotta tell ME that."
    show don level grin
    "Donald then sighed and looked forward blankly."
    d "Yeah, man. I'd say life here's pretty well."
    d right "I dare say that I don't miss Chicago in the slightest."
    a "Wow. You like Smalltown that much?"
    d blank "Well..."
    d "It's less about liking life in Smalltown and more about..."
    d "...not liking life in Chicago."
    a "Ah."
    d_s "..."
    a_s "..."
    "He then got up and stretched again."
    d raised smile straight "Anyway, enough depressing stuff. Let's head back to the party."
    d level grin right "I kinda wanna see how Brit's doing in her bags game."
    a "Alright. Let's--"
    show don straight casual blank
    play sound phone_vibrate
    "We could then hear a buzz coming from Donald's pocket."
    "He took out his phone and looked at the screen."
    show don level
    "He only looked at the screen for a split second before he got an upset look on his face."
    a "What is it?"
    "He kept staring, his eyes moving across the screen as he read the message."
    d left "On second thought, you go on back to the party without me. I gotta go do something."
    a "Like what?"
    d_s straight "..."
    a "Don, what's up?"
    d left "I..."
    play sound phone_vibrate
    "The phone buzzed again."
    d straight "I'm sorry, man. I can't tell you."
    d sad right "If anyone asks where I am, just say you don't know."
    "That won't be hard to do."
    a "Alright, then..."
    d straight "Sorry."
    hide don with easeoutleft
    pause 0.5
    "..."
    "I slowly walked to Donald's front door, as to not seem suspicious."
    "Right as I put my hand on the handle, I turned around to see Donald going towards the end of the street."
    "I certainly got confused when he walked towards one of the houses."
    "Specifically, the house across from mine."
    "The one belonging to Anna Ziphon."
    "I don't get it. Why would Donald be visiting a neighbor who called the cops on him?"
    if cleaningpartner == "Donald":
        "Especially if said neighbor threatened his life?!"
    "He certainly didn't seem willing to go, either..."
    "Hm..."
    "Well, if he really doesn't want to tell me, then I guess the least I can do is respect that."
    "Still, I deserve at least some sort of explanation in the future..."
    "Taking one final look at the Ziphon house, I turned back towards the Waters house and entered."
    jump presenttime

label presenttime:
    $ current_track = "None"
    stop music fadeout(3)
    window hide dissolve
    pause 1
    scene bg fade with wipeleft
    scene bg living_w with wipeleft
    pause 0.5
    window show dissolve
    pause .1
    "Finally, it was time to open presents."
    $ current_track = "\"Brotato Chips\""
    play music donald
    "Donald started with Brittney's gift, first."
    show don p1 level blank straight at middle with dissolve
    pause .1
    d_s "..."
    "It was wrapped in a shoe box, as to not give it away."
    d_s casual dot "...!"
    d smile "Whoa! A new baseball glove!"
    show don at twoleft
    show brit p2 straight sad grin at tworight
    with easeinright
    pause 0.1
    b "I figured since you're always saying you want a new one..."
    d sad right grin "No, I get it! Thank you!"
    $b_blink = True
    b closed blush "You're welcome~!"
    hide brit
    show don at middle
    with easeoutright
    pause .1
    $b_blink = True
    "Up next was Christeena's."
    d straight level blank "Hm..."
    "It looked exactly like a wrapped-up gift card, but showed nothing about what exactly it was for."
    show don casual wide
    "That said, when he DID see what it was..."
    d "A $50 Vapor card?!"
    d sad smile "Chris, that's awesome! Thanks!"
    show don at twoleft
    show chris p2 straight sad grin at tworight
    with easeinright
    pause .1
    c "N-No problem, Don! I'm glad you like it!"
    d raised left blank "I mean, I can't really get anything triple-A..."
    $d_blink = False
    d closed sad grin "...but there are actually a few indie titles I've been wanting, and this'll cover it nicely!"
    show chris left p1
    "You could see the weight of fear lifted off of her at the sight of Donald's excitement."
    "I turned towards Brittney, who looked just as surprised at Donald's happiness."
    hide chris
    show don at middle
    with easeoutright
    pause .1
    "Next up, he grabbed my gift."
    "Oh, boy...{w} I hope he enjoys it..."
    $d_blink = True
    d_s straight level blank "..."
    if persistent.choices["12"] == 1:
        d casual dot "A Bulls jersey?"
        d smile "Thanks, Al!"
        a "You really like it?"
        a "I wasn't too sure what to get..."
        d sad grin "Of course I like it, man!"
        "I gave a mental sigh of relief."
        "I don't know if he LOVED it, but at least he didn't hate it."
        $ D_Points += 1
    elif persistent.choices["12"] == 2:
        d casual wide "No way!"
        d "{i}Clunker's Bad Day{/i}?!"
        "That's always a good sign."
        d sad grin "Dude, I've been looking for a cartridge for years!"
        a "Seriously?"
        d "Yeah! Where did you find this?"
        a "The game store in the mall!"
        d casual dot "What?"
        d level left blank "I've looked there hundreds of times and have never found it...!"
        a "Lucky me, then, huh?"
        d raised straight grin "Apparently!"
        d sad smile "Anyway, thanks again, man!"
        a "No problem!"
        $ D_Points += 2
    elif persistent.choices["12"] == 3:
        "He stared at the opened box in a bit of confusion."
        a "I remembered you drawing when we were younger."
        "I explained in a bit of a nervous tone."
        show don casual dot
        "That seemed to get the gears turning."
        d smile "Oh, yeah! I can't believe you actually remembered that!"
        d level right grin "Man, that used to be a pretty fun way to pass time back then..."
        d "I might just actually get into that again now!"
        a "Oh, don't feel like you have to--"
        d straight raised smile "I don't feel like I have to."
        d "I actually want to."
        a "Well, alright, then! Glad I could help!"
        "I looked towards Brittney and Christeena, who were certainly a bit surprised to see Donald's reaction."
    else:
        "..."
        "Well, somehow you managed to have skipped a section or something."
        "Oh, well. The show must go on."
    $ current_track = "\"Chillaxin'\""
    play music chillaxin
    hide don with dissolve
    pause 0.1
    window hide dissolve
    nvl show dissolve
    narrate """
    He eventually got around to everyone else's presents.

    Socks, swim trunks, movies, sports gear, games, etc.

    He thanked everyone for the gifts, and after that, it was time for cake.

    After singing the birthday song, with Brittney singing much louder and obnoxiously, Donald blew out his candles and we began eating.
    
    {clear}

    The rest of the day went by pretty smoothly, all things considered.

    Guests slowly started to leave, with Donald being sure to thank each one for coming.

    Eventually, by around 5 o'clock, it was just the Waterses, Trumans, and Sprouses left in the house.

    Our families agreed to all head out to watch the fireworks show later that evening, but for now, we all just continued to hang out.
    """
    nvl clear
    nvl hide dissolve
    window show dissolve
    pause 0.1
    show don p1 straight casual grin at threeright
    show brit p1 straight casual grin at middle
    show chris p1 straight casual grin at threeleft
    with dissolve
    pause 0.1
    b p2 raised opened_smile "Not a bad birthday, right, Donnie?"
    d raised left smile "Far from it!"
    d straight sad grin "Thanks again for coming, guys. Really means a lot to me."
    c p2 smile "No problem, Donald!"
    b left level derp "Well, I only came because I didn't have any other plans until the fireworks."
    d level left "Oh, yeah. That reminds me: I'm gonna be out of town on October 5th."
    b straight mad opened_smile p1 "I was kidding, dum-dum!"
    $d_blink = False
    d closed sad smile "So was I!"
    show chris level p2 left grin
    "Christeena just rolled her eyes as she grinned and gave a disappointed shake of the head."
    a "So, now what?"
    $d_blink = True
    d straight casual blank "Well, I'm a bit hungry, but I'm not in the mood for more brats or burgers."
    d level right "And Kelly's is closed on the 4th..."
    b straight casual grin "We could see about ordering pizza or something."
    d straight casual smile "That'll work!"
    d "I'll ask my parents."
    hide don
    hide brit
    hide chris
    with dissolve
    pause 0.1
    "And so, all three of our families had pizza for dinner."
    "Two meat lovers', two plain cheeses, and two Hawaiians."
    "Hey, pineapple DOES belong on pizza, and I will literally fight anyone who says otherwise. {w}Just ask Christeena."
    "Anyway, after that, my family left to get dressed into warmer clothes, with the Trumans right behind."
    window hide dissolve
    scene bg white with dissolve
    pause 0.5
    scene bg cg_02
    with dissolve
    window show dissolve
    pause 0.1
    "We all eventually made it to the spot that was said to be 'good' for the show."
    "It was along a gravel road surrounded by corn fields."
    "I swear, Smalltown consists of 55\% fields, 40\% wooded area, and 5\% 'town'."
    "Anyway, there were other cars pulling up along the road, as well, seeming to validate the claim of this spot being good."
    "Brittney and Christeena even said they recognized a few of them from Trenburg."
    "I guess the fireworks are better here than there."
    "Soon, the fireworks started."
    show white
    pause 0.01
    show firework
    hide white
    pause 0.1
    play sound fireworks
    hide firework with dissolve
    pause 0.5
    show white
    pause 0.01
    show firework
    hide white
    pause 0.1
    hide firework with dissolve
    pause 0.5
    show white
    pause 0.01
    show firework
    hide white
    pause 0.1
    hide firework with dissolve
    if persistent.choices["25"] == 2:
        "Chris certainly was right when she said that fireworks aren't as much of a 'wow' factor as they once were."
    else:
        "Admittedly, as I've gotten older, I haven't found fireworks to have that 'wow' factor as much as they used to."
    "Still..."
    "Hearing the cheers of people around me, including Harry..."
    "I dunno. I guess it just kinda brought back some nostalgic feeling."
    "The feeling when everything seemed alright in the world, when I didn't have to focus on bigger things."
    "..."
    "Yeah, I'm aware of how stupid I sound."
    "But I'm too in the moment to think anything differently."
    window hide dissolve
    show white
    pause 0.01
    show firework
    hide white
    pause 0.1
    play sound fireworks
    hide firework with dissolve
    pause 0.5
    show white
    pause 0.01
    show firework
    hide white
    pause 0.1
    hide firework with dissolve
    pause 0.5
    show white
    pause 0.01
    show firework
    hide white
    pause 0.1
    hide firework with dissolve
    window show dissolve
    pause .1
    "I guess while I'm thinking of things that are seemingly stupid..."
    "This first month I've spent in Smalltown certainly has been quite a change for me."
    "Yet, I can't, at this point in time, say I'm upset that we moved."
    if persistent.choices["25"] == 3:
        "I wouldn't go as far as Donald and say that I don't miss Chicago, but..."
    "I finally have friends, plural, as well as the chance to reconnect with the only one I had growing up."
    "I honestly don't know what my future in Smalltown holds, and as far as I know, it might just get worse."
    "But right now, as I'm looking at giant explosions in the sky..."
    "...I just wanna sit back and enjoy how good everything is in the here and now."
    show white
    pause 0.01
    show firework
    hide white
    pause 0.1
    play sound fireworks
    hide firework with dissolve
    pause 0.5
    show white
    pause 0.01
    show firework
    hide white
    pause 0.1
    hide firework with dissolve
    pause 0.5
    show white
    pause 0.01
    show firework
    hide white
    pause 0.1
    hide firework with dissolve
    $ daydesc = 0
    $ replay = False
    $ renpy.end_replay()
    $ progress += 1
    jump progress
