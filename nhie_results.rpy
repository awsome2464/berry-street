################################################################################
# Brittney######################################################################
################################################################################

label nhie_b:
    "Well, Brittney was intended to get out first, anyway."
    "The bigger question now is whether or not I make sure I win or Donald wins."
    "I guess we'll see when the time comes."
    show screen finger_points
    show nhie at left zorder 3
    show don p1 straight casual blank at close_left_d_2
    show chris p1 straight sad blank at middle
    show brit p2 straight casual blank at close_right_b_2
    with dissolve
    pause 0.1
    a "Never have I ever...{w} had my mom marry another man."
    b_s small hanging "...!"
    b p1 straight mad grin "Well, well, well. Bravo, Mr. Sprouse!"
    $ nhie_b_points -= 1
    with dissolve
    "Brittney then lowered her final finger, officially marking her out of the game."
    # Points: A = 3, B = 0, C = 1, D = 1
    show don level grin
    "Donald looked at me and winked in thanks."
    $ b_eyelids = "wink"
    b mad tongue p2 "Alright; time to see which one of you losers will get the honor of making me do a dare."
    show don right
    d "Yes, time to see, indeed."
    hide brit
    hide chris
    show don at close_d
    with easeoutright
    pause 0.1
    show don straight raised
    $ b_eyelids = "blink"
    "Donald looked at both Christeena and I with giant grins."
    d smile "Never have I ever..."
    d_s grin "..."
    d smile "...needed to wear glasses."
    $ nhie_a_points -= 1
    with dissolve
    "I rolled my eyes as I lowered a finger."
    # Points: A = 2, B = 0, C = 1, D = 1
    show don at close_left_d
    show chris p1 straight casual blank at tworight
    with easeinright
    pause 0.1
    d right casual blank "Wait a minute; Christeena, didn't you wear glasses at one point?"
    c raised "Why the heck would you think that?"
    d straight level "I thought I saw a picture of you in glasses before..."
    c_s level "..."
    c raised "...wait a minute..."
    c p2 hanging "Are you talking about that picture where I was wearing my mom--"
    c blank "...er, Martha's glasses just for fun?"
    d small casual "Oh."
    $b_blink = False
    show don at close_left_d_2
    show chris at middle
    show brit p2 closed sad closed_smile at close_right_b_2
    with easeinright
    pause 0.1
    b "Nice try, Donnie."
    $ b_eyelids = "partial"
    $b_blink = True
    extend level straight huhu " But it would appear as though your plan backfired."
    d straight level blank "It would appear so, indeed."
    d right grin "Alright, Christeena; you're up!"
    hide don
    hide brit
    with dissolve
    pause 0.1
    $ b_eyelids = "blink"
    c casual smile "Okay, then!"
    c level left dot "Hm..."
    c p1 straight raised smile "Oh, I've got a good one!"
    c left blank "As gross as it is..."
    c straight grin "Never have I ever peed standing up!"
    show chris at tworight
    show don p1 straight level blank at close_left_d
    with easeinleft
    pause .1
    $ nhie_d_points -= 1
    $ nhie_a_points -= 1
    with dissolve
    pause 0.1
    "And, with that, Donald and I each lowered a finger, thus marking Donald out of the game."
    # Points: A = 1, B = 0, C = 1, D = 0s
    hide don with dissolve
    show chris at twoleft
    show brit p1 straight casual opened_smile at close_right_b
    with easeinright
    pause 0.1
    b "{cps=15}DAAAAAAAAAMN!{/cps}{w=.5} Nice one, Chris!"
    $ c_blush = True
    $ c_blink = False
    show chris closed_happy grin p2 sad
    "Brittney raised her hand for a high-five, to which Christeena quickly accepted and slapped."
    b level "There's just one problem."
    $ c_blush = False
    $ c_blink = True
    c p2 straight casual blank "What's that?"
    b p2 "It's Alex's turn.{w} And he may be able to get you out with something stupidly easy."
    $ c_blush = True
    c small sad dot "Oh."
    "Well, Brittney does have a point..."
    "If I wanted to win, I could easily get Christeena out, making me the winner and the one to have Brittney perform a dare."
    "Hmm..."
    "Then again, Christeena might enjoy this win.{w} Making her older sister perform any dare she wishes could be pretty fun on her end..."
    if persistent.choices["19"] == 1:
        jump chris_out
    elif persistent.choices["19"] == 2:
        jump chris_win
    else:
        menu:
            "What should I do?"

            "Get Christeena out":
                $ persistent.choices["19"] = 1
                jump chris_out

            "Let Christeena win":
                $ persistent.choices["19"] = 2
                jump chris_win

#######################
#######################
# Get Christeena Out #
#######################
#######################

label chris_out:
    "Sorry, Christeena; better luck next time."
    hide brit
    show chris at middle
    with easeoutright
    pause 0.1
    $ c_blush = False
    show chris p1 straight level blank at middle
    a "Never have I ever peed sitting down after I was potty trained."
    $ c_blush = True
    c mad "Ugh!"
    $ nhie_c_points -= 1
    with dissolve
    "And with that, Christeena lowered her final finger."
    hide screen finger_points
    hide nhie
    hide chris
    show brit p2 straight raised opened_smile at close_b
    with dissolve
    pause 0.1
    $ c_blush = False
    b "Oooo, using her own move against her! Clever, Mr. Sprouse."
    b p1 casual grin "Alrighty, then; what shall I do for you, my good sir?"
    "She seems very eager to be doing this dare."
    "She truly is an oddball."
    "But to answer her question..."
    "Hm..."
    "If I'm being honest with myself..."
    "Using this dare for something romantic would be pretty cool."
    "It might even make Donald jealous."
    "Sure, it would piss him off, but it would be worth it."
    "Probably."
    "Though even something really simple could be good enough."
    "Of course, I could do the opposite and make Donald happy by having her do something for him."
    "She may be mad at me, though, as a result."
    "Then again, I could easily turn the tables and perform a dare nobody would see coming."
    "Alright, time to decide."
    a "Okay, Brittney."
    show brit p2 raised
    a "I dare you to..."
    if persistent.choices["20"] == 1:
        jump b_dare_kiss_a
    elif persistent.choices["20"] == 2:
        jump b_dare_kiss_d
    elif persistent.choices["20"] == 3:
        jump b_dare_hit
    else:
        menu:
            "..."

            "...kiss me.":
                $ persistent.choices["20"] = 1
                jump b_dare_kiss_a

            "...kiss Donald.":
                $ persistent.choices["20"] = 2
                jump b_dare_kiss_d

            "...hit Donald.":
                $ persistent.choices["20"] = 3
                jump b_dare_hit

##################
# Brittney Kiss #
##################

label b_dare_kiss_a:
    a "...kiss me."
    $b_blink = False
    b p1 closed sad opened_smile "Ha!"
    $b_blink = True
    b straight mad grin "You have the chance to make me do anything you want, and you waste it on a kiss?"
    a_s "..."
    b p2 sad "Well, I suppose that shows what kind of guy are, not taking advantage of a sweet, innocent girl."
    show don p1 straight raised blank at close_left_d
    show brit at close_right_b
    with easeinleft
    pause 0.1
    d "'Sweet'?"
    show don:
        ease 0.5 xalign 0.0
    show brit:
        ease 0.5 xalign 1.0
    show chris p2 straight raised blank at middle with dissolve
    pause 0.1
    c "'Innocent'?"
    b p1 small level hanging "Hey!"
    b straight raised grin "None of you are even gonna question the 'girl' part?"
    d level grin "I mean, you could always prove it right now..."
    $ b_eyelids = "partial"
    b p2 huhu level "Oh, how you wish, you pervert."
    hide chris
    hide don
    with easeoutleft
    show brit at close_b
    with easeinright
    pause 0.1
    $ b_eyelids = "blink"
    show brit p1 straight casual grin
    b "Alright, then, Alexander. Let's kiss!"
    a "N-Now? In front of everyone?"
    b p2 raised huhu "Hey, you're the one who wanted a kiss!"
    a "I guess..."
    show brit:
        ease 0.5 zoom 1.1
    pause .6
    $ b_blink = False
    show brit closed_sad casual huhu
    "Brittney then leaned towards me, closed her eyes, and slightly puckered her lips."
    "I turned towards Christeena and Donald."
    hide brit with dissolve
    show chris p2 straight level blank at tworight
    show don p1 level blank straight at close_left_d
    with dissolve
    pause 0.1
    "They both looked curious yet embarrassed."
    scene bg cabin_i_s with dissolve
    pause 0.1
    "With nothing else to really lose, I looked back to Brittney, leaned forward, and pressed my lips against hers."
    $ B_Points += 1
    $ B_Kiss = True
    $ persistent.b_kiss = True
    "She let out a small noise in surprise, but she didn't resist."
    "..."
    "Not gonna lie...{w} Despite the awkwardness of an audience, this feels kinda nice."
    "A few seconds passed before Brittney pulled back, opening up her eyes."
    $b_blink = True
    show brit p2 straight level blank at close_b with dissolve
    pause 0.1
    b "Huh."
    b "You didn't even try going French on me."
    b raised "If you were going to make a weak dare, you could've at least tried to spice it up!"
    a "Uh... Sorry?"
    $b_blink = False
    b p1 sad closed closed_smile "Well, you're lucky your lips were nice."
    a "Well, uh, thanks. Yours were, too."
    $b_blink = True
    b straight sad huhu "Aww, thank you, Sweetheart!"
    show brit at close_right_b
    show don p1 straight mad blank at close_left_d
    with easeinleft
    pause 0.1
    d_s "..."
    b level left "Aww, is Donnie jealous?"
    d_s "..."
    b straight mad closed_smile "Don't worry; you'll get your chance the NEXT time you try to rig a dare competition!"
    d_s small blush "...!"
    b p2 casual grin "Anyhoo, what do you say we call it a night?"
    show don:
        ease 0.5 xalign 0.0
    show brit:
        ease 0.5 xalign 1.0
    show chris p1 straight sad blank at middle with dissolve
    pause 0.1
    c "Good idea."
    d_s "..."
    a "Yeah, before things get too heated."
    jump nhie_end

########################
# Brittney Kiss Donald #
########################

label b_dare_kiss_d:
    a "...kiss Donald."
    $ B_Points -= 2
    show brit level small hanging
    b "Wha-!?"
    show brit at close_right_b
    show don p1 straight casual blank at close_left_d
    with easeinleft
    pause 0.1
    d "!!!"
    a "I mean, he's been wanting it for a while, right?"
    a "It's the least you could do."
    b_s straight blank "..."
    d right level grin "I mean, he does kinda have a point, you know."
    d raised "Besides, you've done worse dares before."
    b_s left "..."
    b "Fine."
    "Her sour attitude was obvious, but that didn't make it any less scary."
    b mad "But I hope you realize that it's just a kiss and nothing more."
    d casual smile "I'll take it."
    b_s level "..."
    b "Just get over here already."
    $d_blink = False
    d closed sad "Yes, Ma'am!"
    hide don
    hide brit
    with dissolve
    pause 0.1
    $d_blink = True
    "Donald then quickly went to the other side of the table, nearly bumping into Christeena on the way."
    "He was really looking forward to this."
    "Brittney, on the other hand..."
    show brit p1 straight mad blank at close_right_b
    show don p1 straight casual grin at close_left_d
    with dissolve
    pause 0.1
    b "Just a kiss, and it'll only last a split second. Understand?"
    d smile "You bet!"
    b_s "..."
    show don:
        ease 0.5 xalign 0.0
    show brit:
        ease 0.5 xalign 1.0
    show chris p1 straight sad blank at middle with dissolve
    pause 0.1
    c "Brit, you really don't have to do this if you don't want to."
    b_s level "..."
    d sad blank "Is the idea of kissing me really that awful?"
    b sad small hanging "I...!"
    b p2 straight blank "It's not anything against you, specifically..."
    b right "...but kissing a close friend, dare or not, is just kinda weird, you know?"
    b "If it was someone like Alex, a guy I hardly even know, then I wouldn't care as much."
    if not persistent.b_kiss:
        "Noted."
        $ persistent.b_kiss = True
    d_s "..."
    b_s "..."
    c_s "..."
    "Well, this got awkward."
    "I can either try to convince Brittney to go through with the dare, or I can have her drop it altogether."
    "One choice will make Donald happy and Brittney less happy, and the other choice has the opposite effect."
    "I better act fast."
    if persistent.choices["21"] == 1:
        jump nhie_b_continue
    elif persistent.choices["21"] == 2:
        jump nhie_b_stop
    else:
        menu:
            "What should I do?"

            "Tell Brittney to do the dare.":
                $ persistent.choices["21"] = 1
                jump nhie_b_continue

            "Tell Brittney to not do the dare.":
                $ persistent.choices["21"] = 2
                jump nhie_b_stop

label nhie_b_continue:
    hide don
    hide chris
    with dissolve
    show brit at close_b with easeinright
    pause 0.1
    a "Brittney..."
    show brit casual straight
    a "I understand where you're coming from."
    a "But you said it yourself: it's just a kiss and nothing more."
    b_s level "..."
    a "Plus, if it'll make Donald happy..."
    b_s "..."
    b left "...alright. Fine."
    b "Donald, let's get this over with."
    show brit at close_right_b
    show don p1 straight level grin at close_left_d
    with easeinleft
    pause 0.1
    "Donald was kind enough to give me a wink of thanks before getting closer to Brittney."
    "She then stood up and grabbed him by the shoulders."
    b p1 straight "Close your mouth."
    d raised "What, no tongue?"
    show brit small mad frown
    d small sad wide "AH!"
    "She quickly tightened her grip on him and got even angrier."
    d blank straight "Okay, okay! I'm sorry!"
    show brit blank straight
    "Her grip loosened."
    "She then gave an annoyed sigh as she quickly leaned forward."
    d small casual "Mph!"
    hide don
    hide brit
    with dissolve
    pause 0.1
    "And just like that, their lips touched."
    "Before Donald could fully appreciate it, though, she pulled back, still sporting that disinterested face."
    $ b_eyelids = "partial"
    show brit p2 level blank straight at close_right_b
    show don p1 small sad blank at close_left_d
    with dissolve
    pause 0.1
    b "There. Happy?"
    d_s "..."
    d raised grin straight "Y-Yeah! Of course!"
    b_s "..."
    b grin casual "Well, I'm glad."
    $ b_eyelids = "blink"
    show brit p1 straight raised grin at close_right_b
    b "If you weren't, that would've made the last few years' efforts completely pointless."
    d level "Yeah, I suppose so."
    $ D_Points += 1
    $ B_Points -= 1
    jump brit_don_kiss_end

label nhie_b_stop:
    hide don
    hide chris
    with dissolve
    show brit at close_b with easeinright
    pause 0.1
    a "Brittney..."
    show brit straight casual
    a "I'm sorry for suggesting this dare."
    a "I was just trying to help Donald out, but it's not worth it if you really are this uncomfortable with it."
    b_s sad "..."
    a "You don't have to kiss him if you really don't want to. I'm sorry."
    b_s right "..."
    show brit at close_right_b
    show don p1 straight sad blank at close_left_d zorder 2
    with easeinleft
    pause 0.1
    d_s "..."
    d "He's right."
    b casual left "Huh?"
    d right "It wouldn't feel right if you're not enjoying it."
    d "If I'm going to kiss you, I want it to be because you want to, not because you have to."
    b_s sad "..."
    b "...Donald..."
    b p1 grin "...that was really sweet of you."
    b_s p2 straight grin "..."
    b level "You know what?"
    b p1 sad opened_smile "I won't kiss you on the lips, but how about the cheek?"
    extend p2 grin " That's a fair enough compromise, right?"
    d_s casual blank "..."
    d smile "Heck yeah, it is!"
    hide don
    hide brit
    with dissolve
    pause 0.1
    "Brittney then reached around and gave Donald a quick peck on the cheek."
    "It may have been quick, but it was still enough for Donald's smile to grow twice as big."
    $d_blink = False
    show don closed sad grin p1 at close_left_d
    show brit p1 straight sad grin at close_right_b
    with dissolve
    pause 0.1
    b "There. We good?"
    d "Yeah, we're good."
    $b_blink = False
    b p2 closed closed_smile "Yay!"
    $ D_Points += 2
    $ B_Points += 1

label brit_don_kiss_end:
    show don:
        ease .5 xalign 0.0
    show brit:
        ease 0.5 xalign 1.0
    show chris p2 straight sad grin at middle with dissolve
    pause 0.1
    c "Well, I'm just glad that it didn't end as chaotic as I expected."
    a "That makes two of us."
    $d_blink = True
    d straight level grin "Alright, then. What do you say we call it a night?"
    $b_blink = True
    b p2 left level huhu "Well, since you got what you really brought us together tonight for, I don't see why not."
    d right "I will neither confirm nor deny if there were other motivations behind this hangout session other than Alex getting to know us better."
    $ b_eyelids = "partial"
    b straight grin casual "Sure thing, Donald. Sure thing."
    jump nhie_end

#######################
# Brittney Hit Donald #
#######################

label b_dare_hit:
    a "...hit Donald."
    b_s level blank "..."
    show don p1 straight level blank at close_left_d zorder 2
    show brit at close_right_b
    with easeinleft
    pause 0.1
    d_s "..."
    b "Um..."
    b raised p1 "Why waste a dare on something I normally do, anyway?"
    a "Because the only reason we're doing this dare in the first place is because he tried to get you to do one for him."
    a "I figured it would be fitting for him to be punished for that by having the dare used against him."
    d_s casual right "..."
    b_s casual left "..."
    b straight grin "Well, can't argue with that logic!"
    show brit mad zorder 1:
        linear 0.15 xalign 0.4
        pause 0.05
        linear 0.15 xalign 0.9
    pause 0.15
    play sound punch
    show white zorder 4
    pause 0.05
    hide white
    d small sad wide "OUCH!!"
    "Man, she didn't even hesitate!"
    hide brit
    show don mad straight blank at close_d
    with easeoutright
    pause 0.1
    "Donald glanced over to me with anger in his eyes."
    "I'm probably on his shit list, but he kinda got what was coming to him."
    $ D_Points -= 1
    $ B_Points += 2
    show don at close_left_d
    show brit p1 straight sad grin at close_right_b
    with easeinright
    pause 0.1
    b "Man, that felt good! Thanks, Alex!"
    a "No problem, I suppose."
    b level "Well, what do you say we get out of here?"
    show brit p2 raised opened_smile zorder 2
    b "I don't think anything we do tonight will get better than that."
    $ current_track = "None"
    stop music fadeout 3.0
    show don zorder 3
    d_s "..."
    hide don with easeoutleft
    play sound door_slam
    pause 1
    b_s casual blank "..."
    show chris p1 straight sad blank at twoleft with easeinleft
    pause 0.1
    c_s "..."
    b "I went too far that time, didn't I?"
    c p2 "Maybe just a little."
    b sad left "Damn it..."
    hide brit with easeoutleft
    pause 1
    "She then ran out of cabin, as well."
    show chris at middle with easeinleft
    pause 0.1
    $ current_track = "\"Reflection\""
    play music reflection
    a "This is all my fault, isn't it?"
    $ c_blush = True
    c p1 hanging "What? No!"
    $ c_blush = False
    show chris p1 straight level blank at middle
    c_s "..."
    c p2 right "...well, a little."
    c straight sad grin "But I'm sure things will work out okay."
    a_s "..."
    c_s blank "..."
    window hide dissolve
    pause 2
    window show dissolve
    a "Well, we should probably catch up to them."
    c p2 grin "Good idea."
    jump nhie_end

######################
######################
# Let Christeena Win #
######################
######################

label chris_win:
    "You know what?"
    "Let's let Christeena have some fun with this."
    show chris straight blank
    show brit casual blank
    a "Never have I ever..."
    a "...graduated high school."
    $c_blush = False
    show chris raised p1 straight blank
    show brit level hanging
    "Both girls looked naturally surprised at my move."
    show brit raised left blank
    "But it didn't take long for Brittney to see what I was doing."
    b p1 level straight opened_smile "Well, Christeena hasn't graduated, either, so she doesn't lose a point."
    c_s casual dot "..."
    b p2 casual grin "Which means you're up, Christeena!"
    hide brit
    show chris at middle
    with easeoutright
    pause 0.1
    c p2 blank "Okay, then."
    c raised grin "Never have I ever had blond hair!"
    $ nhie_a_points -= 1
    with dissolve
    "And with that, my final finger dropped."
    show brit p1 straight mad opened_smile at close_right_b
    show chris at twoleft
    with easeinright
    pause 0.1
    b "{cps=15}Niiiice!{/cps}"
    hide screen finger_points
    hide nhie
    with dissolve
    b casual grin "Isn't this your first time winning 'Never Have I Ever', Chris?"
    c p1 casual smile "It is, actually!"
    b p2 raised "Double nice!"
    b p1 casual opened_smile "Alright, then; let's do this dare!"
    b "You can have me do anything you want."
    c raised blank "Hm..."
    c_s level left "..."
    c mad straight grin "Okay."
    c p2 smile "I dare you to watch a whole season of anime with me."
    b small level hanging "Wha...?"
    b p1 straight mad frown "I'd rather shove a cactus up my ass without lube!"
    c p1 raised grin "I dared you, though. A dare I won fair and square!"
    b_s level blank "..."
    b p2 right "...{fast}fine. I'll do it."
    $c_blink = False
    c closed_happy sad smile "Yes!"
    $c_blink = True
    c straight casual grin p2 "Don't worry, you won't be disappointed!"
    b straight "If you say so..."
    show chris at middle
    show brit at close_right_b_2
    show don p1 straight raised grin at close_left_d_2
    with easeinleft
    pause 0.1
    d "On that note, what do you say we all call it a night?"
    c p1 smile "Yeah! Then we can get started on the anime right away!"
    b p1 right mad "Ugh..."
    $ C_Points += 1
    $ B_Points += 1
    jump nhie_end




################################################################################
# Christeena ###################################################################
################################################################################




label nhie_c:
    "Hm... Christeena might be the best person to perform a certain dare on."
    "I just hope I win; who knows what Donald or Brittney could have her do..."
    show screen finger_points
    show nhie at left zorder 3
    show don p1 straight casual blank at close_left_d_2
    show chris p1 straight casual blank at middle
    show brit p2 straight casual blank at close_right_b_2
    with dissolve
    pause 0.1
    a "Never have I ever..."
    a "...had my dad marry another woman."
    show chris sad hanging at middle
    b p1 mad hanging "{cps=15}WOWWWWWW{/cps}.{w=.5} Dick move, man. Dick move."
    $ nhie_c_points -= 1
    with dissolve
    show chris p2 raised blank
    "Nevertheless, Christeena reluctantly lowered her final finger, officially making her out of the game."
    hide chris
    with dissolve
    show brit at close_right_d
    show don at close_left_b
    with easeinright
    pause 0.1
    # Points: A = 3, B = 1, C = 0, D = 1
    d level grin "Alright, then; that means it's my turn, next."
    b p2 left level huhu "And now that someone else is out and has to perform a dare, that means you have no reason to try to get me out."
    d casual "You're right; I have no reason."
    d mad right "Except that I want to."
    d "So, never have I ever worn a bra."
    $ b_eyelids = "wink"
    show brit tongue mad
    "Brittney playfully stuck out her tongue as she put her final finger down."
    # Points: A = 3, B = 0, C = 0, D = 1
    $ nhie_b_points -= 1
    with dissolve
    hide don
    show brit at close_b
    with easeoutleft
    pause 0.1
    $ b_eyelids = "blink"
    b p1 straight raised grin "Alright, then; whoever wins get to make Christeena perform a dare."
    b p2 level huhu "And I have a feeling that Alex is going to be the winner here, unless he wants the game to last longer."
    b p1 sad grin "Either way, this is going to be fun!"
    show brit at close_right_b
    $ c_blush = True
    show chris p1 straight mad blank at twoleft
    with easeinleft
    pause 0.1
    c "Yeah, for you!"
    b casual "Don't worry; if either of them dares something TOO inappropriate, I'll castrate him with a rusty knife."
    a "Noted."
    hide brit
    hide chris
    with dissolve
    pause 0.1
    $ c_blush = False
    "Well, she's right in the fact that I don't want this game to drag on any longer than necessary."
    "Which means I gotta get Donald out right now."
    "Time to make another dick move."
    show don p1 straight casual blank at close_d with dissolve
    pause 0.1
    a "Never have I ever..."
    a "...asked Brittney on a date."
    show don level
    "You could see the defeat and anger in Donald's eyes as he lowered his final finger."
    $ nhie_d_points -= 1
    with dissolve
    $ c_blush = True
    pause 0.1
    hide don
    show chris p1 straight sad blank at middle
    with dissolve
    pause 0.1
    "Christeena was also looking at me, but with fear in her eyes."
    "I would say that she had no reason to be scared, but if I was a shy teenage girl who had to perform a dare for a teenage boy..."
    c level "Alright. Get it over with."
    a "Huh?"
    c p2 mad "The dare. Just get it over with. Humiliate me, make me do something sexy, whatever."
    hide screen finger_points
    hide nhie
    with dissolve
    pause 0.1
    "..."
    "Alright, then. The big moment."
    "I don't really want her to hate me, yet I still wouldn't mind something fun from this..."
    "Then again, I have one trick up my sleeve that might get all but one person on my side."
    a "Okay, Christeena."
    show chris p1 sad
    a "I dare you to..."
    if persistent.choices["19"] == 1:
        jump c_dare_kiss
    elif persistent.choices["19"] == 2:
        jump c_dare_flash
    elif persistent.choices["19"] == 3:
        jump c_dare_hit
    else:

        menu:
            "..."

            "...kiss me.":
                $ persistent.choices["19"] = 1
                jump c_dare_kiss

            "...flash me.":
                $ persistent.choices["19"] = 2
                jump c_dare_flash

            "...hit Donald.":
                $ persistent.choices["19"] = 3
                jump c_dare_hit

###################
# Christeena Kiss #
###################

label c_dare_kiss:
    a "...kiss me."
    c_s small dot "...!"
    c p2 straight blank "Well, I'm not going to lie..."
    c left "I was expecting something worse."
    c "Though, I'm still not exactly comfortable with this..."
    show chris at twoleft
    show brit p2 left level huhu at close_right_b
    with easeinright
    pause 0.1
    b "Ah, relax, Chris! It's just a kiss!"
    c p1 straight hanging "Huh??"
    c "Y-You're not going to try and stop this??"
    b straight casual blank "Why would I? Again, it's just a kiss!"
    b level huhu "It's not like he dared you to blow him or something."
    c mad scream "BRITTNEY!"
    b sad opened_smile p1 "What?"
    c_s blank "..."
    extend "okay."
    c p2 right "Just... can you and Donald go into the other room, first?"
    $b_blink = False
    b closed closed_smile "Oh, alright."
    hide brit with easeoutright
    show chris at middle with easeinleft
    pause 0.1
    show chris p1 straight sad blank
    $b_blink = True
    "With that, Brittney and Donald walked to the bathroom, closing the door behind them."
    show chris:
        ease 0.5 close_c
    pause 0.6
    play sound chair
    "Christeena got out of her seat and walked over to me, the nervousness on her face growing."
    $ current_track = "None"
    stop music fadeout 3.0
    "That's when I decided to talk quietly, in case the others were eavesdropping."
    "Which, given my knowledge of Brittney, is a very high possibility."
    $ current_track = "\"Reflection\""
    play music reflection
    a "Hey, look; if you really don't want to do this, it's okay."
    a "We can just lie and say we kissed; they'd never have to know."
    c_s "..."
    if C_Points >= 3:
        c "I..."
        c p2 right "I want to."
        a "Huh?"
        c straight "I mean, yeah, I haven't really known you for that long, but..."
        c grin "...you are kinda handsome."
        "{i}Kinda?{/i}"
        c p1 "And... I've never really been offered a kiss from a guy like you before."
        c "So I think it'll be okay."
        c p2 mad blank left "Just... please don't try and make out with me or grope me or something."
        a "The thought never crossed my mind."
        c straight sad grin "Okay then..."
        "She seemed a little less nervous all of a sudden."
        "I suppose that's a good thing, right?"
        c "Alright, let's just get it over with."
        c mad blank "But when I want to stop, we stop. Got it?"
        a "Got it."
        c level grin "Okay... close your eyes."
        "I did as I was commanded and shut my eyes."
        scene bg fade with dissolve
        pause 0.1
        $ c_blush = False
        "I could hear what sounded like her walking a little bit closer."
        "Then, I couldn't hear any more movement."
        "As tempted as I was to open my eyes to see what was up, this certainly wasn't the time to break her trust."
        "..."
        "And then, that's when I felt something slam against my mouth."
        "I let out an audible mumble of surprise, but a second later, I quickly realized it was, indeed, another pair of lips that were against mine."
        $ C_Points += 1
        $ C_Kiss = True
        "After kissing me for a few seconds, Christeena pulled back."
        c "Okay... you can open your eyes."
        scene bg cabin_i:
            xalign 1.0
        with dissolve
        pause 1
        show chris p1 straight sad blank at close_c with dissolve
        pause 0.1
        c "H-How was it?"
        a_s "..."
        a "Well, it was kinda quick..."
        a "...but it was pretty nice."
        c grin "Really?"
        a "Yeah!"
        c_s left "..."
        $ c_blush = True
        c "I'm glad."
        c straight p2 "I enjoyed it, too."
        a "Well, I'm glad."
        a "Sorry if you really were uncomfortable with this."
        $ c_blush = False
        show chris level blank p1 straight at close_c
        c "I was at first, but..."
        $ c_blush = True
        c right sad grin "...it was worth it."
        show chris straight
        "We looked at each other for a little bit longer with goofy grins before Christeena turned to the bathroom door."
    else:
        $ c_blush = False
        c p1 straight raised blank "Really?"
        a "Yes, really."
        c_s left level "..."
        c straight grin "Okay."
        c "Thank you."
        a "No problem."
        a "And sorry about making that dare in the first place."
        c sad "It's alright. I understand."
        c "Boys tend to do before they think, I've discovered, so I get it."
        a_s "..."
        "Christeena then looked towards the bathroom door."
    show chris:
        ease 0.5 middle
    pause 0.6
    c p2 straight raised smile "Okay, you guys can come out now!"
    play sound door_open
    $ current_track = "\"Cabin Fever\""
    play music cabin_fever
    hide chris with dissolve
    pause 0.1
    "Almost on cue, Brittney and Donald exited the bathroom with faces of anticipation."
    $ c_blush = False
    $ b_eyelids = "partial"
    show brit p2 level huhu straight at tworight
    show don p1 straight casual grin at twoleft
    with easeinright
    pause 0.1

    b "Well?"
    if C_Kiss:
        $ c_blush = True
        show brit:
            ease 0.5 xalign .9
        show don:
            ease 0.5 xalign 0.1
        show chris p2 left sad grin at middle with dissolve
        pause 0.1
    else:
        show brit:
            ease 0.5 xalign 0.9
        show don:
            ease 0.5 xalign 0.1
        show chris p2 level straight grin at middle with dissolve
        pause 0.1
    c "Honestly, it wasn't so bad."
    $ b_eyelids = "blink"
    show brit p1 straight mad grin at threeright
    pause 0.1
    b "I told you, it was just a kiss."
    c "Yeah..."
    c p1 "Just a kiss..."
    d raised smile "Anyway, what do you all say we call it a night?"
    d "Don't wanna be out TOO late, right?"
    b level "Aww, is Donnie staying up past his bedtime?"
    d right grin "Ah, screw you."
    $ b_eyelids = "partial"
    b p2 casual huhu "Oh, how you wish."
    jump nhie_end

####################
# Christeena Flash #
####################

label c_dare_flash:
    a "...flash me."
    $ C_Points -= 2
    c p2 mad scream "NO!! Absolutely not!!"
    show don p1 straight casual smile at close_left_d_2
    show chris at middle
    show brit p1 casual straight grin at close_right_b_2
    with dissolve
    pause 0.1
    d "Dang, Al! I didn't think you'd be the one to go for the big one like that!"
    b raised opened_smile "I know, right? Looks like you've got some balls in those pants, after all!"
    c sad hanging "Brit, aren't you gonna try and stop this?!"
    hide don
    show chris at twoleft
    show brit at close_right_b
    with easeoutleft
    pause 0.1
    b p1 casual blank "Why would I? They're just boobs."
    c mad scream p1 "No, they are not 'just boobs', Brittney!!"
    c "Not all girls have a man's chest like you do!"
    $ b_eyelids = "partial"
    b p2 raised "Okay, first of all, fuck you, Cantaloupes."
    $ b_eyelids = "blink"
    show brit p1 straight raised blank
    b "And secondly, that doesn't change the fact that they're just lumps of fat with nipples on them."
    b p2 right level "I mean, yeah, if he wanted you to take your pants off, that would be one thing..."
    b straight grin "...but I'm sure Alex has seen a nipple before, right?"
    c p2 left blank "S-Still..."
    b left huhu "Trust me, you'll survive!"
    b p1 straight raised grin "Plus, you'll make our new neighbor happy!"
    c_s straight hanging "...!"
    b casual "Well, Don and I will leave you both to your business."
    $b_blink = False
    b closed sad opened_smile "Have fun, you two!"
    $ b_eyelids = "partial"
    $b_blink = True
    b p2 straight level huhu "Don't stay here alone for too long; a simple flash could evolve to something more if you're not careful."
    show brit at close_right_b_2
    show chris at middle
    show don p1 straight raised grin at close_left_d_2
    with easeinleft
    pause 0.1
    "Donald gave me a small wink and nod."
    $ current_track = "None"
    stop music fadeout 2.0
    hide brit
    hide don
    with easeoutright
    play sound door_open
    pause 1
    $ b_eyelids = "blink"
    "And with that, Christeena and I were alone in the cabin."
    $ current_track = "\"Reflection\""
    play music reflection
    show chris p1 blank
    "She looked at me with what appeared to be both embarrassment and anger."
    "..."
    "I actually feel kinda bad for even making this dare."
    "She probably hates me right now."
    "..."
    "Though maybe it's not too late to try and make it up to her."
    "I could always suggest we pretend she did it."
    "She might still be mad at me, but at least it would show that I was sorry."
    "Then again..."
    "Boobs are boobs."
    "I better decide quick."
    if persistent.choices["20"] == 1:
        jump c_flash_no
    elif persistent.choices["20"] == 2:
        jump c_flash_yes
    else:
        menu:
            "What should I tell her?"

            "You don't have to do this.":
                $ persistent.choices["20"] = 1
                jump c_flash_no

            "It doesn't have to take very long.":
                $ persistent.choices["20"] = 2
                jump c_flash_yes

label c_flash_no:
    a "Christeena, you don't have to do it if you don't want to."
    c p2 scream "Well, I DON'T want to!"
    a "Okay, then. Then we'll just pretend that you did it. Donald and Brittney don't have to know."
    c_s blank "..."
    $ c_blush = False
    show chris p1 raised straight blank at middle
    c p1 raised "...why the sudden change of heart?"
    a "Honestly, I just thought that was the kind of dare that Brittney and Donald wanted to hear."
    a "I didn't really want to actually do it."
    a "I'm sorry."
    c_s level "..."
    a "You don't hate me, do you?"
    c "No, I don't hate you..."
    c left "Credit where it's due, you at least apologized..."
    c p2 straight "Alright. I'll forgive you, but don't you ever pull a stunt like that again. Got it?"
    a "Got it."
    c grin "Good."
    $ C_Points += 1
    c mad blank p1 "I might not be the most extroverted person on the planet, but I'm not one that can be taken advantage of."
    a "Understood. Again, I'm very sorry."
    c level grin "I believe you."
    c raised p2 "Now, what do you say we get out of here and never mention this again?"
    a "Good idea."
    jump nhie_end

label c_flash_yes:
    a "Christeena, it doesn't have to be very long."
    a "It can even be a millisecond if you want."
    c_s sad hanging "...!"
    c blank p2 "You... You really want this, don't you?"
    a "Well, I mean, I don't think I would make that dare if I didn't want it."
    c_s level left "..."
    c straight mad "Fine."
    c p1 hanging "But only for a quick second, okay?"
    a "Okay."
    hide chris with dissolve
    pause 0.1
    $ c_blush = False
    "She took a deep breath of nervousness before grabbing the bottom of her shirt."
    "Her eyes were closed tightly as she slowly shook her head."
    "It almost looked like she was about to cry or something..."
    "That's when she slowly lifted up her shirt, revealing a somewhat pudgy belly."
    "She stopped right at the bottom of her boobs."
    "Her eyes opened and she looked right at me."
    "She still looked very nervous."
    window hide dissolve
    pause 3
    $ current_track = "None"
    stop music fadeout 3.0
    window show
    "She then dropped her shirt, covering herself back up."
    show chris p2 straight mad blank at middle with dissolve
    pause 0.1
    c "I'm sorry, but I just can't do it."
    c "I've never shown a guy my chest before, and this isn't how the first time I do it is going to happen."
    $ c_blush = True
    c p1 scream "I don't care about this stupid dare; I'm not a whore, and I'm not going to act like one!"
    c "And if you don't like it, then you can go fuck yourself!"
    hide chris with moveoutright
    $ C_Points -= 1
    play sound door_slam
    pause 2
    $ c_blush = False
    "..."
    "Well, this was certainly not the smartest I've been..."
    "If she didn't hate me before, it's safe to say she might now."
    "..."
    "I just hope that Brittney and Donald don't think any less of me as a result of this..."
    "The last thing I need is to lose the closest friends I had since I moved here."
    jump nhie_end

#########################
# Christeena Hit Donald #
#########################

label c_dare_hit:
    a "...hit Donald."
    $ c_blush = False
    show chris p1 straight raised blank at middle
    c "Huh??"
    show brit p2 straight raised blank at close_right_b
    show chris at twoleft
    with easeinright
    pause 0.1
    b "What??"
    show don p1 straight casual blank at close_left_d_2
    show chris at middle
    show brit at close_right_b_2
    with easeinleft
    pause 0.1
    d "Say what?"
    a "The only reason we're doing this stupid dare is because Donald wanted to try and perform it on Brittney."
    a "So, I say we should punish him for trying to be so stupid."
    c_s casual "..."
    b_s casual left "..."
    d_s "..."
    show don right
    "Christeena then turned to look at Donald, who then looked back at her in response."
    show chris grin p2
    "Christeena gave a small shrug before reaching across the table and slapping Donald hard in the face."
    play sound punch
    show white zorder 4
    pause 0.05
    hide white
    d small sad wide "OUCH!!"
    b p1 straight mad opened_smile "Damn! That was a rock-solid slap!"
    hide brit
    hide chris
    show don at close_d
    with easeoutright
    pause 0.1
    show don straight mad blank
    "Donald sat there in silence, rubbing his cheek and moving his jaw."
    "He looked at me with an angry expression."
    "Sorry, buddy, but you can't pull stunts like this and expect things to work out."
    $ D_Points -= 1
    $ C_Points += 2
    hide don
    show brit p1 straight casual grin at close_b
    with dissolve
    pause 0.1
    b "Anyway, let's get out of here, shall we?"
    b p2 raised "I don't know about you, but I don't think anything is going to top that spectacle."
    show don p1 straight mad blank at close_left_d
    show brit at close_right_b
    with easeinleft
    pause 0.1
    $ current_track = "None"
    stop music fadeout 3.0
    d_s "..."
    hide don with easeoutright
    play sound door_slam
    pause 1
    show brit casual blank at close_b with easeinleft
    pause 0.1
    "Donald quickly got up and left the cabin."
    b_s sad "..."
    b p1 "I better check on him; he may actually be hurt."
    hide brit with easeoutright
    pause 1
    $ current_track = "\"Reflection\""
    play music reflection
    show chris p1 straight sad blank at middle with dissolve
    pause 0.1
    c_s "..."
    a_s "..."
    c "H-Hey, Alex?"
    a "Yeah?"
    c_s "..."
    c grin "Thanks."
    a "For...?"
    c p2 "For not making me do anything embarrassing or sexual."
    $c_blink = False
    c closed_happy sad smile "And for letting me hit Donald; that was actually kinda fun."
    a_s "...!"
    $c_blink = True
    $ c_blush = True
    c straight dot p1 "Oh, that wasn't too mean, was it?"
    a "I'm not one to judge."
    c_s blank "..."
    $ c_blush = False
    show chris p2 left level blank at middle
    c "Well, anyway..."
    c straight sad grin "...thanks again."
    a "No problem."
    a "Now, what do you say we catch up to the others?"
    c p1 casual "Good idea."
    jump nhie_end




################################################################################
# Donald #######################################################################
################################################################################




# The stuff that happens to Donald should you get him out first

label nhie_d:
    "I suppose getting Donald out could lead to some fun..."
    "Though I suppose the true 'fun' factor is based on who wins and makes him perform a dare."
    show screen finger_points
    show nhie at left zorder 3
    show don p1 straight casual blank at close_left_d_2
    show chris p1 straight casual blank at middle
    show brit p1 straight casual blank at close_right_b_2
    with dissolve
    pause 0.1
    a "Never have I ever..."
    a "...had curly hair."
    d level dot "!!"
    b p2 level opened_smile left "Wow, talk about a personal attack!"
    d_s blank "..."
    $ nhie_d_points -= 1
    with dissolve
    pause 0.1
    "Nevertheless, Donald lowered his final finger, marking him out of the game."
    # Points: A = 3, B = 1, C = 1, D = 0
    hide don
    with dissolve
    show chris at twoleft
    show brit at close_right_b
    with easeinright
    pause 0.1
    b raised grin "Alright, Chris; your turn!"
    c level left "Hm..."
    c "Never have I ever..."
    c raised straight smile p2 "...moved to a new house within the last month!"
    "Well, I suppose I deserved that one."
    # Points A = 2, B = 1, C = 1, D = 0
    $ nhie_a_points -= 1
    with dissolve
    pause .1
    b p1 straight mad opened_smile "DAMN! Christeena's going for the personal attacks, too!"
    c p1 grin "Well, you would kill me if I intentionally got you out."
    b p2 level right huhu "This is true."
    b p1 straight casual grin "Okay, my turn!"
    b level "Never have I ever..."
    b p2 opened_smile "...eaten a Grilled Ham n Cheddar at Kelly's!"
    $ c_blush = True
    c p2 scream mad "What the hell??"
    c blank "I was just trying to be nice and not get you out, and this is how you return the favor??"
    $ b_eyelids = "partial"
    b casual grin "Rule 1 of this game: never be nice! Being nice results in lame games!"
    show chris p1 left
    if acceptsandwich:
        "Christeena still didn't seem happy, and rightfully so, as we each put a finger down."
        $ nhie_a_points -= 1
        $ nhie_c_points -= 1
        with dissolve
        pause 0.1
        # Points: A = 1, B = 1, C = 0, D = 0
    else:
        "Christeena still didn't seem happy, and rightfully so, as she put her final finger down."
        $ nhie_c_points -= 1
        with dissolve
        pause 0.1
        # Points A = 2, B = 1, C = 0, D = 0
    $ b_eyelids = "blink"
    b p1 straight casual grin "Okay, Al. You're up!"
    a "So I am."
    hide brit
    hide chris
    with dissolve
    pause 0.1
    $ c_blush = False
    if acceptsandwich:
        jump al_1_point
    else:
        "Well, well well. I'm at the perfect opportunity to win this game."
        jump brit_out

label al_1_point:
    "Well, now. What an interesting scenario I've found myself in."
    "Brittney and I each have one point left, meaning it's anyone's game."
    "The question now is if I get Brittney out, making me the one to have Donald perform a dare..."
    "...or do I let her get me out, letting HER have Donald perform it?"
    if persistent.choices["19"] == 1:
        jump brit_out
    elif persistent.choices["19"] == 2:
        jump brit_win
    else:
        "I better decide quickly."
        menu:
            "What should I do?"

            "Get Brittney out.":
                $ persistent.choices["19"] = 1
                jump brit_out

            "Let Brittney win.":
                $ persistent.choices["19"] = 2
                jump brit_win

################
# Brittney Out #
################

label brit_out:
    "Sorry, Brittney."
    show brit p2 straight raised grin at close_b with dissolve
    pause 0.1
    a "Never have I ever chipped a tooth."
    b p1 small sad hanging "Ach!!"
    "She then grabbed at where heart would be on her chest and leaned her head back."
    b "I was so close to victory and you stole it from me!"
    b p2 straight blank "For shame, Alexander. For shame."
    a "You're the one who said to not be nice, Brittney!"
    b level right huhu "I know I am. Doesn't make you any less of a butthole."
    a "Well, regardless, I win!"
    b p1 straight level grin "So you do, indeed."
    $ nhie_b_points -= 1
    with dissolve
    pause 0.1
    "And with that, Brittney's final finger was lowered."
    hide screen finger_points
    hide nhie
    with dissolve
    pause 0.1
    # Points: A = 2, B = 0, C = 0, D = 0
    b casual p2 "So, the question now is what you're going to make Donald do."
    hide brit
    show don p1 straight casual blank at close_d
    with dissolve
    pause 0.1
    "That's... actually a good question."
    "I'm straight, and so is Donald, so anything sexual is out of the picture."
    "That still leaves something embarrassing he could do."
    "After all, this whole dare idea spawned from him wanting to have Brittney do something for him, so it would be ironic for the dare to be used against him."
    "...then again..."
    "I could still use this chance to give Donald what he wants."
    "I better decide what I want to do quickly, though."
    a "Okay, Donald."
    show don raised
    a "I dare you to..."
    if persistent.choices["20"] == 1:
        jump d_dare_pushup
    elif persistent.choices["20"] == 2:
        jump d_dare_pond
    elif persistent.choices["20"] == 3:
        jump d_dare_kiss
    else:
        menu:
            "..."

            "...do 50 push-ups.":
                $ persistent.choices["20"] = 1
                jump d_dare_pushup

            "...jump in the pond.":
                $ persistent.choices["20"] = 2
                jump d_dare_pond

            "...kiss Brittney.":
                $ persistent.choices["20"] = 3
                jump d_dare_kiss

##################
# Donald Pushups #
##################

label d_dare_pushup:
    a "...do 50 push-ups."
    d_s casual dot "..."
    d mad grin "No problem."
    show don at close_left_d
    $ b_eyelids = "partial"
    show brit p2 straight raised grin at close_right_b
    with easeinright
    pause 0.1
    b "Oh, really?{w} I don't think I've ever seen you do a push-up."
    d right raised "Well, prepare to be amazed!"
    hide don
    hide brit
    with dissolve
    pause 0.1
    show bg cabin_i_s:
        ease 0.5 xalign 0.0
    $ b_eyelids = "blink"
    "Donald then got up from his seat and moved to the living area, the rest of us quickly following suit."
    "He seems to be perfectly fine with this dare, though whether it's an act to impress Brittney is not currently clear."
    show don p1 straight raised grin at twoleft
    show brit p1 straight casual grin at tworight
    with dissolve
    pause 0.1
    d "Alright, let's do this!"
    b p2 raised "This is certainly going to be more entertaining than it should be."
    $ b_eyelids = "partial"
    b "But what's stopping you from going the sissy route?"
    d casual blank "What do you mean?"
    b casual "I mean, Alex never clarified when you had to do them or if you had to do them all at once."
    $ b_eyelids = "blink"
    show brit p1 straight mad opened_smile
    b "For all we know, you could just say that you'll do one now and the rest later or some sneaky bull like that."
    d right mad grin "What do you take me for? I'll happily do all 50 right here, right now!"
    show brit p2 raised closed_smile
    b "Okay, this I gotta see."
    hide don
    hide brit
    with dissolve
    pause 0.1
    "Oh, boy. This probably won't end well, but I suppose that's part of his punishment."
    $ current_track = "\"Friendly Competition\""
    play music friendly_competition
    "Donald then dropped on the ground and got into the push-up position."
    "He truly does seem ready for this. Maybe he can do it, after all..."
    show brit p1 straight raised grin at middle with dissolve
    pause 0.1
    b "We're ready when you are, Mr. Waters."
    d "Very well, then!"
    "And with that, he started doing push-ups, with Brittney counting them as he went along."
    b mad opened_smile "5{w=0.5}, 6{w=0.5}, 7{w=0.5}, 8{w=0.5}..."
    "He was actually going at a pretty good pace at first, doing them very quickly."
    "Eventually, though, the speed of his push-ups started to decline."
    b p2 raised grin "...20...{w=1.0}21...{w=1.0}22..."
    show chris p2 straight sad blank at twoleft
    show brit at tworight
    with easeinleft
    pause 0.1
    c "...this isn't going to end well, is it?"
    d "I'll...{w=0.5}be...{w=0.5}fine!"
    b p1 mad closed_smile "25...{w=1.0}26...{w=1.0}27..."
    c_s "..."
    a "C'mon, Don! You're over halfway there!"
    "Donald looked at me with a face that showed...{w}well, I'm not sure what emotion it was supposed to be. Anger?{w} Determination?{w} Constipation?"
    "Regardless, he continued his push-ups."
    b opened_smile "33...{w=1.5}34...{w=1.5}35..."
    b p2 grin raised "Let's go, Waters! Pick up the pace!"
    c p1 mad hanging "Brit, don't overwork the guy!"
    b left level huhu "{i}(37){/i} Well, maybe if he {i}(38){/i} wouldn't make such a {i}(39){/i} bold claim, I wouldn't {i}(40){/i} demand so much!"
    a "10 more, Don! You got this!"
    c_s p2 left sad blank "..."
    b straight grin "43!{w=2.0} 44!{w=2.0} 45!"
    "Donald's arms looked like they were about to give out on him. His body was trembling with weakness. His face was red and sweaty."
    b p1 casual opened_smile straight "48!!{w=2.0} 49!!{w=2.0} {i}50!!!{/i}"
    show chris straight casual dot
    $ current_track = "None"
    stop music fadeout(3)
    "At hearing that magical number, Donald collapsed to the ground, breathing heavily, his arms not moving an inch."
    c p1 hanging "Holy crap! I didn't think he'd actually do it!"
    a "Quite the motivator, aren't you?"
    c level blank p2 "I was just being honest."
    $ current_track = "\"Cabin Fever\""
    play music cabin_fever
    hide chris
    show brit at middle
    with easeoutleft
    pause 0.1
    b p2 sad grin "Well, you told me you could do it, and you did it!"
    b "For that, I give you props, Donnie."
    d "{i}*huff*{/i} Thank... {w=0.75}{i}*huff*{/i} you... {w=0.75}{i}*huff*{/i}"
    b p1 level "Shall we help you up?"
    d "...please..."
    hide brit with dissolve
    pause 0.1
    "And with that, Brittney and I each took one of Don's arms and carefully stood him up, moving him to the couch and sitting him down there."
    "His arms flopped to his sides, almost as if he had lost all feeling in them."
    "Well, if I'm being honest, he probably did."
    show brit p2 level grin straight at tworight
    show don p2 straight sad blank at twoleft
    with dissolve
    pause 0.1
    b "We'll let you sit there until you can move again."
    b sad "Though if I'm being honest..."
    extend p1 opened_smile " That was pretty impressive!"
    d casual dot "You...{w=0.5}really...{w=0.5}think so?"
    b casual "I do!"
    $b_blink = False
    b closed sad closed_smile "I mean, yeah, you look like a limp noodle afterwards..."
    $b_blink = True
    extend p2 straight casual grin "but you certainly had more strength than I gave you credit for!"
    d_s blank level "..."
    d grin "Well... thank you."
    hide brit
    show chris p1 straight sad blank at tworight
    with dissolve
    pause 0.1
    c "Feeling a bit better?"
    d p1 right level "Yeah; I just needed a minute. I'm fine now."
    a "Well, I'm glad; I would've felt terrible if my dare permanently harmed ya."
    show chris:
        ease 0.5 xalign 0.9
    show don:
        ease 0.5 xalign 0.1
    show brit p1 straight mad grin at middle with dissolve
    pause 0.1
    b "Hey, it was his ego that would've done the damage; he could've easily gone the sissy route if he wanted to."
    a "I suppose so."
    c p2 casual grin "Well, now that he's doing better, can we head home? I don't want to be out too late, and it looks like Donald's had enough fun for a while."
    $d_blink = False
    d closed smile sad "Yeah, you could say that."
    $ D_Points += 1
    jump nhie_end

###############
# Donald Pond #
###############

label d_dare_pond:
    a "...jump in the pond."
    $ D_Points -= 2
    d mad "What??"
    d "This late at night, when it's incredibly cold out??"
    a "Yep."
    show don at close_left_d zorder 2
    show brit p2 straight casual hanging at close_right_b zorder 1
    with easeinright
    pause 0.1
    b "Damn! That's harsh!"
    $ b_eyelids = "partial"
    b level huhu "I love it! Let's go!"
    show brit:
        ease 0.25 xalign 0.25
    pause .26
    d "Ah!"
    hide don
    hide brit
    with moveoutright
    pause 0.1
    $ b_eyelids = "blink"
    "With that, Brittney quite literally dragged Donald out of the cabin."
    "Christeena and I quickly followed after them."
    scene bg pond_n with dissolve
    play loop forest_nighttime
    pause 0.1
    "By the time we caught up to them, they were already right by the pond."
    show brit p1 straight mad closed_smile at tworight
    show don p1 straight sad blank at twoleft
    with dissolve
    pause 0.1
    b "C'mon! Get in!"
    d mad "W-Wait! Let me go!"
    show chris p2 straight mad blank at threeleft
    show don at middle
    show brit at threeright
    with easeinleft
    pause 0.1
    c "Brit, calm down!"
    b p2 raised grin "Hey, the only way I know he's going to go in is if he's forced in; he's too chicken to do it, himself!"
    d wide "Hey!"
    b left huhu level "Oh, am I wrong?{w} Go on, then! Jump in!"
    d_s left level blank "..."
    b p1 straight mad closed_smile "Yeah, that's what I thought!"
    hide chris
    show brit at tworight
    show don at twoleft
    with easeoutleft
    pause 0.1
    d "Well, I can't just jump in a pond this late at night without a swimsuit or something!"
    b p2 raised grin "Really? That's what's stopping you?"
    b "Ever hear of swimming in your underwear?{w} Or skinny dipping?"
    d straight mad "!!!"
    d "If I said that exact same thing to you in the exact same context, you'd snap my neck!"
    $b_blink = False
    b p1 closed sad closed_smile "In a heartbeat!"
    $b_blink = True
    $ b_eyelids = "partial"
    extend straight level grin " But the point is you're just too cowardly to do it!"
    d "I...!"
    "Uh-oh. This isn't going very well."
    "Donald really doesn't look very comfortable with this dare, and I don't blame him. After all, this dare was made to humiliate him."
    "But still, even I have a conscience, and it's saying this might not be the best idea."
    "I suppose I could tell him he doesn't have to do the dare, after all...{w}but at the same time, I'm still wanting him to receive some sort of punishment."
    "I better make up my mind right now."
    if persistent.choices["21"] == 1:
        jump d_pond_no
    elif persistent.choices["21"] == 2:
        jump d_pond_yes
    else:
        menu:
            "What should I do?"

            "Tell Donald to not do the dare.":
                $ persistent.choices["21"] = 1
                jump d_pond_no

            "Tell Donald to do the dare.":
                $ persistent.choices["21"] = 2
                jump d_pond_yes

label d_pond_no:
    show don:
        ease 0.5 close_d
    hide brit with dissolve
    pause 0.1
    $ b_eyelids = "blink"
    a "Hey, Donald?"
    d raised "Yeah?"
    a "Look, man, you don't have to do the dare."
    a "I was just trying to do something embarrassing and humiliating to punish you for coming up with the dare idea in the first place, but this just doesn't feel right."
    a "I don't want you getting hypothermia or something because of a stupid dare."
    a "So if you really are uncomfortable with doing this, you really don't have to."
    d_s level "..."
    show don at close_left_d zorder 2
    show brit p2 straight level blank at tworight zorder 1
    with easeinright
    pause 0.1
    b_s "..."
    b sad "Well, shit..."
    extend right " Wow I feel like an ass for trying to force this on you."
    b p1 straight "But, he's right. As much as I love picking on you, I suppose something like this could be pretty dangerous. Sorry, Don."
    b p2 right "I guess I really do get a little crazy when I'm tired..."
    d_s "..."
    d grin "It's alright. I forgive you both."
    d left "I suppose I did kinda deserve some sort of punishment for trying to be sneaky."
    $ b_eyelids = "partial"
    b casual straight huhu "Well, how about this?"
    show brit:
        linear 0.3 xalign 1.55
        zoom 1.0
        yalign 0.2
        ease 0.2 xalign 0.25
    pause 0.5
    play sound punch
    show white zorder 4
    pause 0.05
    show brit:
        linear 0.15 xalign 0.9
    hide white
    d small sad blank "OOF!"
    "Before he could even respond to her, Donald got punched right in the chest. Nothing too serious (at least, that's how it looked), but certainly enough to get one's attention."
    $ b_eyelids = "blink"
    $ b_blink = False
    b p1 closed sad closed_smile "There! We'll call that your punishment!"
    d straight level grin "{i}*cough*{/i} I guess so..."
    show don:
        ease 0.5 middle
    show brit:
        ease 0.5 threright
    show chris p1 straight raised blank at threeleft with easeinleft
    pause 0.1
    c "You guys truly are weird..."
    $b_blink = True
    b p2 left level huhu "I try!"
    a "Well, it actually is pretty cold out here; let's all head home, shall we?"
    b p1 straight casual grin "Sounds like a plan!"
    c p2 casual smile "Yeah, let's!"
    d raised "That sounds nice."
    $ D_Points += 1

    jump nhie_end

label d_pond_yes:
    show don:
        ease 0.5 close_d
    hide brit with dissolve
    pause 0.1
    $ b_eyelids = "blink"
    a "C'mon, Donald. It's not that big of a deal."
    d wide "Not that big of a deal??"
    d "I could get sick or worse from something like this, man!"
    a "Still, you lost the challenge, and now you have to do the dare."
    d_s blank "..."
    hide don with dissolve
    pause 0.1
    "Donald remained silent as he took his phone and wallet out of his pockets and handed them to Christeena."
    show don p1 straight mad blank at tworight
    show chris p1 straight casual blank at twoleft
    with dissolve
    pause 0.1
    d "Here, since you're the only one here that cares about me at the moment."
    c_s sad "...!"
    hide don
    hide chris
    with dissolve
    pause 0.1
    play sound splash
    "With that, Donald quickly ran towards the pond and jumped in, fully clothed, fully submerged."
    "A second later, he walked out of the pond, completely soaked from head to toe."
    "He was also shaking very badly."
    show don p1 straight mad blank at tworight
    show brit p2 straight casual blank at twoleft
    with dissolve
    pause 0.1
    d "A-A-Are you h-happy now??"
    b_s sad left "..."
    a_s "..."
    show chris p1 straight sad blank at threeleft
    show brit at middle
    show don at threeright
    with easeinleft
    pause 0.1
    c "Let's get some towels from the cabin, Donald."
    d "P-P-Please."
    $ D_Points -= 1
    hide chris
    hide don
    with easeoutleft
    $ current_track = "None"
    stop music fadeout 2.0
    pause 3
    $ current_track = "\"Reflection\""
    play music reflection
    a "Well, I'm not as happy as I thought I would be."
    b "Yeah, same here."
    $b_blink = False
    b closed_sad "God, I feel like such a bitch right now...{w} I hope he doesn't get sick from this."
    a "Yeah, same here."
    $b_blink = True
    b p1 straight "I really hope he doesn't hate us."
    a "Well, I may have known him longer, but you know him better; I suppose you'd be the better judge of if he would or not."
    b_s left "..."
    extend "I honestly don't know."
    a "Well, then I guess we'll just have to apologize and hope for the best."
    b "I suppose so..."
    "She still looked rightfully upset as she looked towards where Donald and Christeena had walked off."
    a "We better catch up with them."
    b "Good idea."
    $ persistent.d_pond = True

    jump nhie_end

###############
# Donald Kiss #
###############

label d_dare_kiss:
    a "...kiss Brittney."
    d casual dot "!!!"
    show don at close_left_b
    show brit p1 small sad hanging at close_right_b
    with easeinright
    pause 0.1
    b "What??"
    a "Well, isn't that why you wanted to add a dare element in the first place, Don? To do something like this?"
    d level blank "Uh..."
    extend left " kinda, yeah."
    b straight mad blank "So you're just going to give it to him?"
    a "Hey, who am I to deny my childhood friend something he wants?"
    b_s level "..."
    show don:
        linear 0.5 xalign 0.0
    show brit:
        linear 0.5 xalign 1.0
    show chris p1 straight mad blank at middle with dissolve
    pause 0.1
    c "Well, it doesn't feel right to force Brittney into something she clearly doesn't want to do."
    d sad right "Is the thought of us kissing really that awful?"
    b sad small hanging "I...!"
    b p2 straight blank "It's not anything against you, specifically..."
    b right "...but kissing a close friend, dare or not, is just kinda weird, you know?"
    b "If it was someone like Alex, a guy I hardly even know, then I wouldn't care as much."
    if not persistent.b_kiss:
        "Noted."
        $ persistent.b_kiss = True
    show don:
        ease 0.5 xalign 0.1
    show brit:
        ease 0.5 xalign 0.9
    hide chris with dissolve
    pause 0.1
    d level "Still, you are part of my dare."
    b straight raised blank "Yeah, I know.{w} Though why it feels like I've been punished is beyond me."
    a "You'll survive. It's just a kiss; it doesn't have to mean anything."
    $ b_eyelids = "partial"
    b_s level "..."
    b level "...{fast}fine."
    d sad straight "..."
    b raised "Well? What are you waiting for?"
    d_s "..."
    extend "you really are uncomfortable with us kissing, aren't you?"
    $ b_eyelids = "blink"
    b_s straight p2 sad blank "..."
    extend "if I'm being honest with you...{w=.5} yeah."
    d mad "Then you know what?{w=.5} I think I'll turn down this dare."
    b p1 casual hanging "Huh?"
    d sad right "It just wouldn't feel right kissing a girl that doesn't want to kiss me back."
    d "If we're going to kiss, I want it to be because we both want to, you know?"
    b_s sad blank "..."
    a_s "..."
    d left "I figured that since you're always willing to do a dare, that this might've worked in my favor, but now that it's happened, it just doesn't feel right."
    b p2 "Donald..."
    extend grin " that was really sweet."
    d right "So, you're not mad at me?"
    b p1 level "Of course not. Honestly, if I were in your shoes, I'd be lying if I said that the idea of pulling a similar stunt wouldn't cross my mind."
    b sad opened_smile "Plus, you knew that what you were doing was wrong and apologized, just like the Donald Waters I know."
    d_s grin "..."
    a "What about me? You're not mad at me, are you?"
    b p2 raised grin "Why would I? You were just trying to be a wingman."
    b level right huhu "Makes me wish I could have a friend who could do something like that for me."
    hide don
    show chris p2 straight mad blank at twoleft
    with dissolve
    pause 0.1
    c "Ugh..."
    hide chris
    show don p1 straight casual grin at close_left_d
    with dissolve
    pause 0.1
    b p1 casual grin straight "However, this does mean that you still owe Alex a dare."
    a "Nah, no worries. Let's just forget about that and get out of here."
    b level opened_smile "That works, too."
    d level "Yeah, let's get out of here."
    $ D_Points += 2

    jump nhie_end

################
# Brittney Win #
################

label brit_win:
    "You know what? I'm very curious to see what would happen if the roles reversed, with HER making Donald do a dare."
    show brit p1 straight casual grin at close_b with dissolve
    pause 0.1
    a "Never have I ever graduated high school."
    b_s level dot "..."
    b p2 blank "Well, neither have I."
    a "Huh. So I guess that makes it your turn, then."
    b_s "..."
    b raised left grin "So it does."
    "Looks like she's caught on to my plan."
    b p1 straight mad opened_smile "Never have I ever had a penis!"
    $ c_blush = True
    show brit at close_right_b
    show chris p2 straight mad blank at twoleft
    with easeinleft
    pause 0.1
    c "Really? There was no other option you could've come up with?"
    $ b_eyelids = "partial"
    b level huhu "Nope!"
    c_s left "..."
    hide chris
    show brit at close_b
    with easeoutleft
    pause 0.1
    $ c_blush = False
    $ nhie_a_points -= 1
    with dissolve
    pause .1
    "Nevertheless, I lowered my final finger."
    hide screen finger_points
    hide nhie
    with dissolve
    pause .1
    $ b_eyelids = "blink"
    show brit p1 straight mad opened_smile at close_b
    b "Alright, Donald. I guess I'm going to be making you do a dare!"
    show brit at close_right_b
    show don p1 small sad blank at close_left_d
    with easeinleft
    pause 0.1
    d "{i}*gulp*{/i}"
    b p2 right level huhu "Hmm.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
    extend p1 straight casual opened_smile " Oh, I know!"
    b "I dare you to buy all my pads and tampons for me for a year!"
    d straight level "...{w}that's it?"
    b raised grin "That's it."
    d_s raised "..."
    a "Huh. Even I admit that that's a little underwhelming."
    $ b_eyelids = "partial"
    b "Well, I'm not so cruel that I'd make him do something like jump into the pond."
    if persistent.d_pond:
        a "I highly doubt that."
        $ b_eyelids = "blink"
        show brit p2 straight mad hanging at close_right_b
        b "Hey! I'm not a monster!"
        a "Whatever you say."
    else:
        a "I guess."
    $ b_eyelids = "blink"
    b p1 straight casual grin "Plus, at least all the people at the store will know they're not for you, so if anything, you should be happy!"
    d left "I suppose..."
    b p2 left level huhu "Plus, you'd be making me really happy by giving me something I need...~"
    show don:
        ease 0.5 xalign 0.0
    show brit:
        ease 0.5 xalign 1.0
    show chris p1 straight mad blank at middle with dissolve
    pause 0.1
    c "God, you are so embarrassing, Brit."
    b p1 straight raised grin "What? I really do need them! Don't you?"
    $ c_blush = True
    c p2 hanging "!!!"
    "Christeena's face is understandably red."
    a "Alright, now that that's settled, what do you say we call it a night?"
    $ b_eyelids = "partial"
    b p2 level "I suppose so. I'll be sure to let Donald know when I'm in need for supplies."
    c left blank "Ugh..."
    $ d_buy_stuff = True
    $ B_Points += 2

    jump nhie_end
