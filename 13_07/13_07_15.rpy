label baseball:
    python:
        B_Name = "Brittney"
        C_Name = "Christeena"
        M_Name = "Mrs. Truman"
        current_track = "None"
        b_hat = 1
        b_hair = 0
        c_hair = 0
        outfit_b = "f"
        outfit_ch = "b"
        outfit_c = "a"
        outfit_d = "a"
        outfit_m = "b"
    show text "{size=+50}July, 2013{/size}":
        xalign 0.5 yalign 0.05
    show screen calendarOs
    show calendar july july_15:
        xalign 0.5 yalign 0.67
    show calendar_circle:
        xalign 0.375 yalign 0.63
    with dissolve
    if replay == False:
        $ persistent.todays_date = "July 15th, 2013"
        $ renpy.notify("Game saved!")
        $ renpy.save("1-1")
    pause 4
    hide text
    hide screen calendarOs
    hide calendar
    hide calendar_circle
    with dissolve
    pause 1
    scene bg house_ut with dissolve
    window show dissolve
    pause 0.1
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    $ renpy.block_rollback()
    show martha p1 straight casual smile at m_middle with dissolve
    pause 0.1
    hide screen notify
    mu "Got everything?"
    show martha at m_twoleft
    show don p1 straight casual smile at tworight
    with easeinright
    pause 0.1
    d "Looks like it!"
    "Donald replied as he closed the trunk."
    show martha:
        ease 0.5 xalign 0.1
    show don:
        ease 0.5 xalign 0.9
    show brit p1 straight casual opened_smile at middle with dissolve
    pause 0.1
    b "Alright!"
    b p2 raised closed_smile "Let's kick some ass!"
    mu mad blank "Brittney Anne!"
    $ b_partial = True
    b level blank "..."
    b raised "Let us place our feet onto some posteriors with force."
    mu level grin "..."
    mu "Just get in."
    $ b_partial = False
    $ b_wink = True
    b p1 tongue "Will do!"
    hide martha
    hide don
    hide brit
    with dissolve
    pause 0.1
    $ b_wink = False
    "As Mrs. Truman got into the driver's seat and Brittney got into the passenger seat, the rest of us got into the back."
    "Having two long-legged guys made it challenging, but we managed to squeeze ourselves on the outside seats while Christeena sat comfortably in the middle."
    a "So, is it normal for two school teams to have an unofficial game in the summer?"
    show don p1 straight raised grin at twoleft with dissolve
    pause 0.1
    d "Well, not really 'normal', but the Trenburg Titans still feel cheated by their loss at the end of the season."
    d level left "As if winning this will somehow change the official results..."
    show chris p1 straight raised smile at close_right_c with dissolve
    pause 0.1
    c "Hey, if they wanna get their asses beat again--"
    m_o "Christeena Renee!"
    c mad blank "..."
    c raised grin "If they wanna lose again in front of everyone, let them!"
    c mad smile "It'll only make it satisfying for the rest of us!"
    d closed sad grin "Amen!"
    scene bg house_ut with dissolve
    pause 0.1
    "Honestly, the only sporting events I ever really watched were my own meets while I waited for my next event."
    "Well, you know, besides maybe an occasional Super Bowl, but even then, I was more focused on the ads."
    "Still, I gotta admit the idea of an unofficial rematch game is intriguing."
    "Especially with Brittney at the bat."
    "Plus, baseball is simple enough, I'm sure even I can follow what's happening."
    show don straight sad grin p1 at twoleft with dissolve
    pause 0.1
    $ b_partial = True
    d "You won't regret being dragged along, Al!"
    show brit p2 straight raised closed_smile at tworight with dissolve
    pause 0.1
    b "I'll make sure of it~"
    m_o "Alright, buckle up, chillins!"
    scene bg house_ut with dissolve
    pause 0.1
    $ b_partial = False
    "With that, we pulled out of the driveway and headed to the baseball diamond."
    play sound van_start
    $ current_track = "None"
    stop music fadeout(3)
    window hide dissolve
    pause 0.5
    scene bg fade with wipeleft
    scene bg baseball
    show baseball_overlay zorder 2
    with wipeleft
    pause 0.5
    window show dissolve
    pause 0.1
    $ current_track = "\"Outside the Street\""
    play music outside_the_street
    "After pulling in, we could see several girls already practicing on the field."
    "Judging by the uniform, they were our girls."
    "Once the car was parked, Brittney hopped out and ran to the trunk to get her stuff."
    show brit p1 casual grin straight at middle zorder 3 with dissolve
    pause 0.1
    b "Bat... {w=0.5}glove... {w=0.5}hat... {w=0.5}cleats..."
    $ b_partial = True
    b level closed_smile "I'd say 'cup', but I don't have that disadvantage."
    show brit at tworight
    show chris p1 level straight blank at twoleft zorder 3
    with easeinleft
    pause 0.1
    c "Thanks for that reminder, Brittney."
    hide chris
    show martha p1 straight mad smile at m_twoleft zorder 3
    with dissolve
    pause 0.1
    mu "Alright, you better start practicing!"
    mu casual grin "Good luck, Brittney!"
    $ b_partial = False
    b opened_smile casual "Thanks, Mom!"
    b p2 sad grin "And be sure to save Dad a seat for when he gets here!"
    $ m_partial = True
    mu raised "Brittney, this ain't my first rodeo."
    $ b_wink = True
    b raised tongue "If you say so."
    hide martha
    hide brit
    with dissolve
    pause 0.1
    $ b_wink = False
    $ m_partial = False
    "With that, we parted ways, with Brittney headed towards the field while we popped the trunk, with Donald grabbing the cooler and the rest of us grabbing blankets to sit on."
    "We then found some metal bleachers near the fence that gave us a good view of the home base."
    "Though having no back support on said bleachers would quickly prove to be a problem, but I guess I'll just have suck it up."
    show chris p1 straight casual grin at close_right_c zorder 3
    show don p1 straight casual grin at close_left_d zorder 3
    with dissolve
    pause 0.1
    a "So, is our baseball team really that good?"
    d raised left "Well, I mean, they're not really pros or anything..."
    d mad straight smile "...but we're a very competitive school."
    show chris p2 raised
    "Chris nodded in agreement."
    c smile "I mean, I don't follow sports. Like, at all."
    c p1 level left grin "But when I see a good game, I can't help but get invested, you know?"
    a "I guess."
    d level grin "I mean, if nothing else, you get to see boobs jiggle while the girls run!"
    c mad straight blank "Donald!"
    d right sad smile "I'm kidding!"
    c_s level "..."
    d straight casual "Well, anyway, it'll be entertaining, no matter what."
    a "If you say so."
    show don:
        ease 0.5 xalign 0.0
    show chris:
        ease 0.5 xalign 1.0
    show martha p1 straight casual grin at m_middle zorder 3 with dissolve
    pause 0.1
    mu "Any of you three hungry right now?"
    "She then tapped on the cooler."
    d right grin "You know, I suppose I am a little hungry."
    mu smile "Alright, then. How about you, Christeena?"
    c sad p1 grin "I'm good for now."
    mu grin "Alex?"
    a "I'm fine, thanks."
    mu raised "Suit yourself."
    hide chris
    show martha at m_tworight
    show don at close_left_d
    with easeoutright
    pause 0.1
    "Mrs. Truman then opened the cooler and looked inside."
    mu casual smile "You want ham or turkey, Donald?"
    d "Turkey's fine."
    "She then pulled out a thick square wrapped in tin foil with a giant letter T written on it and handed it to Donald."
    d sad "Thanks! Got anything to drink?"
    mu "Yeah, they're in the other cooler."
    d_s casual blank "..."
    d raised "What other cooler?"
    mu blank "The... one I had you bring to the trunk. The blue one, right next to the red one."
    d right sad "I only saw one cooler, and that's it right there."
    "He replied as he pointed to the red cooler by her feet."
    mu_s sad "..."
    mu "Well, that's not good."
    mu "I could've sworn I had it set right by it..."
    d straight grin "I mean, it's not that big of a deal; I can manage."
    show don at close_left_d_2
    show martha at m_middle
    show chris p1 straight casual blank at close_right_c_2 zorder 3
    with easeinright
    pause 0.1
    c "Well, we could always get fountain drinks from the convenience store a couple blocks away."
    d "Chris, I'm fine, really."
    c level "Well, not to be rude, but you're not the only one here."
    d_s level blank "..."
    d grin "Fair enough."
    "Mrs. Truman then sighed in annoyance."
    mu level "Well, it sucks, but I guess it's the easiest option."
    "She then searched her purse for a few seconds before pulling out a $10 bill."
    mu raised grin "And you're SURE you're fine without a drink, Donald?"
    d_s blank "..."
    d left raised grin "Well, I guess if everyone else is getting one, I might as well get one..."
    $ m_partial = True
    mu level grin "That's what I thought."
    "She then started to stand up."
    d right casual smile "I can get it, Mrs. T."
    $ m_partial = False
    mu casual blank "You sure?"
    d sad grin "Yeah. I brought up this whole drink thing in the first place; it's only fair I fix it."
    mu sad grin "Well, alright, if you insist."
    "She then handed Donald the bill."
    d straight level blank "Although, actually, if we're all getting one..."
    d "...that would be four. I'd need an extra set of hands to carry the drinks."
    c p2 raised "Don't they usually have little cup holder things that you can put 4 cups into?"
    mu "Well, now that I think about it, your father will probably want something, as well."
    c_s level p1 "..."
    c right "Alright, fine. I guess I'll go with."
    c straight raised grin "Besides, I suppose it wouldn't hurt to make sure you remember all the right drinks."
    d sad grin closed "Alright, fair enough."
    d straight casual "Al, you wanna come with, too?"
    c_s casual dot "..."
    a "Huh? Why?"
    d sad "I figure it gives you something to do."
    $ m_partial = True
    mu raised "Or is it because you're scared I might seduce him by the time you get back?"
    d right raised smile "I'm terrified, actually!"
    mu level "Haha."
    d straight casual grin "Anyway, it's up to you, Al."
    c_s blank "..."
    "Well, I've never actually been alone with Mrs. Truman and had a one-on-one talk..."
    "...but maybe I could change that. She seems like an interesting person, much like her daughter."
    "Actually, maybe a conversation with her could help me learn more about Brittney..."
    "...or maybe the whole time Christeena and Donald are gone, it'll just be awkward silence..."
    a "Well, uh..."
    if persistent.choices["31"] == 1:
        jump gowithchris
    elif persistent.choices["31"] == 2:
        jump stayhere
    else:
        "What should I do?"
        menu:
            "Go with Christeena and Donald":
                $ persistent.choices["31"] = 1
                jump gowithchrisanddon
            "Stay here":
                $ persistent.choices["31"] = 2
                jump stayhere

label gowithchrisanddon:
    a "Alright, I guess it wouldn't hurt to go with you guys."
    d smile "Cool!"
    d sad right grin "We'll be back soon, Mrs. T!"
    $ m_partial = False
    mu raised "Oh, I know; you'd hate to miss the game!"
    d closed "True that!"
    c_s level "..."
    hide chris
    hide don
    hide martha
    with dissolve
    pause 0.1
    "With that, Mrs. Truman verified what drink she and her husband wanted, and the three of us were on our way."
    scene bg mainstreet with dissolve
    pause 0.1
    "The ballpark wasn't too out of the way from the downtown district, and as Christeena said, the gas station was only a couple of blocks away."
    "I guess I hadn't realized how much shade the park had, because once we got down Main Street, the sun was beating itself onto me."
    "Looks like getting these drinks would be worth it, after all."
    "After all, everyone knows that soda is the best way to quench your thirst!"
    play sound deli_door
    scene bg conveniencestore with dissolve
    pause 0.1
    "The convenience store was practically empty sans the woman behind the counter."
    "It was as standard as you could get, with a few small aisles full of food and the like, some refrigerators full of drinks along the walls, and a large fountain drink station in the back corner."
    show don p1 straight casual grin at tworight
    show chris p1 straight casual blank at twoleft
    with dissolve
    pause 0.1
    d "Alright, you remember what drinks we need to get?"
    c raised grin "Yep!"
    d raised "Alright, then I'll meet you at the counter."
    c casual dot "Huh? Where are you going?"
    d level right "I'm gonna grab some chips; it'll go great with the sandwiches."
    c mad scream "Really? You're gonna spend my mom's money on something other than what she asked you to get?"
    d straight raised blank "Who said I was using HER money? I have a debit card, you know."
    c_s level blank "..."
    c left "Alright, then."
    c straight grin "In that case, I'll grab the drinks."
    d casual grin "Good deal!"
    show chris:
        ease 0.5 offscreenleft
    show don:
        ease 0.5 offscreenright
    pause 0.6
    hide chris
    hide don
    "And with that, they split up, leaving me alone by the door."
    "..."
    "Did they forget I existed for a second, or...?"
    "Ah, whatever. I suppose I better go after one of them so I'm not just standing around awkwardly."

    if persistent.choices["32"] == 1:
        jump getchipswithdon
    elif persistent.choices["32"] == 2:
        jump getdrinkswithchris
    else:
        menu:
            "Get chips with Donald":
                $ persistent.choices["32"] = 1
                jump getchipswithdon
            "Get drinks with Christeena":
                $ persistent.choices["32"] = 2
                jump getdrinkswithchris

    label getchipswithdon:
        $ D_Points += 1
        "I made my way over to the chip aisle, where Donald was browsing the selection."
        show don p1 straight casual grin at close_d with dissolve
        pause 0.1
        d "What kind of chips are you thinking?"
        a "You're the one who wanted them; you pick."
        d level "Well, I don't wanna get them for JUST me."
        d right "I know Christeena and Mrs. T are fine with original..."
        a "Sounds good to me."
        d blank "Yeah, but I'm personally not a fan."
        a "Alright, so get another one for you."
        d straight raised "That's the problem. I can't decide!"
        d level grin "There are too many good ones to pick from..."
        d "Got any you like?"
        a "Hm..."
        "I browsed the selection on the racks."
        a "I guess sour cream and onion will do."
        d casual smile "Then sour cream and onion, it is!"
        "He grabbed a bag off the shelf."
        d level right grin "Heh. Man, Brittney would kill me if she saw me eating these..."
        a "What do you mean?"
        d straight raised "She keeps telling me how unhealthy chips are and that I should stop snacking on them."
        a "And yet here you are, going out of your way to buy chips."
        d closed sad "Hey, she's the athlete, not me."
        d straight level "Besides, even if I was, she herself said that everyone deserves a cheat day."
        "I don't recall it being worded quite like that, but I'd hate to burst his bubble."
        if delihangout:
            a "So, she's gotten on you about your health, too?"
            d casual dot "'Too'?"
            a "Yeah, when I was at Kelly's with her once, she commented on how I unhealthy I am."
            d level right grin "Heh. Sounds about right."
            d casual straight "But, yeah, she gets on me about that on occasion."
        else:
            a "So, she's trying to get you to eat healthier or something?"
            d casual "Yeah, you can say that."
        a "Why? You're not exactly the most unhealthy person on the planet."
        d closed sad "Aw, thank you for noticing!"
        "He commented as he jokingly flexed his arms."
        d straight "But her mindset is 'Everyone could look better'."
        d level left "I mean, I get where she's coming from, but I dunno. I think she's overreacting a bit."
        d straight casual "Still, it could be worse."
        d closed sad "It's not like she's telling me to eat a vegan diet or something."
        a "Not that you would follow through with that, anyway."
        d mad straight smile "Hey, God wouldn't have made animals taste good if we weren't supposed to eat them!"
        a "Amen!"
        "We then started making our way to the counter."
        a "So, you and Brittney really are close, huh?"
        d raised grin "Odd change of topic..."
        a "Well, I don't think you would give much thought to her suggestions of better eating if you weren't close."
        d level right "Fair enough."
        d straight sad "But, yeah, she's my best friend, after all."
        d level "No offense."
        a "None taken at all."
        a "Still, though, are you sure her being your friend is the only reason?"
        d casual blank "What do you mean?"
        a "Well, you've got that crush on her and all..."
        show don level
        "He then stopped walking and glared at me."
        a "Hey, I'm just curious, that's all."
        "He stared for another second before sighing."
        if pond_scene == "Donald":
            d left "I mean, yeah, I do, but that's not the only reason why I'm nice to her, man."
            d straight grin "I don't really know how to explain it."
            d left "It's like..."
            d straight "Well, it's like I told you at the pond: I know her better than she thinks I do."
            d raised "She'd never admit it, but she needs me in her life."
            a "How do you figure?"
            d sad "Again, just a hunch, or heck, maybe it's the big man upstairs talking to me, but I feel like she was in a rough place before she met me."
            d right "So, it's like I fill a void that she has. Something that makes her feel alive."
            a_s "..."
            "I'll be honest, I have no idea what he's getting at."
            "It seems like a large assumption to make, but then again, he's had years to get to know her, so it's possible that I'm missing something."
        else:
            d left "I dunno, man. No offense, but I don't think you'd understand."
            a_s "..."
            "Well, that kinda stung, but if that's what he thinks, then who am I to press further?"
        "Regardless, I just nodded in agreement as our friend came down the aisle with a less-than-happy face."
        show don at close_left_d
        show chris p2 straight mad blank at tworight
        with easeinright
        pause 0.1
        c "I thought the point of all of us coming here was that one person didn't have to carry all the drinks!"
        "I took a quick glance at the counter and saw all 5 cups sitting by the woman behind the register."
        d straight sad grin "Sorry, Chris. We just got distracted."
        c p1 level "Well, let's just pay and get back; the game's gonna start soon."
        a "We'll make it back on time, don't worry."
        scene bg conveniencestore with dissolve
        pause 0.1
        jump payfordrinks

    label getdrinkswithchris:
        $ C_Points += 1
        "I made my way over to the drink station, where Christeena was pulling out 5 large cups."
        show chris p1 straight casual grin at close_c with dissolve
        pause 0.1
        c "Hey, Alex."
        a "Yo."
        "I then grabbed two of the cups and moved to the other side of the drink selection."
        a "I'll get the two Hilly Dews."
        c sad "Thanks."
        a "No problem."
        "I placed one cup under the correct spot and started filling it while Christeena started filling up her sweet tea."
        a "Man, you really like your tea, don't you?"
        c p2 raised "Eh. It's more of a 'special occasion' drink."
        a "I wasn't aware that a baseball game warranted as a 'special occasion'."
        c mad "That's not what I meant."
        c p1 casual "I can have pop all the time when I'm at home, so when I go out, I like to shake it up a bit, you know?"
        a "Yeah, I guess that makes sense."
        a "Honestly, I get the same way on occa--"
        a "GAH!"
        "I suddenly felt my hand getting wet."
        show chris sad dot
        "I turned and saw that my cup was overflowing!"
        "Christeena grabbed a couple napkins and handed them to me."
        "After thanking her and wiping my hands, I looked at the cup; the bubbles were going down."
        "Once they went down completely, I saw it was only about three-quarters of the way full."
        $ c_blush = True
        c sad blank "S-Sorry for distracting you like that."
        a "Chris, it's okay, really. I should've been paying attention."
        c right "Still..."
        a "Christeena, you're fine, I promise."
        "I gave her a quick pat on the shoulder, as if that would magically fix everything."
        c_s straight grin "..."
        "Huh. Maybe it did."
        if pond_scene == "Christeena":
            c left "I still can't believe that you're still so nice to me like this..."
            a "Is it really that hard to believe that a guy can be nice to a girl?"
            c straight blank "Well, I..."
            c right "I've just... never really had anyone treat me that way after getting to know me."
            a "You say that like everyone is mean to you."
            c straight casual p2 "Well, that's not what I mean."
            c sad grin "I mean that you go out of your way to spend time with me and make me feel happy."
            c right p1 "I've never had that before."
            a_s "..."
            "I'm a bit unsure on how to respond to that..."
            "I knew Christeena was an introvert and that her sister and Donald were essentially her only friends, but hearing her say that..."
            a "Well, you've got it now."
            "I replied with a smile."
            c straight "Yeah..."
            d "Hey, less talk, more fill!"
            show chris casual blank:
                ease 0.5 xalign 0.1
            show don p1 straight raised smile at tworight with easeinright
            pause 0.1
            "We turned to see Donald nearby with two bags of potato chips in his hands."
            a "S-Sorry."
            c_s sad blank "..."
            "And once again, a moment is ruined."
            "Oh, well. I'm sure we'll get another chance."
            scene bg conveniencestore with dissolve
            pause 0.1
        else:
            c left "A-Anyway, let's finish filling up the drinks."
            a "Yeah, good idea."
            hide chris with dissolve
            pause 0.1
        $ c_blush = False
        "And just like that, we finished filling up the cups in silence."
        "Two Hilly Dews, a sweet tea, a Dr. P, and a water."
        if pond_scene != "Christeena":
            "I saw Donald walk over to the counter with two bags of chips before turning towards us and saw us struggling to carry all the cups."
            "He placed the bags on the counter and came over to help us out."

    label payfordrinks:
        "We all made our way to the counter, where the woman scanned the chips."
        "She was about to add the drinks before Christeena interrupted and told her they were separate."
        "Donald just chuckled and informed the woman that she could add the drinks."
        show chris p1 casual straight dot at tworight
        show don p1 straight casual grin at twoleft
        with dissolve
        pause 0.1
        c "Wait, Donald, are you paying for it ALL?"
        d sad "Yeah, might as well. Seems like the right thing to do."
        c_s sad blank "..."
        c p2 raised grin "Well, in that case, you won't mind if I add this beef jerky?"
        d level smile "I most certainly do mind, actually."
        scene bg conveniencestore with dissolve
        pause 0.1
        "With that, Donald hung the plastic bag full of chips on his arm and we split up the drinks as evenly as possible, with Don and I each carrying two while Chris carried her own."
        "We were then on our way back to the ballpark."
        window hide dissolve
        pause 0.5
        scene bg fade with wipeleft
        scene bg baseball
        show baseball_overlay zorder 2
        with wipeleft
        pause 0.5
        window show dissolve
        pause 0.1
        jump gamestart

label stayhere:
    $ B_Points += 1
    a "You guys can go on ahead. I'd probably just slow you down."
    d blank "You sure?"
    a "Yeah, it's fine."
    c_s sad "..."
    d level grin "Alright, then."
    d right casual "C'mon, Chris."
    c_s "..."
    hide don
    hide chris
    hide martha
    with dissolve
    pause 0.1
    $ m_partial = False
    "With that, we all verified what drinks everyone wanted, and Donald and Christeena were on their way."
    show martha p1 straight casual grin at close_m zorder 3 with dissolve
    pause 0.1
    a_s "..."
    mu sad_s "..."
    "Mrs. Truman and I just looked at each other awkwardly before turning back to the field."
    "So far, so good..."
    hide martha with dissolve
    pause 0.1
    "I saw Brittney and a teammate throwing a ball back and forth by the dugout."
    "They had a pretty decent distance between them; maybe about 10 feet?"
    "Brit really looked like she was completely focused on the ball and her teammate, as if nothing else around her existed."
    "I couldn't help but notice that she was able to throw the ball pretty quickly; her teammate almost missed a few times."
    if persistent.choices["25"] == 1:
        "It felt very reminiscent to our bags game at Donald's birthday party."
    "I then turned to Mrs. Truman; I think I finally found a good conversation starter."
    show martha p1 straight casual blank at close_m zorder 3 with dissolve
    pause 0.1
    a "So, is Brittney a pitcher for the team? She looks like she has a good arm for it."
    mu sad grin "No, she's more of an outfielder."
    mu casual smile "That arm of hers has gotten the ball back to the bases quickly on numerous occasions! Her quick throwing has even spared us from losing a few times!"
    a "Dang! That's impressive!"
    mu sad grin "Mhm!"
    a "Does she have any interest in being a pitcher?"
    mu level "Not really; she works better when she has a general area to throw to rather than a confined space."
    mu sad "I love the girl to death, but if she pitched, she'd walk so many players."
    a "I see."
    "I turned back to Brittney. While she was waiting for her teammate to throw the ball back, she was reaching her right arm in the air, as if to stretch it out."
    "Finally, she lowered and shook it before slightly squatting down before having the ball thrown to her."
    "She then reached up and caught it, a loud SMACK being heard as the ball made contact with the glove."
    mu mad smile "Nice catch, Brittney!"
    "Upon hearing her mother's voice, Brittney turned to the bleachers with a smile."
    a "Yeah, that was good, Brit!"
    "After giving a quick nod, she turned back to her teammate, the smile going away and her eyebrows furrowing in focus."
    a "It's kinda funny."
    a "She usually acts so carefree, but here, she's so in focus, it's like she's a different person."
    mu casual grin "Yes, she's always had a knack for having selective focus."
    mu sad "Unfortunately, that's one of the traits she got from her mother..."
    a "I'm gonna take a wild guess and say that her athleticism was another trait she got from you?"
    mu mad smile "Okay, now you're just trying to be funny."
    a "Hey, you never know! Maybe you were a state champion back in the day!"
    mu level grin "Ahaha. Oh, I wish."
    mu "Nah, I was the theatre geek."
    mu sad "It was pretty much the only thing I did in high school that I don't regret."
    mu "Well, you know, besides meeting Brittney's father..."
    a_s "..."
    a "Uh..."
    mu casual "There's no need to feel awkward about it, Alex."
    mu sad "I'm far past the point where talking about him makes me start bawling my eyes out."
    a "Y-Yeah, sorry. I just wasn't really sure what to say to that."
    mu level "It's fine, really."
    "Still feeling a bit awkward, I change the subject."
    a "So, anyway, you said those were the only things you don't regret in high school?"
    mu sad "Yes, unfortunately, Brittney also got her mother's wild side."
    a "You don't seem like the partying type."
    $ m_partial = True
    mu raised "Yet I look like a state champion athlete?"
    a "Heh. Touché."
    $ m_partial = False
    mu "Besides, I wouldn't necessarily say I was a 'party' kind of person."
    mu casual smile "I was more like how Brittney is now: loud, random, carefree, all that jazz."
    a "So, she truly is her mother's daughter?"
    mu sad grin "Essentially."
    mu blank "Which can be a blessing and a curse."
    a "How so?"
    mu grin "Well, like I said, I love the girl to death, and I'll never regret giving birth to her."
    mu "...but..."
    mu "Well, I had her just a little earlier than I would've liked."
    mu "...well, a LOT earlier."
    a "I see."
    "Now that she mentioned it, Mrs. Truman does seem relatively young compared to my mom and Mrs. Waters, despite having the oldest child of the three."
    "I hadn't really thought much of it, to be honest, but I suppose that answers a question I hadn't even really thought to ask."
    mu blank "So, I guess my big worry is that Brittney will follow my footsteps just a little TOO well, if you catch my drift."
    mu "After all, not all men are like John and will stick around..."
    a_s "..."
    mu_s "..."
    "I have no idea how a conversation about Brittney's throwing abilities came to this, but here we are."
    mu grin "S-Sorry. Didn't mean to spill my life story onto ya like that."
    a "Nah, you're fine, Mrs. Truman."
    mu level "Please, 'Martha' is fine."

    if persistent.choices["32"] == 1:
        jump callhermrstruman
    elif persistent.choices["32"] == 2:
        jump callhermartha
    else:
        menu:
            "Call her Mrs. Truman":
                $ persistent.choices["32"] = 1
                jump callhermrstruman
            "Call her Martha":
                $ persistent.choices["32"] = 2
                jump callhermartha

    label callhermrstruman:
        a "Sorry, but 'Mrs. Truman' just feels right to me."
        mu raised "Heh. You truly are a friend of Donald's, aren't ya?"
        a "Took you that long to figure it out?"
        jump donandchrisreturn

    label callhermartha:
        $ M_Name = "Martha"
        $ marthatruman = True
        a "Alright, then, if you say so, Martha."

    label donandchrisreturn:
        hide martha with dissolve
        pause 0.1
        "[M_Name] and I then spent some time watching the girls warm up."
        "Throwing, catching, batting, you name it; they were not only doing it, but they were doing it well."
        "We must've been watching longer than we thought, because before I knew it, I looked and saw some familiar faces come our way, each with their hands full."
        show don p1 straight casual grin at twoleft zorder 3
        show chris p1 straight casual grin at tworight zorder 3
        with dissolve
        pause 0.1
        d smile "Alright, here we are!"
        "Donald carefully climbed up the bleachers while balancing the 4 large Styrofoam cups in the cardboard cup-holding tray."
        "He also had a plastic bag hanging off his arm. It didn't seem very full."
        "Christeena, meanwhile, had only one cup that she was carrying in both hands."
        "Still, they managed to get up the shallow stairs fairly easily."
        show don:
            ease 1.0 close_left_d
        show chris:
            ease 1.0 close_right_c
        pause 1.1
        d level grin "Alright, since Chris was kind enough to take only her own drink..."
        c_s level blank "..."
        d casual "...that means we can sort out our own drinks from here."
        a "What's in the bag?"
        "Donald replied by pulling out a bag of potato chips."
        d smile "I decided to grab a couple of bags for us to munch on."
        d sad right grin "Oh, and here you are, Mrs. T!"
        "Donald then handed her a $10 bill from his pocket."
        show don:
            ease 0.5 xalign 0.0
        show chris:
            ease 0.5 xalign 1.0
        show martha p1 straight sad blank at m_middle zorder 3 with dissolve
        pause 0.1
        mu "Oh, Donald, you didn't have to pay for everything!"
        $d_blink = False
        d closed "I know~"
        mu level grin "..."
        mu sad "Well, thank you."
        hide don
        hide chris
        hide martha
        with dissolve
        pause 0.1

label gamestart:
    $ m_partial = False
    $d_blink = True
    "So, after Donald gave [M_Name] her money back and each of us received our drink, we all sat and chatted until Mr. Truman arrived."
    show martha p1 straight sad blank at m_tworight zorder 3
    show chad p1 straight grin sad at twoleft zorder 3
    with dissolve
    pause 0.1
    mu "Chad, couldn't you have washed up just a little bit before coming over?"
    ct "Sorry; I got off later than I wanted and didn't wanna end up being late to the game!"
    ct left "Doesn't look like I missed much, though."
    show chad at threeleft
    show martha at m_middle
    show don p1 straight smile raised at threeright zorder 3
    with easeinright
    pause 0.1
    d "I mean, unless you wanted to sit and watch the warm-ups."
    ct straight raised "I mean, with the competitiveness in these girls, even that can be enjoyable."
    $d_blink = False
    d closed sad grin "True."
    mu grin "Well, at least you came, I suppose; that's all that Brittney will care about."
    ct casual "Speaking of..."
    "He looked behind us and waved."
    "We turned to see Brittney waving back and jogging over to us."
    hide don
    hide martha
    with dissolve
    $d_blink = True
    show chad:
        ease 0.5 twoleft
    show brit p1 straight sad opened_smile at tworight zorder 3 with easeinright
    pause 0.1
    b "I was starting to get worried you were gonna be a no-show!"
    ct raised "And miss out on the best ball player in Smalltown smoking the Titans? Not a chance!"
    b p2 mad grin "Ha! They won't know what hit them!"
    show chad at threeleft
    show brit at middle
    show martha p1 sad grin straight at m_threeright zorder 3
    with easeinright
    pause 0.1
    mu "Alright, don't get too cocky, Brittney."
    ct sad "Relax, Martha. It's all in good fun."
    $b_wink = True
    b tongue raised "Yeah, totally, Mom!"
    mu "Ahaha..."
    "Girl" "\"Hey, Brittney!\""
    $b_wink = False
    show brit casual blank
    "Brittney then turned around and looked at a teammate standing behind the fence."
    "Girl" "\"Coach wants us all in the dugout!\""
    b p1 opened_smile "Alright, I'll be right there!"
    "She then turned back towards us."
    b p2 sad grin "See you guys later, then!"
    mu "Good luck, Brittney!"
    ct mad "You got this, Brit!"
    ct "Go out and kick some ass!"
    show martha level blank
    b_s level blank "..."
    $b_partial = True
    show brit raised huhu
    "Brittney then looked at her mother with a smug expression."
    mu_s grin "..."
    mu "Fine. You win."
    mu raised "For this game only, everyone's allowed to swear."
    $b_partial = False
    b p1 mad closed_smile "Fuck yeah!"
    mu mad blank "Don't.{w=0.5} Push it."
    $b_wink = True
    b level tongue "{cps=15}Fiiiiine.{/cps}"
    hide chad
    hide martha
    hide brit
    with dissolve
    pause 0.1
    $b_wink = False
    "After we all gave our wishes of good luck, Brittney jogged back towards the dugout."
    "About five minutes later, the game was on."
    window hide dissolve
    scene bg fade with wipeleft
    pause 1.0
    scene bg baseball
    show baseball_overlay zorder 2
    with wipeleft
    window show dissolve
    pause 0.1
    "As far as Brittney goes, she did a good job catching and throwing in the first half of the inning."
    "Not perfect, as she did manage to miss her teammate's glove or throw too late, but she was responsible for 2 of the outs."
    if persistent.choices["31"] == 2:
        "Though with the second half of the inning starting, I realized that [M_Name] and I never talked about her daughter's batting abilities."
    else:
        "Though with the second half of the inning starting, I realized that I hadn't heard anything about her batting abilities."
    "I guess I wasn't really paying too much attention to her when the Saints were practicing that part."
    "Then again, with the chatting amongst us in the bleachers, I don't think any of us were."
    "Though when she walked up to the plate, I was given my chance to see just how good she was."
    show bg baseball:
        xalign 0.5 yalign 0.5
        parallel:
            ease 0.5 zoom 1.25
        parallel:
            ease 0.5 xalign 0.6 yalign 0.3
    show baseball_overlay:
        xalign 0.5 yalign 0.5
        parallel:
            ease 0.5 zoom 1.25
        parallel:
            ease 0.5 xalign 0.6 yalign 0.3
        parallel:
            ease 0.5 alpha 0.0
    pause 0.6
    $b_hat = 2
    show brit p1 straight level blank at close_b with dissolve
    pause 0.1
    "She had that signature determined look on her face as she did a couple of practice swings before taking her stance."
    "The pitcher was still for a few seconds before winding up."
    "..."
    play sound woosh
    "She threw the ball."
    show brit:
        ease 0.2 xalign 0.6
        ease 0.2 xalign 0.5
    "Brittney swung."
    ump "Strike!"
    show brit mad
    "Brittney looked slightly annoyed as some groans of disappointment arose from the crowd."
    "After the ball was thrown back to the pitcher, Brittney took a few more practice swings."
    show brit level
    "..."
    play sound woosh
    pause 1.5
    ump "Strike 2!"
    "That time, Brittney didn't even swing."
    show brit:
        ease 0.5 close_right_b
    show martha p1 sad straight blank at m_twoleft with dissolve
    pause 0.1
    mu "C'mon, Brit! You got this!"
    show brit:
        ease 0.5 close_b
    hide martha with dissolve
    pause 0.1
    "One final chance."
    "Brittney took a deep breath, focused on the pitcher, and stood completely still."
    $current_track = "None"
    stop music fadeout(3.0)
    "The entire crowd was silent."
    window hide dissolve
    pause 2.0
    play sound woosh
    pause 0.5
    show brit:
        ease 0.2 xalign 0.6
        ease 0.2 xalign 0.5
    pause 1.0
    window show dissolve
    pause 0.1
    ump "Strike 3!"
    show brit p2 sad
    "More groans from the crowd, as well as some applause."
    "Though it's hard to tell how many of them were clapping out of pity and how many were clapping because they were from Trenburg."
    hide brit with dissolve
    pause 0.1
    "Regardless, Brittney took a deep sigh before walking back to the dugout."
    "Fortunately, the next girl up to bat gave her a high-five and a smile on her way to the plate."
    "I leaned in towards Christeena and Donald."
    show bg baseball:
        parallel:
            ease 0.5 zoom 1.0
        parallel:
            ease 0.5 xalign 0.5 yalign 0.5
    show baseball_overlay:
        parallel:
            ease 0.5 zoom 1.0
        parallel:
            ease 0.5 xalign 0.5 yalign 0.5
        parallel:
            ease 0.5 alpha 1.0
    pause 0.6
    $current_track = "\"Outside the Street\""
    play music outside_the_street
    show don p1 straight casual blank at close_left_d zorder 3
    show chris p1 straight casual blank at close_right_c zorder 3
    with dissolve
    pause 0.1
    a "So, I'm assuming batting isn't her specialty?"
    d sad grin "It's pretty hit-or-miss."
    d level right "..."
    d "...{fast}no pun intended."
    c sad grin "Yeah, she's way better on the field than she is at the bat."
    c p2 smile casual "Though she still has her moments of contact."
    c "It's mostly just enough to get her on first base, but she's had her share of home runs, as well."
    $d_blink = False
    d closed sad "Basically, she either misses or hits a good one. No in-between."
    a "Gotcha."
    hide don
    hide chris
    with dissolve
    pause 0.1
    $d_blink = True
    "With that, we turned our attention back to the game."
    window hide dissolve
    pause 0.5
    scene bg fade with wipeleft
    pause 1.0
    scene bg baseball
    show baseball_overlay zorder 2
    with wipeleft
    window show dissolve
    pause 0.1
    "The 5th inning ended."
    call newgame
    return
