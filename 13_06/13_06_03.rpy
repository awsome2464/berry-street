label firstday:
    $ current_track = "None"
    stop music fadeout 1.5
    scene bg fade
    with dissolve
    window hide
    pause 2
    if persistent.autosavewarning:
        pass
    else:
        "{b}Notice:{/b} Berry Street autosaves regularly, and a notification will be displayed when it does.{w=1.0}{nw}"
        $ renpy.notify("Game saved!")
        menu:
            "{b}Notice:{/b} Berry Street autosaves regularly, and a notification will be displayed when it does.{fast}"
            "Cool!":
                $ persistent.autosavewarning = True
                pause 2
    $ persistent.progress = 0
    $ renpy.save("1-1")
    if persistent.playthroughs < 1:
        $ warning_selector == 6
    else:
        $ warning_selector = renpy.random.randint(1, 50)
    python:
        if warning_selector == 1:
            warning_message = "Will {i}The Finale{/i} ever be finished? Only time will tell."
        elif warning_selector == 2:
            warning_message = "You have found key 1 of 6,000,405."
        elif warning_selector == 3:
            warning_message = "Do you miss me?"
        elif warning_selector == 4:
            warning_message = "What do you get when you cross a fish and an elephant? Swimming trunks!"
        elif warning_selector == 5:
            warning_message = "The following story is a work of fiction. Names, characters, places, and events are blah blah blah blah you get the picture."
        else:
            warning_message = "The following story is a work of fiction. Names, characters, places, and events are either the products of the author’s imagination or used in a fictitious manner."

    show text "[warning_message]" with dissolve
    $ renpy.pause(delay=7)
    hide text with dissolve

label firstdayreplay:
    if replay == False:
        $ renpy.save("10-1")
    $ B_Name = "???"
    $ b_hairtie = renpy.random.randint(0, 2)
    window hide
    pause 2
    show text "{size=+50}June, 2013{/size}":
        xalign 0.5 yalign 0.05
    show calendar june june_03:
        xalign 0.5 yalign 0.6
    show calendar_circle:
        xalign 0.37 yalign 0.41
    with dissolve
    $renpy.pause(delay=4)
    hide text
    hide calendar
    hide calendar_circle
    with dissolve
    pause 1
    $ current_track = "\"New Life\""
    play music new_life

    scene bg car with dissolve
    window show dissolve

    show harry a1 mad straight blank at close_left_h with dissolve
    with Pause(.1)
    h "Are we there yet?"
    show ginger a2 straight sad grin at tworight with dissolve
    g "Not yet. {w}But we'll be there soon, I promise!"
    h small scream "You've been saying that for hours!"
    hide ginger
    show fred a1 straight casual grin glasses at tworight
    with dissolve
    with Pause(.1)
    f "Just be patient, Son. Okay?"
    h level blank left "Okaaaaaay."
    hide harry
    hide fred
    with dissolve
    with Pause(.1)
    "I wasn't paying too much attention to what they were saying."
    "I was more focused on watching the outside world from my window."
    "I slowly watched the big city transform to nothing but corn fields and dirt roads."
    "It was like going from your home planet to another, going from comfort to the unknown."
    "It truly terrified me."

    show ginger a2 straight casual blank at middle with dissolve
    with Pause(.1)
    g "You're awfully quiet back there, Alex."
    a "Hm?"
    hide ginger
    show fred a1 straight mad glasses blank at middle
    with dissolve
    with Pause(.1)
    f "Daydreaming again?"
    a "..."
    f sad "Look, I know you're still upset about the move, but think of this as a fresh new start for the Sprouse family!"

label choice1:
    if persistent.choice_1 == 1:
        jump whateveryousay
    elif persistent.choice_1 == 2:
        jump dontwantastart
    else:
        menu:
            a "..."

            "Whatever you say.":
                $ persistent.choice_1 = 1
                jump whateveryousay

            "I don't want a fresh start.":
                $ persistent.choice_1 = 2
                jump dontwantastart

    label whateveryousay:
        a "Sure, whatever you say, Dad."
        f level "Well, at least there's some sort of optimism, I suppose."
        hide screen skipchoice
        jump continuemoveconvo

    label dontwantastart:
        a "But what if I didn't want a fresh start?"
        f mad "I..."
        f sad "*sigh*"
        hide screen skipchoice
        jump continuemoveconvo

label continuemoveconvo:
    hide fred with dissolve
    with Pause(.1)
    "I really had to give it to Dad for trying his hardest to make this move easy on us."
    "It's not like I had any close friends that I had to say goodbye to or anything..."
    "Heck, the one true friend I actually had moved away years ago."
    "But when you've spent all 16 years of your life in the same home in the same city, only to have it taken away from you..."
    "...it's just not easy."

    show fred a1 straight glasses casual grin at middle with dissolve
    with Pause(.1)
    f "Well, I still want to thank you for being cooperative about this."
    f "I know this isn't easy, but it's going to be for the better."
    show fred at twoleft
    show ginger a2 straight raised grin at tworight
    with easeinright
    with Pause(.1)
    g "Besides..."
    g sad "At least Donald will be there to greet you once we get there!"
    hide ginger
    hide fred
    with dissolve
    with Pause(.1)
    "She had me there. That was honestly the only true reason I was okay with the move."
    "Donald happens to be the 'one friend' I just mentioned. The one who had moved away years ago."
    "We'd stayed in touch a little bit, but we were both so busy with school and such, we never really got to actually see each other."
    "But by some miracle, his dad managed to get my dad a job at the same company as him. And the rest is history."

    show fred a1 straight glasses casual grin at middle with dissolve
    with Pause(.1)
    f "Anyway, according to the GPS, we should be arriving in about another half hour."
    show fred at tworight
    show harry a1 sad closed_smile straight at close_left_h
    with easeinleft
    pause .1
    h "Hallelujah!"

    "At least we were almost done."

    hide harry
    hide fred
    with dissolve
    scene bg fade
    with dissolve

## Intro

    with Pause(1)
    window hide dissolve
    nvl show dissolve
    narrate """
    My name is Alex Sprouse.

    On June 3rd, 2013, I, along with my parents and younger brother, moved from my hometown of Chicago to Smalltown, IL.

    I didn't know it at the time, but that move was going to be the most important thing that ever happened to me.

    So, please, sit back, relax, and follow me on this journey of my past.

    A journey that all began when I moved...

    ...to Berry Street.
    """
    nvl clear
    nvl hide dissolve
    with Pause(1)

    show text "{size=+15}Good Tales presents{/size}" with dissolve
    with Pause(3)
    hide text with dissolve

    with Pause(1)

    $ current_track = "None"
    stop music fadeout 5.0
    show title at truecenter with dissolve
    with Pause(5)
    hide title with dissolve
    with Pause(1)


    show text "{size=+20}Act 1\n{size=-5}\"Welcome to Smalltown\"{/size}"
    with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)

## Scene 1
    window show dissolve
    with Pause(.1)
    f_o "We're here!"

    "I quickly opened up my eyes."
    "I didn't even realize that I had passed out."
    "I looked outside of my window to see..."

    window hide dissolve

# Show House

    with Pause(1)
    scene bg house_s
    with dissolve
    with Pause(1)

    window show dissolve

    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    "...a house."
    "It was a pretty simple-looking house, but I suppose saying you live in a house is better than saying you live in a cramped apartment."
    "That was admittedly one thing I liked about the move."

    show ginger a2 raised straight grin at middle with dissolve
    with Pause(.1)
    g "Well, go on!"
    g "Let's get out there and take a look!"
    hide ginger
    show harry a1 straight casual closed_smile at middle
    with dissolve
    with Pause(.1)
    h "Yay!"
    hide harry with dissolve
    with Pause(.1)

# Leave Car

    "We exited the car and I got a better look of the house."
    "Two stories, one garage."
    "Definitely an improvement from an apartment in the city."

    show ginger a2 straight casual grin at middle with dissolve
    with Pause(.1)
    g "Hey, Alex?"
    a "Yeah?"
    $ current_track = "None"
    stop music fadeout 3.0
    g raised "What's that over there?"
    hide ginger with dissolve
    with Pause(.1)
    "I looked to where she was pointing."
    "At first, I couldn't see what she was referring to, but then..."

    a "..."
    a "NO WAY!"

# Show Donald

    $ current_track = "\"Brotato Chips\""
    play music donald
    show don b1 straight grin casual at middle with dissolve
    with Pause(1)
    "I couldn't believe my eyes..."
    "He was really here!"

    a "Donald!!"
    d smile raised "Well, if it ain't Mr. Alexander Sprouse!"
    hide don with dissolve
    with Pause(.1)

# Donald/Alex Hug

    "He jogged over, and we hugged tightly."
    "Even though I knew he'd be here, the fact that he truly was right here in front of me was certainly a relief!"

# Stop Hug

    show don b1 straight grin casual at close_d
    with dissolve
    with Pause(.1)
    a "I haven't seen you in years!"
    $d_blink = False
    d closed smile sad "Same here, man!"
    $d_blink = True
    d straight grin sad "You should've seen my face when my parents told me that you were moving here!"
    a "You should've seen MY face when my parents told me we were moving here!"
    show don at close_right_d zorder 2
    show fred a1 straight glasses raised grin at threeleft zorder 1
    show ginger a2 straight level grin at middle zorder 1
    with easeinleft
    pause 0.1
    f "Really? Because I seem to recall that you were against the idea of moving."
    a "That was before you mentioned Donald!"
    g mad "Even then, we basically had to drag you here!"
    a "..."
    hide fred
    hide ginger
    show don at close_d
    with easeoutleft
    pause 0.1
    pause .1
    $d_blink = False
    d b1 closed smile sad "Don't sweat it, man; I get it. Moving away from what you know is hard."
    $d_blink = True
    d straight grin level "At least you had the advantage of knowing a guy. I had nobody when I moved here."
    a "I suppose that's a fair argument."

    show don sad
    "Donald then noticed my brother, and his smile grew even bigger."

    show don:
        ease 0.5 tworight
    show harry a1 casual blank straight at twoleft with easeinleft
    with Pause(.1)
    d smile "Holy smokes! Is that little Harry?"
    h mad frown small "Hey! I'm not little!"
    d grin raised "Well, not anymore, you're not!"
    hide harry
    show don casual at middle
    with easeoutleft
    with Pause(.1)

# Turn to Donald

    d "Man, Al, we have a lot to catch up on, huh?"
    a "Definitely!"
    a "But we still gotta get our stuff into the house..."
    hide don
    show ginger a2 straight sad grin at middle
    with dissolve
    with Pause(.1)
    g "Why don't you boys go to Donald's house to talk and have some fun? Dad and I will take care of the boxes."
    a "Are you sure? Because I can help if you-"
    show ginger at tworight
    show fred a1 straight casual grin glasses at twoleft
    with easeinleft
    with Pause(.1)
    f "Son, like Donald said, you guys have some catching up to do."
    f "We'll get the boxes in the house and you can unpack your things later, okay?"
    f sad "Think of this as a reward for being so cooperative about this whole move."
    a "Well, okay! Thanks!"
    g casual "Don't mention it, Sweetie. Run along, now! Have fun!"
    f level "Just be back by sundown, okay?"
    a "Okay!"
    g sad "It was nice to see you again, Donald!"
    show fred at threeleft
    show ginger at middle
    show don b1 straight grin casual at threeright
    with easeinright
    with Pause(.1)
    d "Same here, Mrs. Sprouse!"
    f casual "See you around, Donald."
    d raised "See you around, Mr. Sprouse."
    hide don with easeoutright
    with Pause(.1)
    show ginger:
        ease 0.5 xalign 0.9
    show harry a1 casual straight blank at middle with dissolve
    pause .1
    g casual "So, Harry, let's see who can get the most boxes in the house!"
    f raised "Well, it's obvious that I will."
    h mad scream small "Nuh-uh!"
    hide ginger
    hide fred
    hide harry
    with dissolve
    with Pause(.1)
    "Harry then ran to the trailer and grabbed a box."

    show don b1 grin straight casual at close_d with dissolve
    with Pause(.1)
    a "Well, that was easy."
    d level right "C'mon; let's walk over to my place. It's just a couple houses over."

    hide don with dissolve
    with Pause(.1)
    "It was in that moment when I actually stopped to look around at the street we were on."

# Show Street

    "There were only 8 houses on the entire street."
    "It was pretty small and seemed to be in the middle of nowhere, but I could see what looked like a small street leading to town on one end and a lake on the other."
    "We then started walking towards his house."

# Hide Street

    scene bg house_ut
    with dissolve
    with Pause(.1)
    "When we were in front of the house between ours, he started talking."
    show don b1 straight sad grin at close_d with dissolve
    with Pause(.1)
    d smile "You're lucky you moved here in the summer; that gives you a chance to explore what all there is to offer here!"
    a "How much is there to offer?"
    d level blank "..."
    d left "Well, not that much, if I'm being honest."
    d straight sad grin "But it's certainly better than nothing!"
    a "Point taken."
    $ current_track = "None"
    stop music fadeout 2.0
    b_o "Hey, Donnie!"
    show brit b1 straight casual grin zorder 1:
        middle
        ease 0.5 twoleft
    show don casual at close_right_d zorder 2 with easeinleft

# Meet Brittney

    with Pause(.5)
    $ current_track = "\"Oddball\""
    play music oddball
    "We turned around to see a girl standing on the porch."
    hide don
    show brit at middle
    with easeoutright
    pause .1
    "She looked a tad older than us, and certainly was tall for a girl; maybe she's an upcoming senior?"
    "And as tall as she was, she was also very thin, having next to no curves on her body, not even on her chest."
    "Honestly, not to be offensive, it was kinda like looking at a female head on a male body."
    "..."
    "I don't suppose there's a way to put that without sounding offensive."
    "Regardless, she quickly jogged over to us."
    hide brit
    show don b1 left casual smile at tworight
    with dissolve
    with Pause(.1)
    d "Hey there, stranger!"
    show brit b2 straight raised grin at twoleft with easeinleft
    with Pause(.1)
    b "Aren't you going to introduce me to your new friend?"
    d dot small level "'New'?"
    d straight grin mad "I'll have you know that I've known this dude longer than I've known you!"
    b casual "No kidding?"
    b right "Would this happen to be the old childhood friend you mention every now and then?"
    d casual left "It would, indeed!"
    b b1 straight raised grin "Well, that's all the more reason to meet him!"
    d straight "Very well, then!"
    d "Alex, this is Brittney."
    $ B_Name = "Brittney"
    show brit small level hanging
    $d_blink = False
    d closed sad smile "She's my girlfriend of 3 years!"
    show brit straight mad blank at punchleft
    with Pause(.15)
    play sound punch
    show white
    with Pause(.05)
    hide white
    $d_blink = True
    d small sad wide "OUCH!"

    "She punched Donald in the shoulder."
    "It wasn't a light, playful punch, either; she really was trying to hurt him."

    b b2 "How about you try that again?"
    d straight blank "Fine. You're right, I'm sorry."
    d grin casual "We've actually been together for a few weeks{nw}"
    show brit b1 small at punchleft
    with Pause(0.15)
    play sound punch
    show white
    with Pause(.05)
    hide white
    d small sad wide "OUCH!"
    d straight blank "Uh... a few days?"

    show brit straight frown
    "She held up her fist again."

    d level blank "Okay, okay! We're not dating!"
    b b2 straight casual opened_smile "And we never will be."

    hide don
    show brit b1 grin at middle
    with easeoutright
    with Pause(.1)
    "She then looked at me with a grin."
    show brit:
        ease 0.5 close_b
    with Pause(.6)
    b "Alex, right?"
    a "Yeah. Alex Sprouse."
    b opened_smile "Brittney Usher."

    "She then held her fist in front of her. Following suit, I bumped her fist with my own."
    "As we shook hands, I couldn't help but notice that there was something off about her mouth..."
    "Was that... a chipped tooth?"

    b b2 huhu right level "It's a pleasure to meet someone else capable of putting up with Donald Waters for longer than 5 seconds."
    show brit zorder 2:
        ease 0.5 xalign 0.1 yalign 0.2
    show don b1 straight mad blank at tworight zorder 1 with easeinright
    with Pause(.1)
    d "Hardy-har-har."
    show brit:
        ease 0.5 twoleft
    pause 0.6
    show brit at twoleft
    b b1 straight sad grin "So, what are you boys up to?"
    d casual grin "We were just going to head to my house to hang out and catch up."
    b level "I see, I see."
    b b2 "Then I'll just leave you boys to do your thing."
    d blank "Oh, you don't want to hang out with us?"
    b b1 sad opened_smile "Nah, it's cool, dude. I understand."
    b "If I saw my friend for the first time in years, I'd want to spend time with just them."
    d raised grin "You sure? I mean, I'm sure Alex wouldn't mind getting to know you better."
    b b2 mad grin "Unless he plans on moving again tomorrow, he'll have plenty of time to get to know me."
    d level blank "..."
    d grin "Well, Alex, what do you think?"

    show brit raised
    "Brittney looked over at me with a curious smile, anticipating my answer."
    hide don
    show brit at middle
    with easeoutright
    with Pause(.1)
    "Well, she does look relatively harmless..."
    "Besides, if she's a friend of Donald's, how bad can she be?"

    show brit at twoleft
    show don b1 straight grin level at tworight
    with easeinright
    with Pause(.1)
    a "Well, I don't mind hanging out with a friend of Donald's."
    d left smile "See?"
    b b1 mad opened_smile "Alright, alright, if you insist. I'll let my mom know real quick, and I'll be right over!"
    d straight sad grin "Sounds like a plan!"
    show brit grin at punchleft zorder 3
    with Pause(.15)
    play sound punch
    show white zorder 4
    with Pause(.05)
    hide white
    d small wide "OUCH!"
    d straight mad blank "What did I do now?"
    $b_blink = False
    b closed closed_smile sad "Nothing; I just like to punch you."

    hide brit with easeoutleft
    with Pause(.1)
    $b_blink = True
    "Brittney then ran into the house with a giant grin plastered on her face."
    show don raised grin at middle with easeinright
    d "She's quite the character, don't you think?"
    a "She's something, alright."
    d level right "Anyway, let's get going to my house."
    a "Sounds good to me!"
    $ current_track = "None"
    stop music fadeout 1.5
    hide don with easeoutright
    with Pause(0.5)

# Donald's House

    $ current_track = "\"Brotato Chips\""
    play music donald
    scene bg house_w
    with dissolve

    "We then went to Donald's house."
    "It was a pretty average-sized house, not too dissimilar to mine."
    "At least, I'm assuming so, since I haven't even entered my own home yet."

    scene bg living_w
    with dissolve

    show don b1 straight grin casual at close_d with dissolve
    with Pause(.1)
    d "Brittney should be on her way by now."
    a "Sounds good."
    a "..."
    a "Where are your parents?"
    d level "On a cruise for their anniversary."
    a "They just let you stay at home by yourself??"
    d raised smile "Dude, I'm almost 17. I'm basically an adult."
    a "I know, but my parents would never allow me to be home alone when they're out of town."
    a "ESPECIALLY if a girl was coming over without their knowledge."
    $d_blink = False
    d closed sad "Yeah, your parents were always kinda overprotective, weren't they?"
    $d_blink = True
    d raised straight grin "But my parents aren't exactly the type that let me do whatever, either, you know."
    d casual "Take Brittney, for instance."
    d "If it was some girl they never or barely met, her coming over uninvited with them not home would never fly."
    d "But they know Brittney and trust her. They know that she won't let anything bad happen."
    d level blank right "Much to my disappointment."
    d raised "Heck, at times, I swear they see her as a babysitter for me."
    a "Babysitter??"
    d straight casual "She keeps me out of trouble and from doing stupid stuff."
    d mad grin "Well, for the most part."
    $ current_track = "None"
    stop music fadeout 1.0
    hide don with dissolve
    pause .1
    play sound door_open
    "The door then opened up, revealing Brittney Usher in all her glory."

    show don b1 straight casual smile at tworight with dissolve
    d "Hey, speak of the devil!"
    $ b_partial = True
    show brit b2 straight level blank at twoleft with easeinleft
    with Pause(.1)
    b "Nice to see you, too, Donnie."
    d blank "It's just an expression."
    $ b_partial = False
    show brit b1 straight raised grin
    b "I know. I just like to mess with you."
    $ current_track = "\"Oddball\""
    play music oddball
    b b2 casual "So, you guys were just talking about me, then?"
    a "Yeah, about how you pretty much keep Donald in line."
    b b1 casual opened_smile "'Pretty much'? That's, like, my sole purpose in life!"
    $d_blink = False
    d closed sad smile "If that's your sole purpose, then you're kinda failing at life."
    show brit mad blank at punchleft
    with Pause(.15)
    play sound punch
    show white
    with Pause(.05)
    hide white
    $d_blink = True
    d small wide "OUCH!"
    d straight mad blank "Stop punching me!"
    b b2 frown "Stop giving me reasons to punch you!"
    a "..."
    a "So, how exactly are you two friends, if I may ask?"
    show brit b1 casual blank
    d raised blank "What do you mean?"
    a "You seem more like you don't get along."
    b b2 opened_smile "Oh, that's just how our friendship rolls."
    b "In fact, it all started when my family first moved here and I introduced myself, with him responding with the worst pickup line I'd ever heard."
    b raised "What was it, again?"
    d small sad "..."

    "Donald quickly got an embarrassed look on his face."
    "That doesn't seem like him at all."

    b huhu right level "C'mon, Donnie; you remember."
    d "..."
    b raised straight opened_smile "Fine, I'LL tell him."
    d "..."

    "I don't feel like this is going to end well."

    b "He said..."
    b b1 mad "{i}'Are your parents retarded? Because you sure look special!'{/i}"
    a "Donald!!"
    d straight mad wide "I thought it was funny!"
    b b2 right grin "Well, it was, afterwards."
    d blank left "Because you slapped me across the face!"
    $b_blink = False
    b b1 closed opened_smile sad "Of course!"
    a "That doesn't really answer my question. If anything, it only makes me ask it even more."
    hide don
    show brit at middle
    with easeoutright
    $b_blink = True
    b b2 straight level blank "Well, after I slapped him, I ran back to my house."
    b left "I honestly didn't want to see him again."
    b b1 straight casual "But a half hour or so later, there was a knock on my door."
    b "Lo and behold, he was standing on my porch with the biggest look of embarrassment I'd ever seen."
    $b_blink = False
    b b2 closed sad opened_smile "The red mark on his cheek was a cute touch."
    $b_blink = True
    b straight level grin "And it was then that he apologized and started his introduction over, this time a little less offensive."

    "{i}'A little??'{/i}"

    b b1 blank "It was clear that Donald was the kind of guy to speak before thinking."
    b casual "But the fact that he apologized and truly meant it?"
    b grin "I thought that maybe this guy has something good in him, after all."
    $b_blink = False
    b b2 closed closed_smile sad "So, I unofficially became his 'tutor', for a lack of a better term."
    a "'Tutor'? For what?"
    $b_blink = True
    b straight casual grin "For behavior!"
    b b1 "I help make sure he doesn't act like a jerk to people who don't deserve it."
    b raised"And if he DOES act like a jerk, I correct him."
    a "By punching him the arm?"
    b opened_smile "Hey, it works, right?"
    show brit at twoleft
    show don b1 mad blank straight at tworight
    with easeinright
    d "Not really."
    $ b_partial = True
    show brit b1 level blank
    "Brittney raised her fist."

    d sad "I mean, yes! Definitely!"
    a "..."
    a "You guys are weird."
    $ b_partial = False
    show brit b1 straight casual opened_smile at twoleft
    show don casual smile
    bd "Thank you!"

    "That wasn't a compliment."

    $ current_track = "None"
    stop music fadeout 1.0
    b grin "Anyway, enough chat. Let's do something!"
    $ current_track = "\"Ivories and Ebony\""
    play music ivories_and_ebony
    d grin raised "Alright; what did you have in mind?"
    b b2 right "I'm up for anything you guys want."
    d "Hm..."
    a "No way!"
    show brit straight blank
    d casual blank "What?"
    hide don
    hide brit
    with dissolve
    with Pause(.1)

    "I glanced into Donald's living room and saw an old yet nostalgic gaming console hooked up to the TV."

    show don b1 straight casual blank at middle with dissolve
    with Pause(.1)
    a "You still have the 64??"
    d raised smile "Well, DUH!"
    d "Everyone knows that's where the best games of all time can be found!"
    show don at tworight
    show brit b1 straight sad grin at twoleft
    with easeinleft
    with Pause(.1)
    b "Ah, video games..."
    b b2 left "Not gonna lie, they're not really my thing."
    b "I'm more of a physical activity kind of gal."
    a "Oh."
    a "Well, I suppose we could do something else..."
    b b1 small hanging "No, no!"
    b b2 straight grin "If you guys wanna play together, I'd be happy to watch. Maybe I'll even learn why men like them so much."
    d straight casual grin "Well, we could always go shoot some hoops in the driveway if you'd be more interested in that."
    b left level derp "Hmm... {w}That does sound pretty tempting."
    b straight blank "But I get the feeling that Alex here isn't a fan of sports."
    a "Huh? What gave you that impression?"
    $ b_partial = True
    b b1 closed_smile mad "Call it a hunch."
    a "..."
    a "Well, I mean, I swam competitively in the summertime for a few years."
    $ b_partial = False
    show brit b2 straight casual grin at twoleft
    b "Huh. That's one more sport than I thought you'd be in."
    a "I only said one."
    $ b_wink = True
    b mad tongue "That's the joke, dum-dum."
    d level "Anyway, what's it going to be? Video games or basketball?"
    $ b_wink = False
    show brit b2 straight casual opened_smile at twoleft
    b "I vote hoops."
    d casual "I vote gaming."
    show brit raised
    show don raised
    bd "Alex?"

label choice2:
    hide screen skipchoice
    if persistent.choice_2 == 1:
        a "Hm..."
        jump videogames_b
    elif persistent.choice_2 == 2:
        a "Hm..."
        jump basketball_b
    else:
        a "Hm...{nw}"

# Video Games or Basketball

        menu:
            a "Hm...{fast}"

            "Video Games.":
                $ persistent.choice_2 = 1
                jump videogames_b

            "Basketball.":
                $ persistent.choice_2 = 2
                jump basketball_b

    label videogames_b:
        $ B_Videogames = True
        $ B_Basketball = False
        $ D_Points += 1
        a "Not gonna lie, I think the best way for Don and I to bond again after all these years is to go back to what we always did best: playing video games that are older than us!"
        a "So my vote is on video games."
        d casual smile "Then it's decided!"
        hide screen skipchoice
        d grin "Let's all go find a game to play."
        b b1 casual grin "Very well."
        b right "Who knows? Maybe you guys can get me into a new hobby."

        jump hangout_b

    label basketball_b:
        $ B_Basketball = True
        $ B_Videogames = False
        $ B_Points += 1
        a "I suppose I could use some exercise."
        a "So my vote is on basketball."
        d casual smile "Then it's decided!"
        hide screen skipchoice
        d grin "I'll go grab a ball from the garage."
        b b1 casual grin "Sounds great!"
        b mad closed_smile "Can't wait to kick you guys' butts out there!"


        jump hangout_b

    label hangout_b:
        hide don
        hide brit
        with dissolve
        with Pause(.1)
        window hide dissolve
        if B_Videogames:
            nvl show dissolve
            with Pause(.1)
            narrate "And so, we picked a game that Donald and I found fun and Brittney found intriguing."
        if B_Basketball:

            scene bg basketball_w
            with dissolve
            nvl show dissolve
            with Pause(.1)
            narrate "And so, we all went outside and played some rounds of HORSE."

        narrate """
        While we all hung out, Donald and I caught up a bit on our lives.

        He was a pretty average student when it came to his grades, but in terms of popularity, everyone seemed to know the name Donald Waters.

        Of course, with a supposedly small class size, it's easy to know the names of everyone.

        Brittney, on the other hand, seemed to be the opposite.

        As I suspected, she was a year ahead of Donald and I, this upcoming school year being her senior year.

        She was doing very well academically, receiving plenty of scholarships to plenty of big colleges across the country.

        She was also a very good athlete, as well, her best and primary sport being baseball, though she also loved basketball and volleyball.
        """

        if B_Basketball:
            narrate "And judging by the fact that she won the first two rounds of HORSE, I can certainly say she's no novice."

        nvl clear
        narrate """
        Yet despite all that, she really didn't seem to have many friends besides Donald and a few teammates.

        She claims it doesn't bother her, saying too many friends can distract you from important things like homework and workouts.

        I mean, I guess she had a point.

        Though I have less friends than her and the focus of a goldfish.

        Still, she seems pretty fine with it, so who am I to complain?
        """

# Sunset
        nvl clear
        narrate """
        Finally, it was almost sunset.

        Not gonna lie, we all lost track of how long we were playing, but it was worth it if it meant we could all hang out together for a while.
        """
        nvl clear
        nvl hide dissolve
        window show dissolve
        with Pause(.1)
        show brit b2 casual straight grin at twoleft
        show don b1 straight casual grin at tworight
        with dissolve
        with Pause(.1)
        a "Well, I think it's about time I head home."
        b b1 opened_smile "Same; I told my mom I'd only be gone for a few hours."
        b grin right "It was nice hanging out with you again, Donald."
        d left smile "Likewise, Brittney!"
        b straight "And it was nice to meet you, Alex!"
        if B_Videogames:
            b b2 mad opened_smile "Thanks for showing how nerdy you and Donald can get!"
        if B_Basketball:
            b b2 mad opened_smile "Thanks for proving that you're not as weak and nonathletic as you look!"
        a "Uh... thanks?"
        b b1 casual grin "Well, adios, amigos!"
        hide brit with easeoutleft
        with Pause(.1)

        if B_Videogames:
            "Brittney then exited the house to head home."
        if B_Basketball:
            "Brittney then jogged next door to head home."

        show don straight grin at middle with easeinright
        d "So, Alex..."

    label choice3:

        if persistent.choice_3 == 1:
            d "What do you think of her?"
            jump britisfunny
        elif persistent.choice_3 == 2:
            d "What do you think of her?"
            jump britischill
        elif persistent.choice_3 == 3:
            d "What do you think of her?"
            jump britisattractive
        elif persistent.choice_3 == 4:
            d "What do you think of her?"
            jump britisinteresting
        else:

            d "What do you think of her?{nw}"

# Thoughts on Brittney

            menu:
                d "What do you think of her?{fast}"

                "She's funny.":
                    $ persistent.choice_3 = 1
                    jump britisfunny

                "She's chill.":
                    $ persistent.choice_3 = 2
                    jump britischill

                "She's attractive.":
                    $ persistent.choice_3 = 3
                    jump britisattractive

                "She's interesting.":
                    $ persistent.choice_3 = 4
                    jump britisinteresting

    label britisfunny:
        a "She's got quite a sense of humor."
        $d_blink = False
        d closed sad smile "True that!"
        d "It matches my style of humor perfectly!"
        hide screen skipchoice
        a "Isn't your style of humor why she constantly punches you and originally didn't want to ever see you again?"
        $d_blink = True
        d straight raised grin "That's in the past, man."
        d "You can't deny that me and her love our playful insults."
        a "That's true."
        $ Brit_Thoughts = 1
        jump goodfriends

    label britischill:
        a "She's pretty chill and mellow."
        $d_blink = False
        d closed sad smile "True that!"
        d "Not many things get under that girl's skin."
        hide screen skipchoice
        a "Such as your antics?"
        $d_blink = True
        d straight raised grin "Ah, she's just playing with that."
        d "It's all an act to mess with me."
        a "If you say so..."
        $ Brit_Thoughts = 2
        jump goodfriends

    label britisattractive:
        a "She was certainly blessed with some good looks."
        $d_blink = False
        d closed sad smile "True that!"
        d "Those eyes, that smile, that body..."
        hide screen skipchoice
        a "All things that are out of your league."
        $d_blink = True
        d straight raised grin "Ah, screw you."
        d "You're just jealous!"
        a "Keep telling yourself that..."
        $ Brit_Thoughts = 3
        jump goodfriends

    label britisinteresting:
        a "She's definitely pretty interesting and mysterious."
        $d_blink = False
        d closed sad smile "True that!"
        d "You never know what's going on inside that girl's head."
        hide screen skipchoice
        a "She probably has several ways of killing you on the mind at all times."
        $d_blink = True
        d straight raised grin "Yeah, yeah, very funny."
        d "Though sometimes it would be nice to know what she thinks about certain stuff..."
        a "I suppose so."
        $ Brit_Thoughts = 4
        jump goodfriends

    label goodfriends:
        a "Well, regardless, I have a better understanding of how you two can be pretty good friends."
        d left level grin "Yeah..."
        $ current_track = "None"
        stop music fadeout(3)
        "Donald's smile went from a natural one to a forced one."

        a "You okay?"
        d blank "Yeah, it's just..."
        d straight "I just wish we could be more than that, you know?"
        if Brit_Thoughts == 3:
            d "You said it yourself: she's got some good looks."
        else:
            d "I don't know about you, but I think she's got a lot of good things about her, physically."

        a "Looks aren't everything."
        d sad "I know, but..."
        d "Call it a gut feeling, but I think she's the one for me, bro."
        a "How do you figure?"
        d grin "Again, just a gut feeling."
        a "Well, no offense, but this isn't the first time I've heard you say that about a girl."
        d blank level "Fair enough."
        d raised grin "Fair enough.{fast} But there's something different about her that just makes me want to be with her."
        d right "Maybe it's God, maybe it's fate..."
        d straight "...but I just get this feeling that Brit and I are meant to be together."
        a "..."
        d mad blank "What's that look for?"
        a "What look?"
        d raised "You looked like I was crazy or something."
        a "I just don't want you to set yourself up for disappointment, that's all."
        a "Again, she shows no signs of romance around you."
        d level left "Still... if I could go on just one date with her..."
        a "..."
        d "..."
        $ current_track = "\"Chillaxin'\""
        play music chillaxin
        a "Anyway, I should probably get home."
        d straight sad grin "Good idea."
        d "'Night, Al."
        a "'Night, Don."
        hide don with dissolve
        with Pause(.1)

        "Donald and I bro-hugged and I started walking home."

        d_o "Hey, Al!"

        "I turned back around to my childhood friend."

        show don b1 mad straight grin at middle with dissolve
        with Pause(.1)
        a "Yeah?"
        d "It was nice to see you again!"

        "I gave a sincere grin and nodded."

        a "Likewise!"
        $ current_track = "None"
        stop music fadeout 1.0
        hide don with dissolve
        with Pause(.1)

# Home

        scene bg house_s
        with dissolve

        "Finally, I'm entering my new home."
        $ current_track = "\"Home Life\""
        play music home_life
        "It's crazy to think that my first day in my new life wasn't spent in the house I was actually living in."
        "Oh, well; I'll have plenty of time to spend here, I suppose."
        play sound door_open
        scene bg living_s_m
        with dissolve
        "I opened up the door and saw my mom opening up a box in the living room."

        show ginger a2 casual straight grin at middle with dissolve
        pause .1
        g "Hey, Alex!"
        a "Hi, Mom."
        g sad "How was your day?"
        a "It actually wasn't that bad."
        a "Donald and I caught up a bit, and I got to get to know our next-door neighbor, Brittney."
        g casual "How is she?"
        a "She's pretty cool. I can see why Donald hangs out with her."
        g sad "Well, I'm glad you're already making a new friend!"
        a "I don't know about 'friend', Mom. More like 'acquaintance'."
        g level blank "Well, still."
        g casual grin "I'm glad you and Donald are getting along. I was a little afraid that all the time you spent apart would cause you boys to have conflicting personalities."

        if B_Basketball:
            a "Still too early to tell, I suppose, but we at least still like to shoot hoops."
        if B_Videogames:
            a "Still too early to tell, I suppose, but we at least still like to play classic video games."

        g raised "That's something, I suppose."

        "I let out a giant yawn."

        a "Well, if you don't mind, I'm going to head to bed."
        g casual "Well, alright. Your toothbrush and such is already laid out in the upstairs bathroom."
        g "As for your bed, it's just a mattress for now."
        a "As long as I have something comfy to sleep on, I don't care."
        g sad "I know."
        a "Don't forget to get some rest, yourself."
        g level "I was just about to finish this box and then head to bed, as well."
        a "Good deal. Goodnight, Mom."
        g sad "Goodnight, Alex. I love you!"
        a "Love ya, too."
        hide ginger with dissolve
        $ daydesc = 0
        $ replay = False
        $ renpy.end_replay()
label progressday01:
        $ progress += 1

        jump progress
