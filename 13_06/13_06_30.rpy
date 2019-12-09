label nhie_start:
    $ B_Name = "Brittney"
    $ C_Name = "Christeena"
    $ b_hair = 0
    $ b_hairtie = renpy.random.randint(0, 2)
    show text "{size=+50}June, 2013{/size}":
        xalign 0.5 yalign 0.05
    show screen calendarOs
    show calendar june june_30:
        xalign 0.5 yalign 0.6
    show calendar_circle:
        xalign 0.31 yalign 0.88
    with dissolve
    if replay == False:
        $ persistent.todays_date = "June 30th, 2013"
        $ renpy.notify("Game saved!")
        $ renpy.save("1-1")
    pause 4
    hide text
    hide screen calendarOs
    hide calendar
    hide calendar_circle
    with dissolve
    pause 1
    window show dissolve
    hide screen notify
    $ renpy.block_rollback()
    "I told my mom about Donald's last-minute plan to hang out."
    "Although I did conveniently fail to mention it would be at a cabin buried in the woods."
    "She was hesitant at first, but she finally agreed, saying that I should try not to be out too late."
    "With that, we had our dinner (which consisted of frozen pizzas), and I was on my way."

    scene bg house_w_s with dissolve
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country

    "It was getting pretty chilly out, so I made sure to put on some jeans and a jacket before heading over to the cabin."
    "I walked past Donald's house and was about to cross the street towards the pond before I heard a voice calling out from behind me."

    b_o "Yo!"

    "I turned around to see Brittney jogging towards me."
    "Christeena seemed to be right behind her, albeit a tad slower."
    "A second or so later, Brittney caught up to me."

    show brit d2 straight casual grin at close_b with dissolve
    with Pause(.1)
    b d1 opened_smile "Perfect timing!"
    b "Now we can all walk over together!"
    a "Yeah, I guess we can."
    a "Which is probably for the best; I'm not fully sure I remember the way to the cabin."
    b d2 raised grin "Don't worry, it's not THAT hidden."

    "Christeena then caught up to us, seeming a bit out of breath."

    show brit:
        ease 0.5 tworight
    show chris d1 straight sad blank at twoleft with easeinleft
    with Pause(.1)
    a "You okay?"
    c "Yeah, it's just hard to catch up to an athlete like Brittney."
    b left level huhu "My athleticism has nothing to do with your inability to--"
    b straight casual blank "..."
    b left level "Nevermind."
    b d1 straight casual grin "Now let's go before it gets too dark to see."
    a "Roger that!"
    c d2 casual grin "Alright!"
    hide brit
    hide chris
    with dissolve
    with Pause(.5)

    # Woods Sunset
    scene bg woods with dissolve
    with Pause(.1)

    "We then entered the woods, with Brittney at the lead."
    "Since there was still some daylight left, it was easy to see where we were going."
    "She was right; it really wasn't that hidden, after all."
    "Granted, you still had to go off the path to find it, but nothing some memorization can't fix."
    "Finally, we found it."

    scene bg cabin_e_s with dissolve
    with Pause(.1)

    "The cabin was there in all its glory."
    "The lights could be seen coming from all the windows, implying that someone was inside."

    show brit d1 straight casual grin at close_left_b with dissolve
    with Pause(.1)
    b "I'm going to assume it's Donald."
    b sad small hanging "Either that, or the masked killer is real and waiting for us..."
    a "Let's assume the first one."
    b d2 straight blank "Well, I'll have you go in first, just in case it's the second one."
    $ b_partial = True
    b level huhu "That way he'll attack you first, giving us time to run away!"
    a "Aww, how thoughtful of you, Ms. Usher."
    $ b_partial = False
    $b_blink = False
    show brit d1 closed closed_smile sad
    b "Ehehehe!"
    hide brit with dissolve
    $b_blink = True
    $ current_track = "None"
    stop music fadeout 3.0
    with Pause(.1)

    scene bg cabin_i_s with dissolve
    with Pause(.1)
    play sound door_open
    "I open up the cabin door, revealing a nice, cozy setup."
    "It all looked like one giant room, the bedroom and kitchen combined together."
    "There was one door against the wall. I'm assuming it's the bathroom."
    "Right there on the bed was a familiar friend of ours."

    $ current_track = "\"Cabin Fever\""
    play music cabin_fever
    show don e1 straight raised grin at middle with dissolve
    with Pause(.1)
    d smile "Alright! You guys made it!"
    $ b_partial = True
    show don at tworight
    show brit d2 straight raised grin at twoleft
    with easeinleft
    with Pause(.1)
    b "We would've been here sooner, but Alex was too scared to go into the woods."
    d grin "Oh, really?"
    $ b_partial = False
    show brit d1 straight sad blank at twoleft
    b "He even said something about wanting me to enter the cabin first in case there was a killer inside."
    d level "You truly are a convincing actress."
    $ b_wink = True
    b d2 mad tongue "And you truly are a dum-dum."
    d raised grin "Anyway, what do you say we start with what I called you here for?"
    $ b_wink = False
    show brit d1 straight casual blank
    b "It would help if we knew what that was."
    d left level "Follow me and find out."
    hide don
    hide brit
    with dissolve
    with Pause(.1)
    show bg cabin_i_s:
        ease 0.5 xalign 1.0
    "Donald walked over to the kitchen area, where he sat down at a small table."
    "There was a chair on each side, one for each of us."

    show don e1 straight raised grin at middle with dissolve
    with Pause(.1)
    d "Take a seat."
    hide don with dissolve
    with Pause(.1)

    "Brittney took a seat across from Donald."
    "Christeena sat to Brittney's right."
    "That just left me across from Christeena."

    show don e1 straight casual grin at close_d with dissolve
    with Pause(.1)
    d "Alright, so hear me out:"
    d "Alex still doesn't really know much about us, correct?"
    d level "I mean, he knew a lot about me from when we were younger, but not any current things, right?"
    show don at close_left_d_2
    show chris d1 straight casual blank at middle
    show brit d2 straight casual blank at close_right_b_2
    with easeinright
    with Pause(.1)
    "The sisters looked at each other, then to me, then back to Donald before giving nods of agreement."
    show don at close_d
    hide brit
    hide chris
    with easeoutright
    with Pause(.1)
    d e1 mad straight grin  "So, I asked myself, 'What's a way for four teenagers to learn about each other while also adding a fun element?'"
    d raised "The answer?"
    d "..."

    "We all stared at him with anticipation."

    d smile "A good ol' game of 'Never Have I Ever'!"
    show don at close_left_d
    show chris d1 small sad hanging at tworight
    with easeinright
    with Pause(.1)
    c "Oh, Lord..."
    hide don
    hide chris
    show brit d1 straight mad opened_smile at close_b
    with dissolve
    with Pause(.1)
    b "Oooo!"
    b d2 raised "Okay, this night just got interesting."
    show brit at close_right_b
    show don e1 right casual grin at close_left_d
    with easeinleft
    with Pause(.1)
    d "I assume everyone here has played before?"
    b grin "I certainly have."
    show don:
        ease 0.5 xalign 0.0
    show brit:
        ease 0.5 xalign 1.0
    show chris d2 right level blank at middle with dissolve
    with Pause(.1)
    c "I have once or twice."
    d straight "Al?"
    a "..."
    a "Uh..."
    d level blank "Wait..."
    d "You haven't??"
    a "Not really."
    show chris casual straight
    b d1 small level hanging "Whaaaaat?"
    b straight mad blank "What kind of teenager are you?"
    a "The kind that has no friends to ever play that with."
    $ b_partial = True
    b d2 raised huhu "Well, that's about to change tonight."

    if persistent.choice_22 == 1:
        d casual "Do you at least know the rules of 'Never Have I Ever'?"
        jump knowtherules
    elif persistent.choice_22 == 2:
        d casual "Do you at least know the rules of 'Never Have I Ever'?"
        jump dontknowrules
    else:

        d casual "Do you at least know the rules of 'Never Have I Ever'?{nw}"

        menu:
            d "Do you at least know the rules of 'Never Have I Ever'?{fast}"

            "Yes":
                $ persistent.choice_22 = 1
                jump knowtherules

            "No":
                $ persistent.choice_22 = 2
                jump dontknowrules

label knowtherules:
    a "Of course I know the rules. I've just never played, that's all."
    $ b_partial = False
    show brit d1 straight raised grin
    b "Alright, glad to see you're not a TOTAL loser."

    jump startnhie

label dontknowrules:
    a "Nope."
    $ b_partial = False
    show brit d1 straight mad frown
    b "Sheesh! I thought you went to a public school!"
    a "What does that have to do with anything?"
    b d2 right level blank "Oh, nothing, I suppose."
    d grin level "Don't worry; I'll give you a quick rundown."
    hide brit
    hide chris
    with dissolve
    show don casual at close_d
    with easeinleft
    with Pause(.1)
    d "So, the game runs like this:"
    d "We each start off with a set amount of points, let's say 3 in this case."
    d level "We represent our points by our fingers."
    "Donald demonstrated this point by holding up 3 fingers."
    d casual "Someone goes first, stating something that they've never done, needing to be completely honest about it."
    d level right "Say, for instance..."
    d straight casual "{i}'Never have I ever been to Australia.'{/i}"
    d raised smile "Now, if another player HAS done that thing, in this case been to Australia, they lose a point and put a finger down, leaving them with 2."
    d grin "Then, the player to the left goes next, saying a thing that THEY'VE never done."
    d "Once you lose all your points, you're out."
    d casual "The game keeps going until only one person is left, with that person being the winner!"
    d level "It really is a simple game, but some of the things that people have and have not done can create a fun experience."
    hide screen don_points
    show don at close_left_d_2 with easeinright
    show brit d1 straight casual grin at close_right_b_2
    show chris d1 straight casual blank at middle
    with dissolve
    with Pause(.1)

    jump startnhie

label startnhie:

    d casual smile "Alright! Let's begin!"
    d raised grin "I'll go first to kick us off. Ready?"
    b raised closed_smile "Yep!"
    c sad "I suppose..."
    a "As ready as I can be, I guess."
    $ c_blush = True
    c left d2 "This is going to be so embarrassing."
    d mad "Well, as long as we're all ready, I'd like to propose an additional twist."
    b d2 casual opened_smile "Oh?"
    $ c_blush = False
    show chris straight d1 casual blank at middle
    c "..."
    d raised right "Whoever wins the game..."
    d smile "...gets to make the first one out perform a dare!"
    c small sad dot "Eh??"
    show brit:
        ease 0.5 xalign 0.9
    show don:
        ease 0.5 xalign 0.1
    hide chris with dissolve
    with Pause(.1)
    b d1 mad grin "Oh, ho ho!"
    b raised "What prompted this idea?"
    d straight grin "Just a little something I thought up to make it more fun."
    $ b_partial = True
    b d2 level huhu "Mhm."
    b "So it would have nothing to do with the TOTALLY fair and NOT rigged chance of me getting out first and you winning?"
    d casual "Well, that outcome is obviously possible, but not because it's rigged."
    b casual grin "I see, I see..."
    $ b_partial = False
    show brit d1 straight mad grin
    b "Well, this game truly is going to be interesting, then."
    hide brit
    hide don
    with dissolve
    with Pause(.1)

    "Oh, boy. {w}Be my luck, I'll lose the game."
    "If that's the case, I hope whoever wins won't make me do something stupid."

    show don e1 straight raised grin at close_d with dissolve
    with Pause(.1)
    d "Alright, I'll go first, then."
    d casual "Everyone, hold up 5 fingers."

    show don at close_left_d_2 with easeinleft
    show chris d1 straight sad blank at middle
    show brit d1 straight raised grin at close_right_b_2
    with dissolve
    $ nhie_d_points = 5
    $ nhie_c_points = 5
    $ nhie_b_points = 5
    $ nhie_a_points = 5
    show nhie at left zorder 3 with easeinleft
    show screen finger_points
    with dissolve
    with Pause(.1)
    "We all held out an open hand, signaling we were ready."
    hide chris
    hide brit
    with dissolve
    show don at close_d with easeinleft
    with Pause(.1)

    # Points: A = 5, B = 5, C = 5, D = 5

    d level blank "Hm..."

    "Donald went deep into thought."

    d "Never have I ever..."
    d right "..."
    d grin "...lost a game of pool."

    $ nhie_a_points -= 1
    $ nhie_b_points -= 1
    $ nhie_c_points -= 1
    with dissolve
    $ b_partial = True
    show don:
        ease 0.5 xalign -0.505
    show chris d1 straight level blank at twoleft
    show brit d2 level grin straight at close_right_b
    with easeinright
    with Pause(.1)
    "All three remaining players put down a finger. Brittney gave a playful grin as she did so."

    # Points: A = 4, B = 4, C = 4, D = 5

    b raised "Kinda hard for you to lose a game of pool when you've never played pool, isn't it, Donnie?"
    show chris at middle
    show brit at close_right_b_2
    $d_blink = False
    show don e1 closed sad smile at close_left_d_2
    with easeinleft
    with Pause(.1)
    d "Indeed."
    $d_blink = True
    d casual straight grin "Alright, Christeena. You're up."
    show don:
        ease 0.5 xalign -0.55
    show brit:
        ease 0.5 xalign 1.55
    pause .6
    hide brit
    hide don
    $ b_partial = False
    c small sad dot "Oh..."
    c d2 straight blank "Um..."
    c "..."
    c "Never have I ever..."
    c left "I don't know..."
    c "..."
    c d1 straight casual smile "Oh, I have one!"
    c raised grin "Never have I ever left the state."

    $ nhie_b_points -= 1
    $ nhie_d_points -= 1
    with dissolve
    pause .1
    show don e1 straight casual grin at close_left_d_2
    show brit d1 straight raised grin at close_right_b_2
    with dissolve
    with Pause(.1)

    "Brittney and Donald each put down a finger."

    # Points: A = 4, B = 3, C = 4, D = 4

    hide brit
    hide don
    with dissolve
    with Pause(.1)
    a "Really? You've never left Illinois?"
    c d2 casual blank "Never."
    c left level dot "The farthest I've ever been is Chicago, and even then, that's only once or twice for field trips."
    a "Dang!"
    a "Doesn't that make you feel kinda isolated?"
    c d1 straight raised blank "Well, you're one to talk; you didn't put your finger down, either."
    a "Well, yeah, but I've still been all over the state for different stuff."
    $ b_partial = True
    show chris at twoleft
    show brit d2 straight raised huhu at close_right_b
    with easeinright
    with Pause(.1)
    b "Still sounds like isolation to me."
    hide chris
    show brit at close_b
    with easeoutleft
    pause .1
    $ b_partial = False
    show brit d1 straight mad grin
    b "Alright, my turn now."

    "She gave a devilish grin at Donald before quickly continuing."

    b d2 raised huhu "Never have I ever masturbated at Kelly's."

    show brit at close_right_b
    show don e1 small blank sad at close_left_d
    with easeinleft
    with Pause(.1)
    "Donald's eyes widened up in fear as he stared at Brittney, who was still grinning."
    "He then looked over and Christeena and I in shame before slowly lowering a finger."
    $ nhie_d_points -= 1
    with dissolve
    pause .1

    # Points: A = 4, B = 3, C = 4, D = 3

    hide don
    hide brit
    show chris d1 small sad scream at middle
    with dissolve
    with Pause(.1)
    c "What??"
    c d1 straight blank "How the hell--?!"
    c level "..."
    $ c_blush = True
    c d2 left mad "Actually, I don't think I wanna know..."
    hide chris with dissolve

    show don e1 straight mad blank at close_left_d
    show brit d1 straight mad grin at close_right_b
    with dissolve
    with Pause(.1)
    $ c_blush = False
    "Donald looked at Brittney with a furious expression."

    d wide "That was supposed to be a secret!"
    $ b_partial = True
    b d2 level huhu "That was before you made us play this game with the added dare challenge!"
    b raised "With something like that, I have no choice but to make sure you lose!"
    a "Do I even want to know how you would even know that fact?"
    $ b_partial = False
    $b_blink = False
    show brit d1 closed opened_smile sad
    b "Oh, it's a great story!"
    $b_blink = True
    b straight grin "You see-"
    d blank blush "Let's just move on!"
    b left level huhu "No, no. He asked, so he has a right to know."

    "Donald's face was red, and rightfully so."
    "Though whether it was more from anger or embarrassment is uncertain."

    hide don
    show brit d2 straight casual grin at close_b
    with easeoutleft
    with Pause(.1)
    b "So, we were together at Kelly's, right?"
    b mad blank "Not as a date or anything, just hanging out."
    b level left grin "Then, he goes to the restroom."
    b raised straight blank "About 10 minutes pass and he's still in there, so I'm a bit concerned, right?"
    b casual "Does he have diarrhea or something? Is he just distracted on his phone?"
    b "So, I walked over to the restrooms and opened the door up a crack."
    $ b_partial = True
    b grin "Before I could even say anything, I could hear a thumping noise from inside."
    b raised "Add the heavy breathing and moans and you could quickly figure out what was happening."
    $ b_partial = False
    show brit d1 mad straight opened_smile
    b "So, I then called out to Donald and asked if he was okay."
    b level huhu "As to be expected, I heard a gasp of surprise and a nervous 'Yeah, I'm okay!'"
    b d2 sad grin "I went back to the table, he returns a few minutes later, and I just tease the hell out of him!"
    b casual d1 "But because I'm such a good friend, I said nothing about it after that day."
    $b_blink = False
    b closed sad opened_smile "Until now, of course."
    $ c_blush = True
    show brit at close_right_b
    show chris d2 left mad blank at twoleft
    with easeinleft
    with Pause(.1)
    c "Ugh, I think I'm going to vomit..."
    hide chris
    hide brit
    with dissolve
    show don e1 small mad blank blush at close_d with dissolve
    with Pause(.1)
    $b_blink = True
    $ c_blush = False
    "Donald looked like he was about to explode with rage. If this was a cartoon, smoke would be pouring out of his ears."

    a "Anyway, I guess that makes it my turn, then?"
    hide don
    show brit d1 straight casual grin at close_b
    with dissolve
    with Pause(.1)
    b "It does, indeed!"
    hide brit with dissolve
    with Pause(.1)

    "Hmm..."
    "I suppose I'm not really trying to get anyone out, unlike these guys, so I guess I'll just go with something simple and see what happens."

    show don e1 straight level blank at close_left_d_2
    show chris d1 straight casual blank at middle
    show brit d2 straight casual blank at close_right_b_2
    with dissolve
    with Pause(.1)
    a "Never have I ever watched a horror movie."

    $ nhie_b_points -= 1
    $ nhie_c_points -= 1
    $ nhie_d_points -= 1
    with dissolve
    pause .1
    show don casual
    show chris raised dot
    show brit level hanging
    "Everyone looked at me in surprise as they all lowered a finger."

    # Points = A = 4, B = 2, C = 3, D = 2

    hide don
    hide chris
    with dissolve
    show brit at close_b with easeinright
    with Pause(.1)
    b d1 raised blank "You've NEVER watched a horror movie? Ever?"

    "I shook my head in response."

    hide brit
    show chris d1 left blank mad at middle
    with dissolve
    with Pause(.1)
    c "Lucky. Brittney forces me to watch them every now and then."
    c straight "Despite my obvious hatred of them."
    show chris at twoleft
    show brit d1 straight raised grin at close_right_b
    with easeinright
    with Pause(.1)
    b "And it looks like Alexander is going to have to receive the same treatment!"
    b d2 sad blank "What should we start with? {i}'Elm Street'{/i}? {i}'Halloween'{/i}?"
    b level "Nah, those are too tame."
    $ b_partial = True
    b huhu "Nah, those are too tame.{fast} I say we start with {i}'Saw'{/i}!"
    show don e1 right raised grin at close_left_d_2
    show brit at close_right_b_2
    show chris at middle
    with easeinleft
    with Pause(.1)
    d "We'll have time to worry about that later; it's my turn again!"
    $ b_partial = False
    show brit d1 straight level grin at close_right_b_2
    b "Very well."
    b raised opened_smile "So, let's see how you're going to screw me over this time, shall we?"

    hide brit
    hide chris
    show don at close_d
    with easeoutright
    with Pause(.1)
    show don straight
    "Donald gave a small chuckle as he leaned forward."

    d level smile "Never have I ever turned down an offer for a date!"

    $ nhie_b_points -= 1
    $ nhie_c_points -= 1
    with dissolve
    pause .1
    hide don
    show brit d2 straight level grin at close_b
    with dissolve
    with Pause(.1)
    "Brittney lowered her finger as she slowly shook her head with a smile."
    "Honestly, that wasn't a shock."
    show brit at close_right_b
    show chris d1 straight casual blank at twoleft
    with easeinleft
    with Pause(.1)
    "What WAS a shock, however, was the fact that Christeena lowered her finger, as well."

    # Points: A = 4, B = 1, C = 2, D = 2

    hide brit
    show chris at middle
    with easeoutright
    with Pause(.1)
    a "Wait, Christeena has turned someone down?"
    c level d2 "You sound surprised."
    a "I just didn't expect that, that's all."
    $ b_partial = True
    show chris at twoleft
    show brit d2 straight level blank at close_right_b
    with easeinright
    with Pause(.1)
    b "And what, pray tell, is that supposed to mean?"
    a "Nothing!"
    b raised d1 "Really? Because it sounds like you thought she either would say yes to anyone who asked her out OR she has never been asked on a date."
    $ b_partial = False
    show brit d1 straight mad blank at close_right_b
    b "Heck, maybe it's both, you judgmental jerk!"
    a "You know what? Let's just forget I said anything. There's no way I'm going to be able to defend myself here."
    b d2 grin "Looks like you've got a brain in that head, after all!"
    c mad d2 "Don't worry about her, Alex. What little filter she initially had is removed when she's tired."
    b level left blank "I'm not ti--{w=.25}{nw}"
    $b_blink = False
    b closed sad hanging "*YAWN*"
    $b_blink = True
    b straight casual blank "..."
    c level "..."
    hide brit
    show chris at middle
    with easeoutright
    with Pause(.1)
    c d2 casual grin "Anyway, I guess I should take my turn, now."
    c level blank "Hmm..."
    c left "Never have I ever..."
    c d1 straight raised grin "...failed a test."
    $ nhie_a_points -= 1
    $ nhie_d_points -= 1
    with dissolve
    pause .1
    hide chris
    show don e1 straight raised grin at close_d
    with dissolve
    with Pause(.1)

    "Donald and I both put down a finger."

    # Points: A = 3, B = 1, C = 2, D = 1
    $b_blink = False
    hide don
    show brit d1 closed opened_smile sad at close_b
    with dissolve
    with Pause(.1)
    b "Looks like girls truly are smarter than men, eh?"
    a "That's kinda sexist."
    $b_blink = True
    b d2 straight level huhu "It's not sexist if it's true, my friend."
    b grin raised "Kinda like how it's not racist if I said that Donald is probably tall because he's black."
    a "...!"
    b d1 opened_smile "I mean, am I wrong?"
    a "Well..."
    $d_blink = False
    show brit at close_right_b
    show don e1 closed sad smile at close_left_d
    with easeinleft
    with Pause(.1)
    d "Relax, man. No worries."
    $d_blink = True
    d straight level grin "It's gonna take a lot more than that to offend me."
    show don zorder 2:
        ease 0.5 close_left_d_2
    show brit zorder 2:
        ease 0.5 close_right_b_2
    show chris d1 straight level blank at middle zorder 1 with dissolve
    pause 0.1
    c "..."
    show don:
        ease 0.5 close_left_d
    show brit:
        ease 0.5 close_right_b
    hide chris with dissolve
    pause 0.1
    d raised "And if it ain't offending me, it shouldn't offend you, either."
    a "I wasn't offended, I was just surprised."
    d level "Well, I'm sure you still get my drift."
    d right casual "Brittney, you're up."
    d level blank "Brittney, you're up.{fast} Unfortunately..."
    b d1 straight casual grin "Relax, I'll go a little easier on ya."
    hide don
    show brit at close_b
    with easeoutleft
    with Pause(.1)
    b level blank d2 "Hm..."
    b grin "Never have I ever eaten a bug."

    $ nhie_c_points -= 1
    $ c_blush = True
    with dissolve
    show brit at close_right_b zorder 2
    show chris d1 straight mad blank at twoleft zorder 1
    with easeinleft
    with Pause(.1)
    "Christeena shot a dirty look at her sister before slowly lowering a finger."

    # Points: A = 3, B = 1, C = 1, D = 1

    b d1 small sad hanging "Oh, shoot! Sorry, I wasn't thinking about that."
    c d2 "{cps=15}Suuuurrrrrre.{/cps}"
    a "Okay, I gotta know the story behind this."
    $ c_blush = False
    show chris d2 straight level blank at twoleft
    c "It's not too much of a story."
    hide brit
    show chris at middle
    with easeoutright
    with Pause(.1)
    c d1 casual "It was a month before our parents got married; she dared me to eat a grasshopper that she found."
    c level "Said it was some sort of 'initiation' to be sisters."
    a "And you did it...?"
    $ c_blush = True
    c d2 mad hanging "I was 9!"
    a "Yeah, 9, not 4!"
    c d1 blank "Yeah, well..."
    c left "I didn't really know anything about how sisters worked, so I thought this was just a normal thing they did."
    show chris at twoleft
    show brit d2 left level huhu at close_right_b
    with easeinright
    with Pause(.1)
    b "I mean, it kinda is, to be fair; big sisters are supposed to mess with little sisters."
    $b_blink = False
    b d1 closed sad opened_smile "And honestly, seeing you actually do it is quite possibly the funniest moment of my life."
    $ c_blush = False
    show chris d2 straight raised blank at twoleft
    c "I wanna believe that's an exaggeration."
    $b_blink = True
    b straight raised grin "Believe what you will, then."
    b d2 sad "Even the scolding from Mom was worth it!"
    c d1 casual smile "Well, the cookie she gave me as a way of apologizing was pretty nice, too."
    b d1 mad "You know, I take that back."
    c blank "Huh?"
    $b_blink = False
    b closed sad opened_smile "The funniest moment of my life was actually when my mom told me to stop picking on you."
    $b_blink = True
    b d2 level right huhu "It's like the woman didn't even know me!"
    b "I pick on any and all people that I think are cool!"
    a "Really? Would have never figured that one out."
    $ b_wink = True
    b d1 straight mad tongue "Oh, hush it, dum-dum."
    hide brit
    hide chris
    with dissolve
    show don e1 straight casual grin at close_d with dissolve
    with Pause(.1)
    $ b_wink = False
    d "Alright, Al. You're up."
    show don at close_left_d
    show brit d2 straight casual opened_smile at close_right_b
    with easeinright
    with Pause(.1)
    b "Ah, now THIS is interesting!"
    d blank "Huh?"
    b d1 raised grin "We all have one point left!"
    show don:
        ease 0.5 xalign 0.0
    show brit:
        ease 0.5 xalign 1.0
    show chris d1 straight sad blank at middle with dissolve
    with Pause(.1)

    "I looked at everyone and discovered that, sure enough, they each had 1 finger up."
    "Christeena in particular didn't look too happy about this scenario."

    b opened_smile "It's the moment of truth!"
    b right level huhu "Quite literally, in fact."
    b raised straight grin d2 "Your next move determines our fate."

    "No pressure or anything, right?"
    hide screen finger_points
    hide nhie
    hide brit
    hide don
    hide chris
    with dissolve
    with Pause(.1)
    "Hm..."
    "If someone gets out this round, then they have to perform a dare for whoever wins."
    "I honestly don't want to be here all night dragging this game on, so I guess I should try and get someone out."
    "But who should I pick?"
    "If I get someone out, they might get mad at me, but if I were to win, I could use my dare for something pleasant to make up for it..."
    "...or not. I could have them do something ridiculous for the heck of it."
    "Alright, it's time to choose."
    "Again, no pressure or anything."
    if persistent.choice_18 == 1:
        jump nhie_b
    elif persistent.choice_18 == 2:
        jump nhie_c
    elif persistent.choice_18 == 3:
        jump nhie_d
    else:
        "Who should I get out?{nw}"

        menu:
            "Who should I get out?{fast}"

            "Brittney":
                $ persistent.choice_18 = 1
                jump nhie_b # nhie_results.rpy
            "Christeena":
                $ persistent.choice_18 = 2
                jump nhie_c # nhie_results.rpy
            "Donald":
                $ persistent.choice_18 = 3
                jump nhie_d # nhie_results.rpy

label nhie_end:
    $ daydesc = 0
    $ replay = False
    $ renpy.end_replay()
    $ progress += 1

    jump progress
