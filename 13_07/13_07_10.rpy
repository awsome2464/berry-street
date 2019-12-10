label swimming:
    python:
        B_Name = "Brittney"
        C_Name = "Christeena"
        E_Name = "???"
        current_track = "None"
        b_hat = 0
        b_hair = 1
        c_hair = 1
    show text "{size=+20}Act 2\n{size=-5}\"Summertime Shenanigans\"{/size}" with dissolve
    pause 3
    hide text with dissolve
    show text "{size=+50}July, 2013{/size}":
        xalign 0.5 yalign 0.05
    show screen calendarOs
    show calendar july july_10:
        xalign 0.5 yalign 0.67
    show calendar_circle:
        xalign 0.5 yalign 0.51
    with dissolve
    if replay == False:
        $ persistent.todays_date = "July 10th, 2013"
        $ renpy.notify("Game saved!")
        $ renpy.save("1-1")
    pause 4
    hide text
    hide screen calendarOs
    hide calendar
    hide calendar_circle
    with dissolve
    pause 1
    scene bg living_s_m with dissolve
    window show dissolve
    hide screen notify
    $ current_track = "\"Home Life\""
    play music home_life
    $ renpy.block_rollback()
    " Anchor " "\"{i}I hope your ACs are up and running, because the heat wave isn't going away, folks!{/i}\""
    "I groaned in annoyance."
    "I suppose it's normal for it to be really hot outside in July, but nobody expected it to be THIS bad."
    "Even Brittney has admitted to not being outside as much. {w}Or, at least, without a large water bottle and restroom in the immediate area."
    "Thankfully, though, all of our ACs are, indeed, up and running, so there's that going for us."
    play loop phone_vibrate_call
    "Suddenly, my phone was ringing. It was Donald."
    stop loop
    a "Yeah?"
    d_o "{font=fonts/LemonMilk.otf}{i}Hey, you got anything planned for the day?{/i}{/font}"
    a "Only sitting on the couch and watching TV."
    d_o "{font=fonts/LemonMilk.otf}{i}Well, with as hot as it is, the girls and I were gonna go swimming at the pond. You willing to cancel your plans for that?{/i}{/font}"
    a "Hm... {w}This couch is pretty comfy, I must admit..."
    d_o "{font=fonts/LemonMilk.otf}{i}Oh, come on!{/i}{/font}"
    d_o "{font=fonts/LemonMilk.otf}{i}Brittney said she's been dying to try out her new bikini!{/i}{/font}"
    a "You seem just a LITTLE too excited at that..."
    d_o "{font=fonts/LemonMilk.otf}{i}Ahaha! Maybe just a little.{/i}{/font}"
    d_o "{font=fonts/LemonMilk.otf}{i}Anyway, you coming? We're planning on heading over there pretty quickly.{/i}{/font}"
    a "Alright, fine, if you insist. I'll let my mom know and get changed."
    d_o "{font=fonts/LemonMilk.otf}{i}Good deal! I'll tell the girls, and we can all meet up at my house.{/i}{/font}"
    a "Sounds like a plan! See ya in a few."
    d_o "{font=fonts/LemonMilk.otf}{i}See ya!{/i}{/font}"
    "I hung up and, very slowly, got off the couch."
    "I hadn't really paid attention to how long I had been sitting on that thing..."
    a "Hey, Mom!"
    "I called towards the kitchen."
    a "I'm gonna go swimming at the pond with the guys!"
    "I heard a shuffle of movement."
    g_o "Are you asking me or telling me?"
    "I lightly sighed and rolled my eyes."
    a "Is it okay if I go swim at the pond with the guys?"
    g_o "That's better!{w} And yes, that would be fine, as long as you're safe."
    a "Mom, I was on the swim team!"
    g_o "And that's the kind of overconfidence that causes accidents!"
    "I rolled my eyes again and started walking up the stairs."
    "On my way past my room, Harry poked his head out of his doorway."
    show harry a1 straight casual blank at close_h with dissolve
    pause .1
    h "You're going swimming?"
    "I suppose I wasn't exactly subtle about my plans."
    a "Yep. At the pond at the end of the street."
    h grin "Can I come?"
    "Ugh."
    a "Why?"
    h mad blank "Because I want to swim!"
    a "Well, I'm not sure how the guys would feel about having to essentially babysit you."
    h small scream "Hey! I don't need to be babysat! I can take care of myself!"
    a "They might not see it that way."
    h straight blank "..."
    h right level "...okay, then. Whatever."
    hide harry with dissolve
    play sound door_slam
    pause .1
    "He then slammed the door, but not so hard that Mom will yell."
    "..."
    play sound door_knock
    "I sighed and knocked on the door."
    a "I'm sorry, okay? You can come if you really want to."
    "..."
    play sound door_open
    "After a few seconds of silence, the door opened."
    show harry a1 straight level blank at close_h with dissolve
    pause .1
    h "Really?"
    a "Really. I'm sure they won't care."
    h "..."
    h casual closed_smile "Okay, then!"
    hide harry with easeoutright
    pause .1
    "He then ran towards the bathroom, where I remember seeing his swimming trunks hanging over the shower rod to dry."
    "..."
    "I then took out my phone and dialed."
    "I'm pretty sure they truly wouldn't mind if Harry tagged along, but just in case..."
    a "Hey, Don?"
    d_o "{font=fonts/LemonMilk.otf}{i}Uh, oh.{w=0.5} Don't tell me you can't make it...!{/i}{/font}"
    a "No, no, I can. I was just wondering if it was okay for Harry to swim with us."
    d_o "{font=fonts/LemonMilk.otf}{i}...{w}heh. Your mom force you to?{/i}{/font}"
    a "Nah. HE did."
    d_o "{font=fonts/LemonMilk.otf}{i}What? Since when do you cave into Harry's orders?{/i}{/font}"
    a "Hey, I'm not a monster! He could use a day of fun; the only friend he's got right now is Daniel, and the Rodriguezes are in town right now."
    d_o "{font=fonts/LemonMilk.otf}{i}Alright, alright. I don't really care, anyway; I'll let the girls know. They shouldn't be bothered by it, either.{/i}{/font}"
    a "Thought so, but you never know."
    d_o "{font=fonts/LemonMilk.otf}{i}Well, anyway, just meet at my house when you two are ready!{/i}{/font}"
    a "Will do. See ya!"
    d_o "{font=fonts/LemonMilk.otf}{i}See ya!{/i}{/font}"
    "I hung up and entered my room; unlike Harry, my trunks were still packed and in my dresser."
    "A quick switch of the bottoms was all it took before I opened the door back up."
    "After Harry and I once again received a small lecture from Mom on being safe, we were on our way towards the end of the street."
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    scene bg house_ut with dissolve
    pause .1
    "We were just about to pass the girls' house before we heard the door open."
    "I turned to see Brittney exiting the house, waving at us with a smile as she did."
    "Waving back, Harry and I paused and let her catch up to us."
    show brit e1 straight casual opened_smile shorts at twoleft with easeinleft
    pause .1
    $ choicevbox = 2
    b "Wassup, homeboys?"

    if persistent.choices["27"] == 1:
        jump thesky
    elif persistent.choices["27"] == 2:
        jump notmuchgirlfriend
    elif persistent.choices["27"] == 3:
        jump likethetopless
    else:
        menu:
            b "Wassup, homeboys?{fast}"

            "'The sky, duh!'":
                $ persistent.choices["27"] = 1
                jump thesky

            "'Not much, girlfriend!'":
                $ persistent.choices["27"] = 2
                jump notmuchgirlfriend

            "'Diggin\' the topless style you got there.'":
                $ persistent.choices["27"] = 3
                jump likethetopless

label thesky:
    a "The sky, duh!"
    $ b_wink = True
    b e2 raised tongue "Psh. What are you, a middle schooler?"
    show harry b1 raised left grin at tworight with easeinright
    pause .1
    h "Mentally, yes."
    $ b_wink = False
    show brit e2 straight level grin shorts at twoleft
    b "Ha! Called out by the little brother, eh?"
    a "Not exactly 'called out'; I don't hide it."
    b raised "Point taken."
    jump chrishasears

label notmuchgirlfriend:
    a "Not much, girlfriend!"
    $ b_wink = True
    b e2 raised "Ayyyy!"
    show harry b1 raised straight grin at tworight with easeinright
    pause .1
    h "You WISH she was your girlfriend!"
    a "Harry!"
    $ b_wink = False
    show brit e1 raised grin straight shorts at twoleft
    b "Ooo, you got awfully defensive there, Alex!"
    a "What, you wouldn't be when someone accuses you of liking your friend like that?"
    b level "Eh."
    a "..."
    jump chrishasears

label likethetopless:
    a "Hey! Diggin' the topless style you got there!"
    b raised grin e2 "Thanks!"
    $ b_partial = True
    b level huhu "If you're patient, next year I can show you the proper topless look~"
    a "I'll hold you to it!"
    $ b_partial = False
    show brit e2 level right huhu shorts
    b "Or maybe it'll happen today. Who knows."
    show harry b1 left raised closed_smile at tworight with easeinright
    pause .1
    h "Even better!"
    $ b_wink = True
    b e1 straight mad tongue "Perv."
    jump chrishasears

label chrishasears:
    $ choicevbox = 1
    hide brit
    hide harry
    with dissolve
    pause .1
    $ b_wink = False
    "The front door opened up again, this time the other sister headed our way."
    "Though, if I'm being honest, it took a second to recognize her."
    show brit e1 straight casual grin shorts at twoleft with dissolve
    pause 0.1
    show chris e1 straight casual grin at tworight with easeinright
    pause 1
    a "Holy crap!"
    show brit e2 blank
    $ c_blush = True
    c sad dot "W-What??"
    "I then pointed at the side of her head."
    a "I didn't know you had ears!"
    $ c_blush = False
    show chris e1 straight casual blank at tworight
    c "..."
    $c_blink = False
    show chris e2 closed_happy sad grin
    "She gave a small smile and chuckle of relief after a second."
    $c_blink = True
    show chris e2 straight sad grin at tworight
    c "Well, with as hot as it is, I wanted my hair out of my face, you know?"
    a "Sure, I get it."
    $ b_wink = True
    b tongue raised "Not me."
    c e1 level blank "That's because you're weird."
    $ b_wink = False
    show brit e1 level straight grin shorts at twoleft
    b "And proud!"
    show brit:
        ease 0.5 offscreenleft
    show chris at twoleft
    show harry b1 straight casual blank at tworight
    with easeinright
    hide brit
    pause .1
    h "What's up with your swimsuit, Christeena?"
    c casual "What do you mean?"
    h level "I've never seen a one-piece suit look like that. It's usually sleeveless and stuff."
    c e2 smile "Well, it's a special thermal suit; it keeps me from getting too cold."
    c level left grin "And trust me, for the pond, this thing is a necessity."
    show harry:
        ease 0.5 offscreenright
    show chris at tworight
    show brit e2 raised grin straight shorts at twoleft
    with easeinleft
    pause .1
    b "It's also because you hate feeling exposed."
    c straight mad hanging "B-Brittney!"
    b level e1 "What? You said it, not me!"
    c left blank "Still, you didn't have to say it like that..."
    $ b_partial = True
    b level e2 huhu "Well, maybe if you were actually comfortable with your body--!"
    $ c_blush = True
    c straight scream e1 "BRITTNEY!!"
    $ b_partial = False
    show brit e1 straight level grin shorts
    b "I'm just saying that you look better than you think you do!"
    c blank left "..."
    b raised opened_smile e2 "Back me up, Al!"
    a "...!!"
    a "H-Huh?"
    b "Do you think she should show off that sexy body of hers?"
    c e2 scream straight "Brittney, shut up!!"
    b e1 casual grin "I just want his honest opinion!"
    c left blank "..."
    "Poor Christeena..."
    "I get Brittney's trying to help, but she could be handling this a lot better."
    "Still, I get the feeling we're not going anywhere until I answer the question."
    $ c_blush = False
    show brit level
    show chris e1 straight level blank at tworight
    a "Well, uh..."
    a "I think..."
    $ choicevbox = 3
    if persistent.choices["28"] == 1:
        jump shelooksfineassheis
    elif persistent.choices["28"] == 2:
        jump sheshouldshowoffmore
    elif persistent.choices["28"] == 3:
        jump gotodonaldshouse
    else:
        menu:

            "'...she looks fine as she is.'":
                $ persistent.choices["28"] = 1
                jump shelooksfineassheis

            "'...she should show off a bit more.'":
                $ persistent.choices["28"] = 2
                jump sheshouldshowoffmore

            "'...we should just go to Donald\'s house.'":
                $ persistent.choices["28"] = 3
                jump gotodonaldshouse

label shelooksfineassheis:
    $ C_Points += 1
    a "...she looks fine as she is."
    show brit e2 casual blank
    c casual dot "Huh?"
    c blank e2 "You... do?"
    a "Yeah!"
    b level grin "Huh. I guess I'm the odd one out, then."
    show brit at threeleft
    show chris at middle
    show harry b1 level straight grin at threeright
    with easeinright
    pause .1
    h "Yep!"
    show brit casual blank
    a "Really? You agree with me, Harry?"
    jump shesnotfatharry

label sheshouldshowoffmore:
    $ B_Points += 1
    a "...she should show off a bit more."
    b e2 raised opened_smile "See?"
    c e1 sad "..."
    a "I mean, you don't gotta wear a bikini or something, but maybe something like a traditional one-piece suit might be worth looking into."
    c right "Eh...{w} I don't know..."
    show brit at threeleft
    show chris at middle
    show harry b1 level straight grin at threeright
    with easeinright
    pause 0.1
    h "I think the suit looks good as it is."
    show brit casual blank
    show chris e1 casual straight
    a "You think so?"
    jump shesnotfatharry

label gotodonaldshouse:
    a "...we should just go to Donald's house."
    b e2 raised opened_smile "Oh, you think you can get out of this?"
    c mad "Brittney, can you just leave him alone?"
    b grin "Fine, fine."
    $ b_partial = True
    b level huhu "I'll just assume that this is his way of saying I'm right, but he doesn't want to admit it."
    a "Assume what you will, then."
    show brit at threeleft
    show chris at middle
    show harry b1 straight level grin at threeright
    with easeinright
    pause 0.1
    h "I think the suit looks good as it is."
    $ b_partial = False
    show brit casual blank straight e2 shorts
    show chris e1 casual straight
    a "You think so?"
    jump shesnotfatharry

label shesnotfatharry:
    $ choicevbox = 1
    h casual closed_smile "Yeah!"
    h mad "I mean, I wouldn't want to show everyone my fat self, either!"
    $ c_blush = True
    show brit e1 mad hanging
    show chris mad hanging
    a "HARRY!!"
    play sound punch
    show harry:
        linear 0.1 xalign 0.85
        linear 0.1 xalign 0.9
    h small sad scream "OWW!!"
    "Almost on instinct, I slapped Harry on the back of the head."
    a "Apologize! {w=0.5}Now!"
    h blank "S-Sorry."
    c level blank e1 "..."
    c left "..."
    "Christeena just looked down, though I'm not sure if she was looking at the ground or herself."
    b e2 level blank "Anyway, let's not keep Donald waiting any longer."
    a "Agreed."
    hide harry
    hide chris
    hide brit
    with dissolve
    pause 0.5
    scene bg house_w with dissolve
    pause 0.1
    $ c_blush = False
    "We walked to Donald's house in awkward silence."
    "Thankfully, that silence went away when we entered the house."
    scene bg living_w with dissolve
    pause 0.5
    show don d1 straight raised smile at middle with dissolve
    pause 0.1
    d "There you guys are! I was starting to think you got lost!"
    show brit e1 straight casual opened_smile shorts at twoleft
    show don at tworight
    with easeinleft
    pause .1
    b "We did, actually, but a magic fairy brought us back on track!"
    d level grin "Well, thank God she did!"
    d casual "So, we all ready?"
    a "Seems like it!"
    $ current_track = "None"
    stop music fadeout(3)
    window hide dissolve
    pause 0.5
    scene bg fade with wipeleft
    scene bg pond
    show pond_foreground zorder 1
    with wipeleft
    pause 0.5
    window show dissolve
    pause 0.1
    $ current_track = "\"The Pond\""
    play music the_pond
    "Within less than a minute, we were at the pond."
    "After placing our towels along the grass, we all walked over to a small dock that was used as a diving board."
    "We stared at the water and then at each other, waiting for someone to head in."
    show chris e1 straight casual blank at four1 zorder 1
    show brit e2 straight casual blank at four2 zorder 2
    show don d1 straight casual blank at four3 zorder 2
    show harry b1 straight casual blank at four4 zorder 1
    with dissolve
    pause 0.1
    a "..."
    b level grin "Donald, you're the one who first wanted to swim; you do the honors!"
    d left raised grin "Ever hear of 'ladies first'?"
    b e1 mad opened_smile "Don't say that like I'm the only female here!"
    h mad left closed_smile "Yeah, Christeena! Let's see if that thermal suit of yours works!"
    c mad "..."
    a "I actually say YOU should go in first, Harry. Call it punishment for your comment from earlier!"
    b e2 level huhu "Ooo! Fair point!"
    d straight casual blank "What comment?"
    b e1 raised opened_smile "Harry called Christeena fat!"
    d dot "He what??"
    d mad grin "Oh, Harry's totally going in first."
    h mad small scream "No, I'm not!"
    show don:
        ease 0.2 xalign 0.85
    pause 0.2
    h sad "Ahh!!!"
    show don:
        linear 0.3 xalign 1.35
    show harry:
        linear 0.3 xalign 1.5
    pause 0.5
    hide harry
    "With little effort, Donald was able to pick Harry up and start walking to the pond."
    show brit e2 grin
    show chris casual
    h_o "Let me go!!!"
    d_o "Hwup!!"
    h_o "AAAHHHHH!!!!!"
    play sound splash
    "And with that, my brother went soaring as Donald tossed him in."
    $d_blink = False
    show don closed sad smile:
        ease 0.5 xalign 0.9
    show chris at threeleft
    show brit at middle
    with easeinleft
    pause 0.1
    d "Man, that was priceless!"
    b e1 mad closed_smile "So is this!"
    show brit:
        linear 0.2 xalign 0.85
    pause 0.15
    $d_blink = True
    show don small sad wide:
        linear 0.2 xalign 1.35
    d "GAH!"
    hide don
    play sound splash
    "Before anyone could react, Brittney had ran and pushed Donald in!"
    d_o "N-Not c-c-cool, Brittney!!"
    $b_blink = False
    b e2 closed sad closed_smile "Says you! Ahahaha!!"
    c raised grin e2 "..."
    show chris:
        linear 0.3 xalign 0.8
    pause 0.25
    $b_blink = True
    show brit small sad hanging:
        linear 0.2 xalign 1.35
    b "Wha--?!"
    hide brit
    play sound splash
    "And so, Brittney was the next one in."
    $c_blink = False
    c e1 sad closed_happy smile "Ahahahaha!!!!"
    b_o "Alright, fine! You won that time!"
    b_o "So which one of you losers is next?"
    $c_blink = True
    show chris raised straight grin at middle with easeinright
    pause 0.1
    c "..."
    a "..."
    "We both looked at each other with the same competitive grin."
    "Her back was facing the pond, and I was staring directly at everyone else wading in the water behind her."
    "One quick charge could knock her in, should she stand still."
    "Besides, the work it would take to drag me in would be a lot, I reckon."
    "Although I could use that to my advantage and get her in while she's focused on dragging."
    "..."
    "Unless I decide to not resist and let her get me in."
    "Hm."
    $ choicevbox = 5
    if persistent.choices["29"] == 1:
        jump chargeather
    elif persistent.choices["29"] == 2:
        jump standstillandresist
    elif persistent.choices["29"] == 3:
        jump standstillanddontresist
    else:
        "How should I approach this?"
        menu:
            "Charge at her.":
                $ persistent.choices["29"] = 1
                jump chargeather

            "Stand still and resist.":
                $ persistent.choices["29"] = 2
                jump standstillandresist

            "Stand still and don't resist.":
                $ persistent.choices["29"] = 3
                jump standstillanddontresist

label chargeather:
    $ current_track = "None"
    stop music fadeout(3)
    "You know what? Fuck it."
    $ current_track = "\"Friendly Competition\""
    play music friendly_competition
    show chris:
        ease 0.3 close_c
    pause 0.3
    "I charged towards Christeena with all my stamina."
    show chris mad e2
    "She still stared at me, not moving an inch."
    show chris:
        ease 0.2 zoom 1.1
        pause 0.5
        linear 0.2 xalign -1.0
    pause 0.9
    hide chris
    "Right as I was about to tackle her, she jumped out of the way!"
    jump splashchris

label standstillandresist:
    $ current_track = "None"
    stop music fadeout(3)
    a "Come at me, Truman! Let's see what ya got!"
    "It's gonna take some skill, but I might just pull this off."
    show chris mad
    "She looked at me with a glare that told me she was ready."
    $ current_track = "\"Friendly Competition\""
    play music friendly_competition
    show chris:
        ease 0.3 close_c
    pause 0.3
    "She then charged towards me with her arms extended, aiming for my forearms."
    "After grabbing onto me, she looked me in the eye with a playful smirk, as if to say {i}'Gotcha!!'{/i}"
    "She quickly tightened her grip and starting yanking me towards her."
    "I pulled back in response, making sure my feet were as planted to the ground as I could."
    "We just glared at each other, our top halves shifting back and forth while our bottom halves stayed put."
    b_o "C'mon, Chris! Get his ass in here!"
    show chris smile
    "With that, Christeena took a step back and yanked hard."
    "Admittedly, I was thrown off for a second, and I did, in fact, go forward."
    "However, we were both right by the edge of the dock, and it was then when I had an idea that might just work."
    "Using all the strength I had, I kept moving forward right towards Christeena."
    show chris:
        ease 0.2 zoom 1.1
    pause 0.2
    c casual dot "Eh?"
    "Before she could fully comprehend what had happened, we were right on top of each other, as if we were about to hug."
    "Her confusion loosened her grip, allowing me to break free with a quick movement and wrap my arms around her, all while the momentum kept me going."
    c sad scream small "AAAHHHH!!!"
    "Realizing what had just happened, Christeena screamed as the full effect of my tackle took place, sending us both into the water!"
    $ current_track = "None"
    stop music fadeout(3)
    hide chris with dissolve
    pause 0.1
    show pond_foreground:
        ease 0.5 ycenter 1.0
    pause 1.0
    hide pond_foreground
    $ c_blush = True
    play sound splash
    pause 1.5
    show chris e2 straight mad blank:
        zoom 1.0
        xalign 0.5 yalign -2.0
        ease 0.3 yalign 0.5
        ease 0.2 yalign 0.3
        ease 0.1 yalign 0.4
    pause 0.6
    show chris:
        linear 0.05 xalign 0.49
        block:
            linear 0.1 xalign 0.51
            linear 0.1 xalign 0.49
            repeat 2
        linear 0.05 xalign 0.5
        block:
            ease 1.0 yalign 0.35
            ease 1.0 yalign 0.4
            repeat
    c "N-Not f-f-fair!!"
    a "Glad to see the thermal suit is working!"
    c "Sh-Shut up!"
    $ current_track = "\"The Pond\""
    play music the_pond
    show chris:
        ease 0.5 yalign 0.25
        close_c_float_2
    show don straight raised smile d1:
        zoom 1.0
        offscreenleft
        yalign 0.2
        ease 0.5 close_left_d_2
        close_left_d_2_float
    show brit e1 straight casual grin:
        zoom 1.0
        offscreenright
        yalign 0.1
        ease 0.5 close_right_b_2
        close_right_b_2_float
    pause 0.6
    jump wereallinnow

label standstillanddontresist:
    $ current_track = "None"
    stop music fadeout(3)
    a "Come at me, Truman! Let's see what you got!"
    "I don't see the harm in getting her a bit in the competitive mood."
    show chris mad
    "She looked at me with a glare that told me she was ready."
    $ current_track = "\"Friendly Competition\""
    play music friendly_competition
    show chris:
        ease 0.3 close_c
    pause 0.3
    "She then charged towards me with her arms extended, aiming for my forearms."
    "After grabbing onto me, she looked me in the eye with a playful smirk, as if to say {i}'Gotcha!!'{/i}"
    "She quickly tightened her grip and starting yanking me towards her."
    "As to not make it seem like I'm not trying, I resisted a little bit, but she still did a good job of dragging me towards the dock."
    h_o "C'mon, Alex! You're stronger than that!"
    b_o "Let's go, Chris! Get him in there!"
    show chris smile
    "We were right by the dock. I was still 'struggling', while she was still pulling."
    show chris:
        linear 0.2 xalign -1.0
    "Right at the last second, she let go, moved to the side, grabbed onto my shoulder and back, and threw me in!"
    jump splashchris

label splashchris:
    $ current_track = "None"
    stop music fadeout(3)
    a "KYAAA!!!!"
    show pond_foreground:
        ease 0.5 ycenter 1.0
    pause 0.5
    hide pond_foreground
    play sound splash
    pause 2
    "After poking my head back up out of the ice-cold water, I stared at Christeena and gave a small golf-clap."
    show chris e1 straight mad grin at middle with dissolve
    pause 0.1
    $ current_track = "\"The Pond\""
    play music the_pond
    a "Now why don't you come in, yourself, coward?"
    show chris at twoleft
    show brit e1 straight level opened_smile at close_right_b_float
    with easeinright
    pause 0.1
    b "Yeah, Chris! You didn't come out here to just watch us, did you?"
    c e2 level "I'll come in on my own time!"
    $ b_partial = True
    b e2 huhu "Not on my watch!"
    "Brittney then quickly threw her arms out of the water and towards Christeena!"
    play sound splash
    show chris sad small scream:
        linear 0.05 xalign 0.24
        block:
            linear 0.1 xalign 0.26
            linear 0.1 xalign 0.24
            repeat 2
        linear 0.05 xalign 0.25
    c "AHHHH!!!"
    "The water landed on her in a large splash!"
    show brit at close_right_b_2_float
    show chris at middle
    show don d1 mad straight grin at close_left_d_2_float
    with easeinleft
    pause 0.1
    d "C'mon, Chris! The water's fine!"
    play sound splash
    show chris:
        linear 0.05 xalign 0.49
        block:
            linear 0.1 xalign 0.51
            linear 0.1 xalign 0.49
            repeat 2
        linear 0.05 xalign 0.5
    pause 0.5
    $ c_blush = True
    c e1 straight mad blank "C-Cut that out!!!"
    "It didn't take long for Harry and I to start splashing Christeena, as well."
    c tightly_shut scream "STOP!!!"
    $ b_partial = False
    show brit e1 straight mad opened_smile
    b "We will when you come in!!"
    play sound splash
    show chris:
        linear 0.05 xalign 0.49
        block:
            linear 0.1 xalign 0.51
            linear 0.1 xalign 0.49
            repeat 2
        linear 0.05 xalign 0.5
    pause 0.5
    c e2 straight blank "Grr...!!"
    c scream "Fine!"
    show don casual
    show brit casual grin
    "Everyone stopped splashing as Christeena looked at the water, took a step back, ran forward, and jumped in."
    $ c_blush = False
    show chris e1 closed_happy sad grin:
        xalign 0.5 yalign 0.5
        parallel:
            ease 0.5 zoom 1.0
        parallel:
            ease 0.2 yalign 1.0
            ease 0.3 yalign -2.0
    pause 0.5
    play sound splash
    pause 1.0
    show chris straight blank:
        ease 0.3 yalign 0.35
        ease 0.2 yalign 0.15
        ease 0.1 yalign 0.25
    pause 0.6
    show chris:
        linear 0.05 xalign 0.49
        block:
            linear 0.1 xalign 0.51
            linear 0.1 xalign 0.49
            repeat 2
        linear 0.05 xalign 0.5
        close_c_float_2
    c "B-B-B-Brrrr!!"
    a "Glad to see the suit is working!"
    c e2 mad "Sh-Shut up!"
    jump wereallinnow

label wereallinnow:
    $ choicevbox = 1
    d straight raised smile "Well, now that we're all in..."
    d casual "...let's get swimmin'!"
    b e2 raised opened_smile "Roger that!"
    show brit:
        ease 0.2 yalign 0.25
        ease 0.3 yalign -3.0
    pause 0.6
    play sound splash
    "Brittney then ducked into the water and started undulating away on her back."
    play sound splash
    $b_blink = False
    show brit e2 closed_sad sad frown:
        zoom 0.75
        xalign 0.9 ycenter 2.0
        ease 0.3 ycenter 0.5
        ease 0.3 ycenter 0.58
        ease 0.2 ycenter 0.5
        threeright_float
    pause 0.9
    b "Brrrrrrr!!"
    $b_blink = True
    b straight raised opened_smile "I tell ya, this place is a good place to go to wake yourself up!"
    b level right huhu "If not the water, itself, then the Antarctic temperature!"
    show brit:
        ease 0.5 twoleft
        twoleft_float
    show don:
        ease 0.5 xalign -0.5
    show chris:
        ease 0.5 xalign -0.5
    show harry b1 left raised grin at close_right_h_float with easeinright
    pause 0.1
    hide don
    hide chris
    $ c_blush = False
    h "I'm sure having most of your body exposed isn't helping!"
    $ b_partial = True
    b straight "What, not a fan of a mostly-naked girl?"
    h straight mad scream "That's not what I--!!"
    $ b_partial = False
    show brit e1 straight mad closed_smile
    b "Anything you wanna tell us, Harry? It's okay! We won't judge!"
    a "Oh, I'll certainly judge."
    h level grin "Oh, please. If I was gay, wouldn't I ENJOY seeing a masculine body like hers all exposed?"
    a "HARRY!"
    h mad small scream "What?!"
    b level blank "..."
    b e2 grin "Alright, fair enough."
    h raised left closed_smile "Thank you!"
    $ b_partial = True
    b huhu "So, tell me. If you don't like Christeena's body, and you don't like my body, then what DO you like?"
    h sad small blank "H-Huh?"
    b raised "I mean, those are two totally opposite girl bodies, and you don't like either?"
    b mad closed_smile "Maybe there IS something you aren't telling us!"
    h mad scream "I-I didn't say I hated the way either of you looked!"
    $ b_partial = False
    show brit e2 straight raised grin
    b "Oh? So which one do you prefer?"
    h straight blank "I...!!"
    show harry:
        ease 0.5 xalign 1.0
        block:
            ease 1.0 yalign 0.5
            ease 1.0 yalign 0.45
            repeat
    show chris e2 straight mad blank:
        zoom 1.0
        offscreenleft
        yalign 0.4
        ease 0.5 xalign 0.0
        block:
            ease 1.0 yalign 0.35
            ease 1.0 yalign 0.4
            repeat
    show brit:
        ease 0.5 middle
        middle_float
    pause 0.6
    c "Brittney, leave the poor kid alone!"
    play sound splash
    show brit:
        ease 0.4 ycenter 2.0
    pause 0.5
    play sound splash
    $ b_wink = True
    show brit e1 dot mad:
        ease 0.4 ycenter 0.5
        block:
            ease 1.0 ycenter 0.52
            ease 1.0 ycenter 0.5
            repeat
    pause 0.4
    show chris sad small scream:
        linear 0.05 xalign -0.01
        block:
            linear 0.1 xalign 0.01
            linear 0.1 xalign -0.01
            repeat 2
        linear 0.05 xalign 0.0
        block:
            ease 1.0 yalign 0.35
            ease 1.0 yalign 0.4
            repeat
    c "AHH!!"
    "Brittney had bent down and spat water on her sister."
    $ b_wink = False
    show brit e1 level straight grin
    b "Fine, if you insist."
    b e2 raised opened_smile "We'll just have to pick this up later."
    h mad right blank "Grr..."
    hide brit
    hide chris
    hide harry
    with dissolve
    pause 0.1

################################################################################
################################################################################

    $ players = {"Brittney": B_Points, "Christeena": C_Points, "Donald": D_Points}
    $ route = max(players, key=players.get)
    if route == "Brittney":
        if B_Points >= 7:
            $ pond_scene = "Brittney"
            jump b_pond
        else:
            $ pond_scene = "Eleanor"
            jump e_pond
    elif route == "Christeena":
        if C_Points >= 6:
            $ pond_scene = "Christeena"
            jump c_pond
        else:
            $ pond_scene = "Eleanor"
            jump e_pond
    elif route == "Donald":
        if D_Points >= 3:
            $ pond_scene = "Donald"
            jump d_pond
        else:
            $ pond_scene = "Eleanor"
            jump e_pond

################################################################################
################################################################################

label b_pond:
    "With that, Brittney ducked back under the water and swam back towards us."
    play sound splash
    show brit e1 straight casual grin:
        size (720, 1440)
        xalign 0.5 yalign -2.0
        ease 0.3 yalign 0.25
        ease 0.3 yalign 0.15
        ease 0.2 yalign 0.2
        block:
            ease 1.0 yalign 0.25
            ease 1.0 yalign 0.2
            repeat
    pause 0.9
    b e2 raised "Hey, Alex, you said you were on a swim team, right?"
    a "Yeah...?"
    b e1 "Competitive swimming is actually a sport I've never really tried."
    b mad closed_smile "So, how about you and me race so I can get a feel for it?"
    a "Well, I mean, I haven't swam in forever, and I don't have any goggles or a cap, but sure, I'll race ya!"
    b opened_smile "Still think you got any skill in ya?"
    $ b_partial = True
    b level huhu "If you even had it in the first place, that is."
    "I gotta admit, this girl knows how to push my buttons."
    a "Oh, I know I do."
    "I then looked around the pond to see if I can find a section that could be used as a decent length to race."
    a "Alright! We'll do a 25 from there to there!"
    "I challenged as I pointed to the dock and the opposite shoreline."
    $ b_partial = False
    b blank e2 "...{w}a what?"
    a "Whoever gets there first wins."
    b level grin "Gotcha."
    show brit at close_right_b_float
    show don d1 straight raised grin at close_left_d_float
    with easeinleft
    pause 0.1
    d "Alright, this is gonna be a good one!"
    d smile "Novice swimmer Brittney Usher vs. out-of-practice swimmer Alex Sprouse!"
    a "Thanks, man."
    hide brit
    hide don
    with dissolve
    pause .1
    show pond_foreground with dissolve
    pause 0.1
    "Brittney and I got out of the pond and back onto the dock."
    "It was just big enough for the two of us to stand side-by-side, like it was one giant starting block."
    show harry b1 straight mad closed_smile at twoleft_float
    show chris e1 straight casual blank at tworight_float
    with dissolve
    pause 0.1
    h "Who you bettin' on, Christeena?"
    c e2 level "I mean, Alex has more experience, so I guess it would make more sense for him to win..."
    $ b_partial = True
    show chris at threeright_float
    show harry at middle_float
    show brit e2 level blank straight at close_left_b zorder 2
    with easeinleft
    pause 0.1
    b "Glad to see you have so much faith in your sister, Chris!"
    c e1 mad hanging "I'm just being honest!"
    c level grin "Then again, you've been known to be sneaky when it comes to a competition."
    b casual grin "Hehehe."
    a "Should I be worried?"
    b closed_smile "Not at all, Alexander~"
    "Yes. Yes, I should be worried."
    hide harry
    hide chris
    with dissolve
    pause 0.1
    show don d1 straight raised smile at tworight_float zorder 1 with dissolve
    pause 0.1
    d "You two ready?"
    $ b_partial = False
    b e1 grin "Yep!"
    a "I suppose..."
    d casual "Alright!"
    d "Swimmers, on the block!"
    show brit:
        ease 0.5 xalign 0.5
    hide don with dissolve
    pause 0.1
    "Brittney and I lined up next to each other at the edge of the dock."
    b e2 blank "So, do we start this like a track race or something?"
    a "Basically. We just bend down as if we were gonna do a sprint, and when the race starts, we just dive right in and go."
    a "You're a lifeguard, so I'm sure you get the idea of how to dive properly."
    b level grin "Well, if you say that, then I guess it's not too much different, then."
    a "Alright, Donald! Say 'take your mark', and when we're bent down, tell us to go!"
    d_o "Roger!"
    d_o "Swimmers, take your mark!"
    $ current_track = "None"
    stop music fadeout(3)
    hide brit with dissolve
    pause 0.1
    "Brittney and I bent down and grabbed the ledge."
    "I placed one leg behind me, preparing to lunge."
    "I was serious when I said I haven't swam competitively in forever; hopefully muscle memory can get me through this."
    "I looked to the side and saw Brittney looking at me with a sneaky smirk."
    "..."
    "What's she planning...?"
    window hide dissolve
    pause 2.0
    window show
    d_o "GO!"
    "I quickly looked forward, about to lunge."
    "Right before I did, though, I saw movement to my left.{w} Only it wasn't going towards the water; it was going towards ME."
    a "Wha--{w=0.5}{nw}"
    "I felt a swift tug on my swim trunks."
    "I then quickly felt the breeze against my lower body."
    a "GAH!"
    play sound splash
    "Right as I stood up to pull my trunks up, I saw a tall, slender body dive right into the water!"
    "..."
    "Fuck it."
    "Drawers still pulled down, I dove right in after her."
    show pond_foreground:
        ease 0.5 ycenter 1.0
    $ current_track = "\"Friendly Competition\""
    play music friendly_competition
    play sound splash
    window hide dissolve
    nvl show dissolve
    narrate """
    I closed my eyes and undulated my legs, making sure to stay under the water and cover as much distance as I can.

    While I did, I could feel my trunks get closer and closer to my ankles.

    Having them down there would certainly hinder my ability to kick well...

    Sucking it up, I quickly kicked off my trunks and rose up to the surface.
    """
    hide pond_foreground
    nvl clear
    narrate """

    Once up, I kicked as hard as I could and turned my head to the side, seeing if I could find any sign of Brittney.

    Unfortunately, I couldn't.

    I turned my head back into the water and kept moving my arms and legs, ignoring the flow of water against my junk.

    1,{w=0.25} 2,{w=0.25} 3,{w=0.25} breathe!

    I turned my head the other direction, caught a quick breath, and stuck my face right into the water, continuing to move as fast as I can!

    1,{w=0.25} 2,{w=0.25} 3,{w=0.25} breathe!

    I continued this pattern for what felt like forever.

    Surely I had to have been close to the end by now...

    I mean, I know the length I had selected wasn't the standard 25 meters (honestly, it might've been more of a 50), but I feel like I've been swimming too long.

    Unless I really am that out of practice...
    """
    nvl clear
    narrate """
    Right as I thought that, though, I could feel my legs touch something as I kicked.

    It was the ground!

    I did one of the 'no-noes' of swimming and looked directly forward.

    I was essentially right at the shore!

    There was also no Brittney to be found...

    I turned around and saw splashing far behind me.

    She was certainly getting closer, but it was too late; I had already won!
    """
    $ current_track = "None"
    stop music fadeout(3)
    nvl hide dissolve
    window show dissolve
    pause 0.1
    "I floated my way to the shore and relaxed as Brittney took her time catching up."
    "When she had finally arrived, I had my bottom half underwater, but my top half leaning back in a mock seductive pose."
    $ current_track = "\"The Pond\""
    play music the_pond
    show brit e2 straight level hanging at close_b_float with dissolve
    pause 0.1
    a "Like what ya see~?"
    $ b_partial = True
    b huhu "Eh. I've seen better."
    a "Well, for the record, I'm sure there's a rule about pantsing your opponent."
    $ b_partial = False
    $ b_wink = True
    b raised tongue "Oops."
    $ b_wink = False
    b casual grin "Still, late start AND no shorts, yet you still won?"
    b e1 sad opened_smile "Kudos to you, man."
    "She held out her fist for a bump, a gesture I politely accepted."
    "I turned towards everyone else, who was still at the dock area where we had started."
    "Well, MOST of them were there; Donald was a bit further ahead, holding up my trunks in one hand and giving a thumbs-up with the other."
    a "Well, we should probably get back there."
    b blank "Aw, so soon?"
    a "What, you wanna be over here alone with a naked guy?"
    a "..."
    a "Actually, now that I say that out loud..."
    $ b_partial = True
    b e2 level huhu "Huhuhu. You wish."
    $ b_partial = False
    b grin left e1 "But I guess you're right; don't wanna keep them waiting for too long."
    b straight raised closed_smile "I'll try not to look at your little dick, though."
    a "Hey, that's what happens when men go in cold water!"
    $b_blink = False
    b closed sad "Ahahaha! You're so pathetic!"
    $b_blink = True
    b small casual hanging "Ah!"
    b sad straight blank "S-Sorry. That was..."
    b e2 right "Sorry."
    "..."
    "Talk about a one-eighty."
    a "You're good, Brittney."
    b straight grin "O-Okay."
    play sound splash
    "We could then hear splashing from nearby."
    b casual left blank e1 "Eh?"
    "We turned and could see Donald walking towards us in the water."
    show brit at close_right_b_float
    show don d1 straight raised smile at twoleft_float
    with easeinleft
    pause 0.1
    d "Figured you could use these!"
    "He told me as he held up my trunks."
    a "As a matter of fact, I could!"
    "He then tossed them over to me. Keeping my bottom half under the water, I slipped them on, making sure the strings were tied as tight as comfortably possible."
    d casual grin "So, shall we swim back?"
    a "I suppose we shall."
    "I stood up and stretched my arms in the air."
    "Thankfully, I wasn't breathing as heavy as I was after the race."
    "In hindsight, I suppose a cooldown lap after the race might've helped."
    "Then again, when you're unwillingly naked in the water, you have other things on your mind."
    a "Brit, you ready?"
    b e2 straight sad grin "Well, I'm not gonna lie..."
    b right "...I'm still a bit pooped."
    b "I feel like I might get exhausted and drown on the way back..."
    d blank "Really? You don't seem that tired."
    b straight level "I'm an athlete. I do my best to hide how exhausted I really am."
    b e1 sad "I think I'll walk around back to you guys, if that's okay."
    d sad grin "Sure, as long as you're okay."
    b "Yeah, I'll be fine."
    show brit:
        ease 0.5 yalign 0.25
    "Brittney then fully stood out of the water."
    show brit:
        linear 0.2 yalign 0.0
    $ current_track = "None"
    stop music fadeout(5)
    b small hanging "Ah!"
    "...before falling down onto her knees."
    d wide "Brit!"
    "Thankfully, I was able to grab onto her before she toppled over completely."
    show don:
        ease 0.5 close_left_d
    pause 0.6
    "Donald grabbed onto her other side and we carefully picked her back up."
    show brit:
        ease 1.0 yalign 0.2
    pause 1.1
    d blank "Brittney, are you sure you're okay?"
    b e2 straight grin "Y-Yeah! I promise!"
    "She then shook us off her, allowing her to stand on her legs by herself, albeit a bit unstable."
    "Still, at least she was standing up."
    d level "..."
    b e1 "Donald. I'm fine."
    b "It's just exhaustion from the race! That's all!"
    d "..."
    a "I think we should walk back with you."
    b blank "You guys don't have to--"
    d mad "Yes, we do."
    b mad "..."
    b e2 level right "...fine."
    b "If it'll please you, I'll walk back with you."
    b straight raised hanging "But don't expect me to need your help."
    d level "Brittney, now's not the time to boost your ego."
    b mad "I'm not--!"
    d mad "We're only trying to help you, Brittney!"
    b e1 "I get that, and I appreciate it, but I don't...!"
    b level blank "..."
    $b_blink = False
    b closed_sad "*sigh*"
    b "On second thought, I can make it back with only one of you."
    b "Alex, will you walk back with me?"
    d level "..."
    a "Uh, yeah. No problem."
    $b_blink = True
    b straight "Thanks."
    d left "..."
    d straight grin "I'll meet you guys back there, then."
    a "Alright."
    hide don with easeoutleft
    pause 0.5
    show brit at close_b with easeinright
    pause 0.1
    b "..."
    "She just stared at Donald as he walked towards the other side before finally breaking into a swim."
    a "..."
    a "Brittney, be honest with me."
    a "Are you--{nw}"
    b mad e2 hanging "I'm fine, Alex!!"
    a "..."
    a "Alright. If you don't need my help, then go walk onto the shore."
    b level grin e1 "Fine. I will."
    "Brittney then started walking towards the edge."
    show brit sad
    "I could see that she looked uncomfortable with something."
    "Her having a limp isn't helping me buy the 'I\'m fine' claim."
    "Finally, she reached the edge."
    $b_blink = False
    show brit closed_sad frown:
        ease 0.3 yalign 0.0
    pause 0.3
    "And fell down again."
    "With a slight annoyed groan, I quickly went over to her and helped her sit down on the shore."
    show brit:
        ease 1.0 yalign 0.2
    pause 1.1
    a "Okay, Brittney. Stop bullshitting."
    a "What's wrong?"
    $b_blink = True
    b straight blank "..."
    $ current_track = "\"Reflection\""
    play music reflection
    b right e2 "Okay, fine."
    b "When I got closer to the shore, I was kicking, and..."
    b "...I don't know what exactly I hit, but..."
    $ b_wince = True
    b straight "...I hit my shin hard."
    b left "Like, REALLY hard."
    $ b_wince = False
    b straight "And it's been hurting ever since."
    b "I thought it would stop by now, but it's still bad."
    $ b_wince = True
    b right hanging "It's not broken or anything, but it still hurts."
    a "..."
    a "Okay, next question:"
    a "Why didn't you just say that?"
    $ b_wince = False
    $b_blink = False
    b closed_sad blank "Because..."
    b "*sigh*"
    $b_blink = True
    b straight "I didn't want you guys to worry, okay?"
    b right "Especially Donald."
    a "So Donald was right? This was more of a way for you to save face or something?"
    b e1 straight mad hanging "I..."
    b level blank "..."
    b e2 left "...It's complicated, Alex."
    a "How?"
    b straight mad hanging "Alex, just--!!"
    $b_blink = False
    b closed_sad level blank e1 "..."
    "She lightly growled at herself as she placed her face in her hands."
    b "..."
    a "..."
    a "Okay."
    a "If you don't wanna tell me, then you don't have to."
    a "Just..."
    a "Let me help you get back. Please."
    $b_blink = True
    b straight "..."
    b e2 grin "...okay. Sure."
    hide brit with dissolve
    pause 0.1
    nvl clear
    window hide dissolve
    nvl show dissolve
    pause 0.1
    narrate """
    With that, I helped her stand up.

    She leaned against me while she hovered the foot of her hurt leg over the ground.

    It took time to get a rhythm going, but we managed to essentially play a three-legged race around the outside of the pond, only one outer leg was nonexistent.

    Occasionally, we had to stop for a few seconds so she could give her leg a rest.

    We were silent the entire time, if you don't count things like 'You good?' and 'Hold on.'.
    """
    nvl clear
    narrate """
    Brittney sure can be stubborn, but this whole thing seems too off.

    Not wanting to tell her best friend about something minor to keep him from worrying makes sense.

    But a potential broken or bruised shin? It's not normal to keep that hidden.

    Then again, she's not the most normal of people.
    """
    if persistent.choices["18"] == 3 and persistent.choices["20"] == 3:
        narrate "Even the fact that she claims to not trust him with everything seems off."
        narrate "I don't know what kind of 'things' she doesn't want Donald to know, but this seems like one of them."
    narrate """
    Still, who am I to interfere with whatever it is these two have going on?

    Maybe this is just something they'll just get over and forget about quickly.

    You know, unless a hosptial visit is in order.
    """
    $ current_track = "None"
    stop music fadeout(3)
    nvl hide dissolve
    window show dissolve
    show pond_foreground with dissolve
    pause 0.1
    "Finally, we made it back to everyone."
    "Christeena was the first to rush over to us."
    $ current_track = "\"The Pond\""
    $ c_blush = True
    play music the_pond
    show chris e1 sad straight dot at middle with easeinleft
    pause 0.1
    c "Brittney, are you alright?!"
    show brit e1 straight sad grin at tworight
    show chris at twoleft
    with easeinright
    pause 0.1
    b "Yeah, I'm fine, I promise."
    hide chris
    show don d1 level straight blank at twoleft
    with dissolve
    pause 0.1
    $ c_blush = False
    d "..."
    b blank "..."
    b e2 "Hey, Donald?"
    d casual "Yeah?"
    b "I..."
    b right "I'm sorry for how I acted back there."
    b straight grin "I truly am thankful that you tried to help."
    d "..."
    d grin "..."
    d "You sure you're okay, then?"
    b "Yeah!"
    d level "Really? Because that limping says otherwise."
    b blank "W-Well, uh..."
    d "C'mon Brit."
    b e1 "...okay."
    b level right "I hit my shin, and it hurt really bad."
    b straight grin sad "But it doesn't hurt that much anymore, so I think it'll be okay."
    d raised "Promise?"
    "She responded by pointing her pinkie towards him."
    $d_blink = False
    show don closed sad
    "Donald gave a small chuckle in response as he wrapped his own pinkie around hers."
    $d_blink = True
    d straight casual "Alright, then. If you want to get back in, feel free!"
    b e2 raised opened_smile "Feel free, I do!"
    $ b_partial = True
    b level huhu "Oh, and by the way, Christeena, you're welcome."
    hide don
    show chris e1 straight raised blank at twoleft
    with dissolve
    pause 0.1
    c "Huh?"
    b closed_smile "Because of me, you finally got to see a naked guy in person!"
    $ c_blush = True
    c mad scream "...!!!"
    $ b_partial = False
    $b_blink = False
    b e1 closed sad "So, once again, you're welcome!"
    c left blank "..."
    hide chris
    hide brit
    with dissolve
    pause 0.1
    $b_blink = True
    play sound splash
    "And so, Brittney jumped back into the water, as if nothing had happened."
    "Christeena just closed her eyes and shook her head."
    "Donald looked like he was about to go in, himself, but he turned to me, first."
    show don d1 level straight blank at close_left_d with dissolve
    pause 0.1
    d "Hey, Alex?"
    a "Yeah?"
    d raised "Is she really gonna be okay?"
    a "Well, I'm no doctor, but she seems fine now, so I'd say so."
    d level grin "Alright. Cool. Thanks."
    "He said as he gave me a quick pat on the shoulder."
    hide don with easeoutright
    pause 0.1
    play sound splash
    "Donald then jumped back into the pond."
    "..."
    "That sorted itself out just a little too easily..."
    "..."
    "Well, I suppose we're all here to have a good time, so who am I to focus on the negatives?"
    "Following suit, I jumped right back into the pond."
    jump pond_end

################################################################################

label c_pond:
    "Brittney then floated around on her back, acting completely oblivious to our presence."
    show chris e2 left mad blank at close_c_float with dissolve
    pause 0.1
    c "That girl..."
    a "If I had a nickel for every time you said that..."
    c e2 straight raised "Well, there's a reason I constantly say it."
    a "Yeah, I know."
    show chris at close_left_c_float
    show harry b1 straight casual grin at close_right_h_float
    with easeinright
    pause 0.1
    h "I like her. She's my kind of crazy."
    a "Harry, she literally just accused you of being gay. {w=0.5}TWICE!"
    h level "Yeah, but she's just messing with me."
    h "..."
    h small blank "...right?"
    "I gave my brother a pat on the back."
    a "I'll leave that for you to decide."
    h sad "..."
    h "Christeena, she doesn't really think I'm gay, does she??"
    c level e1 "..."
    h "..."
    c left "..."
    h casual straight "..."
    h level "...Are you still mad about earlier?"
    c straight "..."
    h sad "Christeena, I really am sorry!"
    $ current_track = "None"
    stop music fadeout(3)
    c "..."
    h "..."
    a "..."
    a "Harry, why don't you go hang out with Brittney and Donald for a bit?"
    h level "..."
    h right "...okay."
    pause 0.5
    hide harry with easeoutright
    pause 0.5
    show chris sad at close_c_float with easeinleft
    pause 0.1
    "And so, as Harry wandered towards Brittney and Donald, who were treading in the water nearby, talking about who-knows, Christeena looked at me awkwardly."
    $ c_blush = True
    c "..."
    a "..."
    $ current_track = "\"Reflection\""
    play music reflection
    a "Look, Chris, you don't gotta say anything if you don't want to..."
    a "...but just know that Harry really is sorry."
    a "Trust me. I can tell."
    c level "..."
    a "I know he still shouldn't have said what he did, but--"
    c e2 "But he still said it."
    c right "And he only would've said it if that's what he really thought."
    a "Not necessarily. In all honestly, he probably was just trying to be funny."
    a "A very poor attempt at comedy, sure, but..."
    c straight "..."
    a "..."
    a "So, forgive me if I'm digging a little too far, but..."
    a "...Brittney's comment about you not liking your body..."
    c sad left e1 "..."
    c "...I mean..."
    c straight "I don't exactly HATE the way I look, but..."
    $ c_blush = False
    c level right e2 "...I guess maybe I just wish I could look better."
    a "Why? You look great!"
    c straight "How?"
    c left e1 "I mean... what kind of guy would go for a fat girl?"
    a "Christeena, you're not fat!"
    $ c_blush = True
    c mad straight hanging "Alex, look at me!"
    "She stood up out of the water a bit and gestured at herself."
    window hide
    show chris e2:
        ease 0.5 yalign 0.6
    $ renpy.pause(delay=3)
    window show
    "..."
    "Honestly, in this swimsuit of hers, it's giving a better idea of how she actually looks."
    "I suppose she has a bigger belly than I had thought, but still..."
    a "Christeena, I promise you I've seen bodies worse than that."
    c blank "And I'm sure you've seen bodies better."
    c level "I mean, look at her."
    "She pointed towards Brittney."
    "She, Donald, and Harry were all chatting in a circle. I could hear some laughs coming from the area."
    $ c_blush = False
    c e1 sad "I give her crap about being a bit too revealing in her outfit choices at times, but..."
    c left "...at least she has a body worth showing off."
    a "..."
    if persistent.choices["28"] == 1:
        a "Chris, I was serious when I said that you look fine the way you do now."
        a "In a way, I'm glad that you respect yourself enough to not walk out of the house essentially naked."
    elif persistent.choices["28"] == 2:
        a "Chris, I was serious when I said you already have a body worth showing off."
        a "Again, you don't gotta go overboard, but you might actually get some positive attention."
    elif persistent.choices["28"] == 3:
        "She really is upset about this..."
        "Maybe I should've answered Brittney's question when I had the chance..."
    c "..."
    a "..."
    show chris:
        ease 1.0 yalign 0.35
        ease 1.0 yalign 0.4
        repeat
    "She slowly sunk herself back into the pond with sadness."
    a "What do you say we swim for a bit? Have some fun?"
    c "Eh..."
    c straight "Honestly, I'm not really too much in a swimming mood."
    a "Well, do you wanna take a walk or something?"
    c casual "..."
    c e2 grin "Okay. That might be nice."
    c mad "Just don't try to murder me while we're alone."
    a "Fine, only because you asked nicely."
    hide chris with dissolve
    pause 1.0
    scene bg woods with dissolve
    pause 0.1
    $ current_track = "\"The Pond\""
    play music the_pond
    play loop forest_daytime
    "After grabbing our towels and putting on our sandals, we took a walk through a path in the wooded area around the pond."
    "We could hear the sounds of birds and other animals nearby. Honestly, it was kind of relaxing."
    show chris straight casual blank e1 at close_c with dissolve
    pause 0.1
    a "Feeling better?"
    c left level grin "A little."
    a "Well, it's a start."
    c straight blank "Hey, Alex?"
    a "Yeah?"
    c raised e2 "Why are you being so nice to me?"
    a "What kind of question is that? Would you prefer I be a dick?"
    c mad "Well, no, but..."
    c left level e1 "I dunno. I guess it's because ever since we've met, you've wanted to spend so much time with me."
    a "Is that a problem?"
    c straight raised "No."
    c sad grin "In fact, I..."
    $ c_blush = True
    c right e2 "I actually appreciate it a lot."
    c "It's nice to have someone else I consider a good friend."
    a "Aw, stop. You're gonna make me tear up."
    $ c_blush = False
    c straight casual blank "But I guess what I don't fully understand is..."
    c e1 sad "...why me?"
    c left "Donald is your close friend from your childhood, Brittney is a funny cute girl..."
    c "...yet you prefer spending time with me?"
    a "Christeena..."
    $ current_track = "None"
    stop music fadeout(3)
    "I cut her off and stopped right in front of her, placing my hands on her shoulders."
    $ c_blush = True
    c straight casual blank "..."
    a "..."
    "She was starting to blink quickly, and I think her breathing got a little shallower."
    a "Christeena..."
    c "..."
    "I'm not gonna lie, I kinda did all this on impulse."
    "Still, she seems calm enough."
    show chris:
        ease 0.5 size(792, 1584)
    pause 0.6
    "I moved a bit closer to her, all while never breaking eye contact."
    c "..."
    a "..."
    $ current_track = "\"Reflection\""
    play music reflection
    a "Christeena, you're not as bad as you think you are."
    c sad "..."
    a "I like spending time with you because you're a great person."
    a "You're honest. You care about your friends."
    a "And dare I say you look very cute."
    c grin "..."
    if persistent.choices["4"] == 2:
        a "When I said I thought you were pretty that day I first met you..."
        a "...I wasn't lying."
    else:
        a "It's true, Christeena."
        a "I really do think you're very cute."
    c left "A-Alex...!"
    "She sounds a bit choked up."
    a "And who cares if you have the body that you do?"
    a "I certainly don't. In fact, I've only been noticing the other stuff."
    a "Honesty, kindness, and cuteness."
    a "Add all those things together, and you have Christeena Truman, a great person who I'm glad to have met."
    c "..."
    c straight "..."
    hide chris with dissolve
    pause 0.1
    "The next thing I knew, she was hugging me tightly."
    "Returning the hug, I closed my eyes and felt myself smiling."
    "..."
    "It's a bit weird having that wet swimsuit of hers against my bare chest, but eh."
    "We must've been hugging for about 30 seconds or so before she finally broke it and looked at me."
    show chris e1 straight sad grin at close_c with dissolve
    pause 0.1
    c "Thank you, Alex."
    a "Just being honest."
    c e2 right "Not just for what you just said."
    c straight "For just being a great person, yourself."
    c e1 raised left "Not gonna lie, when I learned you were an old childhood friend of Donald's, I wasn't really sure what to expect."
    c straight sad "But I'm glad it was you."
    "Okay, I'm definitely smiling like a dumbass now."
    a "Thanks, Christeena."
    $ c_blush = False
    c raised smile "Just being honest."
    hide chris with dissolve
    pause 0.1
    $ current_track = "None"
    stop music fadeout(3)
    stop loop fadeout(3)
    play sound twig_snap
    pause 0.5
    "Suddenly, we heard what sounded like movement in the trees nearby."
    show chris e1 straight casual dot at close_c zorder 2 with dissolve
    pause 0.1
    c "..."
    a "..."
    c level grin "Probably just a deer or something."
    a "Probably."
    a "Anyway, what were we just{nw}"
    play sound scare_and_scream
    show brit e1 small mad frown zorder 1:
        size (720, 1440)
        xalign 1.5 yalign 0.2
        linear 0.1 xalign 0.75
    pause 0.1
    $ c_blush = True
    show brit:
        linear 0.1 xalign 0.77
        linear 0.1 xalign 0.75
        repeat 10
    show chris small sad scream:
        linear 0.1 xalign 0.52
        linear 0.1 xalign 0.5
        repeat 10
    pause 3.5
    "After comprehending what the hell just happened, Christeena's look of fear was replaced with one of rage."
    c straight mad "BRITTNEY!!!!"
    $ current_track = "\"Oddball\""
    play music oddball
    play loop forest_daytime
    $b_blink = False
    b e2 closed sad opened_smile "AHAHAHAHAHA!!!!"
    show chris:
        ease 0.5 xalign 0.1 yalign 0.25
    show brit at close_right_b with easeinleft
    pause 0.1
    "Christeena broke off from her sister's shoulder grab and started hitting her hard."
    show chris:
        ease 0.2 xalign 0.65
        ease 0.2 xalign 0.1
    play sound punch
    c "That's!{w=0.5}{nw}"
    show chris:
        ease 0.2 xalign 0.65
        ease 0.2 xalign 0.1
    play sound punch
    c "That's!{fast} Not!{w=0.5}{nw}"
    show chris:
        ease 0.2 xalign 0.65
        ease 0.2 xalign 0.1
    play sound punch
    c "That's!{fast} Not!{fast} Funny!"
    "Despite it not being funny, Brittney was still laughing."
    "She was hardly putting up a fight against the punches being thrown at her."
    "Finally, though, she took a deep breath, wiped her eyes, and looked at us."
    $b_blink = True
    b e1 straight "God, that was fuckin' priceless!!"
    c left blank "!!!"
    a "Brittney, what are you even doing here?"
    b straight casual blank "Well, we noticed you two were gone, so I went out looking for you."
    b e2 raised grin "I soon heard your voices, came over to investigate..."
    $ b_partial = True
    b level left huhu "...and decided to have some fun."
    b straight raised "But clearly not as much fun as you two were having~"
    c straight hanging "...!!"
    $ b_partial = False
    b e1 mad closed_smile "You really enjoyed having a nice, long hug like that, didn't you, Alex?"
    a "Wh-What makes you say that?"
    $ b_partial = True
    b level huhu "What, you can't tell that you have a massive boner right now?"
    show chris casual blank
    "With that, I quickly looked down."
    $ b_partial = False
    $b_blink = False
    b e2 closed sad opened_smile "Oh, my God! You actually thought you did!!"
    a "..."
    $b_blink = True
    b level straight grin "Well, you should still thank me."
    a "For...?"
    b raised "Getting Christeena to look at your crotch."
    c mad hanging "I-I wasn't--!!"
    $ b_partial = True
    b level left huhu "You totally were, Christeena. Don't deny it."
    c scream "Brittney, just go away!!"
    $ b_partial = False
    b e1 straight level grin "Okay, then."
    $ b_partial = True
    b "I'll give you two your privacy~"
    c "GO AWAY!!!!"
    c "God, have you learned nothing from that day at the mall?!?!"
    $ current_track = "None"
    stop music fadeout(3)
    $ b_partial = False
    b blank "..."
    c blank "..."
    b e2 right "...okay, then. Sorry."
    pause 0.5
    hide brit with easeoutright
    pause 0.5
    show chris at close_c with easeinleft
    pause 0.1
    c left "..."
    a "..."
    $c_blink = False
    c closed_sad sad "..."
    c "Why would she do that?"
    a "It doesn't seem unlike her to get me to think I--"
    c "Not that."
    c "Interrupting us, in general."
    c "She could clearly tell we were having a serious moment..."
    a "..."
    "Well, I'm glad I'm not the only one who noticed how special that conversation we had was."
    "But she's right; thanks to Brittney, that moment is now gone."
    "...unless..."
    show chris:
        ease 0.5 size (792, 1584)
    pause 0.6
    $c_blink = True
    c straight "..."
    "I brought her into another hug."
    c "..."
    c grin "..."
    "It took a second, but she accepted it and grabbed onto me."
    a "We probably should get back to the pond, though."
    a "I mean, who knows what Brittney is going to tell the guys that we're doing?"
    $ c_blush = False
    c level left "Heh. Not that they'd probably believe it, anyway."
    c straight "But yeah, you're right. We came here to swim, right?"
    a "Right."
    c "Okay, then."
    show chris:
        ease 0.5 close_c
    pause 0.6
    c "Let's go, then."
    a "Yeah."
    "It was clear that neither of us wanted to go."
    "But it's not like this will be our only chance to have privacy like this, right?"
    stop loop fadeout(3)
    window hide dissolve
    pause 0.1
    scene bg fade with wipeleft
    pause 1.0
    scene bg pond
    show pond_foreground
    with wipeleft
    pause 0.1
    window show dissolve
    pause 0.1
    $ current_track = "\"The Pond\""
    play music the_pond
    $ c_blush = False
    "And so, Christeena and I made our way back to the pond."
    "Brittney, Donald, and Harry were all talking by the dock, but smiled and waved when they saw us come over."
    show chris e1 straight level grin at twoleft
    show don d1 straight raised smile at tworight
    with dissolve
    pause 0.1
    d "There you are!"
    d level blank "What were you two doing?"
    a "We didn't feel like swimming at the time, so we decided to go walk in the woods."
    d raised grin "Really? That's ALL you did?"
    c blank "...what are you implying?"
    d sad "I'm not implying anything."
    d level "Though Brittney did mention something about a long hug..."
    c mad "..."
    a "Hey, man; don't worry about it."
    a "The point is we're back and ready to swim."
    d raised smile "Alright, fair enough."
    hide don
    show brit e2 straight level blank at tworight
    with dissolve
    pause 0.1
    b "..."
    c level "..."
    b sad "Chris, can I talk to you for a second?"
    c "..."
    c "...sure."
    hide chris
    hide brit
    with dissolve
    pause 0.1
    "And so, both girls walked away from the pond and towards Berry Street. Brittney started talking quietly when they were a fair distance away."
    show harry b1 straight mad closed_smile at close_h with dissolve
    pause 0.1
    h "You two made out, didn't you?"
    "I was startled by my brother's seemingly random appearance, but regardless, I rolled my eyes."
    a "No, Harry, we did not make out."
    h level grin "Did you at least kiss her?"
    a "No, Harry! It was nothing like that!"
    h blank "..."
    h closed_smile "You're lying."
    "I groaned and pinched the bridge of my nose."
    a "Why do I bother trying to explain myself? You'll only believe what you want to believe."
    h casual blank "..."
    h "You... really didn't kiss her or anything?"
    a "Once again, no, Harry!"
    h "..."
    h level grin "And I'M the gay one?"
    a "Yep."
    h mad scream small "Hey!"
    hide harry with dissolve
    pause 0.1
    "With that, I walked towards the pond."
    "Now that I was dried up, I could feel the heat beating on me once again; I needed to cool off."
    "Before I went in, though, I could see that Brittney and Christeena were still talking."
    "I couldn't hear what they were saying, but based on their movements and expressions, it wasn't exactly a pleasant conversation."
    "I wouldn't call it 'fighting', necessarily, but it was a more serious discussion."
    "Regardless, I should do what I came here to do and have fun."
    jump pond_end

################################################################################

label d_pond:
    "Before I could do anything else, I could hear movement from behind me."
    "I turned around and saw it was Donald coming closer."
    show don d1 straight raised grin at close_d_float with dissolve
    pause 0.1
    d "Hey, can I talk to you for a second?"
    a "Yeah, sure."
    "He then motioned his head towards an area away from everyone else."
    "After moving in that direction for a short bit, he leaned in close to me."
    d level "Okay, so here's the deal."
    d right "Every year, Brittney and I have a little challenge of sorts."
    a "Oh?"
    d straight raised "Basically, every time we go swimming, I have to sneak up behind her and undo her top."
    a "!!"
    a "And she's okay with that...?"
    d level "She says I'll never be able to do it, so yeah, she's up for it."
    a "And let me guess; you've never actually done it."
    d left blank "That's correct."
    d "She's either noticing my movements, or her hair gets in the way."
    d casual straight "BUT! I think this year, I can actually pull it off."
    d level grin "Literally."
    d "This new bikini of hers wouldn't be too hard to yank down if I grab at the sides."
    d raised "It won't be completely off, sure, but we agreed that getting her boobs exposed still counts."
    d raised smile "But in order to do it, I'll need your help."
    a "Why would I help you do something like this?"
    d mad "You're telling me you don't wanna potentially see a topless girl today?"
    a "..."
    a "Alright, so what's the plan?"
    d casual grin "I need you to distract everyone."
    d raised "No witnesses means not getting caught sneaking behind her."
    a "And how exactly am I supposed to distract 3 people?"
    d right level blank "Admittedly, adding Harry to the mix did throw it off a bit..."
    d straight casual smile "But you're smart. You'll find a way."
    d left raised grin "I shouldn't need too much time, anyway."
    d straight "Just get 'em all focused on you."
    d "Talk about something controversial. That'll get a conversation going."
    a "Well, I'll try my best."
    d raised smile "You got this, man!"
    hide don with dissolve
    pause 0.1
    "We then made our way back to my brother and the girls."
    show chris e1 straight casual blank at threeleft_float
    show brit e2 straight casual blank at middle_float
    show harry b1 straight casual blank at threeright_float
    with dissolve
    pause 0.1
    b "What was that about?"
    hide harry
    show don casual straight blank d1 at close_right_d_float zorder 2
    with dissolve
    pause 0.1
    d "What was what about?"
    b level "You two being all secretive. What were you talking about?"
    d raised left grin "Guy stuff."
    show chris level
    b "..."
    "I mean, technically, that's the truth."
    "Still, both girls are clearly suspicious..."
    "That's gonna make getting their guard down that much harder."
    d straight casual smile "So, Alex, what's up?"
    a "Huh?"
    d level grin "What's new in your life?"
    "Man, he said that really casually. It's kinda scary how normal he can act when he's being sneaky."
    a "Well, uh..."
    a "Not much. I've been spending my time watching TV and playing games."
    b grin "..."
    b e1 "Sounds like quite a boring life."
    "Either Brittney is stupider than she looks, or she's smarter than she looks."
    a "Oh, really? Can't be more boring than spending your time working out."
    b raised opened_smile "Is that right?"
    a "Yep!"
    hide don
    show harry b1 straight casual blank at threeright_float
    with dissolve
    pause 0.1
    "As I spoke, I could see Donald get closer and closer to Brittney."
    "In typical Donald Waters fashion, he was very smooth and sneaky about it."
    show harry left
    b e2 level grin "Well, at least I'm being productive with my time."
    $ b_wink = True
    b tongue "Though, at times, I feel like there's only one person in my household that's NOT."
    $ c_blush = True
    c mad hanging "Hey!!"
    $ b_wink = False
    b e1 mad grin "I didn't even say who, did I?"
    c level blank "Well, uh..."
    $ b_partial = True
    b e2 level huhu "Exactly."
    $ c_blush = False
    c mad hanging "Well, so what? Just because I--!"
    c casual blank "!!!"
    c mad scream "Donald, what the hell are you doing?!"
    $ current_track = "None"
    stop music fadeout(3)
    "Oh, shit."
    show brit zorder 2
    show don d1 mad straight grin zorder 1:
        alpha 0.0
        size (540, 1080)
        xalign 0.6 yalign 0.5
        ease 0.5 alpha 1.0
        block:
            ease 1.0 ycenter 0.52
            ease 1.0 ycenter 0.5
            repeat
    pause 0.5
    "Realizing he's been busted, Donald quickly grabbed Brittney's top by the sides in a last-minute attempt to win."
    $ b_partial = False
    show brit e1 mad frown
    "Almost on cue, Brittney placed one arm across her chest and used the other to quickly jerk her fist towards his face."
    show white zorder 3
    play sound punch
    hide don
    show don d2 small sad zorder 1:
        size (540, 1080)
        xalign 0.6 yalign 0.5
        block:
            ease 1.0 ycenter 0.52
            ease 1.0 ycenter 0.5
            repeat
    pause 0.025
    hide white
    d "GAH!!!"
    hide chris
    hide harry
    with dissolve
    show brit:
        ease 0.5 twoleft
        twoleft_float
    show don:
        ease 0.5 tworight
        tworight_float
    pause 0.6
    "Brittney showed no remorse as she glared at him angrily."
    b "What the fuck, Donald?!"
    b e2 hanging "I'm fine with the casual teasing, but that's crossing a fucking line!!"
    show don straight
    "Donald didn't respond as he cupped his mouth."
    a "Brittney, calm down! He was just doing the challenge you guys had set up!"
    b level blank "..."
    b raised "...What challenge?"
    a "..."
    "I then glared at Donald, myself."
    a "Okay, my turn:{w=0.5} What the fuck, Donald?!"
    d mad left "..."
    "Everyone's eyes were on him as he continued to cover up his face."
    "His eyes, though, were on Brittney, and he did not look happy."
    "Finally, since he knew some sort of response was in order, he looked at all of us, though he still looked angry."
    d straight "..."
    d right level "...sorry."
    "His response was muffled, but understandable."
    show brit at threeleft_float
    show don at middle_float
    show harry b1 casual left blank at threeright_float
    with easeinright
    pause 0.1
    h "Donald, are you okay??"
    hide brit
    show chris e2 straight mad scream at threeleft_float
    with dissolve
    pause 0.1
    c "Who cares? The perverted bastard deserves it!"
    c blank "It's moments like this that make me wonder why you bother wearing that necklace!"
    d straight "..."
    d right "..."
    pause 1.0
    hide don with dissolve
    pause 1.0
    show brit e1 level straight blank at middle_float with dissolve
    pause 0.1
    "Defeated and embarrassed, Donald slowly floated towards the dock."
    $ current_track = "\"Reflection\""
    play music reflection
    c e1 "Yeah, just run away like the coward you are!"
    a "Christeena, just let it go."
    c scream "And you! Don't think I forgot about you!"
    c "You were helping him! Why the fuck would you do that?!"
    a "Hey, I would've never helped if I had known he was lying to me!"
    c "That doesn't change anything!"
    $ c_blush = True
    c blank "What kind of sick fuck thinks it's funny to do that to a girl?!"
    a "Okay, fine. So I'm not innocent."
    a "I'm sorry, Brittney. I really thought this was something you knew about."
    b "..."
    b e2 level grin "It's okay, Alex."
    h straight level "...Guys, he really does look hurt."
    $ c_blush = False
    show chris straight casual
    show brit straight casual blank
    "We all turned to the dock, where we could see Donald sitting and opening his mouth."
    "...it looked awfully red inside."
    b e2 sad hanging "Oh, shit..."
    b "I didn't think I hit him THAT hard!"
    c mad e1 "I still say he deserves it."
    hide chris
    hide brit
    hide harry
    with dissolve
    pause 0.1
    "Ignoring Christeena's comment, I started heading towards Donald."
    "After hearing movement behind me, I turned and saw Brittney wasn't too far back."
    "She seems less angry than I had thought she would've been, given the circumstances."
    show pond_foreground
    show don d1 straight mad blank at close_left_d
    with dissolve
    pause 0.1
    d "..."
    a "You okay, man?"
    "He replied by spitting red saliva into the pond."
    "At least, I'm hoping most of it was saliva..."
    $ b_wince = True
    show brit e2 sad straight hanging at close_right_b with dissolve
    pause 0.1
    b "Jesus Christ, Donald..."
    b blank "I'm so sorry!"
    d right "..."
    d "Why would you do that to me, Brittney?!"
    $ b_wince = False
    b e1 hanging "I said I'm sorry! I didn't see where I was aiming!"
    d "I meant throwing me under the bus!"
    b e2 blank "..."
    d wide "You made me look like a lying sicko!"
    $b_blink = False
    b closed_sad "I-I know... I'm really sorry..."
    a "..."
    a "Hold on a second..."
    a "So you're telling me that the challenge WAS real?!"
    d straight blank "Of course it was!"
    a "Brittney! Why would you act like it wasn't?!"
    $b_blink = True
    b straight "I..."
    $ b_wince = True
    b right "I just..."
    d right wide "You just what?!"
    b "..."
    d "Well?!"
    b straight hanging "I don't know, okay?!"
    b "I clearly wasn't thinking!!"
    d casual blank "..."
    $ b_wince = False
    $b_blink = False
    show brit closed_sad blank e1
    "She then placed her face in her hands and shook her head."
    d sad "..."
    a "..."
    b "..."
    d grin "Hey..."
    "He then reached over and gave her a pat on the shoulder."
    d "Look, just..."
    d "Just know that I don't hate you or anything."
    $b_blink = True
    b straight "..."
    d "I'm serious."
    b "..."
    b grin "..."
    d level "But you probably should tell Christeena and Harry the truth."
    b "Heh."
    b e2 right "Yeah, I probably should..."
    b blank "..."
    b straight "I really am sorry, Donald."
    d level "Apology accepted."
    b grin "O-Okay..."
    $ current_track = "None"
    stop music fadeout(3)
    hide brit with dissolve
    pause 0.5
    show don at close_d with easeinleft
    pause 0.1
    d "..."
    a "..."
    $ current_track = "\"The Pond\""
    play music the_pond
    a "You know what I still don't get?"
    d straight casual blank "What?"
    a "Why didn't you just call her out in front of everyone when she denied it?"
    d level "Oh, trust me, I wanted to."

    if persistent.choices["30"] == 1:
        d raised grin "But be honest; would you have believed me if I had said she was lying?"
        jump ofcourse
    elif persistent.choices["30"] == 2:
        d raised grin "But be honest; would you have believed me if I had said she was lying?"
        jump no
    else:
        d raised grin "But be honest; would you have believed me if I had said she was lying?{nw}"
        menu:
            d "But be honest; would you have believed me if I had said she was lying?{fast}"

            "\"Of course!\"":
                $ persistent.choices["30"] = 1
                jump ofcourse

            "\"No...\"":
                $ persistent.choices["30"] = 2
                jump no

    label ofcourse:
        a "Of course I would've!"
        d level blank "Hm."
        d right grin "Well, you gotta admit that not many other people would've, given the circumstances."
        a "I guess that's fair."
        jump d_pond_end

    label no:
        a "No..."
        d level "Exactly."
        d right grin "I wasn't exactly in the best situation to explain myself."
        a "Yeah, that's true."
        jump d_pond_end

    label d_pond_end:
        show don straight casual blank
        c "The FUCK?!"
        "We looked and saw Christeena glaring at Brittney with a shocked yet angered look."
        d level grin "Well, it looks like the truth is officially out."
        a "Yeah, but that's another thing I don't get."
        a "She had literally no reason to lie when I mentioned the challenge."
        d level right grin "Not exactly."
        a "Huh?"
        $d_blink = False
        d closed sad smile "By some miracle, Christeena was never aware of the challenge, as I'm sure you noticed."
        $d_blink = True
        d straight casual blank "But believe it or not, that was intentional."
        a "Is that right?"
        d level grin "Dude, if Christeena had known, she would've been on me at all times when we were in the water."
        d raised left "No progress would have ever been made!"
        a "Okay, but if the gig was up, why continue to lie?"
        d straight level blank "Well..."
        d right "Yeah, I'll admit, I'm stumped there."
        d raised "Maybe she didn't want Christeena to know she was actually 'easy' enough to do something like that."
        a "As if she doesn't already know?"
        d straight casual "I mean, Brittney teases about things like that all the time, but it's clear she's kidding."
        d "Maybe actually being serious this time made her have second-guesses."
        d left level "I dunno. It's hard to know for sure what she's thinking."
        d sad grin "But..."
        d straight "Even if I knew everyone would've believed me if I had told them the truth..."
        d "...I wouldn't have said anything."
        a "Why?"
        d "You saw how embarrassed she was over here."
        d right "I could never make her feel that way in front of more people than necessary."
        a "But you clearly were pissed at her."
        d straight level blank "Well, yeah, of course."
        d grin "But I know her better than she thinks I do."
        d "If I had called her out right then and there..."
        d left blank "...she would not have taken that well."
        d straight grin "I figure it's better for her to get that temporary victory before setting things right."
        a "..."
        a "So, if I'm understanding you correctly, you would've rather looked like the bad guy so she could look like the good guy?"
        d sad "More or less."
        a "Wow."
        a "You must really love her."
        d right level "Heh..."
        d "I guess I really do."
        "He then stared towards the girls and Harry, who were talking seemingly casually, so it's safe to assume that Christeena got all of her anger out."
        "Maybe."
        "Regardless, I could tell he was looking at Brittney in particular."
        "..."
        "I don't think I can pinpoint for sure what it is Donald sees in her, but..."
        "...I'm glad he's found a girl that he really seems to care about."
        "Unfortunately, neither of us can pinpoint what exactly she DOESN'T see in him..."
        "..."
        "Donald spit some more into the pond, only this time, less red."
        a "Oh, I almost forgot; how's your mouth doing?"
        d straight raised "Still tastes bloody, but I think I'll be good. No broken teeth or anything."
        a "Darn. You and Brit could've been matchers."
        $d_blink = False
        d closed sad smile "Ahahaha!"
        d "Except my parents wouldn't let me go without fixing it!"
        a "Haha, yeah, that's fair."
        a "Well, anyway, the fire seems to have died down. What do you say we head back over there?"
        $d_blink = True
        d casual straight "Sounds good to me."
        hide don
        hide pond_foreground
        with dissolve
        pause 1.0
        show chris e1 straight level blank at threeleft_float
        show brit e2 straight sad blank at middle_float
        show harry b1 straight casual blank at threeright_float
        with dissolve
        pause 0.1
        b "H-How are you feeling, Donald?"
        hide harry
        show don d1 straight sad grin at close_right_d_float
        with dissolve
        pause 0.1
        d "I'll survive."
        d left raised smile "Still mighty impressed that you got me that good from behind!"
        d "You really are stronger than you look!"
        b "..."
        b level grin "W-Well, if I wasn't strong, I'd never be able to punch you in the arm the way I do!"
        $d_blink = False
        d closed sad grin "Very true!"
        c "..."
        c left "I'll never understand you two..."
        "Well, I'm glad things seem back to normal."
        "Though, Brittney still doesn't seem quite like herself..."
        a "Hey, we're all here to swim, right? Let's have some fun and forget about this whole thing."
        $d_blink = True
        d straight casual "I'm with Alex; let's enjoy ourselves!"
        b e1 casual "Yeah!"
        c "..."
        jump pond_end

################################################################################

label e_pond:
    "With that, Brittney ducked under the water and swam towards Donald."
    "Christeena quickly followed behind, leaving Harry and I by ourselves."
    show harry b1 straight casual grin at close_h_float with dissolve
    pause 0.1
    h "You coming?"
    a "Yeah, I just--"
    a "..."
    a "Shit..."
    h blank "What?"
    a "I forgot my goggles back home."
    h level grin "Pft. Goggles? What, are you 6?"
    a "Well excuse me for not wanting dirty pond water in my eyes!"
    h "You're still lame."
    a "Ah, whatever. I'll be back."
    hide harry with dissolve
    pause 0.1
    "As I was heading towards the edge of the pond, Donald and Brittney asked where I was going."
    "After giving my response, Brittney was quick to tease, as to be expected."
    "Donald, meanwhile simply told me to not take too long."
    $ current_track = "None"
    stop music fadeout(3)
    scene bg bs with dissolve
    pause 0.1
    "It admittedly did take a bit longer to find my goggles than I had thought, but fortunately, I found them and was on my way back to the pond."
    "On my way back towards the pond, I could see a door across the street open up."
    e "Are you fucking kidding me?!?!"
    scene bg house_y with dissolve
    pause 0.5
    $ E_Name = "Eleanor"
    show elie c1 straight mad scream at middle with dissolve
    pause 1.0
    $ current_track = "\"Chaotic Evil\""
    play music chaotic_evil
    "Eleanor Yellman."
    if persistent.choices["12"] == 3:
        "This is my first time seeing her since that day at the mall."
        "While she wasn't really THAT angry and moody then, she's certainly furious now."
    else:
        "This is my first time seeing her since that day at Dolmart."
        "And she looks just as pissed as I remember."
    "Thankfully, that anger didn't seem to be targeted towards me."
    "She stomped towards the curb, where I could see a garbage can knocked over, its contents spilled all over the sidewalk."
    e frown "When will those fucking retards learn to do their fucking job right?!"
    "She seemed unaware of my presence as she moved the garbage can straight up and started putting the spilled waste back inside."
    "..."
    "I probably should just keep going on back to the pond..."
    "...but my conscience says I should at least TRY to help."
    "Taking a deep breath and saying a quick prayer, I made my way across the street."
    show elie:
        ease 1.0 close_e
    pause 1.0
    a "Do you need help?"
    show elie casual blank
    "She turned towards me with a surprised look, which I guess is to be expected when you thought you were alone."
    show elie mad frown
    "Though that look of surprise didn't last long."
    e "No, I do not."
    "She then grabbed another bag and tossed it in."
    a "Okay, then."
    hide elie with dissolve
    pause 0.1
    "Well, I can't say I didn't try."
    "I continued to walk towards the pond."
    $ current_track = "None"
    stop music fadeout(3)
    "That's when I heard a loud clanking sound behind me."
    "I turned and saw her holding a garbage bag that was completely ripped along the bottom, its contents spilled all over."
    show elie c1 straight mad scream at middle with dissolve
    pause 0.1
    e "MotherFUCKER!!!"
    "She threw the bag on the ground in defeat before kicking the spilled garbage still remaining on the sidewalk."
    hide elie with easeoutleft
    pause 0.1
    play sound door_slam
    "She then stormed into her house, leaving the trash where it was."
    "..."
    "..."
    "..."
    "I finally sighed and walked over to the garbage."
    "There were a few bags left on the curb, so I placed those into the can."
    "As for the garbage from the ripped bag, I carefully picked up what I could and placed it back into the bag, with the hole in the bottom as the new top."
    "..."
    "I couldn't help but notice that a majority of it was beer cans."
    "Along with the occasional TV dinner tray and cigarette butt."
    "Looking on the sidewalk revealed a spread-out pile of ash nearby."
    "..."
    "I remember hearing somewhere that someone's garbage can tell you a lot about their life; this doesn't feel like an exception."
    play sound door_open
    "The door opened back up."
    "I looked and saw her shaking open a new garbage bag."
    "About halfway down the sidewalk, she looked up and stared at me."
    show elie c1 straight level blank at close_e with dissolve
    pause 0.1
    e "..."
    a "..."
    "We just looked at each other awkwardly."
    "At least, I found it awkward."
    "She might just simply be pissed. I don't know."
    "Still making eye contact with me, she shook the new garbage bag once more before continuing my way."
    e neutral "Move."
    "Yes, Ma'am."
    "I stood up and backed away a bit."
    "She then grabbed the old, ripped bag and carefully placed it into the new bag."
    "Tying it tightly, she placed it into the can and dusted her hands."
    e level "Looks like it'll be full for another week."
    e mad frown "AGAIN."
    e "Why they love to just fuck me over and not pick up my shit, I don't know!!"
    "She didn't seem to be talking to me, in particular; most likely, I was just a verbal punching bag."
    e level blank "Anyway..."
    "This time, she was facing me."
    e "...thanks, I guess."
    a "Oh, uh, no problem."
    "Huh."
    "She actually seem less hostile right now."
    "Maybe I can take advantage of this opportunity..."
    if persistent.choices["12"] == 3 and persistent.choices["15"] == 1:
        if persistent.choices["16"] == 1:
            a "Hey, I don't know if you remember me, but I went up to you at the art store a couple weeks ago."
        elif persistent.choices["16"] == 2:
            a "Hey, I don't know if you remember me, but I introduced myself at the art store a couple weeks ago."
    else:
        a "I'm Alex, by the way."
    e neutral frown "Cool. I don't care."
    a "..."
    e "..."
    a "A-Anyway, I'll just, uh... be going now."
    e level blank "Okay."
    hide elie with dissolve
    pause 0.1
    "She then walked back into her house as if I weren't there."
    "..."
    "All things considered, that went pretty well."
    "Making sure I had my goggles, I finally made my way to the pond."
    window hide dissolve
    pause 0.5
    scene bg fade with wipeleft
    pause 0.5
    scene bg pond
    show pond_foreground
    with wipeleft
    pause 0.5
    window show dissolve
    pause 0.1
    $ current_track = "\"The Pond\""
    play music the_pond
    "All eyes were on me as I made my way back to the pond."
    show chris e1 straight casual blank at threeleft_float
    show brit e2 straight casual blank at middle_float
    show don d1 straight raised blank at threeright_float
    with dissolve
    pause 0.1
    d "There you are!"
    a "Yeah, sorry; I didn't mean to be gone that long."
    a "I had a little run-in with Eleanor on the way back."
    $ c_blush = True
    show don level
    show brit e1 level
    c mad "Ugh..."
    c "What happened?"
    a "Well, she was picking up trash that had been knocked out of the can, and I helped her out."
    $ c_blush = False
    show don casual
    show brit casual
    c casual "..."
    c "You what?"
    a "What? What's the problem with helping someone out?"
    c e2 mad hanging "The problem is that she's a fucking bitch!"
    d raised left "Chris, even the worst of people deserve kindness."
    c blank "Well, SHE doesn't!"
    c "She's just so fucking rude for literally no reason!!"
    c "She just makes our lives hell every time she's near!!"
    b raised "Honestly, the only thing I'm confused about is the fact she let you help her."
    a "Well, she didn't, at first, but I tried again, and she just rolled with it."
    b e2 left level "Huh."
    d straight casual grin "Well, I'm glad you did the neighborly thing, Al."
    $ c_blush = True
    c e2 left "..."
    d raised "Since you're back, I suppose that means we can swim now."
    a "Oh, I didn't want you guys to feel like you had to wait for me or anything!"
    b casual straight grin "Nah, it's cool, dude. Just being in the water was good enough for me."
    $ b_partial = True
    b mad closed_smile "That said, it's time for some REAL fun!"
    "I don't like the sound of that."
    hide brit
    hide chris
    hide don
    with dissolve
    pause 0.1
    $ b_partial = False
    $ c_blush = False
    "As the guys started moving towards the middle of the pond, I could see Harry come closer."
    show harry b1 straight casual blank at close_h_float with dissolve
    pause 0.1
    h "Isn't Eleanor that girl who screamed at us at Dolmart that one day?"
    a "Yeah, that's her."
    h level "Huh."
    h right "Okay, then."
    hide harry with dissolve
    pause 0.5
    "..."
    "Am I really such a bad guy for helping out someone who needed it?"
    "..."
    "Eh, whatever. Let's just do what we came here to do and have fun."
    jump pond_end

################################################################################
################################################################################

label pond_end:
    window hide dissolve
    pause 0.5
    scene bg fade with wipeleft
    pause 1.0
    scene bg pond with wipeleft
    pause 0.5
    nvl clear
    $ c_blush = False
    nvl show dissolve
    pause 0.1
    narrate "The rest of the time went pretty smoothly."
    narrate "There really wasn't much actual 'swimming' most of the time, just treading in the water and talking about this and that."
    narrate "Though, we did have some occasional moments of doing flips off the dock."
    narrate "Well, in the case of some of us, we TRIED."
    narrate "Still, we were enjoying ourselves to the point where we hadn't really paid attention to what time it was."
    narrate "Finally, at around 3:00, we decided to wrap it up for the day."
    nvl hide dissolve
    window show dissolve
    pause 0.1
    show chris e1 straight casual grin at threeleft_float
    show don d1 straight casual smile at middle_float
    show brit e1 straight casual grin at threeright_float
    with dissolve
    pause 0.1
    d "What do you guys say we head to Kelly's, if you're up for it?"
    b e2 opened_smile "Sounds good to me!"
    b level right derp "I'm sure she won't mind if we show up in wet swimsuits, right?"
    d right level grin "I mean, I'm sure she wants to keep SOME level of professionalism in her business."
    $ b_partial = True
    b straight huhu "{cps=15}FIIIIINE{/cps}."
    $ b_partial = False
    b e1 mad opened_smile "But if I starve to death in the time it takes me to get dressed and over there, I'll haunt you forever."
    $d_blink = False
    d closed sad "Ooooo, so scary!"
    play sound splash
    $ b_wink = True
    show brit e2 raised tongue
    "She splashed him in response."
    a "Alright, then. Let's get out of here."
    hide chris
    show harry b1 straight sad blank at threeleft_float
    with dissolve
    pause 0.1
    h "Wait!"
    h "Can I at least do one more jump off the dock?"
    h casual grin "I want to be able to get at least one flip in!"
    $d_blink = True
    d left casual "Sure, bud! You got it this time!"
    $ b_wink = False
    b e1 level grin "I dunno..."
    $ b_partial = True
    b raised closed_smile "It'll have to take a miracle in order to pull that off, at this point."
    h mad closed_smile "Heh! I'll show you!"
    hide harry
    hide don
    hide brit
    with dissolve
    pause 0.1
    $ b_partial = False
    "Harry then got out of the water and onto the dock."
    "All eyes were on him as he looked down at the water."
    show chris e1 straight casual blank at close_left_c_float with dissolve
    pause 0.1
    c "Do you really think he'll be able to do a flip?"
    c level left dot "The best he's done so far is what looked like a partial cartwheel..."
    a "Hey, it's better than your attempt at a flip, Ms. BellyFlop!"
    c straight mad smile "Well, at least I actually went up and tried!"
    a "Alright, fair enough; that's better than I thought you would've done."
    c e2 raised grin "Exactly."
    show harry b1 straight mad closed_smile at tworight with dissolve
    pause 0.1
    h "You two done? I wanna make sure you all see this!"
    a "Alright, alright! We're watching!"
    show harry at truecenter
    hide chris
    with easeoutleft
    pause 0.1
    "Harry then swung his arms in anticipation."
    "He took some pretty deep breaths."
    a "You're not getting nervous, are ya?"
    h grin "Heck no! I got this!"
    show harry:
        parallel:
            ease 0.5 yalign 1.0
        parallel:
            ease 0.5 zoom 0.7125
    pause 0.6
    "Harry then backed up, ready to pounce."
    show harry:
        parallel:
            ease 0.5 zoom 1.0
        parallel:
            ease 0.2 yalign 1.0
            ease 0.3 yalign -2.0
    pause 0.6
    play sound splash
    pause 2.0
    "Well, he didn't do the flip, but he got closer that time."
    "..."
    "..."
    $ current_track = "None"
    stop music fadeout(3)
    "..."
    show brit e2 straight casual blank at close_right_b_2_float
    show don d1 straight sad blank at close_left_d_2_float
    show chris e1 straight sad dot at close_c_float_2
    with dissolve
    pause 0.1
    c "Uh, g-guys...?"
    b e1 sad "Let me go down and check."
    show brit:
        ease 0.2 yalign 0.25
    pause 0.2
    play sound splash
    show brit:
        ease 0.3 yalign -3.0
    pause 0.4
    "Brittney then ducked under the water and swam towards where Harry landed."
    "..."
    "It's probably nothing. Maybe he's just trying to be funny."
    "..."
    "Maybe..."
    "Oh, God, please let him be okay...!"
    c e2 casual hanging "There!"
    "Christeena then pointed to some movement from the water."
    $ b_wince = True
    play sound splash
    show brit e1 straight sad blank:
        zoom 0.75
        xalign 0.9 ycenter 2.0
        ease 0.3 ycenter 0.5
        ease 0.3 ycenter 0.58
        ease 0.2 ycenter 0.5
        threeright_float
    pause 0.9
    "..."
    "Harry was in her arms."
    "But he wasn't moving."
    $ c_blush = True
    show chris e1 sad dot
    show don wide
    a "No..."
    a "NononononoNO!!!"
    "I could feel my heart beating faster and faster."
    "My breathing became quicker and quicker."
    a "Th-This can't be...{w=1.0} No, it... It...!!"
    d blank "Alex, stay calm!"
    a "I-I-I can't!"
    a "Oh, God... Wh-What am I gonna tell my parents?!"
    d "Alex, please stay calm! Try to breathe!"
    $b_wince = False
    b e2 hanging "Someone get out and call 911! I'll try and do CPR!"
    h_o "Sounds good to me!"
    $ b_wince = False
    $ c_blush = False
    show brit casual blank
    show chris casual
    show don casual
    "We all instantaneously turned towards my brother, whose head was turned towards Brittney with his lips puckered."
    a "Harry!!!"
    hide brit
    hide don
    hide chris
    with dissolve
    pause 0.1
    "I quickly swam over to Brittney and proceeded to yank my brother out of her arms."
    show harry b1 sad small blank at close_h_float with dissolve
    pause 0.1
    h sad small blank "Urk!"
    "I gripped onto my brother's shoulders tightly."
    a "What the fuck, Harry?!"
    h mad straight "Dude, calm down!"
    a "Calm down?!"
    a "CALM DOWN?!"
    h sad small "...!"
    "I could feel tears coming out of my eyes, as well as large lump in my throat."
    a "That wasn't fucking funny at all, Harry!!"
    a "It's never funny to pretend to fucking DIE!!"
    a "Don't ever pull shit like that again, Harry! You hear me?!"
    h "Y-Yes!!"
    a "..."
    "I then let him go and took a deep breath."
    "..."
    "..."
    "After covering my face and thinking for a few seconds, I turned back to him."
    a "I'm sorry. I just..."
    "I gave another small sigh."
    a "Please never do that again.{w} Please."
    h straight "..."
    show harry at close_left_h_float
    show don d1 straight sad blank at tworight_float
    with easeinright
    pause 0.1
    d "You ARE okay, right Harry?"
    h "Y-Yeah. I'm fine."
    d level grin "Alright. That's all that matters, then."
    d sad "C'mon. Let's all get some lunch."
    a "Yeah. That... That sounds like a good idea."
    hide harry
    hide don
    with dissolve
    pause 1.0
    "In hindsight, maybe I overreacted a little bit."
    "But the thought of him being gone..."
    "I don't know if my family would've been able to handle that."
    $ daydesc = 0
    $ replay = False
    $ renpy.end_replay()
    $ progress += 1
    jump progress
