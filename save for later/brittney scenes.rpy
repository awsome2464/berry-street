label brit_sibling_talk:
    # Context:
    # Brittney and Alex are sitting on the pond's dock, chatting casually.
    # The topic of siblings is brought up.
    python:
        b_hair = 1
        b_hat = 0
        B_Name = "Brittney"
        outfit_b = "a"
        b_blink = True
        current_track = "\"From the Heart\""
        renpy.music.set_volume(0.5, channel='loop')
        b_hair_color = "Blonde"
        b_eyelids = "blink"
        b_eye_bags = ""
    play music from_the_heart
    play loop forest_nighttime
    scene bg pond_n
    show pond_foreground zorder 1
    show brit p2 right grin sad at close_b zorder 2
    a "Heh. It's a bit weird when you think about it."
    b straight casual blank "What is?"
    a "I always thought families having multiple kids was the most common thing in the world..."
    a "...yet out of everyone in Berry Street, Harry and I are the only ones with a biological sibling."
    b_s level right grin "...{w=0.5}{nw}"
    b "...{fast}you're not wrong."
    b sad left "...although that almost wasn't the case, you know."
    a "What do you mean?"
    b level "Heh. Well, uh..."
    b straight p1 "When I was 4, my mom actually got pregnant again."
    a "She did?"
    b p2 casual opened_smile "Yep. She and my father could hardly believe it."
    b grin "Her having one child was rare enough, but another on top of that?"
    $b_blink = False
    b closed "It was like winning the lottery!"
    a "They really wanted another kid, huh?"
    $b_blink = True
    b level left huhu "It was mostly my father. He always dreamed of having a big family."
    b raised straight grin p1 "My mom only wanted at least one child, so you could say that my presence was good enough for her."
    b sad closed "But I definitely have some clear memories of that time in my family's history. The idea of my mommy giving me a little brother or sister made me happy."
    "I suppose it's not difficult to figure out what happened next, but..."
    a "...so, what happened?"
    show brit p2 sad right
    "She took a deep breath as her smile looked a lot more forced all of a sudden."
    b "Well, she was pretty far along. I think 6 or 7 months."
    b "Far enough along to where they had a name picked out for her: Elizabeth."
    b "All seemed to be going well up until that point, from what I've been told."
    b blank "But then, one day..."
    b "...out of nowhere..."
    b_s "..."
    $b_blink =  False
    show brit closed_sad
    "She closed her eyes and swallowed hard before finishing with:"
    $b_blink = True
    b "...Elizabeth's heart stopped beating."
    a "Dang..."
    $b_eyelids = "wince"
    b left "Yeah."
    b "My mom was warned many times throughout her life that complications could happen during pregnancy, but that still didn't properly prepare her for that moment."
    $b_eyelids = "blink"
    b straight "I was definitely as hurt as a kid my age could've been at finding out that my little sister wasn't coming, after all, but I obviously didn't really understand everything."
    $b_eyelids = "wince"
    b right p1 "I still have some faint memories of my mom crying not too long afterwards."
    b grin "I tried anything I could to make her feel happy. Like I said, I didn't fully understand the situation."
    a "Of course."
    $b_eyelids = "blink"
    b straight blank "I don't remember too many things about my father at that time, but one thing for sure still sticks in my mind to this day."
    b level left p2 "I was already tucked in bed for the night, but I could hear them through the wall; my room was right next to the dining room."
    b "He told her that he still loves her."
    b sad "And that he always would, no matter how many kids they had."
    "I could see her eyes starting to water up a bit as she recalled the event."
    a "Wow... I had no idea your family went through all that."
    b level straight p1 grin "Heh. It doesn't exactly make for a good conversation starter."
    a "Valid point."
    show brit sad
    "We both gave awkward chuckles before sighing."
    b p2 sad "But you know what the craziest part was?"
    a "What?"
    b level "She was willing to try having another baby."
    a "You're kidding."
    $b_eyelids = "wink"
    b raised tongue "I didn't inherit my stubbornness from my old man, you know."
    $b_eyelids = "blink"
    b casual grin p1 "But she really was insistent on having another kid."
    b sad left "Giving me a younger sibling to bond with, giving my father his wish of a bigger family..."
    b p2 "That's something I'll never stop respecting about my mom: she loves her family and is willing to do anything for them."
    a "Yeah, I've certainly noticed."
    a "But still. Wanting to try getting pregnant again right after she--"
    b casual straight blank "Oh, it wasn't right away."
    b "She was still hit pretty hard by the loss of Elizabeth."
    b sad "We all were."
    b grin "But she swore she'd try again when she was ready."
    b right "...of course, by the time she was ready..."
    b "...my father... you know..."
    a "...yeah."
    b_s blank "..."
    "It's like she wasn't even trying to hide the pain she was feeling anymore."
    $b_blink = False
    show brit closed_sad
    "She moved her legs up and against her chest, hugging them against her as she let out another sigh."
    a "I'm sorry you guys went through that."
    b grin "It is what it is."
    a_s "..."
    a "Well, I'm not sure how much better it'll make you feel, but..."
    a "...my family's been through a very similar situation, too."
    $b_blink = True
    b straight casual blank "Really?"
    b "Your mom miscarried, too?"
    a "Worse."
    a "Worse;{fast} he died AFTER he was born."
    b hanging p1 "Oh, my god!"
    "She let her legs go and turned towards me completely."
    b blank "What happened?"
    a "Well, to make a long story short..."
    a "...around 5 years before I was born, my parents had their first kid, Zachary."
    extend " About 2 years later, he died from a brain tumor."
    $b_eyelids = "wince"
    b p2 sad hanging "Jesus...!"
    "She quickly covered her mouth in shock."
    b "I thought you meant like he died literally right after he was born!"
    a "Nah, he was around for a while afterwards."
    $b_eyelids = "blink"
    b blank "I'm so sorry...!"
    a "I mean, I never met him. Like I said, this was years before I was even conceived."
    b p1 "Still..."
    b "I had no idea..."
    a "Like you said, it's not exactly something to randomly bring up."
    a "Plus, it's not like your situation where you can remember firsthand some of the things that happened."
    b p2 left "I suppose..."
    $b_eyelids = "wince"
    b "Still, though. That had to have been so awful on your parents."
    a "Yeah, I can only imagine."
    a "Honestly, part of me believes that they still haven't really gotten over it even to this day."
    $b_eyelids = "blink"
    b p1 "Well, I don't think pain like that ever goes away completely."
    b straight "Even with Mom and Elizabeth... Sometimes I wonder..."
    "We then stared at each other in silence for a few seconds, not really sure where to go from here."
    show brit p2 right level
    "Brittney then turned back towards the pond with a look of heavy thought."
    b "Hey, Alex?"
    a "Yeah?"
    b "So, like..."
    b "You believe in God and Heaven and all that stuff, right?"
    "I was thrown off for a second at the seemingly sudden change of topic."
    a "Yeah. Why?"
    show brit sad
    "She took a deep breath before continuing."
    b "Well, Donald's always told me that he believes everything happens for a reason."
    b "He says that God allows certain things to happen, no matter how painful they may be at the time, to help you in the long run."
    a "He's not wrong. There are plenty of stories in the Bible where something like that happens."
    b level "Alright. So I guess what I'm trying to wrap my head around is..."
    b straight raised "...how did losing Elizabeth help my family?"
    a_s "..."
    "No matter how many times it happens, seeing Brittney be serious like this never stops feeling weird."
    a "Well, honestly, I don't really know how to answer that."
    a "I don't exactly know the full context of everything that's happened in your lives the way you do."
    b_s level left "..."
    b "I suppose that's fair..."
    a "Though if you want to hear an explanation from my family's situation..."
    b_s straight raised "..."
    a "I think losing Zach really made my parents a lot better at keeping me and Harry safe."
    a "I know his death wasn't because of anything they did or didn't do, but like you said, that kind of pain doesn't really leave."
    a "Seriously, if I had a dollar for every time our dad told us something along the lines of {i}\"I buried one kid, I'm not burying another!\"{/i} when we did something dangerous..."
    b_s sad "..."
    a "Yeah, I get annoyed sometimes about how OVERprotective they can be, and how my dad can guilt trip us like that sometimes..."
    a "...but looking back, I'm sure if they didn't behave that way, one or both of us might've been really hurt or killed on multiple occasions."
    a "Chicago isn't exactly a 'child-friendly' place, after all."
    b left sad grin "Heh..."
    b "I guess I see what you mean."
    b blank "But I dunno. I can't really see anything like that for my family's case."
    b "First Elizabeth, and then my father..."
    a "Well, sometimes these things aren't really noticed until much, much later in life."
    b "Maybe."
    a_s "..."
    b_s "..."
    hide brit with dissolve
    pause 0.1
    nvl clear
    window hide dissolve
    nvl show dissolve
    narrate """
    More silence.

    This time, it lasted for what felt like several minutes.

    We both just faced towards the pond and took in the view.

    {nw}

    I know Brittney can get pretty deep on occasion, but topics like this had never really come up around me.

    Still, it was a pretty interesting conversation, even if it did end a bit awkwardly.

    Finally, she stood up.
    """
    nvl hide dissolve
    window show dissolve
    show brit p1 straight level grin at close_b zorder 2 with dissolve
    pause 0.1
    b "It's getting pretty late. We better head home."
    a "Yeah, good idea."
    hide brit with dissolve
    pause 0.1
    "I stood up, as well, and we walked back to Berry Street."
    "We didn't say anything on the way."
    "After a minute or so, we made it to her house."
    scene bg house_ut with dissolve
    pause 0.1
    "Before we went on our separate ways, she stopped and turned to me."
    show brit p1 straight sad grin at close_b with dissolve
    pause 0.1
    b "Hey, Al?"
    a "Yeah?"
    b p2 "Thanks."
    a "For...?"
    b "That talk back there."
    b right "It was...{w=0.5} It was nice to talk about that with someone. Get a different perspective and all that."
    a "Oh. Uh, yeah. No problem."
    a "Same to you. Thanks."
    b p1 straight raised "Anyway, see ya tomorrow."
    "She held her fist in front of her."
    a "See ya tomorrow."
    "I replied as I bumped it."
    "With that, she walked towards her porch."
    hide brit with easeoutright
    pause 1
    "..."
    "Before she opened the door, she turned around and looked at me."
    "She gave a small smile and wave when she did, I gesture I returned."
    "She then went into her house."
    "After taking a deep breath, I walked back to my house."
    $current_track = "None"
    stop music fadeout(3)
    "Brittney truly is something else."
    "I gotta admit, seeing her not be a crazy pervert and instead be a calm and mature young woman really makes me even more fascinated with her."
    "I just hope she actually thinks about what I said to her."
    return

#############################################################################################################

label brit_shopping:
    python:
        b_hair = 1
        b_hat = 0
        B_Name = "Brittney"
        outfit_b = "b"
        b_blink = True
        current_track = "None"
        b_eye_bags = ""
    window hide
    stop music
    scene bg fade
    pause 1
    $current_track = "\"Friendly Competition\""
    play music friendly_competition
    scene bg basketball_park with dissolve
    pause 0.5
    show brit p1 straight mad closed_smile:
        zoom 1.0
        xalign 0.45 yalign 0.2
        parallel:
            linear 0.4 xalign 0.55
            linear 0.4 xalign 0.45
        parallel:
            linear 0.2 yalign 0.25
            linear 0.2 yalign 0.2
            repeat 2
        repeat
    with dissolve
    pause 0.1
    window show dissolve
    pause 0.1
    b "C'mon, Sprouse! Let's see what ya got!"
    "I dribbled the ball in front of me, looking her dead in the eye."
    "The last thing I need to do is give any indication of weakness or fault."
    $current_track = "None"
    stop music fadeout(3)
    hide brit with dissolve
    pause 0.1
    "{i}Alex wins the 1 on 1.{/i}"
    $current_track = "\"Outside the Street\""
    play music outside_the_street
    show brit p2 straight level grin at close_b with dissolve
    b "Heh.{w=0.2} Not bad."
    a "Oh, admit it; you're impressed."
    b left derp "I will admit to no such thing."
    $b_eyelids = "partial"
    b p1 straight huhu "Anyway, what do you say we get out of here before I feel the urge to rematch you?"
    a "Whatever you say, sore loser."
    $b_eyelids = "wink"
    b p2 raised tongue "Nyeh."
    hide brit with dissolve
    pause 0.1
    $b_eyelids = "blink"
    "She then jogged over to the bench where our bags were laying."
    "How she can still have the energy to move is beyond me."
    "Then again, she's the trained athlete while I'm the average Joe in training."
    b "...dammit..."
    "As I picked up my bag, I could hear her mutter to herself."
    show brit p2 right level blank at close_b with dissolve
    pause 0.1
    "She was looking at her phone in annoyance."
    a "What's up?"
    b "My mom said she needed me to get some stuff from Dolmart on my way home."
    show brit straight sad
    "She then looked at me with a slightly sheepish expression."
    b "You don't mind, do you?"
    a "Not at all."
    b p1 level grin "Alright, good. Thanks."
    b sad "It's not a lot, I promise."
    a "Hey, don't worry about it, really."
    a "Trust me, I know how inconvenient parents can be."
    b p2 left level huhu "You said it, not me."
    window hide dissolve
    pause 0.5
    scene bg fade with wipeleft
    pause 1
    play loop dolmart fadein(0.5)
    scene bg dolmart_i with wipeleft
    pause 0.5
    window show dissolve
    show brit p1 straight casual grin at close_b with dissolve
    pause 0.1
    b "Alright, so obviously, it'll be faster if we each take half the list."
    a "Right.{w=0.2} So, how are we going to tackle this?"
    b left level derp p2 "Hm..."
    b straight raised closed_smile "I guess I can take the soda and shampoo while you get the milk and apples."
    a "Sounds like a plan."
    a "Well, the milk and soda are pretty close to each other, so we may as well walk over there together."
    $b_eyelids = "partial"
    b p1 level grin "What, do you wanna be around me that much?"
    a "Just thinking logically."
    $b_eyelids = "blink"
    b p2 level left huhu "Mhm.{w=0.2} Sure thing."
    hide brit with dissolve
    pause 0.1
    "After a quick walk down the main aisle, we approached the soda aisle."
    show brit p2 straight casual grin at threeleft with dissolve
    pause 0.1
    b "Alright, let's text each other when we've got our stuff and then meet up at the checkout."
    "I gave her a thumbs-up, and she walked down the aisle."
    show brit:
        ease 0.75 xalign -1.0
    hide brit with dissolve
    pause 0.5
    "With that, I kept moving towards the back of the store."
    $current_track = "None"
    stop music fadeout(3)
    stop loop fadeout(3)
    "...at least, I DID until I heard quick movement behind me."
    "I turned around to see what the noise was."
    $b_eyelids = "wince"
    pause 0.5
    show brit p2 small sad hanging at threeleft with easeinleft
    pause 1
    "I managed to see Brittney finishing what appeared to be a quick bolt out of the aisle and pressing her back against the end display."
    "Her hand was clutching at her chest, eyes were completely wide, and appeared to be breathing quickly and heavily!"
    "Overall, she looked like she had just witnessed a murder or something."
    "At that sight, I moved back to her quickly."
    show brit:
        ease 0.5 close_b
    pause 0.6
    a "Are you okay??"
    b blank straight "Wha--?"
    "She seemed spaced for a moment before realizing I had noticed her."
    $b_eyelids = "blink"
    b level grin p1 "O-Oh, yeah! Of course."
    b p2 left "I-It's just...{w=0.5} ya know..."
    b sad "It just...{w=0.5} It doesn't make sense to grab the soda first."
    b right "I'd have to lug a 24-pack across the store to grab the shampoo, which would just kill my arms."
    b straight level "S-So I'll just grab the shampoo and then come back for the soda.{w=0.5} Just makes more sense that way, ya know?"
    a_s "..."
    "I mean, her logic isn't exactly wrong, but..."
    "Well, Brittney may be weird, but this is unusual behavior even for her."
    a "Uh, yeah, sure.{w=0.2} Makes sense."
    b right "Alright, cool."
    hide brit with easeoutright
    pause 1
    a_s "..."
    "Once she was far enough away from me, I approached the soda aisle."
    pause 0.5
    play loop dolmart fadein(1)
    scene bg cg_andi_aisle
    with Dissolve(1)
    pause 1
    "There was nobody in the aisle except for one person."
    "A girl around our age was putting a couple of 2-liter bottles of soda into a cart."
    "I didn't recognize her, but assuming nobody left since she bolted, Brittney did."
    "And based on her reaction, she's clearly terrified of her."
    "But why?"
    "The girl must've felt my eyes piercing her, because she then glanced my way."
    "I quickly looked away and walked towards the dairy section."
    scene bg dolmart_i with dissolve
    pause 0.1
    "Now I'm left with more questions than I started with."
    "But right now, I guess I should focus on the task at hand."
    window hide dissolve
    pause 1
    scene bg fade with wipeleft
    pause 1
    scene bg dolmart_i with wipeleft
    window show dissolve
    pause 0.1
    $current_track = "\"Outside the Street\""
    play music outside_the_street
    "We were quickly able to grab the 4 things and meet at the self-checkout."
    show brit p1 straight level grin at middle with dissolve
    pause 0.1
    "Brittney looks like she's calmed down since I had last seen her."
    "Yet I still couldn't help but feel like there was a hint of worry in her face."
    "Regardless, we didn't really talk as she rang everything up."
    "After making sure we had everything, we brought it back to her car and were on our way home."
    window hide
    pause 0.5
    play sound truck_start
    pause 1
    stop loop fadeout(1.5)
    scene bg brit_car
    with Dissolve(1.5)
    pause 1
    window show dissolve
    show brit p1 straight level grin at middle with dissolve
    pause 0.1
    "There was still silence as she drove, save for the occasional groan or hum in response to traffic."
    "..."
    "It was honestly very uncomfortable, and part of me felt like she was thinking the same thing."
    "..."
    "I guess it's only fair to continue the last conversation we had, right?"
    a "Hey, Brit?"
    b casual "Yeah?"
    a "Out of curiosity, did you know that girl in the soda aisle?"
    $current_track = "None"
    stop music fadeout 3
    b_s level blank "..."
    "In the blink of an eye, her entire demeanor changed."
    "She tensed up immensely, the panic reappearing on her face."
    "I think she looked paler all of a sudden, as well."
    b "I don't wanna talk about it."
    "..."
    "Okay, THAT was scary:{w=0.2} there was not an ounce of emotion anywhere in that sentence."
    "This is honestly getting me more and more curious about the situation."
    "..."
    window hide
    menu:
        "Press for more info.":
            jump press_brit
        "Leave it be.":
            jump leave_it_be

label press_brit:
    $B_Points -= 2
    window show dissolve
    pause 0.1
    a "I'm just saying you looked like you did."
    b_s "{cps=*0.1}. . .{/cps}"
    a "And your reaction to seeing her was pretty worrying."
    b_s mad "{cps=*0.1}. . . . .{/cps}"
    "It looked like she was gripping the steering wheel even harder."
    "And I wasn't sure if it was just the vehicle moving, but it looked like she was shaking a bit."
    b "I said I don't wanna talk about it."
    "Now her voice had an emotion: annoyance."
    "But I feel like I'm getting somewhere here."
    a "I'm just curious, that's all."
    a "I mean, it almost comes off like she hurt you or--"
    play sound tire_squeal
    show brit small frown
    "Before I could even finish my sentence, she slammed on the brakes!"
    "By the time I could collect my thoughts, I realized she was leaning into my face."
    show brit straight frown:
        linear 0.2 close_b
    b "{i}I SAID I DON'T WANNA FUCKING TALK ABOUT IT!!!{/i}"
    show brit:
        parallel:
            linear 0.2 zoom 1.2
        parallel:
            linear 0.2 yalign 0.1
    b "{i}CAN YOU NOT GET THAT THROUGH YOUR FUCKING HEAD?!{w=0.2} I DON'T WANT TO FUCKING TALK ABOUT IT!!!{/i}"
    $b_eyelids = "wince"
    show brit:
        parallel:
            linear 0.2 zoom 1.4
        parallel:
            linear 0.2 yalign 0.1
    b hanging "{i}AND IF YOU BRING IT UP ONE MORE TIME, I'M GONNA BASH YOUR FUCKING FACE IN!!!{/i}"
    show brit:
        parallel:
            linear 0.2 zoom 1.6
        parallel:
            linear 0.2 yalign 0.05
    b frown "{i}SO JUST!!{w=0.5} FUCKING!!{w=0.5} DROP IT!!!{/i}"
    a_s "{cps=*0.1}. . . . . . . . . ."
    a "Okay."
    a "I'm sorry."
    b_s blank "..."
    $b_eyelids = "blink"
    $b_blink = False
    show brit p2 closed_sad level:
        ease 0.5 middle
    "She leaned back into her seat and grabbed her head, taking a long, deep breath."
    $b_blink = True
    show brit right
    "After wiping her eyes and checking the road, she continued the drive home."
    "..."
    "The rest of the ride home was even more silent than before."
    jump brit_shopping_finished

label leave_it_be:
    window show dissolve
    pause 0.1
    a "Alright, then."
    "I suppose if I really wanted to pursue this, a certain sister of hers might be a good source."
    "With that, we drove the rest of the way home."

label brit_shopping_finished:
    hide brit with dissolve
    pause 2
    
    return

#############################################################################################################

label checking_on_brit:
    # Context:
    # After around a month of Donald ignoring Brittney, she enters a heavily depressed state.
    # Alex comes over to check up on her as a request from Christeena, who is currently spending the week with her birth mother in Californa.
    python:
        b_hair = 9
        b_hair_color = "Brown"
        b_hat = 0
        B_Name = "Brittney"
        outfit_b = "z"
        b_blink = True
        current_track = "None"
        b_eyelids = "partial"
        b_eye_bags = "_Bags"
    stop music
    scene bg brit_room_e
    play sound door_knock
    a "Hey, Brittney?"
    "..."
    "I thought I heard a slight movement from the other side."
    a "Brit, open up."
    "..."
    a "Please."
    "I could feel my voice crack at that plea."
    b_s "...{w=0.5}{nw}"
    b "...{fast}why should I?"
    "I let out a small, shaky sigh of relief;{w=0.2} I had confirmation that she was at least alive."
    "The fact that I needed that confirmation still worries me, but I gotta be positive."
    "That said, her voice sounded hoarse and was barely audible."
    a "I wanna see how you're doing."
    b_s "..."
    a "I'm worried about you, Brit.{w=0.2} So is Chris."
    b_s "..."
    "A few more seconds of silence."
    "I was about to speak again, but I heard what sounded like her getting off her bed."
    "After a few seconds of slowly-paced footsteps, the door handle turned."
    window hide
    play sound door_open
    pause 1.5
    show brit p2 straight level blank at middle
    with Dissolve(3.0)
    pause 1
    window show dissolve
    "Oh, Lord..."
    "I knew she was a depressed wreck, but this is worse than I imagined."
    "I could probably see my reflection in her face with how oily it was."
    "Her hair looked frizzled and knotty.{w} Oh, I meant the hair on her head, not her legs."
    "And those bags under her eyes...{w=0.2} How much sleep has she been getting?"
    b "There.{w=0.5} I'm here.{w=0.5} Happy?"
    a "Not at all.{w=0.2} You look awful."
    b left "Yeah, that's what every woman wants to hear."
    "Well, at least her wit is still there, even if it's delivered in deadpan."
    play sound stomach
    "That's when I heard a loud gurgling from her stomach."
    a "Geez, when was the last time you ate?"
    b right "I dunno."
    a "...Brit..."
    b straight "Yeah?"
    a_s "..."
    $ current_track = "\"From the Heart\""
    play music from_the_heart
    "This is honestly breaking my heart."
    "It's so hard to believe that this was the same person who spent half a year helping me better myself."
    "And now here she is looking like an absolute train wreck in every way possible."
    "..."
    "Well, I guess it's about high time I returned the favor."
    a "Let's get you some food.{w=0.2} Is there anything you want?"
    b_s left "..."
    "I'll take that as a {i}\"Surprise me!\"{/i}..."
    a "Alright, I'll be back in a minute. I'll see what you guys have downstairs."
    b_s "..."
    a_s "..."
    "With that, I went to the kitchen to find anything edible.{w=0.2} Shouldn't be too hard."
    window hide
    pause 1
    scene bg fade with wipeleft
    pause 0.5
    scene bg brit_room_i with wipeleft
    window show dissolve
    pause 0.1
    a "Alright, he--"
    "I paused in shock at the state of her room."
    "Laundry tossed everywhere, a few things on the shelves and dresser knocked over, and there was a slight disgusting smell coming from somewhere."
    "And no, it wasn't coming from Brittney;{w=0.2} the stench SHE was radiating was the unmistakable scent of B.O."
    "Speaking of Brittney, she was lying on her bed, hands by her side, staring blankly at the ceiling."
    a "Um, anyway, I grabbed a granola bar from your cupboard.{w=0.2} I've got some water, too."
    show brit p2 level right blank at middle with dissolve
    pause 0.1
    b_s "..."
    show brit straight
    "She eventually turned her head towards me, eyes locking onto the wrapped treat and bottled liquid in my hands."
    show brit p1
    "Slowly, but surely, she sat up and turned towards me, her arm extending towards the food."
    "I handed her the bar, which she proceeded to slowly unwrap and take an ever-so-tiny bite out of."
    "All while doing this, she was staring blankly towards the ground."
    "I honestly felt like I was watching a machine rather than a human."
    "Giving a silent sigh, I walked over and sat next to her on the bed."
    show brit:
        ease 0.5 close_b
    pause 0.6
    a "Better?"
    b p2 right "Not really."
    "Her voice was still somehow more gravely than our smoker neighbor."
    show brit straight
    "I opened and offered the water bottle, a move she accepted just as slow as the granola bar."
    "After a few gulps from the bottle, she closed it up and laid it beside her."
    b left "...thanks."
    "It was still a whisper, but it was clear."
    a "You're welcome."
    b_s "..."
    a_s "..."
    "We both then sat in silence while she continued to eat and drink."
    "At least she was actually doing it, which I guess is a step in the right direction of fixing her up."
    "Though somehow, I don't feel like I'm in the best position to be helping her bathe, even if I HAVE seen her naked.{w} And I definitely ain't shaving her." # Context: the two have had sex at this point
    "At last, she finished her first meal in who knows how long and sighed."
    a "How you feeling?"
    b_s straight "..."
    a_s "..."
    a "Brit, please talk to me."
    b_s right "...{w=0.5}{nw}"
    b "...{fast}what's there to say?"
    b "I look like shit, I feel like shit, and I AM shit."
    a "Brittney, that's not true."
    "Well, one of those things aren't, at least."
    a "You're not shit.{w=0.2} You're nothing like that."
    b grin "Heh."
    "Showing emotion.{w=0.2} Progress."
    b "You don't know anything about me, Alex."
    a "I know you're kind.{w=0.2} I know you're funny.{w=0.2} I know you care about people."
    b straight "See, that's where you've got it all wrong."
    b "That's just who everyone wants me to be.{w=0.2} That's just who I am to try and make everyone happy."
    b right blank "But sooner or later, the real me slips through the cracks.{w=0.2} And before you know it..."
    $b_blink = False
    $b_eyelids = "blink"
    b closed_sad "...they hate me."
    a "Brittney, what the hell are you talking about?{w=0.2} Nobody hates you."
    $b_blink = True
    $b_eyelids = "partial"
    b straight "You know that's not true."
    b left "If he didn't hate me, he would've said something to me by now."
    b sad "If...{w=0.5} If he didn't hate me...{w=0.75} he would have at least acknowledged that I exist..."
    "Her voice was starting to crack, and her lip was starting to quiver."
    a "Brittney, Donald doesn't hate you.{w=0.2} That's just not like him."
    $b_eyelids = "wince"
    b p1 straight mad hanging "Oh, don't act like you haven't seen how he's been treating me!"
    "Okay, maybe dial the emotion back just a tiny bit."
    b p2 left blank "I mean, FUCK!{w=0.2} I know I'm worthless, but still!"
    $b_eyelids = "blink"
    b straight "I've tried everything I could to get him to say something to me, but nothing!"
    $b_eyelids = "wince"
    b p1 hanging "For God's sake, I dyed my fucking hair just so he would say SOMETHING to me!!"
    b p2 right blank "He could've told me it was horrible, that I looked ugly, that I should've dyed it hot pink!!"
    b "Just ANYTHING that required him to say a single syllable directed at me!!"
    $b_eyelids = "blink"
    b straight "You don't go this far out of your way to avoid talking to someone if you don't hate them, Alex!"
    b left "I mean, yeah, I knew he would hate me one day, but fuck, it doesn't mean it doesn't hurt like a fucking bitch!"
    $b_blink = False
    b closed_sad frown p2 "Just...{w=0.75} ARGH!!!"
    "She grabbed and squeezed the top of her head as she leaned back onto the bed with a growl of frustration."
    $renpy.block_rollback()
    "I paused for a second or so;{w=0.2} there was a lot to unpack in all of that."
label brit_depression_questions:
    if brit_depress_questions >= 3:
        jump brit_comes_out
    else:
        menu:
            "What should I ask about [first_or_next]?"

            "\"You think you're worthless?\"" if britdepression["worthless"] == 0:
                jump thinks_shes_worthless

            "\"That's why you dyed your hair?\"" if britdepression["dye"] == 0:
                jump dyed_her_hair

            "\"You 'knew' he would hate you?\"" if britdepression["donhate"] == 0:
                jump knew_he_would_hate

label thinks_shes_worthless:
    a "You think you're worthless?"
    python:
        brit_depress_questions += 1
        britdepression["worthless"] = brit_depress_questions
        first_or_next = "next"
        b_blink = True
        b_eyelids = "blink"
    b p2 level straight blank "I KNOW I am."
    a "Brit, that is not--"
    b p1 mad "Yes, it IS true, Alex!"
    $b_eyelids = "wince"
    b p2 right "I'm just a disposable piece of trash that everyone forgets about in due time!"
    b "Yeah, maybe they'll like me at first, but once they find someone better, I'm just a speck in their memory!"
    b "They'll stop thinking about me.{w=0.2} They'll stop checking in on me.{w=0.2} They'll stop prioritizing me, no matter how special I once was to them."
    $b_eyelids = "partial"
    b raised "Hell, the only ones who've stayed by my side the longest are my parents and Chris."
    b "But we're not all gonna be living together forever.{w=0.2} And once we're all in separate houses, they'll slowly stop thinking about me, too."
    a "Brittney...!"
    b straight mad "Save the pity, Alex."
    b "It's happened to everyone else I knew; it'll eventually happen to everyone I currently know, as well."
    $b_eyelids = "blink"
    b p1 hanging "Including you."
    a "Fat fucking chance."
    a "You mean way too much to me for me to just forget about you."
    $b_eyelids = "partial"
    b p2 level blank right "Hmph.{w=0.2} If I had a fucking nickel..."
    "I had no idea that Brittney thought this low of herself, though I guess if what she's saying about losing friends and loved ones is true, then I truly do feel for her."
    "Though as much as I hate to admit it, I don't think I'm gonna be changing her mind about her self worth in this conversation."
    jump brit_depression_questions

label dyed_her_hair:
    a "That's why you dyed your hair?"
    python:
        brit_depress_questions += 1
        britdepression["dye"] = brit_depress_questions
        first_or_next = "next"
        b_blink = True
        b_eyelids = "partial"
    b straight level grin p1 "Pretty sad, right?"
    "She ran her fingers through her ratty hair with a chuckle."
    b "Ruined my perfect and natural blonde hair just so my friend would say something to me."
    b p2 left "And it didn't even fucking work."
    b straight "So there's time and money down the toilet."
    a "Well, I mean, it seems that everyone else likes it, myself included."
    b right blank "Yeah.{w=0.2} Everyone but the one person I did it for."
    b raised "Or maybe he DOES like it and just didn't bother to say it.{w=0.2} I dunno."
    b straight "Point is, the plan failed.{w=0.2} So fuck me, I guess."
    "She really is very desperate to get Donald to acknowledge her."
    "If only I could get Donald to see just how much his petty grudge is destroying her."
    jump brit_depression_questions

label knew_he_would_hate:
    a "You 'knew' he would hate you?"
    python:
        brit_depress_questions += 1
        britdepression["dye"] = brit_depress_questions
        first_or_next = "next"
        b_blink = True
        b_eyelids = "partial"
    b p2 raised straight blank "Of course I did."
    b right "After all, everyone always does, in the end."
    a "Right, that whole thing about your \"real\" self, whatever that means."
    b p1 level straight "I'll tell you exactly what it means."
    b left "Imagine, if you will, an annoying piece of shit who constantly roasts those she cares about."
    b "Now imagine that every now and then, she says something that goes a bit too far."
    b "Something that hits her loved one close to home and kills their mood."
    a "But if it was a joke, then that's their fault."
    b straight mad "Doesn't matter whether it a joke or not;{w=0.2} they take it personally, regardless."
    $b_eyelids = "blink"
    b p2 right "They take it personally, and you end up feeling awful for hurting them."
    b "And yet, despite feeling awful about it, you still continue to do it without even stopping to think about the consequences."
    b straight raised "That's what I mean by my real self."
    b "Sure, I come off as a kind, funny person, but deep down, I'm just a bitch who's only satisfied when she's hurting those around her."
    $renpy.pause(hard=True)

label brit_comes_out:

