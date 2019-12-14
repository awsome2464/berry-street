label tour:
    python:
        B_Name = "Brittney"
        b_hat = 1
        outfit_b = "a"
        outfit_d = "a"
    show text "{size=+50}June, 2013{/size}":
        xalign 0.5 yalign 0.05
    show screen calendarOs
    show calendar june june_04:
        xalign 0.5 yalign 0.6
    show calendar_circle:
        xalign 0.435 yalign 0.41
    with dissolve
    if replay == False:
        $ persistent.todays_date = "June 4th, 2013"
        $ renpy.notify("Game saved!")
        $ renpy.save("1-1")
    $renpy.pause(delay=4)
    hide text
    hide screen calendarOs
    hide calendar
    hide calendar_circle
    with dissolve
    pause 1
    scene bg bedroom_a_m with dissolve
    window show dissolve
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    $ renpy.block_rollback()
    "I opened my eyes and saw sunlight pouring in through the window."
    "I gave a yawn and rubbed my eyes."
    "Looks like the first night in my new home was a success!"
    "I took out my phone and looked at the clock."
    "9:34 AM"
    "Well, at least I didn't sleep in too late."
    play loop phone_vibrate_call
    "Suddenly, I was receiving a phone call."
    "My eyes were still waking up, but it looked like it was from Donald."
    "I yawned again and answered the phone."
    stop loop
    a "Hello?"
    d_o "{font=fonts/LemonMilk.otf}{i}Morning, Sunshine!{/i}{/font}"
    a "Donald, why are you calling me this early?"
    d_o "{font=fonts/LemonMilk.otf}{i}Well, we gotta give you a tour of the town sooner or later, so we decided sooner!{/i}{/font}"
    a "'We?'"
    d_o "{font=fonts/LemonMilk.otf}{i}Just get ready and head over to Brittney's house; I'll meet you guys there soon enough.{/i}{/font}"
    "I gave another yawn and rubbed my eyes."
    a "Alright, whatever you say, man."
    d_o "{font=fonts/LemonMilk.otf}{i}Good deal! See ya soon!{/i}{/font}"
    a "See ya soon."
    "Donald then hung up, and I put my phone away."
    "Well, I guess it's time for me to see how well the shower works."
    window hide dissolve
    scene bg fade with wipeleft
    scene bg house_ut with wipeleft
    window show dissolve
    "I told Mom I was hanging out with Donald, and she simply said to have fun and not to be out too late."
    "I walked over to the house next door, the one belonging to Brittney Usher, and went onto the porch."
    "I don't know why we had to meet here, but who am I to question the Great Donald Waters?"
    scene bg porch_ut
    with dissolve
    play sound door_knock
    "I knocked on the door and waited."
    "..."
    play sound door_open
    "A few seconds later, the door opened up."
    $ current_track = "None"
    stop music fadeout 2.5
    "I was expecting to see Brittney, but I was quite surprised to see..."
    window hide dissolve
    pause 0.5
    show chris p2 straight casual blank at middle with dissolve
    pause 1
    window show dissolve
    "...well, NOT Brittney."
    $ current_track = "\"Violet Wonder\""
    play music violet_wonder
    "It was a girl about my age, a little bit shorter than me and certainly shorter than Donald."
    "Despite her height, she certainly seemed rather big."
    "Not necessarily 'fat', but she certainly had some thickness and chubbiness to her."
    "Of course, saying that aloud would most likely result in me going down a path I don't want to go down."
    "Although something about her eyes were quite...{w} What's the right word? Mesmerizing?"
    a "Uh..."
    a "Hello."
    a "I'm looking for Brittney."
    c_s dot "..."
    "She then turned towards the interior of the house."
    c up hanging raised "Hey, Brittney!"
    b_o "Yeah?"
    c "Some guy's here to see you!"
    b_o "Oh! Is he tall, blonde, and wearing glasses?"
    show chris straight casual blank
    "She looked back at me, ran her eyes up and down, and turned back to the house."
    c up hanging raised "Yes!"
    b_o "Cool! Tell him I'll be down in a minute!"
    show chris straight casual blank
    "The girl turned back to me."
    c "She said-"
    a "Thank you, but I'm not deaf."
    $ c_blush = True
    c sad grin "Oh, right.{w=0.5} Of course."
    $ c_blush = False
    show chris p1 straight casual grin at middle
    c "Anyway, would you like to come in?"
    a "If you insist."
    hide chris with dissolve
    pause 0.1
    "I then entered the house."
    scene bg living_ut with dissolve
    "My hostess gestured to the couch, an offer I politely accepted."
    a "Man, this couch is comfy!"
    show chris p1 raised grin straight at close_c with dissolve
    pause 0.1
    c "I know, right? I could sit on it all day!"
    a "You and me both!"
    $c_blink = False
    show chris smile closed_happy sad
    "We both then laughed and sighed."
    $c_blink = True
    c straight p2 casual grin "So, if I'm going to be letting you in my house, I suppose I should at least know your name."
    a "Oh, right."
    a "I'm Alex Sprouse. I just moved into the house next door."
    c sad p1 "I should've guessed."
    c level left "Brittney had mentioned meeting our new neighbor. Something about him being Donald's old friend."
    a "Yes, that would be me."
    a "So are you Brittney's sister, I assume?"
    $c_blink = False
    c p2 closed_happy sad smile "Yep!"
    $c_blink = True
    c straight casual grin "I'm Christeena Truman, Brittney's younger sister."
    $ C_Name = "Christeena"
    c "That's Christeena with two 'e's."
    a_s "..."
    $ c_blush = True
    c p1 left sad "Yeah, I know that's not how it's normally spelled, but-"
    a "Oh, that's not why I'm confused."
    a "You said your last name is Truman?"
    $ c_blush = False
    show chris p1 straight casual blank at close_c
    c "Yeah. Why?"
    a "I thought Brittney said her last name was Usher."
    c small sad dot "Oh, right! {w}Sorry, I should've clarified."
    c p2 straight casual grin "I'm Brittney's STEP sister!"
    a "Oh! That makes more sense."
    $c_blink = False
    c p1 closed_happy sad smile "Yeah, my dad married Brittney's mom around 5 years ago, though we all lived together for a little while before that."
    $c_blink = True
    $ c_blush = True
    c p2 left grin "When you spend so long calling yourself sisters, you sometimes forget that you're not blood relatives."
    $ c_blush = False
    show chris p2 straight casual blank at close_c
    c "Although, you still do get some constant reminders."
    a "Such as...?"
    c level "Well, physically, we look different, of course."
    c right "I mean, she's tall, thin, blonde, pretty..."
    c "And then you have..."
    "She then pointed at herself with her thumbs."
    $ choicevbox = 3
    c p1 sad straight "...NOT that."
    hide screen skipchoice
    if persistent.choices["4"] == 1:
        jump theyreopposite
    elif persistent.choices["4"] == 2:
        jump christeenaspretty
    elif persistent.choices["4"] == 3:
        jump britisntpretty
    else:
        menu:
            a "..."

            "Yeah, you are pretty opposite.":
                $ persistent.choices["4"] = 1
                jump theyreopposite

            "I think you're pretty, too.":
                $ persistent.choices["4"] = 2
                jump christeenaspretty

            "Brittney isn't pretty.":
                $ persistent.choices["4"] = 3
                jump britisntpretty

label theyreopposite:
    a "I suppose you two do look pretty different."
    c p2 left grin "Yeah..."
    jump waitingforbrit

label christeenaspretty:
    $ C_Points += 1
    a "Hey, now; I think you look pretty, too!"
    c_s small casual dot "...!"
    $ c_blush = True
    c p2 right sad blank "Well, uh, thank you, but I know you're just saying that to be nice."
    a "No, I wasn't."
    c straight "If you say so..."
    jump waitingforbrit

label britisntpretty:
    $ britnotpretty = True
    $ C_Points -= 1
    a "Well, to be fair, Brittney isn't that pretty, so I don't think you have anything to worry about."
    c casual dot "Eh?"
    c_s p2 left mad blank "..."
    a_s "..."
    "I have a feeling I accidentally insulted both sisters at once."

label waitingforbrit:
    $ choicevbox = 1
    hide chris with dissolve
    pause 0.1
    $ c_blush = False
    "We could then hear footsteps on the staircase."
    "We looked and saw Brittney coming down while pulling her ponytail through her baseball cap."
    show chris p1 straight grin casual at twoleft with dissolve
    show brit p1 straight casual grin at tworight with easeinright
    pause 0.1
    b "Hello, Alex!"
    b p2 left "I see you've met my sister from another mister, Christeena."
    a "Yes, I have, indeed."
    b straight mad opened_smile "I hope you don't think she's too weird."
    c level blank "Brittney...!"
    a "Honestly, the only weird thing about her is how her name is spelled; never seen it with two e's before."
    $c_blink = False
    c closed_happy sad smile "Yeah, that's because that's how my dad thought it was normally spelled, believe it or not."
    $c_blink = True
    c p2 mad straight grin "But I think it makes me a little bit unique."
    a "That's one way of putting it."
    hide brit
    hide chris
    with dissolve
    $ current_track = "\"Ivories and Ebony\""
    play music ivories_and_ebony
    play sound door_open
    "The front door then opened up, revealing Donald strutting in like it's his own house."
    show brit p1 straight casual grin at threeright
    show chris p2 straight casual dot at middle
    with dissolve
    show don p1 straight casual smile at threeleft with easeinleft
    d "Hello, everybody!"
    c p1 grin "Hi, Donald!"
    b p2 raised "Sup?"
    a "Hey, man!"
    d raised grin "Anything exciting happen while I was gone?"
    b p1 casual "Not much; just Alex and Christeena meeting each other."
    d level right grin "I can only imagine how well that went."
    c level blank "...what's that supposed to mean?"
    d straight sad grin "Nevermind."
    b raised opened_smile "Anyway, shall we head out?"
    d casual smile "If you and Al are ready, sure!"
    d "We've got a lot to show our new neighbor."
    c casual dot "Wait, 'you and Al'?"
    d grin "Yeah, Brittney and I were going to-{nw}"
    b p2 casual left grin "Do you wanna come with us, Christeena?"
    c p2 smile "Sure!"
    c "It beats being home alone."
    a "Where are your parents?"
    c p1 grin "Work."
    c "Dad works at an auto-repair garage, and Mom works at a local deli."
    a "I swear, parents here are never around."
    $c_blink = False
    c closed_happy sad smile "Yeah, it is awfully convenient, isn't it?"
    $c_blink = True
    d blank level right "Well, are you sure you're fine with walking around town all day?"
    c straight casual dot "Walking?"
    d raised grin "Well, it's a nice day, and there's no need to burn gas if we don't have to."
    c p2 left mad blank "In that case, I'll pa{nw}"
    b p1 straight mad opened_smile "Ah ah ah! No take-backs, Missy!"
    c straight "Hmph."
    d straight casual grin "Don't worry, it shouldn't take THAT long."
    d raised "After all, the name 'Smalltown' wasn't just pulled from thin air."
    c p1 casual grin "Very true, though I personally don't often go that far outside of Berry Street."
    c right sad "Well, besides a local restaurant. And school, of course."
    b p2 blank "Christeena, it's June. Any and all mentions of school should be avoided until August."
    c p2 straight mad blank "I was just saying!"
    hide brit
    hide chris
    with dissolve
    show don at middle with easeinleft
    pause 0.1
    d smile "Anyway, let's start our tour, shall we?"
    d grin "Here's a list."
    d raised "We don't need to see EVERYTHING in town, but I've marked all the stuff that's most important."
    d casual smile "We've got all morning, so feel free to backtrack as much as you like!"
    hide don
    show chris p2 left mad blank at middle
    with dissolve
    c "Ugh..."
    show chris at twoleft
    show brit p2 huhu left level at tworight
    with easeinright
    b "C'mon, some exercise never killed anyone."
    if persistent.tour_1 == 0:
        hide chris
        hide brit
        show don p1 straight casual grin at middle
        with dissolve
        d "Where should we go first?"

label tourtown:
    if tour_town == 0:
        if persistent.tour["1"] == 1:
            jump tourberrystreet
        elif persistent.tour["1"] == 2:
            jump tourpond 
        elif persistent.tour["1"] == 3:
            jump tourdowntown
        elif persistent.tour["1"] == 4:
            jump tourschool
    elif tour_town == 1:
        if persistent.tour["2"] == 1:
            jump tourberrystreet
        elif persistent.tour["2"] == 2:
            jump tourpond 
        elif persistent.tour["2"] == 3:
            jump tourdowntown
        elif persistent.tour["2"] == 4:
            jump tourschool
    elif tour_town == 2:
        if persistent.tour["3"] == 1:
            jump tourberrystreet
        elif persistent.tour["3"] == 2:
            jump tourpond 
        elif persistent.tour["3"] == 3:
            jump tourdowntown
        elif persistent.tour["3"] == 4:
            jump tourschool
    elif tour_town == 3:
        if persistent.tour["4"] == 1:
            jump tourberrystreet
        elif persistent.tour["4"] == 2:
            jump tourpond 
        elif persistent.tour["4"] == 3:
            jump tourdowntown
        elif persistent.tour["4"] == 4:
            jump tourschool
    elif tour_town == 4:
        jump tourcomplete
    menu:
        "Berry Street" if tour_berrystreet == False:
            jump tourberrystreet
        "Pond" if tour_pond == False:
            jump tourpond
        "Downtown" if tour_downtown == False:
            jump tourdowntown
        "School" if tour_school == False:
            jump tourschool


label tourberrystreet:
    if persistent.tour["1"] == 0:
        $persistent.tour["1"] = 1
    elif persistent.tour["2"] == 0:
        $persistent.tour["2"] = 1
    elif persistent.tour["3"] == 0:
        $persistent.tour["3"] = 1
    elif persistent.tour["4"] == 0:
        $persistent.tour["4"] = 1

    scene bg bs with dissolve
    $ current_track = "\"Welcome to Berry Street!\""
    play music main_theme
    show don p1 straight casual smile at middle with dissolve
    pause 0.1
    d "Welcome to your new home: Berry Street!"
    d raised grin left "To be honest, most of the people you'll realistically interact with on a regular basis are already here with you."
    d straight sad "Still, it doesn't hurt to know more about your neighbors!"
    show don at tworight
    show brit p1 raised straight closed_smile at twoleft
    with easeinleft
    pause 0.1
    b "Until they call the cops on you for stalking them."
    d mad wide "That only happened once!"
    d right level blank "And I wasn't 'stalking'..."
    hide brit
    show don at middle
    with easeoutleft
    pause 0.1
    d straight raised grin "So, anyway, let's check out house number one!"
    hide don with dissolve
    pause 0.1
    window hide dissolve
    scene bg house_ro
    with pushleft
    window show dissolve
    show don p1 straight casual grin at middle with dissolve
    pause 0.1
    d "Right there is Mr. and Mrs. Rodriguez."
    d "They immigrated here from Mexico about 10 years ago."
    show don at twoleft
    show brit p2 straight casual grin at tworight
    with easeinright
    pause 0.1
    b "And honestly, their English is so good, I would've never guessed they weren't originally from here!"
    a "What brought them from Mexico to Smalltown?"
    hide don
    hide brit
    show chris p1 straight casual blank at middle
    with dissolve
    pause 0.1
    c "I think it was something about Mr. Rodriguez knowing a guy who knew a guy, or something similar."
    c p2 grin "He works with my dad. Very nice guy."
    hide chris
    show brit p1 raised straight opened_smile at middle
    with dissolve
    pause 0.1
    b "And Mrs. R makes the BEST cookies you'll ever taste!"
    b p2 left casual grin "She gives them to Trick or Treaters on Halloween; it's honestly the only reason anyone comes to Berry Street during that time."
    hide brit
    show don p1 straight raised smile at middle
    with dissolve
    pause 0.1
    d "But we can't forget about their son, Daniel."
    $c_blink = False
    hide don
    show chris p1 closed_happy sad smile at middle
    with dissolve
    pause 0.1
    c "Oh, he is so cute!"
    $c_blink = True
    c p2 straight casual grin "He's only 9, and he's the nicest kid I've ever met!"
    show chris at twoleft
    show brit p2 straight casual grin at tworight
    with easeinright
    pause 0.1
    b "Yeah, I'll admit he makes the wait for the bus pretty enjoyable."
    b "So full of energy, but not to the point where it's annoying."
    hide chris
    hide brit
    show don p1 straight casual grin at middle
    with dissolve
    pause 0.1
    d "You like kids, right, Alex?"
    a "Only when they're not little pains in the neck."
    $d_blink = False
    d closed sad smile "Then you shouldn't have any issues with Daniel!"
    a "So, quick question:"
    $d_blink = True
    show don straight casual blank
    a "You said they moved here about 10 years ago..."
    a "...and that their son is 9...?"
    $b_blink = False
    hide don
    show brit p2 closed sad closed_smile at middle
    with dissolve
    pause 0.1
    b "Hehehe."
    $b_blink = True
    $ b_partial = True
    b straight huhu raised "Hehehe.{fast} Let's just say they celebrated their immigration the right way."
    hide brit
    show don p1 raised straight grin at middle
    with dissolve
    pause .1
    $ b_partial = False
    d "Alright, then; moving on."
    hide don with dissolve
    pause 0.1
    window hide dissolve
    scene bg house_z with pushright
    window show dissolve
    show don p1 straight casual grin at middle with dissolve
    pause .1
    d "Next up, we have the home of Anna Ziphon."
    d mad blank right "She would be the neighbor Brittney was referring to earlier."
    d straight "You know, the one that called the cops on me?"
    d level "Honestly, she's kinda reclusive; she hardly ever leaves the house."
    a "Why's that?"
    show don at twoleft
    show brit p1 straight blank casual at tworight
    with easeinright
    pause 0.1
    b "She's a scientist that's always conducting experiments in her lab."
    a "Seriously?"
    $c_blink = False
    show don at threeleft
    show brit at middle
    show chris p1 closed_happy sad smile at threeright
    with easeinright
    pause 0.1
    c "I know it sounds crazy, but we're serious!"
    $c_blink = True
    c p2 straight blank casual "Apparently, she was a government worker or something, but left to work independently, creating all sorts of stuff to try and help the world."
    a "Sounds like quite a nice person."
    $b_blink = False
    $c_blink = False
    $d_blink = False
    show don closed sad smile
    show brit p2 closed sad opened_smile
    show chris p1 closed_happy sad smile
    "They all started laughing like I had told a joke."
    show don:
        ease 0.5 offscreenleft
    show chris:
        ease 0.5 offscreenright
    pause 0.6
    $b_blink = True
    $c_blink = True
    $d_blink = True
    show brit p1 raised straight grin at middle
    b "Oh, you think that now, but if you ever find yourself face-to-face with her, you'll be crapping your pants."
    a "Huh?"
    hide brit
    show don p1 blank level straight at middle
    with dissolve
    pause 0.1
    d "She's, to put it simply, intimidating."
    d left "Her blank, emotionless expressions and her empty, monotone voice just makes you feel like you're talking to a machine."
    hide don
    show brit p2 left level grin at middle
    with dissolve
    pause 0.1
    b "In fact, there are a lot of people in town that think she IS a machine, some sort of artificial intelligence robot on the lam."
    b p1 straight casual "There are also rumors of her being fine with sacrificing human lives if it can help progress her research."
    b p2 level "So, basically, try and avoid any and all interaction with her, or you may regret it."
    a "...okay, then..."
    hide brit with dissolve
    pause 0.1
    "What the hell kind of neighborhood is this...?"
    window hide dissolve
    scene bg house_re with pushright
    window show dissolve
    show don p1 straight casual grin at middle with dissolve
    d "Up next is the Reagan household."
    $d_blink = False
    d closed sad "And no, there is no biological relation to the former president; it's just a stage name."
    a "'Stage name?'"
    hide don
    show brit p2 straight casual opened_smile at middle
    with dissolve
    pause .1
    $d_blink = True
    b "The Reagans are a cover band."
    b grin raised "They'll basically perform any song they've practiced enough times, but they mostly prefer songs from the 80s, hence the name."
    b left level "There's Percy, the lead singer, Nicole, the backup singer, James, the keyboardist, Karrie, the drummer, and Mike, the guitarist."
    b straight raised "Rock, pop, rap, you name it. If it's a song that exists, they'll perform it."
    a "They any good?"
    hide brit
    show chris p2 straight grin casual at middle
    with dissolve
    pause 0.1
    c "I personally think Percy does a good George Michael."
    c left level dot "His Michael Jackson could use some work, though."
    show chris at tworight
    show don p1 raised straight grin at twoleft
    with easeinleft
    pause 0.1
    d "But we all agree his Bon Jovi is spot-on."
    show chris at threeright
    show don at middle
    show brit p2 straight opened_smile level at threeleft
    with easeinleft
    pause 0.1
    b "Oh, no doubt."
    c p1 straight casual grin "Absolutely!"
    d casual "They sometimes add their own instrumental takes on the songs, probably to avoid lawsuits, but it's honestly kinda refreshing."
    d "We're trying to get them to perform at prom this upcoming school year, since it's rumored that the 80s is the theme."
    b p1 sad closed_smile "Fingers crossed!"
    scene bg house_re with dissolve
    pause 0.1
    "So, Mexican immigrants, a mad scientist, and a cover band all on the same street."
    "If I didn't know any better, I'd say I had stumbled upon the plot of a sitcom."
    window hide dissolve
    scene bg house_y with pushright
    window show dissolve
    show don p1 straight casual grin at middle with dissolve
    pause 0.1
    d "Over here, we have the Yellman house."
    d "There's only one resident, Eleanor. She's in Brittney's class."
    d blank level "She's..."
    d right "How do I put this..."
    show chris p2 straight mad blank at twoleft
    show don at tworight
    with easeinleft
    pause .1
    c "A cunt."
    "Christeena's sudden mood change was both noticeable and frightening."
    d straight sad "...yeah, that."
    d raised "It's really no secret that not a lot of people like her, ourselves included."
    a "Why?"
    hide chris
    hide don
    show brit p1 straight blank casual at middle
    with dissolve
    pause 0.1
    b "Well, I'm not really the kind of person to bad-mouth someone, but-"
    show brit at twoleft
    show chris p2 straight mad blank at tworight
    with easeinright
    pause 0.1
    c "She's a slut who will constantly treat everyone like useless garbage."
    b_s small dot "..."
    b p2 left sad blank "That actually hit the nail on the head perfectly."
    hide brit
    show chris at middle
    with easeoutleft
    pause 0.1
    c "All you really need to know is that she lives there and she's evil. Got it?"
    a "Er... yeah."
    c p1 casual grin "Good. Moving on."
    hide chris with dissolve
    pause 0.1
    "The way Christeena is handling this seems like she and this Eleanor girl have a personal history."
    "I'll definitely have to talk to Brittney or Donald about this."
    window hide dissolve
    scene bg bs with dissolve
    window show dissolve
    show don p1 straight casual grin at middle with dissolve
    pause 0.1
    d "Then we have my house, of course, then the girls', and then yours."
    d raised "I assume no further explanation is required."
    a "So what about that last house?"
    hide don with dissolve
    scene bg house_n with dissolve
    pause 0.5
    show chris p2 straight grin casual at middle with dissolve
    pause 0.1
    c "Oh, that one's been for sale for as long as we've been here."
    show chris at tworight
    show brit p2 right huhu level at twoleft
    with easeinleft
    b "Though, people have heard noises coming from inside at night. My vote is on 'haunted'."
    c p1 mad blank "Keep telling yourself that, Brit."
    b p1 straight sad opened_smile "I will and you cannot stop me!"
    hide brit
    hide chris
    with dissolve
    scene bg bs with dissolve
    pause 0.1
    show don p1 straight casual grin at middle with dissolve
    pause 0.1
    d "So, there's your basic rundown of our neighbors."
    d "I'm sure you'll find opportunities to properly introduce yourself to them, but for now, that's all there is to talk about!"
    $ tour_town += 1
    $ tour_berrystreet = True
    jump tourtown


label tourpond:
    if persistent.tour["1"] == 0:
        $persistent.tour["1"] = 2
    elif persistent.tour["2"] == 0:
        $persistent.tour["2"] = 2
    elif persistent.tour["3"] == 0:
        $persistent.tour["3"] = 2
    elif persistent.tour["4"] == 0:
        $persistent.tour["4"] = 2
    scene bg pond
    show pond_foreground
    with dissolve
    $d_blink = False
    $ current_track = "\"The Pond\""
    play music the_pond
    show don p1 closed sad grin at middle with dissolve
    pause 0.1
    d "Ah, the pond."
    $d_blink = True
    d straight casual "Honestly, it's a nice place to go if you just want to get away from it all."
    hide don
    show brit p1 casual grin straight at middle
    with dissolve
    pause 0.1
    b "It's especially nice in the summer months."
    b p2 left opened_smile "Cookouts, fishing, swimming..."
    b straight raised grin "The water's cold enough to turn your nipples to diamond, but it's worth it."
    show brit at tworight
    show chris p1 straight mad blank at twoleft
    with easeinleft
    pause 0.1
    c "Really, Brittney?"
    b left huhu level "Well, am I wrong?"
    c p2 hanging "I just..."
    $ c_blush = True
    c left blank "Nevermind."
    hide brit
    hide chris
    show don p1 straight casual grin at middle
    with dissolve
    pause 0.1
    $ c_blush = False
    d "Anyway, when it gets colder outside, people like to go ice skating on it, so there's something if you're into that."
    a "Not really."
    hide don
    show brit p1 straight grin casual at middle
    with dissolve
    b "What, can you not skate?"
    a "I mean, I've skated before, but not in a while and never on an actual pond."
    a "Plus, I'm not really the kind of guy who likes to be outside in the winter."
    b p2 raised opened_smile "Wow. You're kinda lame, aren't you?"
    a "You know it."
    if C_Points >= 1:
        hide brit
        show chris p1 straight grin casual at close_c
        with dissolve
        pause 0.1
        c "Well, I don't think you're lame."
        show brit p2 straight level huhu at tworight
        show chris at close_left_c
        with easeinright
        b "Ooo, does Christeena have a crush?"
        $ c_blush = True
        c_s small sad hanging "...!"
        show chris p2 straight blank mad at close_to_left
        pause 0.1
        c "C-can't a girl compliment a guy without it coming off as flirting?"
        $b_blink = False
        b p1 closed sad opened_smile "Alright, alright; fair enough."
    else:
        hide brit
        show chris p1 straight casual blank at middle
        with dissolve
        pause 0.1
        c_s "..."
        "Christeena looks like she wants to say something..."
        "...though I'd hate to put her on the spot and fluster her."
    hide brit
    hide chris
    show don p1 straight casual grin at middle
    with dissolve
    pause 0.1
    $ b_blink = True
    $ c_blush = False
    d "Anyway, there's something over here I want you to check out."
    d smile "Follow me!"
    hide don with dissolve
    pause 0.1
    "Donald started walking toward a wooded area near the pond."
    "The girls followed right behind him, as if they knew where he was going."
    "I guess that means it's safe to follow suit."
    "Probably."
    scene bg fade with dissolve
    pause 0.1
    d_o "There it is, in all its glory!"
    scene bg cabin_e with dissolve
    pause .1
    "Donald then gestured towards what appeared to be some sort of cabin."
    "It didn't look brand-spanking-new, but it didn't look centuries old, either."
    show don p1 straight casual grin at close_left_d with dissolve
    pause 0.1
    a_s "..."
    a "Dare I even ask?"
    d raised smile "It's an old, abandoned shack, for starters."
    d level right blank "I don't know for sure when it was built."
    d grin "But based on its size and interior, I'm guessing it's an old hunting cabin."
    d casual straight "Just enough room for the bare necessities: a bed, a kitchen, a bathroom, and a fireplace."
    a "And you're showing me this because...?"
    hide don
    show brit p2 straight casual opened_smile at close_b
    with dissolve
    pause .1
    b "Donald likes to drag us out here from time to time to hang out and escape reality."
    a_s "..."
    b p1 mad frown "No, I'm not talking about drugs!"
    a "I didn't say anything!"
    b p2 blank level left "Well, anyway..."
    b p1 straight casual grin "It is pretty cool to be out here, I gotta admit."
    b p1 small hanging sad "Though hiding from the masked, chainsaw-wielding killer that comes out from time to time can be a pain."
    a "Yeah, very funny."
    show brit:
        ease 0.5 twoleft
    show don p1 sad straight blank at tworight with easeinright
    pause 0.1
    d "No, she's serious."
    $ current_track = "\"...\""
    $renpy.music.set_pause(True, channel='music')
    a_s "..."
    d_s casual "..."
    b_s p2 straight casual blank "..."
    show brit at threeleft
    show don at middle
    show chris p1 straight casual blank at threeright
    with easeinright
    pause .1
    c_s "..."
    a "You're all messing with me, right?"
    $b_blink = False
    b p1 closed sad opened_smile "Of course we are, dum-dum!"
    $ current_track = "\"The Pond\""
    $renpy.music.set_pause(False, channel='music')
    $d_blink = False
    d closed sad smile "But, man, you should've seen the look on your face!"
    $ c_blush = True
    $c_blink = False
    show chris p2 closed_happy grin sad
    "Even Christeena was trying to hide laughter."
    $d_blink = True
    hide brit
    hide chris
    show don p1 straight casual smile
    with dissolve
    pause .1
    $b_blink = True
    $c_blink = True
    $ c_blush = False
    d "Anyway, maybe we can all hang out here one day and you can get a good idea of why we like it so much."
    a "Maybe."
    d raised grin "Well, that's pretty much all there is about the pond; what do you say we get out of here?"
    $ tour_town += 1
    $ tour_pond = True
    jump tourtown


label tourdowntown:
    if persistent.tour["1"] == 0:
        $persistent.tour["1"] = 3
    elif persistent.tour["2"] == 0:
        $persistent.tour["2"] = 3
    elif persistent.tour["3"] == 0:
        $persistent.tour["3"] = 3
    elif persistent.tour["4"] == 0:
        $persistent.tour["4"] = 3
    scene bg mainstreet
    with dissolve
    $ current_track = "\"Outside the Street\""
    play music outside_the_street
    show don p1 straight grin casual at middle with dissolve
    pause 0.1
    d "And here we have the downtown district, where you can find next to all of your basic needs."
    d level right "Post office, police station, firehouse, grocery stores, etc."
    d straight casual "Truth be told, most of the bigger stuff, like hospitals and bigger restaurants, is in the next town over."
    hide don
    show brit p1 straight casual opened_smile at middle
    with dissolve
    pause .1
    b "But that frankly doesn't bother us, because the only restaurant we need is right here!"
    hide brit with dissolve
    pause 0.5
    scene bg deli_e with dissolve
    pause 0.1
    "Brittney then pointed at a small building with a sign reading 'Kelly's Deli'."
    show chris p1 straight casual grin at close_left_c with dissolve
    pause .1
    c "Yeah, our mom works here, but that's not why we love it so much."
    c p2 smile "This place has the best food you'll ever eat in your life!"
    show brit p1 straight grin casual at tworight with easeinright
    pause 0.1
    b "She ain't exaggeratin', either!"
    b p2 mad closed_smile "One bite of Kelly's signature sandwich is enough to make your mouth orgasm!"
    show chris level blank
    a "Ew."
    $b_blink = False
    b p1 closed sad opened_smile "What I'm saying is it's good!"
    $b_blink = True
    if tour_town >= 3:
        b p1 left casual grin "In fact, since we've already toured everything else in town, what do you say I buy us all some lunch?"
    else:
        b p1 left casual grin "In fact, what do you say I buy us all some lunch once we're done touring the town?"
    show chris:
        ease 0.5 threeleft
    show brit at middle
    show don p1 straight raised grin at threeright
    with easeinright
    pause .1
    d "Well, I mean, if you're paying..."
    c p1 sad smile "Yeah, that sounds nice."
    b p2 straight raised "Al?"
    a "Well, I guess if you all say it's good, I may as well try it out."
    $d_blink = False
    d sad closed smile "That's the spirit!"
    b p2 mad blank "Just don't be a douche and order the most expensive things on the menu."
    $d_blink = True
    d left mad grin "No promises."
    if tour_town >= 3:
        scene bg deli_e with dissolve
        pause 0.1
        scene bg deli_i_e
        show deli_entrance_sign zorder 2
        with dissolve
        pause 0.1
        jump lunchatkellys
    else:
        hide brit
        hide chris
        show don straight casual grin at middle
        with easeoutleft
        pause .1
        d "That said, let's hurry it up with the tour!"
        $ tour_town += 1
        $ tour_downtown = True
        jump tourtown

label tourschool:
    if persistent.tour["1"] == 0:
        $persistent.tour["1"] = 4
    elif persistent.tour["2"] == 0:
        $persistent.tour["2"] = 4
    elif persistent.tour["3"] == 0:
        $persistent.tour["3"] = 4
    elif persistent.tour["4"] == 0:
        $persistent.tour["4"] = 4
    hide don
    show brit p1 mad straight frown at middle
    with dissolve
    pause 0.1
    b "I thought I made it clear that any and all mentions of school were to be avoided!"
    show brit at tworight
    show don p1 level grin right at twoleft
    with easeinleft
    pause 0.1
    d "Relax, it won't take long."
    d "After all, Alex will need to know how to get there, eventually, right?"
    b p2 level blank right "I suppose..."
    a "You know, Brittney, you kinda struck me as the kind of person who likes school."
    b casual straight "Whaddaya mean?"
    a "I mean, the way you were talking yesterday about how important grades and stuff are."
    b level "Well, yeah, I do think it's important..."
    b p1 raised hanging "...but it's the beginning of summer vacation! Why would I put any effort into thinking about school during that time?"
    a "Well, I suppose there's no arguing there."
    d straight casual grin "C'mon; the sooner we get there, the sooner we can leave!"
    hide brit
    hide don
    with dissolve
    pause .1
    scene bg school_e
    with dissolve
    $ current_track = "\"Getting Educated\""
    play music getting_educated
    pause 1
    show don p1 straight casual grin at close_d
    with dissolve
    pause .1
    d "Here we are!"
    d "As you can see, it's a pretty small building right in the middle of nowhere."
    d right blank level "Even compared to other schools in the area, this place is tiny."
    d "The average graduating class has only 100 students."
    a "Seriously??"
    hide don
    show chris p1 straight casual blank at middle
    with dissolve
    pause .1
    c "Seriously."
    c p1 left level dot "It seems to get smaller and smaller every year, though..."
    a "Oh, yeah, I meant to ask:"
    a "Are you in the same grade as Donald and I, Christeena?"
    c p2 straight casual grin "No, I'm a year younger than you guys, so I'll be a sophomore this year."
    a "So you're a sophomore, Donald and I are juniors, and Brittney is a senior?"
    show chris at twoleft
    show don p1 straight raised grin at tworight
    with easeinright
    pause .1
    d "You got it!"
    d casual "But don't worry; there are plenty of opportunities for people of all ages and grades to interact."
    c p1 smile "Yeah, there's the time before school, lunchtime, study hall, etc."
    c grin "Heck, even some of the classes, themselves, have mixed grades in there."
    a "How does that happen?"
    d level "Well, several ways, actually."
    d right "Maybe someone failed that class and needs to retake it, or they're a new student and have to take a required class that freshmen usually take..."
    a "So, like me?"
    d sad straight smile "Yeah! Exactly!"
    c p2 raised "Don't worry; taking classes with freshmen isn't as bad as it sounds."
    d left mad blank "Says you."
    c mad blank "Would I lie to a new student?"
    d_s casual "..."
    d "Point taken."
    d raised straight grin "That's more of your sister's job."
    hide don
    hide chris
    show brit p1 mad straight hanging at middle
    with dissolve
    pause 0.1
    b "Hey! That's..."
    $b_blink = False
    b p2 closed opened_smile sad "...pretty accurate."
    a "So, what's the school like, in general?"
    hide brit
    show don p1 straight casual grin at middle
    with dissolve
    pause 0.1
    $b_blink = True
    d "Well, again, it's a small school, which has advantages and disadvantages."
    d blank level right "On one hand, it's easier to get to know everyone, but on the other hand, gossip spreads faster than wildfire."
    hide don
    show chris p2 left mad blank at middle
    with dissolve
    pause 0.1
    c "Ugh."
    a "Personal experience?"
    c p1 straight raised "Something like that."
    "I'm curious to know what happened, but I have a feeling she may not want to talk about it."
    hide chris
    show don p1 straight level grin at middle
    with dissolve
    pause 0.1
    d "But overall, it's pretty cool."
    d raised right "The teachers are good, for the most part, homework is homework, so do with that information what you wish..."
    d casual straight "I mean, you'll only have to deal with it for 2 years, so if anything, you're luckier than all of us."
    hide don
    show brit p1 straight level blank at middle
    with dissolve
    pause 0.1
    b "That's very true."
    b p2 sad left "Though, it's a shame we'll only be in school together for a year."
    $ b_partial = True
    b straight opened_smile raised "Guess we'll just have to make the most of it!"
    show brit at tworight
    show chris p1 straight mad blank at twoleft
    with easeinleft
    pause 0.1
    c "Oh, Lord..."
    hide brit
    hide chris
    show don p1 straight casual grin at middle
    with dissolve
    pause 0.1
    $ b_partial = False
    d "So, now you know how to get to the school and what the general feel of the place is."
    d "Hopefully you'll be able to take care of things from there."
    a "Yeah, hopefully..."
    $ tour_town += 1
    $ tour_school = True
    jump tourtown

label tourcomplete:
    hide don
    show brit p1 straight grin casual at middle
    with dissolve
    pause 0.1
    b "Well, it looks like we've checked out everything that Donald wanted to see!"
    b p2 raised left opened_smile "What do you say we grab our lunch now?"
    show brit at twoleft
    show don p1 raised straight smile at tworight
    with easeinright
    pause 0.1
    d "Sounds like a plan!"
    show brit at middle
    show don at threeright
    show chris p1 straight smile casual at threeleft
    with easeinleft
    pause 0.1
    c "Yeah! Let's eat!"
    a "Alright, I guess so."
    hide brit
    hide don
    hide chris
    with dissolve
    pause 0.1
    scene bg fade with wipeleft
    scene bg deli_i_e
    show deli_entrance_sign zorder 2
    with wipeleft
    pause 0.1


label lunchatkellys:
    play sound deli_door
    play loop deli_crowd
    $ current_track = "\"Dinin' In\""
    play music dinin_in
    "We then entered the deli."
    "The interior looked like your average, small-town diner."
    "There didn't seem to be a lot of customers at the moment, though it was a weekday morning, so maybe it's just a naturally slower time for business."
    "Right near the entrance, a young woman around our age was standing behind a podium. She gave us a grin when she saw us enter."
    gr "Welcome back to Kelly's Deli, you three!"
    gr "I see you brought a new friend this time."
    show brit p2 straight grin casual at middle with dissolve
    pause 0.1
    b "We have, indeed."
    gr "Would you prefer a booth or a table today?"
    b p1 opened_smile "Booth is fine, thank you."
    show brit at tworight
    show chris p2 straight smile casual at twoleft
    with easeinleft
    pause 0.1
    c "Preferably by the window."
    gr "No problem; follow me!"
    hide brit
    hide chris
    with dissolve
    pause .1
    scene bg deli_i_wb
    show deli_table zorder 2
    with dissolve
    "The greeter grabbed 4 menus and walked over to the main dining area, with all of us right behind her."
    "She placed the menus on the table and we all sat down, boys on one side, girls on the other."
    "I found myself sitting across from Christeena, both of us right by the window."
    gr "Someone will be right over to take your order."
    show brit p1 straight opened_smile casual at middle with dissolve
    pause 0.1
    b "Thanks!"
    gr "No problem!"
    hide brit with dissolve
    pause .1
    "The greeter then left, leaving only the 4 of us at the table."
    a "So, how often do you guys come here?"
    show don p1 straight casual grin at close_d zorder 3 with dissolve
    pause 0.1
    d "As often as we can, though we aim for about once a week at the very least."
    a "Is the food really that good that you come here that often?"
    hide don
    show brit p1 straight level grin at tworight
    with dissolve
    pause 0.1
    b "Well, yeah, but that's not the only reason."
    b p2 sad "It just feels nice having a public place where you can just hang out."
    a "You mean a place that isn't a cabin in the woods?"
    $b_blink = False
    b closed opened_smile "Exactly!"
    $b_blink = True
    b p1 straight raised grin "A place that makes you feel like you're in a simpler time, where you don't need to look at a screen to keep yourself entertained."
    b p2 left level huhu "In fact, we often have bets about who checks their phones first."
    $ c_blush = True
    show chris p1 left mad blank at twoleft with easeinleft
    pause 0.1
    c "It's usually me."
    hide chris
    show chris p2 straight hanging mad at twoleft
    c "But only because I'm checking the time."
    b p1 straight mad grin "Still counts."
    c p1 left blank "Yeah, yeah..."
    hide brit
    hide chris
    with dissolve
    pause 0.1
    $ c_blush = False
    "That's when our waitress approached us with a giant smile."
    show bg deli_i_wb:
        ease 0.5 xalign 1.0
    show deli_table:
        ease 0.5 xalign 1.0
    pause 0.6
    show martha p1 straight casual grin at m_threeright with dissolve
    pause 0.1
    mu "Well, howdy, strangers!"
    show brit p1 straight sad grin at twoleft with easeinleft
    pause .1
    b "Howdy, stranger!"
    mu raised "What, did you decide to come in to once again try and get a discount?"
    b p2 mad opened_smile "Nah; we wanted to show Alex how good the food was!"
    show martha casual
    hide brit with easeoutleft
    pause 0.1
    "The waitress looked at me and smiled."
    mu sad "So you're the mysterious new neighbor I've been hearing about?"
    a_s "..."
    mu sad "Oh, right."
    mu casual smile "I'm Martha, Brittney and Christeena's mom."
    $ M_Name = "Mrs. Truman"
    a "Oh! That makes me feel less confused."
    $b_blink = False
    show brit p1 closed sad opened_smile at twoleft with easeinleft
    pause .1
    b "Yeah, we did, after all, tell you that she works here."
    $b_blink = True
    b p2 right level huhu "Though, that family discount does sound nice..."
    $ m_partial = True
    mu level blank "For the thousandth time, the employee discount only applies when the employee, themselves, is the one paying for the meal."
    b straight raised opened_smile "Then can--"
    mu "No."
    $ b_partial = True
    b straight level blank "Darn."
    $ b_partial = False
    show brit p1 straight raised grin
    b "Well, I guess that means it's time to order."
    $ m_partial = False
    show martha p1 raised straight grin
    mu "Indeed."
    mu casual smile "So, Mr. Waters, what will you have today?"
    hide brit
    hide martha
    show don p1 blank level straight zorder 3 at close_d
    with dissolve
    pause .1
    d "Hmm..."
    d right "I think I'll go for..."
    "Donald then stared at his menu in thought, as if his decision decided the fate of the entire galaxy."
    d raised straight grin "...a Swiss Miss and a Hilly Dew."
    show don at close_left_d
    show martha p1 straight raised grin at m_threeright
    with easeinright
    pause .1
    mu "Since when do you eat Swiss cheese?"
    $d_blink = False
    d closed sad smile "Since your daughter became the one whose money will be wasted if I don't like it."
    show bg deli_i_wb:
        ease 0.5 xalign 0.0
    show deli_table:
        ease 0.5 xalign 0.0
    show don zorder 3:
        ease 0.5 xalign 0.8
    show martha zorder 1:
        ease 0.5 xalign 1.4
    show brit p1 small level derp zorder 1:
        zoom 0.75
        xalign -0.4 yalign 0.5
        ease 0.5 xalign 0.25
    pause .6
    b "And here I thought you loved me."
    $d_blink = True
    d straight raised grin "I see it as tough love."
    show bg deli_i_wb:
        ease 0.5 xalign 1.0
    show deli_table:
        ease 0.5 xalign 1.0
    show martha level:
        ease 0.5 m_threeright
    hide brit
    hide don
    with easeoutleft
    pause 0.1
    "Mrs. Truman wrote down the order with a grin."
    mu "Brittney?"
    show brit p2 straight raised grin at twoleft with easeinleft
    pause 0.1
    b "Well, since I want to see if my hard-earned money is worth it, I shall get a Swiss Miss, as well."
    mu raised "And a water?"
    b p1 casual opened_smile "Of course!"
    mu mad smile "You got it."
    mu raised grin "What about you two?"
    hide brit
    show chris p2 straight casual smile at twoleft
    with dissolve
    pause 0.1
    c "I'll get my usual."
    mu casual "As to be expected."
    mu raised "And you, young man?"
    hide chris
    hide martha
    with dissolve
    pause .1
    "Well, there were certainly no shortage of options..."
    "There was the Classic Kelly's Deli Sandwich, which is apparently the Big Mac or Whopper of the place..."
    "'Made with freshly-sliced ham and turkey, topped with sharp white cheddar cheese.'"
    "Though the Meatball Miracle, which consisted of hot, juicy meatballs, homemade marinara sauce, and shredded mozzarella, certainly caught my eye."
    "Then again, I could play it safe with some chicken tenders, which was made sure to be advertised as 100\% real chicken meat."
    show martha casual p1 straight grin at m_threeright with dissolve
    pause 0.1
    mu "Have you made a decision?"
    if persistent.choices["5"] == 1:
        a "Hm..."
        jump classicsandwich
    elif persistent.choices["5"] == 2:
        a "Hm..."
        jump meatballmiracle
    elif persistent.choices["5"] == 3:
        a "Hm..."
        jump chickentenders
    else:
        menu:
            a "Hm..."
            "Classic Sandwich":
                $ persistent.choices["5"] = 1
                jump classicsandwich

            "Meatball Miracle":
                $ persistent.choices["5"] = 2
                jump meatballmiracle

            "Chicken Tenders":
                $ persistent.choices["5"] = 3
                jump chickentenders

    label classicsandwich:
        $ delifoodorder = "a Kelly's Deli Classic Sandwich"
        a "I suppose I'll try the Classic Sandwich and see what the fuss is about."
        mu sad "Excellent choice! Your taste buds will thank you."
        hide screen skipchoice
        jump orderdrink

    label meatballmiracle:
        $ delifoodorder = "a Meatball Miracle"
        a "The Meatball Miracle sounds pretty good, so I'll go with that."
        mu sad "Meatball Miracle it is, then!"
        hide screen skipchoice
        jump orderdrink

    label chickentenders:
        $ delifoodorder = "chicken tenders"
        a "I'll just go for the chicken tenders, I suppose."
        mu sad "Very well, then. Simplicity never hurt anyone."
        hide screen skipchoice

    label orderdrink:
        mu casual "And to drink?"
        if persistent.choices["6"] == 1:
            jump soda
        if persistent.choices["6"] == 2:
            jump lemonade
        if persistent.choices["6"] == 3:
            jump water
        else:
            menu:
                a "Hmm..."

                "Soda":
                    $ persistent.choices["6"] = 1
                    jump soda

                "Lemonade":
                    $ persistent.choices["6"] = 2
                    jump lemonade

                "Water":
                    $ persistent.choices["6"] = 3
                    jump water

    label soda:
        $ delidrinkorder = "Hilly Dew"
        a "I could use some caffeine, so I'll just get some Hilly Dew with no ice."
        show martha raised smile
        mu "You got it!"
        jump waitingforfood

    label lemonade:
        a "Nothing like some lemonade on a nice, hot day, right?"
        show martha raised smile
        mu "Couldn't agree more!"
        jump waitingforfood

    label water:
        a "I'll just take a water, please."
        show martha raised smile
        mu "Yes, sir!"

    label waitingforfood:
        hide martha with dissolve
        pause 0.1
        "Mrs. Truman took all of our menus and let us know that the food would be ready soon."
        "We thanked her, and she was on her way."
        show bg deli_i_wb:
            ease 0.5 xalign 0.0
        show deli_table:
            ease 0.5 xalign 0.0
        pause 0.6
        show brit p2 straight casual blank at middle with dissolve
        pause 0.1
        a "Well, she seems cool."
        b p1 opened_smile "Thanks!"
        b p2 left level huhu "Not to brag or anything, but my mom is, like, the coolest mom ever."
        b straight sad grin "She's the reason I am who I am today."
        $d_blink = False
        show brit:
            ease 0.5 twoleft
        show don p1 closed sad smile zorder 3 at close_right_d with dissolve
        pause .1
        d "Yeah, clearly the sexiness gene runs in the females of the Usher family."
        $d_blink = True
        show don:
            linear 0.1 yalign 0.3
            linear 0.1 yalign 0.2
        d small wide "OUCH!"
        d straight mad "That was my shin!"
        b p1 small sad hanging "Oh, sorry!"
        $ b_partial = True
        b p2 straight blank level "I was actually trying to go for your kneecap."
        b raised "Though if you call me or my mom sexy again, I'll be sure to be more accurate."
        d blank "Alright, alright. Sorry."
        d right "On that note, I'm going to the restroom."
        d straight raised "Alex, if the food gets here before I come back, I'm putting you in charge of making sure Brittney doesn't take a bite out of my sandwich!"
        a "...she ordered the same thing as you."
        d level grin "That won't stop her."
        b casual grin "Guilty."
        a "Okay, then..."
        hide don with easeoutright
        pause 0.1
        "Donald then got up and headed to the restroom."
        "Now that it was just me, Brittney, and Christeena, I guess I could finally ask a question that was on my mind."
        show chris p2 straight casual blank at twoleft
        show brit at tworight
        with easeinleft
        pause 0.1
        $ b_partial = False
        show brit p2 straight casual blank
        a "So, is it alright if I ask you girls a personal question?"
        b p1 raised grin "Hit me."
        c p1 sad "...I suppose..."
        a "Martha is Brittney's mom, and she's married to Christeena's dad, right?"
        b casual "That's correct."
        a "So, if you don't mind me asking, where are your other parents? The biological ones, I mean?"
        $ current_track = "None"
        stop music fadeout 3.0
        stop loop fadeout 3.0
        show brit p2 blank
        show chris casual
        "The girls paused for a second and looked at each other, seeming to wait for the other to start talking."
        "Finally, Christeena broke the silence."
        show chris:
            ease 0.5 middle
        hide brit with dissolve
        pause 0.1
        $ current_track = "\"Reflection\""
        play music reflection
        c "Well, my mother's in California."
        c p1 left level dot "She moved there after she divorced my dad, and quickly moved on to a younger, richer man."
        a "Ouch."
        a "I'm sorry to hear that."
        c p2 straight sad grin "It's alright."
        c left blank mad "At first, she wanted nothing to do with me, but after hearing of my dad's remarriage, it's like she's trying to win me back or something."
        a "What do you mean?"
        c p1 straight raised "Well, for starters, she finally acknowledged my birthdays, sending me expensive gifts that were easily worth more than anything my dad gave me."
        c left "She also keeps trying to get me to live with her instead of him, saying now that he has a new wife and step daughter, he doesn't need me to keep him company anymore."
        a "She sounds...well, uh..."
        $ c_blush = True
        c straight sad grin "It's okay, Alex. I get what you're trying to say."
        $ c_blush = False
        c p2 level blank "Honestly, I suppose living with her could be fun..."
        c sad "...but I don't know if I can trust her."
        c p1 level blank "I mean, if I did live with her, would she really love me and treat me like her daughter..."
        c left "...or would I be more of a trophy in this silly contest of 'who's the better parent?' that she's created in her head?"
        a "So that's why you're still here?"
        c p2 straight casual "Partially."
        c sad "My dad has always been there for me when she wasn't. It would break his heart to have the only original family he has left leave him."
        c p1 grin "Plus, Martha has been a better mother to me than my own mother ever was, and Brittney's the closest I have to a sister and best friend."
        $c_blink = False
        c closed_happy smile "And, I'm not gonna lie, I would miss Donald's silliness."
        a "So, the pros of staying outweigh the cons?"
        $c_blink = True
        c p2 straight casual grin "Yeah, you can say that."
        a "Wow."
        show chris:
            ease 0.5 twoleft
        show brit p2 straight blank casual at tworight with dissolve
        pause 0.1
        a "So what about you, Brittney?"
        a "Where's your dad?"
        show brit:
            ease 0.5 middle
        hide chris with dissolve
        pause 0.1
        b left sad grin "Well, depending on what you believe, he's either in a better place or simply laying six feet under."
        a "Oh."
        a "I'm sorry; I didn't know."
        b p1 straight level "That's exactly why there's no need to be sorry, dum-dum."
        a "So, then, if you don't mind me asking..."
        b p2 sad "He was a firefighter."
        b right blank level "His squad was putting out a house fire in town, and the whole building collapsed on him."
        b "Died instantly."
        a "Wow..."
        b sad "Yeah."
        b p1 straight casual "I was six at the time, so I was pretty heartbroken to learn that Daddy was never coming home."
        b "My mom was pretty upset, too, of course, but not as bad as you might think."
        b p2 sad "After all, she can't say she didn't know something like that could happen every day he left home, y'know?"
        a "Right."
        b left level "Still, I remember it taking her quite a bit to move on."
        b "Though, looking back, I wonder how much longer it would've taken if she wasn't putting all of her focus on raising me."
        a "It can't be easy being a widow and raising your daughter alone."
        b straight sad "No, it can't be."
        b grin "But she did it."
        b p1 opened_smile "When I say she's the reason I am who I am today, I mean it."
        a "I'm sure you do."
        a_s "..."
        a "So, do you ever miss him?"
        b p2 mad blank "Of course I do. It's not like we've completely cut him from our memory."
        b casual grin "On his birthday, we visit his grave, and on the anniversary of his passing, we visit the firehouse."
        b p1 opened_smile "The firefighters are so incredible. They just love telling stories about him."
        b p2 sad grin "But we can't keep dwelling in the past forever, right?"
        b left "I've got a new dad now, an amazing one at that, and my birth dad wouldn't want us to just sit and mourn him forever."
        a "Very true."
        "I could tell that, despite her smile, she wasn't as happy and energetic as she was a few minutes ago."
        a "I'm sorry if I killed your good mood."
        b p1 straight casual blank "Oh, you did no such thing, Alex."
        b sad grin "Besides, even if you did, there still wouldn't be anything to be sorry about."
        b p2 right "I'm sure you were going to figure it out sooner or later, so it's nice to know it now, right?"
        a "I suppose so."
        hide brit with dissolve
        pause 0.1
        show bg deli_i_wb:
            ease 0.5 xalign 1.0
        show deli_table:
            ease 0.5 xalign 1.0
        pause 0.6
        $ current_track = "None"
        stop music fadeout 3.0
        "The men's room door opened up and Donald emerged, quickly finding his way back to the booth."
        $ current_track = "\"Dinin' In\""
        play music dinin_in
        play loop deli_crowd
        show don p1 straight mad blank at close_right_d zorder 3 with dissolve
        pause 0.1
        d "One thing I must say I dislike about this place is the crappy restroom."
        d "It's just so old and broken down that I'm scared the toilet will overflow every time I flush."
        $ b_partial = True
        show brit p2 straight blank level at twoleft with easeinleft
        pause 0.1
        b "Thanks for that, Mr. Waters."
        hide brit
        hide don
        with dissolve
        pause .1
        $ b_partial = False
        "It was at that moment when Mrs. Truman arrived carrying a tray of food and drinks."
        show martha p1 straight raised grin at m_threeright with dissolve
        pause 0.1
        mu "Alright, let's see here..."
        mu casual "We've got a Swiss Miss and Hilly Dew..."
        show don p1 straight casual grin at close_left_d zorder 3 with easeinleft
        pause 0.1
        "She placed the order in front of Donald."
        hide don with easeoutleft
        pause 0.1
        mu level "...Swiss Miss with water..."
        show brit p1 straight casual grin at twoleft with easeinleft
        pause 0.1
        "Brittney then received her meal."
        hide brit with easeoutleft
        pause 0.1
        mu sad "...Grilled Ham n Cheddar with iced tea..."
        show chris p1 straight casual grin at twoleft with easeinleft
        pause 0.1
        "Huh. So I guess that's Christeena's 'usual'."
        hide chris with easeoutleft
        pause 0.1
        mu casual "And [delifoodorder] with [delidrinkorder]."
        a "Thanks!"
        mu smile "Enjoy your meal, then!"
        show brit p2 straight casual opened_smile at twoleft with easeinleft
        pause 0.1
        b "Thanks, Mom!"
        show martha sad grin
        "Mrs. Truman smiled and walked to a nearby table."
        hide martha
        hide brit
        with dissolve
        pause 0.1
        show bg deli_i_wb:
            ease 0.5 xalign 0.0
        show deli_table:
            ease 0.5 xalign 0.0
        pause 0.6
        show don p1 straight raised smile at close_d zorder 3 with dissolve
        pause .1
        d "Let's all wait for a second. I gotta see Alex's reaction to this food."
        show don grin at close_right_d
        show brit p1 straight raised closed_smile zorder 1 at twoleft
        with easeinleft
        b "Agreed."
        show brit at middle zorder 1
        show chris p2 straight grin raised at threeleft zorder 1
        with easeinleft
        pause .1
        "Even Christeena was looking at me with a curious smile."
        "Thanks for putting me on the spot, Don."
        if delifoodorder == "chicken tenders":
            "I looked down at my tenders. They certainly did smell delicious."
            "I finally picked one up and took a bite."
        else:
            "I looked down at my sandwich. It certainly did smell delicious."
            "I finally picked it up and took a bite."
        "..."
        window hide dissolve
        with Pause(2)
        window show
        a "Holy crap...!"
        d casual smile "Told ya!"
        a "I mean, you guysh had shaid it wush good, but..."
        "I was trying my hardest to not be rude by speaking with my mouth full, but it was just so good that I had to say something!"
        b p2 grin "Finish your bite, THEN give your feedback."
        "I took a quick drink to wash my bite down."
        a "Well, I can certainly see what you guys were talking about!"
        $c_blink = False
        c p1 closed_happy sad smile "There's a reason why this place is so beloved by the townspeople."
        $c_blink = True
        c straight blank raised "It's crazy how the best food always comes from local restaurants and not those money-hungry chain restaurants."
        a "Yeah, crazy is a good way to describe it."
        d mad left grin "Well, regardless, what do you say we all follow suit and eat up?"
        b p1 mad grin "I second this notion!"
        c casual smile "Agreed!"
        hide brit
        hide chris
        hide don
        with dissolve
        pause .1
        "We all then began to dig into our meals."
        show don p1 casual straight blank at close_d zorder 3 with dissolve
        pause .1
        a "How's the Swiss Miss?"
        d smile "You know, I'm not gonna lie; Swiss cheese is actually pretty good!"
        hide don
        show brit p1 straight casual grin at middle
        with dissolve
        pause .1
        b "Yeah, I'm honestly surprised!"
        b p2 level "It goes really well with the smoked turkey."
        b raised "I guess you really do learn something new every day."
        show brit:
            ease 0.5 twoleft
        show don p1 left raised grin at close_right_d zorder 3 with dissolve
        pause 0.1
        d "Indeed. Nice to know I didn't waste your money, after all!"
        b casual "Same here. Because if you did, indeed, waste my hard-earned money..."
        $ b_partial = True
        b mad closed_smile "...I would've slit your throat while you sleep tonight."
        d level straight "Love ya too, Brit."
        $ b_partial = False
        $b_blink = False
        show brit p2 closed sad grin at twoleft
        b "Ehehe!"
        "These two certainly are quite an odd pair."
        hide don
        hide brit
        with dissolve
        $b_blink = True
        pause 0.1
        show chris p1 left level dot at middle with dissolve
        pause 0.1
        a "Anyway, Christeena..."
        c p2 straight casual blank "Hm?"
        "She seemed like she was spaced out, only to be brought back into reality by the mention of her name."
        a "I take it you order that a lot?"
        "I pointed at her food as I asked, to which she nodded with a grin."
        c p1 sad grin "I know it's basically a grilled cheese sandwich with ham slices, but it's so good that I don't care."
        c_s casual blank "..."
        c "Do you want a bite?"
        a "!"
        a "Are you sure?"
        c p2 grin "Yeah, I don't mind."
        if persistent.choices["7"] == 1:
            a "Uh..."
            jump accept_sandwich
        elif persistent.choices["7"] == 2:
            a "Uh..."
            jump decline_sandwich
        else:
            menu:
                a "Uh..."

                "Sure!":
                    $ persistent.choices["7"] = 1
                    jump accept_sandwich
                "No, thank you.":
                    $ persistent.choices["7"] = 2
                    jump decline_sandwich

    label accept_sandwich:
        $ C_Points += 1
        $ acceptsandwich = True
        a "Well, okay, then."
        hide chris with dissolve
        pause 0.1
        "She placed her sandwich on her plate and lightly pushed it across to me."
        "I wrapped my fingers around the bottom..."
        a "Ouch!"
        "I pulled my hands away and lightly shook them to cool them off."
        show chris p1 straight sad dot at middle with dissolve
        pause 0.1
        c "Oh, I'm sorry! I should've told you it was hot!"
        a "Nah, you're good; I should've figured that out, myself."
        c p2 blank "Are you okay?"
        a "Yeah, I was more surprised, if anything."
        a "Alright, take two."
        $c_blink = False
        $ c_blush = True
        show chris closed_happy sad grin
        "Christeena gave a small giggle at that."
        hide chris with dissolve
        $ c_blush = False
        $_blink = True
        "Being more cautious, I carefully picked up the sandwich with my fingers wrapped more towards the edges."
        "Lifting it up, I can see the steam pouring out from between the bread slices."
        "How the heck was Christeena able to eat this thing without burning her mouth??"
        "Regardless, I took a small bite."
        "..."
        a "Ah!"
        show chris p1 straight sad dot at middle with dissolve
        pause 0.1
        c "You okay?"
        "I partially opened my mouth to try and vent out the steam; it was hot!"
        "Still, I gave a small nod in response to Christeena's question, even though I probably looked like a moron with my mouth open and nodding."
        hide chris with dissolve
        pause 0.1
        "It only took a second or two to cool down, which is when I closed my mouth and chewed."
        "..."
        "I swallowed the bite, placed the sandwich back on the plate, and passed it back to Christeena."
        show chris p2 straight casual blank at middle with dissolve
        a "You were right; it's pretty good!"
        $c_blink = False
        c p1 closed_happy sad smile "Good! Glad you liked it!"
        show chris:
            ease 0.5 twoleft
        show brit p2 left level huhu at tworight with dissolve
        pause 0.1
        b "Aw, would you look at that?"
        b "They're already sharing their food!"
        $c_blink = True
        $ c_blush = True
        c_s sad straight hanging "...!!"
        a "What's that supposed to mean?"
        b p1 straight raised closed_smile "Oh, nothing...~"
        "Her devilish grin said otherwise."
        show chris p2 left blank
        "Meanwhile, Christeena's face turned slightly pink as she looked down at her plate and ate her sandwich."
        jump paythebill

    label decline_sandwich:
        a "Nah, I'm good."
        c p1 dot "Are you sure?"
        if delifoodorder == "chicken tenders":
            a "Yeah, these tenders are good enough to know that all the food here must be good."
        else:
            a "Yeah, this sandwich is good enough to know that all the food here must be good."
        c p2 left level blank "O-okay, then."
        "She then took a bite of her sandwich."
        "..."
        "I hope I didn't offend her or something by declining her offer..."

    label paythebill:
        window hide dissolve
        scene bg fade with wipeleft
        scene bg deli_i_wb
        show deli_table zorder 2
        with wipeleft
        window show dissolve
        $ c_blush = False
        "Soon, we were all finished with our food."
        show don p1 straight casual smile at close_right_d zorder 3
        show brit p2 straight casual grin at twoleft zorder 1
        with dissolve
        pause 0.1
        d "Thanks for treating us to lunch, Brit."
        b p1 opened_smile "It's my pleasure, Don."
        b raised "I'm glad Alex enjoyed his food."
        a "Of course."
        a "I'm glad that the food was as good as advertised."
        b p2 grin "Would I lie to you?"
        a_s "..."
        d_s level blank "..."
        show brit at middle zorder 1
        show chris p2 straight mad blank at threeleft zorder 1
        with easeinleft
        pause 0.1
        c_s "..."
        b p1 level "Yeah, that was a dumb question."
        "Brittney then turned to glance at the clock hanging by the entrance."
        b casual "On that note, I gotta get ready for work."
        d casual "Already?"
        b p2 sad "Well, I like to get there early if I can help it."
        a "Where do you work?"
        b p1 opened_smile casual "I'm a lifeguard at the pool in town."
        a "No kidding?"
        b p2 grin level "No kidding."
        b raised "It's just a summer job, nothing too big."
        c p1 casual grin "And actually, there's some shopping I wanted to do while I was in town, so I guess I could head over there."
        a "And I suppose I should start unboxing some of my stuff."
        d level grin "Alright, then; fair enough."
        d casual "Still, it was nice to all hang out today."
        b casual opened_smile "Yeah, it certainly was."
        $c_blink = False
        show chris closed_happy sad
        "Christeena gave a small nod in agreement."
        show chris:
            ease 0.5 twoleft
        show brit:
            ease 0.5 tworight
        hide don with dissolve
        pause .1
        b p1 sad "Just let me know when you're on your way home, okay, Christeena?"
        $c_blink = True
        c p2 straight casual "Will do."
        $ current_track = "None"
        stop music fadeout 3.0
        hide brit
        hide chris
        with dissolve
        pause 0.1
        "With that, Brittney paid the bill, as well as left a fair tip, and we left the diner."
        stop loop fadeout 0.5
        scene bg house_s with dissolve
        pause 0.1
        $ current_track = "\"Home Life\""
        play music home_life
        "Brittney, Donald, and I walked back home to Berry Street while Christeena headed to one of the stores."
        "I thanked them for the town tour and entered my house."
        scene bg living_s_m with dissolve
        pause 0.1
        "I found my parents unboxing stuff in the living room."
        "Mom was surprised that I was home earlier than expected, but she didn't complain."
        "It certainly didn't take her long to try and get me to help unbox."
        show ginger p2 casual straight grin at middle with dissolve
        pause 0.1
        g "Why don't you at least start on your room, for now?"
        g "You don't have to get the whole thing done today, but at least try to get everything in the general area of where you want it."
        a "Got it."
        hide ginger with dissolve
        pause 0.1
        "With that, I went upstairs towards my room."
        "On the way, I could see Harry in his own room, sliding boxes across the floor."
        "I poked my head in the doorway."
        show harry p1 straight casual blank at middle with dissolve
        pause 0.1
        a "Need help?"
        h level "No, thanks; I got it."
        a "You sure? Some of those seem heavy."
        h "I'll be fine."
        a "Alright, but don't hesitate to ask for help if you need it, okay?"
        h mad "I'm not a little kid anymore, you know."
        a "I know, but-"
        h small frown "I'll be fine!"
        a "If you insist."
        hide harry with dissolve
        pause .1
        "I then continued down into my own room."
        "Harry sure can be stubborn at times, but he's at the near-puberty age where he just feels like he needs to show his adulthood."
        "I guess as long as he doesn't do anything stupid, like try to lift a 50-pound weight or hit on an older girl, we'll be fine."
        scene bg bedroom_a_m with dissolve
        pause 0.1
        "With that, I finally entered my room to begin unpacking."
        "Man, it's crazy how you never realize how much crap you own until you have to pack it all up."
        "I had to give away a lot of my old stuff for the move, stuff I honestly didn't even remember I owned."
        "Then there's the stuff I WANTED to get rid of, but Mom made me keep, like stuffed animals and such."
        "Well, I guess all that matters in the end is I have all my essentials for the move, and it hopefully shouldn't take TOO long to unpack."
        play sound phone_vibrate
        "Before I could get to the first box, though, I got a text."
        "Looking at the screen revealed it to be from a number I didn't recognize."
        nvl show dissolve
        unknown_nvl "{font=fonts/LemonMilk.otf}{i}Hey is this Alex?{/i}{/font}"
        a_nvl "{font=fonts/LemonMilk.otf}{i}Yeah. Who's asking?{/i}{/font}"
        nvl hide dissolve
        "I open up the first box I see."
        "Ah, these are all my books."
        "I admittedly don't read as much as I used to, but I've been meaning to get back into it."
        "After all, a good story can really change a person."
        play sound phone_vibrate
        "I get another text."
        nvl show dissolve
        if C_Points == -1 or C_Points == 0:
            unknown_nvl "{font=fonts/LemonMilk.otf}{i}It's Brittney. Swiped your digits from Donnie ;) :P{/i}{/font}"
            $ have_number = "Brittney"
        else:
            unknown_nvl "{font=fonts/LemonMilk.otf}{i}It's Christeena. Donald gave me your number.{/i}{/font}"
            $ have_number = "Christeena"
        a_nvl "{font=fonts/LemonMilk.otf}{i}Oh, hey! What's up?{/i}{/font}"
        nvl hide dissolve
        "Let's see here..."
        "Most of these books are books I've read before, though there are still a few I've been meaning to read."
        "Honestly, I don't know why I keep these books when I've finished them; I've never reread a book I've already read."
        "Yeah, it's weird. I'll rewatch a movie multiple times and replay a video game until I've uncovered everything, yet I won't reread a book. I'm just crazy like that."
        play sound phone_vibrate
        "Another text."
        "I suppose I should focus more on the conversation than the unboxing, for now."
        "I look at the text."
        nvl clear
        nvl show dissolve
        if C_Points == -1:
            b_nvl "{font=fonts/LemonMilk.otf}{i}Just curious if you have anything against my sister{/i}{/font}"
            a_nvl "{font=fonts/LemonMilk.otf}{i}Huh? No. Why do you ask?{/i}{/font}"
            b_nvl "{font=fonts/LemonMilk.otf}{i}Just wondering. She doesn't seem too fond of you{/i}{/font}"
            b_nvl "{font=fonts/LemonMilk.otf}{i}Of course not sure how I feel either with you telling her that I'm not pretty and all{/i}{/font}"
            "Ouch..."
            nvl clear
            a_nvl "{font=fonts/LemonMilk.otf}{i}I'm sorry about that. Really.{/i}{/font}"
            b_nvl "{font=fonts/LemonMilk.otf}{i}Well I don't really know you that well so I'll give you another chance{/i}{/font}"
            b_nvl "{font=fonts/LemonMilk.otf}{i}Although I'll never forget that you said I'm ugly lol XD{/i}{/font}"
            a_nvl "{font=fonts/LemonMilk.otf}{i}Hey, I never said you were ugly!{/i}{/font}"
            b_nvl "{font=fonts/LemonMilk.otf}{i}You said I wasn't pretty. That's close enough.{/i}{/font}"
            b_nvl "{font=fonts/LemonMilk.otf}{i}Talk to ya later dum-dum!{/i}{/font}"
            a_nvl "{font=fonts/LemonMilk.otf}{i}Okay then...{/i}{/font}"
            nvl clear
            nvl hide dissolve
            "Yeah, in hindsight, maybe saying that to Christeena was a bad idea."
            "Honestly, I guess Christeena doesn't really seem too fond of me at the moment, anyway."
            "Although, it has only been a day; bad first impressions happen all the time. I'm sure I can find ways to redeem myself."
        elif C_Points == 0:
            if B_Points == 1:
                b_nvl "{font=fonts/LemonMilk.otf}{i}You seem like a pretty cool dude you know that?{/i}{/font}"
                a_nvl "{font=fonts/LemonMilk.otf}{i}Uh, thanks.{/i}{/font}"
                b_nvl "{font=fonts/LemonMilk.otf}{i}Just being honest XD{/i}{/font}"
                b_nvl "{font=fonts/LemonMilk.otf}{i}Anyway now that you've got my number we can talk whenever we want!{/i}{/font}"
                b_nvl "{font=fonts/LemonMilk.otf}{i}Although I'm not much of a texter{/i}{/font}"
                b_nvl "{font=fonts/LemonMilk.otf}{i}Or a phone-caller{/i}{/font}"
                a_nvl "{font=fonts/LemonMilk.otf}{i}So why even give me your number?{/i}{/font}"
                b_nvl "{font=fonts/LemonMilk.otf}{i}So you'll have a female contact that isn't your mom lol{/i}{/font}"
                if britnotpretty:
                    b_nvl "{font=fonts/LemonMilk.otf}{i}Even if said contact supposedly isn't pretty{/i}{/font}"
                    "Shit..."
                    a_nvl "{font=fonts/LemonMilk.otf}{i}I'm sorry. I didn't mean that.{/i}{/font}"
                    b_nvl "{font=fonts/LemonMilk.otf}{i}Oh, I'm sure you didn't. Doesn't mean I'll forget it X'D{/i}{/font}"
                b_nvl "{font=fonts/LemonMilk.otf}{i}Anyway I'll stop buggin you. See ya whenever dum-dum!{/i}{/font}"
                nvl clear
                a_nvl "{font=fonts/LemonMilk.otf}{i}Okay...? See you.{/i}{/font}"
                nvl clear
                nvl hide dissolve
                "Man, this girl is weird."
                "Still, she is pretty cool, and she doesn't seem to hate me, so I suppose there's that."
            else:
                b_nvl "{font=fonts/LemonMilk.otf}{i}Just thought I'd get your number on the off-chance you wanted to talk or something{/i}{/font}"
                a_nvl "{font=fonts/LemonMilk.otf}{i}Ah. Well, I'm unpacking my room right now, so I'm a bit busy with that.{/i}{/font}"
                b_nvl "{font=fonts/LemonMilk.otf}{i}Cool beans. I'll let you get to that then.{/i}{/font}"
                a_nvl "{font=fonts/LemonMilk.otf}{i}Sorry.{/i}{/font}"
                b_nvl "{font=fonts/LemonMilk.otf}{i}Oh no problem at all I promise.{/i}{/font}"
                a_nvl "{font=fonts/LemonMilk.otf}{i}Okay, then. See ya.{/i}{/font}"
                b_nvl "{font=fonts/LemonMilk.otf}{i}See ya!{/i}{/font}"
                nvl clear
                nvl hide dissolve
                "I suppose I could've talked to her for a bit, but something about Brittney is just... weird."
                "I'm sure she's a nice girl, but her personality certainly isn't for everyone. Still, who knows? Maybe I'm judging a book by its cover."
        elif C_Points == 1:
            c_nvl "{font=fonts/LemonMilk.otf}{i}Just wanted to say that I liked hanging out today. You seem pretty cool.{/i}{/font}"
            a_nvl "{font=fonts/LemonMilk.otf}{i}Well, thanks! You seem pretty cool, too.{/i}{/font}"
            c_nvl "{font=fonts/LemonMilk.otf}{i}Lol thanks.{/i}{/font}"
            c_nvl "{font=fonts/LemonMilk.otf}{i}Anyway, that's all I really wanted to say.{/i}{/font}"
            a_nvl "{font=fonts/LemonMilk.otf}{i}Alrighty, then. Talk to you later.{/i}{/font}"
            c_nvl "{font=fonts/LemonMilk.otf}{i}Same.{/i}{/font}"
            nvl clear
            nvl hide dissolve
            "Huh. I kinda took Christeena to be the kind of introverted girl who wouldn't go out of her way to send a text to someone she hardly knew, but I guess I was wrong."
            "Although she was quick to end the conversation, if you even want to call it that. So I guess she's still a little shy."
        else:
            c_nvl "{font=fonts/LemonMilk.otf}{i}Just wanted to say that I liked hanging out today. You're a really sweet guy.{/i}{/font}"
            a_nvl "{font=fonts/LemonMilk.otf}{i}Well, thanks! I try my best.{/i}{/font}"
            c_nvl "{font=fonts/LemonMilk.otf}{i}:){/i}{/font}"
            c_nvl "{font=fonts/LemonMilk.otf}{i}Anyway, what's up?{/i}{/font}"
            a_nvl "{font=fonts/LemonMilk.otf}{i}Unpacking.{/i}{/font}"
            c_nvl "{font=fonts/LemonMilk.otf}{i}Oh, I'm not distracting you, am I?{/i}{/font}"
            a_nvl "{font=fonts/LemonMilk.otf}{i}You're okay, I promise.{/i}{/font}"
            c_nvl "{font=fonts/LemonMilk.otf}{i}You sure?{/i}{/font}"
            a_nvl "{font=fonts/LemonMilk.otf}{i}Positive.{/i}{/font}"
            c_nvl "{font=fonts/LemonMilk.otf}{i}Okay, then. :) still, I should let you work on that; we could always talk later if you wanted.{/i}{/font}"
            a_nvl "{font=fonts/LemonMilk.otf}{i}That sounds great! I'll let you know when I'm done for the night.{/i}{/font}"
            c_nvl "{font=fonts/LemonMilk.otf}{i}Okay :) talk to you later.{/i}{/font}"
            a_nvl "{font=fonts/LemonMilk.otf}{i}Talk to you later!{/i}{/font}"
            nvl clear
            nvl hide dissolve
            "Huh. I kinda took Christeena to be the kind of introverted girl who wouldn't go out of her way to send a text to someone she hardly knew, but I guess I was wrong."
            "She really seems happy at the idea of us talking, even though we hardly know each other."
            "I don't know whether to be excited that she's not scared of me or worried that she's some sort of hyper-obsessed girl."
        "Anyway, I better keep focused on this unpacking..."
        $ daydesc = 0
        $ replay = False
        $ renpy.end_replay()
    label progressday02:
        $ progress += 1
        jump progress
