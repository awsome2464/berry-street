label churchends:
    python:
        B_Name = "Brittney"
        C_Name = "Christeena"
        E_Name = "Eleanor"
        b_hair = 1
        outfit_b = "c"
        outfit_c = "c"
        outfit_d = "c"
        outfit_e = "b"
    show text "{size=+50}June, 2013{/size}":
        xalign 0.5 yalign 0.05
    show screen calendarOs
    show calendar june june_23:
        xalign 0.5 yalign 0.6
    show calendar_circle:
        xalign 0.31 yalign 0.77
    with dissolve
    if replay == False:
        $ persistent.todays_date = "June 23rd, 2013"
        $ renpy.notify("Game saved!")
        $ renpy.save("1-1")
    pause 4
    hide text
    hide screen calendarOs
    hide calendar
    hide calendar_circle
    with dissolve
    pause 1
    scene bg church_e with dissolve
    $ current_track = "\"Sunday Service\""
    play music sunday_service
    window show dissolve
    $ renpy.block_rollback()
    "When service ended, I walked outside the church, the realization that I'd been in a building for a couple hours coming to me as my eyes were blinded by the sun."
    "Once they adjusted, I could feel a hand grab onto my shoulder."
    show don p1 straight casual grin at close_d with dissolve
    pause 0.1
    d "Great to finally see you here, Man!"
    a "Yeah, it's nice to finally BE here!"
    a "It's been a while since we went to church, so having some sort of familiar routine back in place feels great."
    "We had been so busy packing in Chicago and unpacking in Smalltown that we either forgot or didn't have time to attend church services."
    "Now that we were finally unpacked, though, we were able to start attending again."
    "Well, Harry and I were, at least."
    "Mom and Dad decided to take one more week off to relax. Honestly, I probably would've done the same if it weren't for Harry's insistence of me bringing him."
    "Speaking of which..."
    show don:
        ease 0.5 tworight
    show harry p1 casual straight closed_smile at twoleft with easeinleft
    pause 0.1
    h "THERE you are!"
    a "Here I am."
    d raised left "What did you think?"
    h level blank "Well, it was different than what I'm used to..."
    h sad grin "...but everyone was so friendly, including the preacher!"
    $d_blink = False
    d closed sad smile "Always nice to hear!"
    a "Yeah, gotta agree with Harry on this."
    h raised "For once?"
    a "For once."
    $d_blink = True
    d raised straight grin "You two, I swear..."
    h sad small blank "Shoot!"
    show don straight casual blank
    a "What?"
    h "I left my Bible in there! I'll be right back!"
    hide harry with easeoutleft
    pause 0.5
    show don at middle with easeinright
    d raised grin "That boy sure knows how to run."
    a "Yeah, tell me about it."
    a "Say, I'm a little curious..."
    d casual "Yeah?"
    a "Why aren't the girls here? Haven't you ever invited them?"
    d level blank right "More times than I can count."
    d straight raised "Christeena's an atheist, so getting her to go is as difficult as you'd think."
    a "She's not one of those atheists who constantly make fun of religion, is she?"
    d level grin "Would I be her friend if she was?"
    a "Yes."
    d_s blank "..."
    d right grin "Yeah, you're right."
    d straight casual "But she's generally pretty accepting about religion."
    d mad blank left "I mean, yeah, we've had our fair share of debates over the subject that turned ugly..."
    d straight casual grin "...but for the most part, we get along just fine, as I'm sure you've noticed."
    a "So what about Brittney? Is she an atheist, too, or...?"
    d blank level "Nah, she's..."
    d right "Ah, what's the word... It also starts with an 'A'... You know, where someone isn't really sure if God is real or not...?"
    a "Agnostic?"
    d straight casual smile "Agnostic! Yes, that's it!"
    d blank "She doesn't seem opposed to coming to church, and she does seem to be curious about my beliefs."
    a "But?"
    d level right "But she likes to work out on Sunday mornings, as she claims they work the best for her."
    a "Kinda sounds like an excuse."
    d straight casual grin "Well, either way, she's not against the idea, so there's always hope."
    a "I guess so."
    h_o "*huff* *huff*"
    show harry p1 straight raised closed_smile at twoleft
    show don at tworight
    with easeinleft
    pause 0.1
    h "I'm back!"
    a "That's a relief; I was starting to miss your whining."
    h mad frown small "Jerk!"
    a "I've been called worse by better."
    h left level blank "Ah, whatever."
    h raised straight grin "Anyway, I'm hungry. Can we go out and eat?"
    a "Why spend money when we have perfectly good leftovers at home?"
    h mad frown "Do you ever think about what you say before you say it?"
    d raised smile "I can't tell if seeing you two interact should make me wish I had a brother or be thankful I'm an only child."
    a "Yes."
    $d_blink = False
    d closed sad grin "Well, anyway, I better get back in and help or else my folks will have my head."
    a "We wouldn't want that, now would we?"
    $d_blink = True
    d straight raised smile "I'll talk to you guys later."
    h casual closed_smile "See ya, Donald!"
    a "Later, Dude!"
    hide don with dissolve
    pause 0.5
    show harry:
        ease 0.5 close_h 
    pause 0.6
    a "We should probably be getting home."
    h mad blank "I still say we should go out to eat."
    a "Leftovers never killed anyone. Now let's go."
    hide harry with dissolve
    pause 0.1
    "With that, we got into the van and drove."
    $ current_track = "None"
    stop music fadeout(3)
    window hide dissolve
    scene bg fade with wipeleft
    pause 1
    scene bg house_s with wipeleft
    window show dissolve
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    "By some miracle, I was able to remember the way home, though that didn't mean I didn't second-guess myself at times."
    "Harry got out of the van and went towards the house.{nw}"
    play loop phone_vibrate_call
    "Harry got out of the van and went towards the house. {fast}I was going to do the same, but my phone started ringing."
    "I looked at the screen and saw that it was Christeena."
    stop loop
    a "Hello?"
    c_o "{font=fonts/LemonMilk.otf}{i}Hey, are you doing anything today?{/i}{/font}"
    a "Not that I'm aware of. Why?"
    c_o "{font=fonts/LemonMilk.otf}{i}Well, you know how Donald's birthday is coming up?{/i}{/font}"
    a "He'd never forgive me if I forgot."
    c_o "{font=fonts/LemonMilk.otf}{i}Hahaha! Well, Brittney and I were going to go out shopping for gifts for him today; you wanna come with?{/i}{/font}"
    a "You? Inviting a boy to go shopping with you?"
    c_o "{font=fonts/LemonMilk.otf}{i}H-Hey, now! Don't get any weird thoughts!{/i}{/font}"
    a "Too late."
    c_o "{font=fonts/LemonMilk.otf}{i}You're an asshole.{/i}{/font}"
    a "And the sun is a star."
    "I could hear a snort of contained laughter escape her."
    c_o "{font=fonts/LemonMilk.otf}{i}Anyway, you wanna come with us or not? Doesn't matter either way.{/i}{/font}"
    "Well, I'll admit that with all that's been happening, I had forgotten that Donald's birthday was coming up. I mean, I remembered the day, but I didn't realize it was that close."
    "Of course, with as often as he loves to brag about sharing a birthday with the entire country, how could ANYONE forget the day?"
    "Still, with the 4th coming quickly, and me realistically forgetting to go gift shopping after today..."
    a "Yeah, I'll go with you guys. When are you leaving?"
    c_o "{font=fonts/LemonMilk.otf}{i}Whenever Brittney's ready, which could be anywhere between 10 minutes and 10 hours.{/i}{/font}"
    a "Hahaha! Alright, I'll be there ASAP; just gotta let my parents know."
    c_o "{font=fonts/LemonMilk.otf}{i}Alrighty! See ya in a bit!{/i}{/font}"
    a "See ya!"
    "We hung up, and I got out of the van."
    "I realized that this was actually the first time that someone other than Donald had asked me to hang out with them."
    "You would think the fact that it was a girl asking would make me feel weird, but honestly, I don't mind it, though it's still a foreign thought to me."
    "I've only known Christeena and Brittney for about a month, which is enough time to get the basics of their personalities, but I can't say I could possibly be at the level where I'd call them my 'best friends' or something."
    "But they are still pretty cool girls, and I don't see any harm in spending time shopping with them, although to an outsider, it may look weird."
    "Anyway, after getting changed into more casual clothes and telling my Mom about the plan, as well as receiving some money from her, I quickly jogged over to Brittney and Christeena's house."
    scene bg porch_ut with dissolve
    pause 0.1
    play sound door_knock
    "After knocking on the door and waiting, the door finally opened up."
    play sound door_open
    pause 1
    $ current_track = "\"Violet Wonder\""
    play music violet_wonder
    show chris p1 straight casual smile at middle with dissolve
    pause 0.1
    c "Hi!"
    a "Yo."
    c mad left blank "Brittney's still getting ready; she claims she's almost done."
    c straight raised "Though she's been claiming that for the past hour."
    a "I'm a patient man."
    c mad "Well, I'm not."
    a "Thanks for clarifying that you're not a man."
    $ c_blush = True
    c p2 left "You know what I meant."
    c "God, if I wanted smartass replies, I'd be up there with Brittney."
    a "Alright, alright, sorry. I guess she's just rubbing off on me."
    $ c_blush = False
    show chris p1 straight casual grin at middle
    c "Anyway, you wanna come in?"
    a "Sure."
    hide chris with dissolve
    pause 0.5
    scene bg living_ut with dissolve
    pause 0.5
    show chris p1 straight mad blank at close_c with dissolve
    pause 0.1
    c "Ugh... Why must my sister be so slow?"
    a "What's the rush? We've got the whole rest of the day."
    c p2 level "I just wanna get as much shopping done as we can before Donald gets home and wonders where we all are..."
    c left dot "We could give every excuse in the book and he'd still piece together what we're doing."
    a "Well, he made it sound like that church potluck was going on all afternoon, so I think we'll be fine."
    c p1 straight casual blank "You know about that?"
    a "Yeah, he told me today when I was at church with him."
    c level dot "You go to church, too?"
    a "I do, indeed. Don and I went together all the time back in Chicago."
    c p2 casual grin "Well, that's cool! It's nice for him to finally have someone here go with him."
    if persistent.choices["11"] == 1:
        jump whydontyou
    elif persistent.choices["11"] == 2:
        jump yesitis
    else:

        menu:
            "..."

            "'Why don't you?'":
                $ persistent.choices["11"] = 1
                jump whydontyou

            "'Yes, it is.'":
                $ persistent.choices["11"] = 2
                jump yesitis

label whydontyou:
    a "Why don't you go? I'm sure he'd appreciate it."
    c level blank "Eh..."
    c p1 left "No offense, but I've never really bought any of that stuff. Doesn't really make a lot of sense to me."
    a "I guess that's fair enough. It doesn't really make complete sense to us, either."
    c straight raised "So then why bother believing it?"
    a "I..."
    "I remembered what Donald said earlier about conversations he's had with her."
    a "You know what? I don't feel like having this debate right now. Maybe another time."
    c p2 left level grin "Alright, then."
    jump britisready

label yesitis:
    a "Yes, it is; he was very happy to see me there today."
    $ c_blush = True
    $ c_blink = False
    c closed_happy sad "Good!"

label britisready:
    "Christeena then looked at her phone screen."
    $ c_blink = True
    $ c_blush = False
    show chris p2 straight mad blank at close_c
    c "Ugh..."
    "She stormed over to the bottom of the staircase and looked up."
    show chris at close_to_right
    pause 0.6
    c scream "BRITTNEY, HURRY UP!!"
    b_o "I'm coming, I'm coming!"
    "As she said this, I could hear footsteps moving towards the top of the stairs."
    c p1 left blank "About damn time..."
    a "Does it really take that long to put on a T-shirt and--"
    a_s "..."
    "I then glanced at the stairs, and I was speechless."
    $ current_track = "None"
    stop music fadeout(2)
    window hide dissolve
    hide chris with dissolve
    pause 0.5
    show brit p1 straight casual grin at middle with dissolve
    pause 1
    window show dissolve
    $ current_track = "\"Different Yet Equal\""
    play music different_yet_equal
    "I'll admit that I didn't recognize her at first."
    "Of course, I'm still not sure if I do recognize her."
    "Undone hair, tight shirt, short shorts..."
    "This is the exact opposite of what I've come to expect from Brittney."
    show chris p1 straight mad blank at twoleft
    show brit at tworight
    with easeinleft
    pause 0.1
    c "Thanks for keeping us waiting, Brit!"
    b blank "Huh? 'Us'?"
    "That's when Brittney actually looked and noticed my presence."
    b hanging "Oh! Alex! What are you doing here?"
    c casual grin "I invited him to go shopping with us."
    b p2 sad opened_smile "Well, that was nice of you."
    b raised grin "But is Alex really okay with shopping with a couple of girls?"
    a_s "..."
    "I was just still in awe at how Brittney looked."
    "The tight clothing gave a better idea of her body shape, while also revealing that she actually does have boobs."
    "Yeah, I know it's stupid to point out, like of course she has them, but her normal choice of loose shirts makes them look nonexistent, while seeing her in this top..."
    b p1 opened_smile "Hellooooo?{w=.5} Earth to dum-dum!"
    "Brittney waved her hand in front of my face, causing me to break out of my spaced-out trance."
    a "H-Huh?"
    b casual "There you are!"
    b p2 raised grin "Oh, and I might not have much to see down there, but that doesn't mean you have my consent to stare at my chest."
    a "Huh? I-I wasn't staring at your chest!"
    c p2 level blank "You kinda were."
    a "Uh..."
    "Well, this awkward situation just got worse."
    a "I was just in shock, I guess."
    b "Oh? Why is that?"
    a "I've just never seen you look... you know..."
    b p1 opened_smile "Like a girl?"
    a "Y-Yeah, I guess."
    $ b_partial = True
    b p2 straight raised huhu "Well, Alexander, believe it or not, I do, in fact, have a vagina, which means if I wanna look like a girl, I'm free to."
    c mad p1 "That could've been worded so much better."
    $ b_partial = False
    show brit p1 straight raised grin at tworight
    b "'Differently'? Yes. 'Better'? No."
    "Well, she may look like a different person, but that's clearly still the brain of Brittney Usher inside that head."
    b p2 casual "Anyway, we ready to go?"
    c p2 "Yeah, FINALLY!"
    b mad blank "Not my fault! It was this damn earring; it wouldn't stay in."
    c hanging "Seriously?? Your hair is covering your ears! We can't even see your earrings!!"
    $ b_partial = True
    b left raised huhu "And we can't see your panties, but I'm willing to bet you're wearing those pink polka-dotted ones that make you feel cute."
    $ c_blush = True
    c_s small sad "...!!!"
    "She looked like she had seen a ghost, but her look of shock and embarrassment soon turned to one of anger."
    c p1 straight mad blank "W-Well, I'll have you know..."
    "She then glared at me with an awkward look before turning back to her sister."
    c "...that I'm NOT wearing those ones."
    $ b_partial = False
    show brit p1 straight raised grin at tworight
    b "Oh, yeah?"
    b opened_smile "Prove it."
    c p2 hanging "NO!!"
    b p2 mad grin "Well, then how else am I supposed to believe you? After all, the only time you're NOT wearing those is when--"
    b small casual hanging "OH!"
    b p1 straight sad blank "S-Sorry. I don't know how I forgot..."
    c_s p1 left blank "..."
    "Feeling like I'm missing an inside joke, as well as not being a fan of the awkwardness, I cleared my throat and changed the topic."
    a "Anyway, where are we shopping at?"
    $ c_blush = False
    show brit p1 straight casual opened_smile at tworight
    show chris p1 straight sad blank at twoleft
    b "There's a mall in the next town over. Not the biggest or most crowded of malls, but it's good for what it is."
    b p2 grin sad "I'm sure there's gotta be something there we can get Donald for his birthday."
    c mad hanging "Not if we don't get going, we can't!"
    b left level huhu "Alright, alright! Calm your tits!"
    scene bg living_ut with dissolve
    pause 0.1
    "Brittney grabbed her keys and we went out to the driveway. We then got into her bright red '95 SUV and went on our way."
    "If she were in her normal getup, seeing her with a vehicle like that would make more sense, but her being dolled up and driving this just looks weird, like a puppy using a litter box."
    play sound truck_start
    scene bg white with dissolve
    pause 0.5
    show cg_01 a_right a_level a_blank b_raised b_right b_grin c_left c_casual c_blank with dissolve
    pause 0.5
    $persistent.cg_1 = True
    b_o "So, what are you guys thinking we should buy?"
    show cg_01 c_level c_right with dissolve
    c_o "I guess that's a good thing to think about, isn't it?"
    b_o "Alex, you've known him the longest; what do you think?"
    a "Hey, you two have known the more recent Donald; I don't know if his opinions on certain things have changed."
    show cg_01 b_casual with dissolve
    b_o "Well, name some of them, and we'll tell you."
    show cg_01 a_raised with dissolve
    a "I mean, I know he still loves classic video games, but I don't know if he's still obsessed with them as he used to be."
    show cg_01 c_up c_casual c_grin with dissolve
    c_o "I wouldn't call him 'obsessed', but a video game in general might be a good idea."
    b_o "Well, there's a video game store in the mall, so we can check there. Anything else?"
    a "Basketball's another one I know he still kinda likes, but he doesn't seem to play it as much as he used to."
    show cg_01 b_level with dissolve
    if B_Basketball:
        b_o "He still plays from time to time, like that day when you first moved here."
    else:
        b_o "He still plays from time to time, like he offered when you first moved here."
    b_o "I guess it wouldn't hurt to check some of the sports stores to see if anything catches our eyes."
    show cg_01 c_left c_sad c_blank with dissolve
    c_o "I mean, I hate to be THAT person, but we could always just get him a gift card."
    show cg_01 b_mad b_blank with dissolve
    b_o "Only as a last resort; he deserves something better and more personal than that."
    show cg_01 c_right c_mad with dissolve
    c_o "It was just a suggestion!"
    show cg_01 a_casual with dissolve
    a "Well, maybe something we wouldn't think of will show up and we'll get that. You never know."
    show cg_01 b_casual b_grin with dissolve
    b_o "Very true!"
    "The conversation died down after that, and Brittney turned on the radio."
    $ current_track = "\"Generic 80s Song\""
    play music generic_80s_song
    pause 1
    show cg_01 b_mad b_opened_smile with dissolve
    b_o "Aw, hell yeah!"
    show cg_01 c_right c_casual with dissolve
    "It was some song from the 80s (or somewhere around there) that I recognized, but didn't really know the lyrics to."
    "Brittney, on the other hand, was a different story."
    "She was jamming along to the words, bobbing her head to the beat, and acting completely oblivious to her passengers, although she was at least paying attention to the road, surprisingly."
    "I grinned and turned to Christeena."
    show cg_01 a_left a_raised a_grin with dissolve
    a "I'm gonna go on a limb and say that she enjoys this song?"
    show cg_01 c_up c_level c_grin with dissolve
    c_o "It's that obvious?"
    b_o "Hush! It's getting to the good part!"
    "As she continued to jam, I just leaned back and chuckled while Christeena rolled her eyes with a small grin."
    $ current_track = "None"
    stop music fadeout(3)
    "Finally, the song ended and the DJ started speaking, which is when Brittney lowered the volume."
    $ current_track = "\"Different Yet Equal\""
    play music different_yet_equal
    show cg_01 a_right with dissolve
    a "You truly are something else."
    show cg_01 b_grin b_raised with dissolve
    b_o "How so?"
    a "For the few weeks that I've known you, you've come off as this tomboy who didn't do anything girly, and here you are today acting like a totally stereotypical teenage girl."
    b_o "Well, could it be because of the fact that I AM a teenage girl?"
    a "Well, you certainly haven't acted like it around me until today."
    show cg_01 b_casual with dissolve
    b_o "What can I say? I like to spice things up from time to time."
    b_o "Some days I wanna dress in a simple T-shirt and blue jeans and feel casual, other days I wanna wear a sundress and feel pretty."
    if britnotpretty:
        show cg_01 b_mad with dissolve
        b_o "I mean, I know YOU don't think I'm pretty, but ya know."
        "I rolled my eyes in annoyance; I just know she's never going to let me forget that I said that."
    a "Well, from one friend to another, I'd say you look really good today."
    show cg_01 b_casual b_opened_smile with dissolve
    b_o "Awww! How sweet of you, Alex!"
    a "In fact, and I don't mean to sound offensive..."
    show cg_01 b_level b_grin with dissolve
    b_o "It's gonna have to be really bad to have even a sliver of a chance of offending me."
    a "Well, anyway, if it weren't for your chipped tooth, I'd go as far as say you look flawless."
    show cg_01 b_mad b_opened_smile with dissolve
    b_o "HA!"
    b_o "Ya hear that, Chris? He just blamed you for me not looking perfect!"
    show cg_01 c_right c_mad with dissolve
    c_o "Oh, shut it."
    show cg_01 a_casual a_blank with dissolve
    a "Wait...{w=.5} You mean CHRISTEENA is the one who chipped your tooth??"
    show cg_01 b_blank b_casual with dissolve
    b_o "You haven't heard this story yet?"
    a "How would I?"
    b_o "I figured you would've asked Don or Chris about it by now."
    a "I figured it would be one of those things you shouldn't ask about someone you hardly knew."
    show cg_01 b_level with dissolve
    b_o "Geez. You're too respectful."
    a "Uh... thanks?{w} Anyway, so what happened with your tooth?"
    show cg_01 b_grin with dissolve
    b_o "Okay, so it was about a year before our parents got married; I was 11 and Chris was 9."
    show cg_01 c_casual with dissolve
    "As Brittney started this story, I could see Christeena looking at her sister with a grin, as if she was looking forward to this."
    b_o "We had this trampoline in the backyard that we liked to play on during the summer; we were just obsessed with this thing!"
    b_o "Well, one day, we were both jumping on it, and we decided to play a game of Popcorn. I was the kernel balled up the middle, and she was the one trying to jump and make me 'pop open'."
    b_o "You would think it would be easier for a girl her size, but she underestimated my grip."
    show cg_01 c_level c_blank with dissolve
    "Christeena's smile faded and was replaced with a more awkward, yet angry look."
    show cg_01 b_casual b_blank with dissolve
    b_o "About 30 seconds had passed before it happened."
    b_o "The timing was just right.{w=.5} I landed on my back, and I could see her falling towards me."
    b_o "Before I could react or try to move..."
    show cg_01 b_mad
    b_o "{b}BAM!!!{/b}{fast}"
    b_o "Kneecap straight to the kisser!"
    show cg_01 c_up c_casual with dissolve
    c_o "I just want to clarify that it was completely and totally an accident!"
    b_o "That doesn't change the fact you technically won as I let go of my grip to grab onto my bleeding mouth!"
    show cg_01 a_level with dissolve
    a "Oh, geez...!"
    show cg_01 c_sad with dissolve
    c_o "Yeah, it was not a pretty sight."
    show cg_01 b_level with dissolve
    b_o "It wasn't a pretty feeling, either."
    b_o "Christeena called for our parents like I was dead, us both crying for different reasons, and I was rushed to the ER."
    b_o "At the end of the day, it was just a cut lip and the chipped tooth. I guess it could've been a lot worse."
    a "Didn't your parents try to get it fixed?"
    show cg_01 b_grin with dissolve
    b_o "Yep. And they even want it fixed to this day."
    a "So why not fix it?"
    b_o "Why would I? It's basically a scar, but cooler."
    show cg_01 a_raised with dissolve
    a "I don't think I see why that's a good thing."
    show cg_01 c_level with dissolve
    c_o "Brittney has this unhealthy obsession with scars."
    show cg_01 b_mad b_blank with dissolve
    b_o "Well, you make it sound like I try to give myself scars or something!"
    show cg_01 b_grin b_casual with dissolve
    b_o "I'm just fascinated by them because there's a story behind every one. Sure, they're not always good stories, but it's a story nonetheless, and it's a part of your past."
    b_o "Take my tooth, for example. If I had it fixed, what are the realistic odds that you'd ever learn about the time Christeena kneed me on a trampoline?"
    b_o "The only reason we even casually mention that day is because of that tooth. And now it's become something we both look back and laugh at."
    show cg_01 a_level with dissolve
    a "I guess I see where you're coming from."
    a "So, does that mean you have other scars, then?"
    b_o "Oh, with the life I've lived? Absolutely! You can see a few of them on my arms and legs, but I've got them everywhere."
    b_o "Hell, I've even got one right on my asscheek if you're interested in seeing that one."
    show cg_01 c_right c_mad with dissolve
    c_o "Brittney Anne, don't you fucking dare!"
    show cg_01 b_mad b_blank with dissolve
    b_o "Geez, I wasn't actually going to show him, Mother!"
    c_o "I can never tell with you..."
    show cg_01 a_raised with dissolve
    a "Wait, so how the heck did you even get a scar there?"
    show cg_01 b_raised b_opened_smile with dissolve
    b_o "Oh, as much as I'd love to share that story right now, we better focus back on getting gifts for Donald; we're here!"
    window hide dissolve
    scene bg mall_e with dissolve
    pause 1
    window show dissolve
    a "THIS is the mall?"
    show brit p2 straight raised grin at twoleft
    show chris p1 straight casual blank at tworight
    with dissolve
    pause 0.1
    b "Hey, it may not be the super-expensive skyscraper malls with a thousand stores inside that you're used to up north, but it's still a mall."
    c p2 smile "I like the simplicity of it; you don't feel lost or confused."
    b p1 casual "Plus, there are still a decent amount of stores inside."
    b p2 opened_smile "C'mon! We'll show ya!"
    scene bg mall_e with dissolve
    pause 0.5
    scene bg mall_i with dissolve
    pause 0.1
    $ current_track = "\"The Mall\""
    play music the_mall
    play loop mall
    pause 0.5
    "Well, call it being used to greater things, but the interior was about as underwhelming as the exterior."
    "The aesthetic was pretty decent, I suppose; the ceiling being one giant skylight certainly gave a nice atmosphere."
    show brit p1 straight casual grin at twoleft
    show chris p2 straight dot casual at tworight
    with dissolve
    pause 0.1
    b "So, where should we head first?"
    c p1 grin "Well, we decided between the game store and the sports store for sure, and they are pretty close to each other."
    b p2 raised opened_smile "It might be a bit easier to split up, then."
    c raised blank "How do you figure?"
    b level huhu right "What do YOU know about basketball?{w=.75} Or sports in general?"
    c level left "Uh..."
    b p1 mad grin straight "That's what I thought, just like how I know jack-diddly-squat about video games."
    c p2 casual grin straight "Well, when you put it that way, I guess you have a point."
    c level blank "But, wait; what about Alex?"
    b p1 casual "I guess that's up to him."
    "Honestly, I'm sure Donald would be happy with either one, but--"
    "I lost my train of thought when I saw an art supply store nearby."
    a "Does Donald still like to draw or do any sort of art?"
    b p2 blank "{i}'Still'{/i}? You mean he used to draw?"
    c left p1 dot "That's news to me, too."
    "I suppose that answers that."
    "I remember Donald drawing when we were younger; he was good, too.{w} Maybe he just does it on the side or is just hiding it from them for some reason."
    "I guess it wouldn't hurt to look, but maybe it might be better to go between things we know for sure he likes."
    b p1 raised grin "Anyway, I'm headed to the sports store, and Chris is headed to the game store. Al, where are you headed?"
    show chris straight casual blank
    if persistent.choices["12"] == 1:
        jump sportsstore
    elif persistent.choices["12"] == 2:
        jump vgstore
    elif persistent.choices["12"] == 3:
        jump artstore
    else:
        "Well, I better decide where I'm going shopping."
        menu:
            "Where should I go?"

            "Sports Store":
                $ persistent.choices["12"] = 1
                jump sportsstore

            "Video Game Store":
                $ persistent.choices["12"] = 2
                jump vgstore

            "Art Store":
                $ persistent.choices["12"] = 3
                jump artstore

label sportsstore:
    $ B_Points += 1
    a "I guess I'll go with you to the sports store."
    b p2 casual opened_smile "Cool beans!"
    b grin "And when we're each done, whaddaya say we meet in the food court for some lunch?"
    c p1 smile "Okay!"
    a "Sounds good."
    b p1 raised "You know, I must say I'm glad you decided to go with me, Mr. Sprouse."
    a "Why's that?"
    b closed_smile "I was thinking of stopping at Violet's Secret if we had time, and I could use a man's opinion on what looks sexy."
    c p2 mad blank "Like Hell you are!"
    b p2 right mad blank "Damn, you don't know a joke when you hear it, do you?"
    b "And even if I was serious, what would it matter to you, anyway?"
    c p1 hanging "Well, maybe if you weren't constantly acting like such a slu--"
    c blank right "Nevermind."
    b p1 straight hanging "No, go ahead! Say it!"
    $ c_blush = True
    c straight "I said nevermind!"
    hide chris with easeoutright
    pause 0.1
    $ c_blush = False
    "And with that, Christeena stormed off towards the game store, leaving Brittney and I standing there awkwardly."
    show brit at middle with easeinleft
    pause 0.1
    $b_blink = False
    b blank closed_sad sad p2 "*sigh*"
    a "Is everything okay between you two...?"
    $b_blink = True
    b straight p1 "Yeah, it's fine, I promise."
    b p2 grin "We're sisters. These things happen. You get it, right?"
    a_s "..."
    b left "A-Anyway, let's start shopping then, shall we?"
    a "Sure."
    hide brit with dissolve
    pause 0.1
    "The awkwardness still in the air, Brittney and I walked over to the sports store."
    pause 0.5
    $ current_track = "\"Oddball\""
    play music oddball
    scene bg sports with dissolve
    pause 0.5
    show brit p1 straight casual opened_smile at close_b with dissolve
    pause 0.1
    b "Ah, here's a sight I always love to see!"
    "Sports merchandise and equipment could be seen all over the place, which, yes, was to be expected, but there was certainly a lot of variety."
    "Baseball, basketball, football, soccer, hockey, and the list goes on."
    b p2 sad grin "It's just so beautiful..."
    a "You know, hearing you say that while you're dressed like a sports-hating teenage girl just hurts my brain."
    $ b_partial = True
    b level huhu "Good."
    $ b_partial = False
    show brit p1 straight raised grin
    b "So, let's look around and see if anything catches our eye."
    a "Should we start somewhere specific, or...?"
    b p2 casual "Eh. I like to just circle around the place and look at everything."
    b raised "But you can do what you want, I suppose. Whatever works for you."
    a "In that case, I think I'll start at the basketball stuff, since I know he likes that one the most."
    b p1 casual opened_smile "Coo'."
    hide brit with dissolve
    pause 0.1
    "With that, she walked over to the outer wall and started making her away around, looking at everything with a giant grin."
    "As she was walking away from me, my heart almost skipped a beat as I looked at her from behind."
    "With her tight short shorts, her butt looked just a bit bigger than normal.{w} Or has it always been that big...?"
    "Feeling my face start to heat up, I turned away and walked to the basketball section."
    window hide dissolve
    scene bg fade with wipeleft
    pause 0.5
    scene bg sports with wipeleft
    window show dissolve
    pause 0.1
    "After a few minutes of looking around, Brittney walked towards me."
    show brit p1 straight casual grin at close_b with easeinleft
    pause 0.1
    b "Any luck?"
    a "Well, I've been looking at these jerseys, but I don't really know what teams he likes."
    b raised p2 "The Bulls."
    "Wow. No hesitation."
    a "I mean, I guess I should've figured, but I didn't know if he still enjoyed them as much as he did."
    b p1 casual opened_smile "He always roots for the Chicago teams, even the ones that suck balls."
    b p2 level huhu left "Which, let's be honest, are basically all of them."
    b raised straight opened_smile "ESPECIALLY those Cubs."
    a "Eh. There's something to be said about having pride in your hometown."
    b p1 sad grin "Oh, I get his logic. I do."
    $ b_partial = True
    b level huhu "But that doesn't mean I'm ever going to stop making fun of him for hoping crappy teams will win."
    $ b_partial = False
    show brit p2 straight raised opened_smile
    b "I keep telling him he's setting himself up for disappointment each time, but oh well."
    b mad grin "Hell, we even made a deal that if the Cubs win the World Series within our lifetime, I'll suck his dick."
    a "Wow. {w=.25}That's, uh...{w=.25} pretty confident of you."
    $b_blink = False
    b closed sad closed_smile p1 "Well, I always make bets I know I'll win."
    a "So, what about you? Any luck finding something?"
    $b_blink = True
    b p2 straight casual blank "Maybe."
    b left level "I remember him mentioning that he had lost his baseball glove, and that that was his excuse for never playing catch with me."
    a "Playing catch? How old are you again?"
    b p1 straight mad frown "Hey! There's nothing wrong with or childish about it!"
    b p2 blank "I need to make sure I'm always keeping my aim and throws in peak condition, so unless you know a better solution...!"
    a "Sorry, sorry. I guess the way it was worded just threw me off."
    b left level "Hm..."
    b p1 straight raised opened_smile "Okay, I'll let you off the hook this time."
    b casual "Anyway, back to my point: I'm thinking about buying him a new glove."
    a "So you're basically buying him a new glove simply for your benefit?"
    b p2 sad blank "Well, when you say it like that, it makes it look selfish."
    a "That's because it IS selfish."
    b left level huhu "I know."
    b p1 straight casual opened_smile "But I know he'd really enjoy it."
    b p2 raised grin "After all, he'd give up his nuts if it meant he could spend time with me."
    a "Well, I suppose that's true. But doesn't that still seem kinda wrong?"
    b casual blank "How?"
    a "You're basically taking advantage of his crush on you."
    b mad p1 hanging "Well, NOW you're making me sound like a cruel, friendzoning bitch."
    b raised blank right "I may not like him the same way he likes me..."
    b straight "...but that doesn't mean I hate his company. He's still my friend, even if he wishes we were more."
    a "Doesn't that ever get annoying, though? Him constantly wanting to be more?"
    b p2 casual "Eh. At times."
    $ b_partial = True
    b grin "But that's what these are for."
    "She then held up her fists."
    $ b_partial = False
    show brit p1 casual straight grin
    b "Besides, it's clear he really enjoys spending time as just friends, as well, so it's not like he's just hanging out with me simply because he wants to date me."
    b blank "I've made it clear to him in many ways that it'll never happen, so if he refuses to accept it, that's on him, not me."
    a "So nothing he could do would ever make you consider being his girlfriend?"
    b p2 sad grin "If there were something, he would've tried it by now, and it would've worked."
    b right "As horrible as it sounds, there's nothing that could ever make me fall in love with Donald."
    a_s "..."
    b straight casual blank "What?"
    a "What?"
    b level "You looked at me like I was wrong or something..."
    a "I don't know what you're talking about."
    b_s left "..."
    a "So, are you gonna get him the glove, then?"
    b p1 straight casual grin "Might as well. You getting him a jersey?"
    a "Might as well."
    hide brit with dissolve
    pause 0.1
    "We bought our gifts and exited the store."
    pause 0.5
    scene bg mall_i with dissolve
    pause 0.5
    show brit p2 straight casual blank at close_b with dissolve
    pause 0.1
    a "Off to the food court, then?"
    b p1 grin "Yep. I texted Christeena and let her know we're on our way."
    $ current_track = "None"
    stop music fadeout(2)
    show brit:
        ease 0.5 middle
    b opened_smile "C'mon! I'll race you there!"
    a "I don't even know where I'm going."
    $ b_blink = False
    b closed sad closed_smile "Exactly!"
    $ current_track = "\"Friendly Competition\""
    play music friendly_competition
    hide brit with easeoutright
    pause 0.1
    $ b_blink = True
    a "H-Hey!!"
    "And just like that, she started sprinting away."
    "After a few seconds, she slowed down to a steady jog, but was still a fair distance away from me."
    if persistent.choices["14"] == 1:
        jump raceher
    elif persistent.choices["14"] == 2:
        jump dontraceher
    else:
        menu:
            "What should I do?{fast}"

            "Race her":
                $ persistent.choices["14"] = 1
                jump raceher

            "Don't race her":
                $ persistent.choices["14"] = 2
                jump dontraceher

    label raceher:
        $ B_Points += 1
        "You know what? Screw it. Let's play along."
        window hide dissolve
        nvl clear
        nvl show dissolve
        narrate """
        I picked up my speed, keeping her in my sight and avoiding the other people around me.

        I wasn't breaking into a sprint like she did, but it was still a steady pace.

        After a few seconds, she looked behind her to see where I was. She honestly looked surprised to see me chasing after her, but she still had that competitive look in her eye.

        Upon seeing me, she turned back around and picked up her pace, leading me to do the same.

        After a quick turn to the left, I lost sight of her for a few seconds, but once I rounded the corner, I caught sight of her again, though she still had a large distance ahead of me.

        {clear}

        I knew I couldn't catch up to her at this point, but I was still jogging after her, despite the weird looks I was getting from the people nearby.

        Thankfully, I didn't lose sight of her, so it didn't take me long to find my way to the food court via her direction.
        """
        jump britfoodcourt

    label dontraceher:
        "Yeah, no thanks. Not only is that really childish, but I'm pretty sure we could get in trouble for running through the mall like that."
        "Still, I kinda need to know where the food court is..."
        window hide dissolve
        nvl clear
        nvl show dissolve
        narrate """
        I saw a mall map nearby, so I walked over to there.

        After looking at the map for a few seconds, I found that the food court was in the middle of the mall, and that I was already pretty close to it.

        With that, I walked towards the food court, still hearing Brittney's running in the distance. I wonder if she's noticed that I'm not running behind her.

        Finally, I made it to the food court a few minutes later, where I saw Brittney leaning against a table. She looked over at me when she saw me.
        """

    label britfoodcourt:
        $ current_track = "None"
        stop music fadeout(3)
        nvl clear
        nvl hide dissolve
        pause 0.25
        scene bg mall_fc with dissolve
        pause 0.1
        window show dissolve
        pause 0.25
        show brit p2 straight raised opened_smile at middle with dissolve
        pause 0.1
        b "*huff*{w=.25} I{w=.2} *huff*{w=.2} win!"
        a "For an athlete, you certainly seem out of breath."
        b p1 grin "We're {w=.2}*huff*{w=.2} human, too, {w=.2}*huff*{w=.2} you know!"
        b "Whoo! I need a drink!"
        hide brit with dissolve
        pause 0.1
        $ current_track = "\"The Mall\""
        play music the_mall
        "She walked over to a nearby water fountain and got a drink. As she did, I sat down at a nearby table and waited."
        "By the time Brittney got back, Christeena had made it to the food court, herself, and walked next to us."
        show brit p1 straight casual grin at twoleft with dissolve
        pause 0.1
        show chris p1 straight casual grin at tworight with easeinright
        pause 0.1
        c smile "Hey, guys!"
        b p2 raised "Yo."
        c p2 grin "What did you guys get him?"
        a "I got him a Bulls jersey, and Brittney got him a baseball glove."
        c raised blank "A baseball glove?{w=.5}{nw}"
        c mad p1 "A baseball glove?{fast} You didn't get him that so you could have someone to practice throwing with, did you?"
        b p1 casual blank "Was it that obvious?"
        c left "Ugh..."
        a "Hey, I'm sure Donald will still enjoy it."
        c raised straight "We'll see, I suppose..."
        b p2 grin "What about you? What did you get him?"
        $ c_blush = True
        c p2 right level "I...{w=.25} I honestly didn't know what to get him, so I just got him a $50 Vapor gift card."
        $ b_partial = True
        b level blank "A gift card? Really?"
        c straight mad hanging "Hey, it's better than getting him nothing!!"
        a "Girls, girls! Settle down!{w=.5} What's important is that we each got him a gift that I'm sure he'll enjoy."
        a "Now, come on. Let's eat some lunch."
        $ b_partial = False
        show brit p1 straight casual grin at twoleft
        b "Well, how can I say no to that offer?"
        jump eatatfc

label vgstore:
    $ C_Points += 1
    a "I guess I'll head to the game store with Christeena and see what we can find."
    b p2 casual opened_smile "Sounds like a plan!"
    b grin "And when we're each done, whaddaya say we meet in the food court for some lunch?"
    a "Where is that, exactly?"
    c grin "Don't worry; I'll show you when we're done."
    b p1 opened_smile "Well, then I'm off."
    b right level huhu "Enjoy your alone time, you two. Try not to make out for too long~"
    $ c_blush = True
    c p2 mad hanging "Brittney!!"
    $ b_blink = False
    b p2 closed sad closed_smile "Hehehe!"
    hide brit with easeoutleft
    pause 0.5
    $b_blink = True
    show chris at middle with easeinright
    pause 0.1
    $ c_blush = False
    show chris p1 left mad blank at middle
    c "Ugh... that girl..."
    a "You shouldn't let things like that bother you so much; as an older sibling, myself, I know she's only doing it because it riles you up."
    c straight raised "Yeah, I know, but it's still unnecessary for her to say."
    c "She's always just saying things that don't need to be said, especially in front of other people."
    $ c_blush = True
    c level right p2 "Like that comment earlier... about my underwear..."
    a "It's just underwear. Everyone wears it."
    c_s "..."
    a "Christeena, it's only a big deal if you make it a big deal."
    c straight sad "If you say so..."
    c p1 right "A-Anyway, let's get to the store."
    a "Lead the way."
    pause 0.1
    hide chris with dissolve
    pause 0.5
    scene bg games with dissolve
    pause 0.5
    show chris p1 straight casual grin at close_c with dissolve
    pause 0.1
    $ current_track = "\"Violet Wonder\""
    play music violet_wonder
    $ c_blush = False
    c "Here we are!"
    "I let out a surprised whistle as I glanced around the store."
    "It was a used game store, which means they're cheaper than buying them new, so there's already that advantage."
    "That said, a lot of them seemed to be missing their covers, but Donald isn't really the kind of guy to get upset at that, as long as the disk works."
    a "So, where should we start looking?"
    c p2 raised "Well, Donald's modern console of choice is the 360, so let's check there."
    a "Alrighty, then!"
    hide chris with dissolve
    pause 0.1
    "We looked over the games in the selection. They were all alphabetized, so finding a specific game we had in mind wouldn't be an issue."
    "That said, it would help if we had a game in mind."
    show chris straight casual blank p1 at close_right_c with dissolve
    pause 0.1
    a "What kind of games does Donald play that he wouldn't already have?"
    c left level dot "Hm..."
    c p2 "He likes playing puzzle games, but the only ones for console that I can think of are {i}Wormhole 2{/i} and {i}Crops vs. Zombies{/i}, both of which he bought and played countless times by now."
    a "I mean, I don't blame him; those games are masterpieces."
    c p1 straight casual blank "I wouldn't know, to be honest."
    a "You're dead to me."
    $ c_blush = True
    c mad hanging "!!"
    a "I'm kidding!"
    $ c_blush = False
    show chris p2 straight mad grin at close_right_c
    c "I know, but it's still mean."
    a "Not my fault you call yourself a gamer and then not play the best games ever made."
    c raised p1 "First of all, that's completely opinionated."
    c "Second, puzzle games aren't my thing; I'm more of an online shooter player."
    "If I had a drink in my mouth, it would've been spat out."
    a "You?{w=.75} A girl?{w=.75} Playing online shooters?"
    c p2 level "It's not that uncommon, you know."
    a "It's not that common, either."
    $c_blink = False
    c closed_happy sad smile "It just seems that way because we don't use our mics or tell people we're girls."
    $c_blink = True
    c straight raised grin "If we did, all the little horndog nine-year-olds wouldn't leave us alone."
    a "Fair enough.{w} Hey, maybe we could play together some time."
    $ choice_xalign = 0.3
    $ choicevbox = 4
    c p1 smile "Maybe, if you're prepared to be dominated."
    if persistent.choices["13"] == 1:
        jump isthatachallenge
    elif persistent.choices["13"] ==2:
        jump becauseidletyou
    elif persistent.choices["13"] == 3:
        jump stilltalkingaboutgames
    else:
        menu:
            c "Maybe, if you're prepared to be dominated.{fast}"

            "'Is that a challenge?'":
                $ persistent.choices["13"] = 1
                jump isthatachallenge

            "'Only because I\'d let you win.'":
                $ persistent.choices["13"] = 2
                jump becauseidletyou

            "'We\'re still talking about video games, right?'":
                $ persistent.choices["13"] = 3
                jump stilltalkingaboutgames

    label isthatachallenge:
        a "Is that a challenge?"
        c grin p2 "I don't know; is it?"
        if cleaningpartner == "Christeena":
            "The fiery passion in her eyes is intriguing; the last time I saw it was when we were talking about books in my room."
        else:
            "The fiery passion in her eyes is intriguing."
        a "Well, if it is, then challenge accepted! Name a game and a time!"
        c smile p1 "I'll think about both of those things, I assure you."
        c p2 casual grin "For now, let's focus back on Donald."
        a "Alright."
        hide chris with dissolve
        pause 0.1
        jump pickagame

    label becauseidletyou:
        a "Yeah, only because I'd let you win."
        c p2 grin "Oh, REALLY?"
        a "Yes, really; everyone knows girls only win because the guys go easy on them."
        c "Well, we shall see, Alex. We shall see."
        c p1 casual grin "Anyway, what do you say we get back to focusing on a game for Donald?"
        a "Yeah, that sounds like a good idea."
        hide chris with dissolve
        pause 0.1
        jump pickagame

    label stilltalkingaboutgames:
        $ C_Points -= 1
        a "We're still talking about video games, right?"
        c_s blank "...?"
        $ c_blush = False
        c small sad hanging "OH!"
        c straight mad blank "Y-Yes, we're still talking about video games, you pervert!"
        c left p2 "Can't I have just one fucking conversation without someone cracking a dirty joke or some shit like that??"
        a "...I'm sorry."
        c "Whatever. Let's just get a game for Donald."
        a "Alright, then..."
        hide chris with dissolve
        pause 0.1

    label pickagame:
        $ choice_xalign = 0.5
        $ choicevbox = 1
        $ c_blush = False
        "We looked back at the game selections."
        "Donald's love of puzzle games did seem to limit our console selection..."
        show chris p1 straight sad blank at close_right_c with dissolve
        pause 0.1
        c "I think I may have to get him a Vapor gift card so he can buy whatever game he wants..."
        c p2 right "I mean, I really, REALLY hate to do that, but I'm at a loss on what to do."
        a "Well, maybe we're thinking too modern."
        c straight casual "Huh?"
        a "Do they have a section for older games from older systems?"
        c left level dot "I believe so... I think it's towards the back."
        a "Let's check it out; we may find something there."
        c p1 straight raised blank "Do you really think he'd be happy with getting an older game?"
        a "If you really have to ask that, you don't know Donald as well as you think."
        c level "I suppose that's possible; I can't really say I know a whole lot to begin with."
        a "What do you mean? You've known him for years and you're always together."
        c p2 raised "And have you noticed that most of time we're together, Brittney is there, too?"
        a_s "..."
        a "...{fast}huh. I guess you're right."
        c level "If I'm being completely honest, Donald and I are less of 'friends' and more of 'friends of a friend'."
        c p1 left "I mean, yeah, we get along for the most part when we're together, but we hardly hang out on our own."
        c straight mad "I mean, the only reason he brought me to your house on Friday was so I could help you unpack."
        c p2 level "We're just so different, you know? Even more than Brittney and I."
        a "Sure, I get it. He even mentioned to me today how you two have had your share of debates and arguments over certain topics."
        $ c_blush = True
        c p1 right sad "Yeah..."
        a "But, hey, if you can still be around each other without trouble, that's something, right?"
        $ c_blush = False
        show chris p1 straight sad blank at close_right_c
        c "I suppose so."
        c grin "He's a sweet guy, and I know he means well."
        c p2 left "Honestly, a part of me wishes Brittney would come to her senses and go out with him."
        c straight raised blank "But me and her have seen firsthand what happens when you force relationships."
        a "Oh, really?"
        c p2 mad "Yeah, and I'm not going to elaborate, so let's get back to focusing on why we're here."
        a "If you insist."
        hide chris with dissolve
        pause 0.1
        "{i}'Seen firsthand'{/i}, huh?"
        "As curious as I am, if she really doesn't want to talk about it, then who am I to force it out of her?"
        "Maybe I can get Brittney to spill the beans if I wanted to."
        "We then went to the back of the store and found the older games. PA2, GamePrism, PA1, and on and on."
        show chris p2 straight casual blank at close_c with dissolve
        pause 0.1
        c "Is there any game in particular you're thinking of?"
        a "Kinda... When we were younger, he would always talk about how he wanted to play {i}Clunker's Bad Day{/i}, but his parents wouldn't let him."
        c p1 raised "Isn't that that game that looks like a kid's game but is actually full of sex jokes and stuff?"
        a "That would be the one. I didn't see it at his house, so it's safe to say he still may not have it."
        a "If I'm lucky, this place might just--{w=.2}"
        c p2 smile casual "Is that it?"
        "I looked where she was pointing. It was a collection of games for the 64. Right smack in the middle of them was..."
        a "Yes! That's it!"
        "I grabbed it from the shelf and looked it over."
        "It was just the cartridge, but the label was still on and it seemed to be in good shape."
        a "So, that's that. What about you?"
        c p1 left raised blank "Well, I'm still not sure how he'll feel about getting an older game, so I think I'll just have to go with the card."
        c straight sad "Do you think $50 will be enough?"
        a "I'd say so."
        hide chris with dissolve
        pause 0.1
        "We then paid for our gifts and exited the game store."
        scene bg mall_i with dissolve
        pause 0.1
        show chris p1 straight casual blank at close_c with dissolve
        pause 0.1
        a "So, where's this food court we're supposed to meet up at?"
        c p2 grin "It's towards the middle of the mall. I'll text Brit and let her know we're on our way there."
        a "Sounds good."
        $ current_track = "None"
        stop music fadeout(1)
        hide chris with dissolve
        pause 0.5
        scene bg mall_fc with dissolve
        pause 0.5
        show chris p1 straight casual grin at close_c with dissolve
        $ current_track = "\"The Mall\""
        play music the_mall
        c "Brittney said she's already here waiting."
        a "Where at?"
        a "Oh, nevermind; I see her."
        "Sitting at a table by the Chinese restaurant was a tall, thin blonde waving her hand at us. Waving back, we both walked over and sat down."
        show chris:
            ease 0.5 tworight
        show brit p2 straight casual grin at twoleft with easeinleft
        pause 0.1
        a "Did you find anything good?"
        b p1 sad opened_smile "I hope so; Donald's been mentioning how he's lost his baseball glove, so I bought him a new one."
        c mad blank "Are you sure this isn't so you have an excuse to get him to go outside and play catch with you?"
        b mad hanging "What? No!"
        b p2 left level huhu "That wasn't my ONLY reason..."
        b p1 straight casual grin "Anyway, did you guys find anything?"
        c smile casual "Well, Alex got him an older game Donald always wanted to play, and I got him a Vapor card."
        $ b_partial = True
        b p2 level blank "A gift card? Really?"
        c p2 mad hanging "Hey, it was more difficult than we thought, okay?"
        a "Alright, alright, let's settle down here and get some food. Sound good?"
        $ b_partial = False
        b p1 straight casual grin "Sounds excellent! I was about to wither to nothing over here waiting for you slowpokes!"
        jump eatatfc

label artstore:
    a "I think I'll take a look at this art store over here for the heck of it."
    b p2 casual blank "You sure you'll find something Donald would like?"
    a "I won't know unless I try."
    b level grin "Alright, then; if that's what you want to do, go for it."
    b p1 casual "And once we're each done, whaddaya say we meet up in the food court for some lunch?"
    a "Where is that, exactly?"
    c p2 grin "It's towards the middle of the mall; you can't miss it."
    b raised p2 "Oh, you'd be surprised; blondes certainly have a way of raising the stupidity limits."
    c_s raised blank "..."
    a_s "..."
    a "...{fast}you do realize--"
    b opened_smile "Never said I was an exception. If anything, I'm proof."
    c_s level "..."
    b p1 casual "Well, I'm off. TTYL!"
    hide brit with easeoutleft
    pause 0.5
    show chris at middle with easeinright
    pause 0.1
    a "Well, that might be the first time I've seen someone simultaneously insult someone else AND themselves."
    c p1 left "Yeah..."
    a "Everything good?"
    c straight grin "Peachy."
    c casual "Well, I hope you find a gift for Donald."
    a "You, too."
    pause 0.1
    hide chris with easeoutright
    pause 0.5
    "With that, I walked over to the art store alone."
    pause 0.5
    scene bg art with dissolve
    pause 0.5
    "I must say, I was impressed with the looks of this place."
    "It seemed more catered to traditional 2D art, like drawing and painting, which is exactly what I was looking for."
    "I suppose I don't need anything super fancy, especially since I'm not fully sure how well Donald still enjoys drawing, and I can't exactly just ask without sounding suspicious."
    "I'll just get him a simple sketchbook and pencils, maybe some colored ones, as well. After all, it's the thought that counts, right?"
    $ current_track = "None"
    stop music fadeout(3)
    "I walked over to the sketchbook section, but as I did, I stopped dead in my tracks; someone else was there, too. Someone familiar."
    pause 0.1
    show elie p1 left casual blank at middle with dissolve
    pause 0.5
    $ current_track = "\"Chaotic Evil\""
    play music chaotic_evil
    "Eleanor."
    "She didn't seem to notice me; she was looking at the books, seeming to find a specific one."
    "Thankfully, she was at the far end of the aisle, so I just stayed towards the end I was already at."
    hide elie with dissolve
    pause 0.1
    "I looked at the sketchbooks in front of me. They all seemed a little too big; I want one a little smaller, about the size of a normal school notebook."
    "Those ones, however, were more towards the middle."
    "Being careful not to look suspicious or nervous, I moved to the middle of the aisle and looked at the selection. These are more the style I'm looking for."
    "Grabbing one of the sketchbooks, I saw movement from my peripheral vision."
    pause 0.1
    show elie p1 straight casual blank at close_e with dissolve
    pause 0.1
    "Eleanor was coming this way."
    "She still wasn't looking at me, but she honestly didn't look very threatening. In fact, she kinda looked...{w} normal."
    "Well, as normal as a held-back high school student with tattoos and revealing clothing can get."
    "She seems to be in a good mood, which from what the guys have told me, is as rare as winning the lottery."
    "We haven't really been properly introduced to each other... Does she even know that I'm her neighbor?"
    "I wonder if I should try talking to her..."
    if persistent.choices["15"] == 1:
        jump talktoher
    elif persistent.choices["15"] == 2:
        jump donttalktoher
    else:

        menu:
            "Talk to her":
                $ persistent.choices["15"] = 1
                jump talktoher

            "Don't talk to her":
                $ persistent.choices["15"] = 2
                jump donttalktoher

    label talktoher:
        "You know what? What's the worst that could happen?"
        a "Excuse me."
        show elie neutral frown
        "She stopped in her tracks and turned to me, her attitude quickly becoming more sour."
        e raised "Yes?"
        "Wow. The amount of attitude in that one word was unimaginable."
        "Maybe this was a mistake..."
        if persistent.choices["16"] == 1:
            jump nevermind_e
        elif persistent.choices["16"] == 2:
            jump introduceyourself
        else:

            menu:
                "'Nevermind'":
                    $ persistent.choices["16"] = 1
                    jump nevermind_e

                "'Hi, I'm Alex, your neighbor.'":
                    $ persistent.choices["16"] = 2
                    jump introduceyourself

        label nevermind_e:
            a "N-Nevermind."
            e_s level "..."
            jump wasteoftime

        label introduceyourself:
            $ E_Points += 1
            "No; I can get through this."
            a "H-Hi. I'm Alex, your neighbor."
            e level blank "Okay...?"
            a_s "..."
            e_s "..."
            a "I, uh... just wanted to introduce myself properly."
            e raised "Well, you did it. You done?"
            a "Y-Yeah. I'm done."
            e mad "Good."

    label wasteoftime:
        $ current_track = "None"
        stop music fadeout(5)
        pause 0.1
        hide elie with dissolve
        pause 0.1
        "Eleanor walked away with an annoyed look while slowly shaking her head."
        "Well, that was certainly a waste of both of our times."
        jump checkoutart

    label donttalktoher:
        "Eh. Better not risk it."
        $ current_track = "None"
        stop music fadeout(5)
        pause 0.1
        hide elie with dissolve
        pause 0.1
        "Eleanor walked past me, seeming to not know I was even there."
        "I'll consider that a blessing."

    label checkoutart:
        $ current_track = "\"The Mall\""
        play music the_mall
        "After grabbing some pencils, both graphite and colored, I bought everything and exited."
        pause 0.5
        scene bg mall_i with dissolve
        pause 0.5
        "Once I left the store, I shot both girls a text in a group chat between the 3 of us."
        nvl clear
        window hide dissolve
        nvl show dissolve
        a_nvl "{font=fonts/LemonMilk.otf}{i}Hey, I'm done shopping.{/i}{/font}"
        b_nvl "{font=fonts/LemonMilk.otf}{i}Already?{/i}{/font}"
        c_nvl "{font=fonts/LemonMilk.otf}{i}That was fast...{/i}{/font}"
        a_nvl "{font=fonts/LemonMilk.otf}{i}I had a fair idea of what I wanted to get. I just hope he likes it.{/i}{/font}"
        b_nvl "{font=fonts/LemonMilk.otf}{i}I'm sure he will.{/i}{/font}"
        b_nvl "{font=fonts/LemonMilk.otf}{i}At least, he'll PRETEND to like it lol XD{/i}{/font}"
        a_nvl "{font=fonts/LemonMilk.otf}{i}I'm on my way to the food court. Should I wait for you guys?{/i}{/font}"
        b_nvl "{font=fonts/LemonMilk.otf}{i}I won't be upset if you start eating without me.{/i}{/font}"
        c_nvl "{font=fonts/LemonMilk.otf}{i}I think I'm almost done, anyway, so I should be there soon, if you wanna wait.{/i}{/font}"
        a_nvl "{font=fonts/LemonMilk.otf}{i}Alright.{/i}{/font}"
        nvl clear
        nvl hide dissolve
        window show dissolve
        pause 0.1
        "With that, I was on my way to the food court."
        pause 0.5
        scene bg mall_fc with dissolve
        pause 0.5
        "After finding it by walking towards the middle of the mall (while also checking a map, just to be safe), I sat down at one of the tables."
        "I wasn't super hungry at the moment, so I saw no harm in waiting for the girls."
        window hide dissolve
        scene fade with wipeleft
        pause 0.5
        scene bg mall_fc with wipeleft
        window show dissolve
        pause 0.1
        "A good 10 minutes had passed before I saw a familiar face come my way."
        pause 0.1
        show chris p2 straight casual grin at close_c with dissolve
        pause 0.1
        c smile p1 "Hi!"
        a "'Sup?"
        c grin "So, what did you get Donald?"
        a "I got him a sketchbook and some pencils."
        c p2 left level "That's cool, I guess."
        a "Well, we'll see how he likes it come the 4th."
        c straight casual "I suppose so."
        a "What about you? What did you get?"
        c blank sad "...I..."
        c p1 right "...I didn't know what game to get, so I just got him a $50 Vapor card."
        a "Oh."
        c straight "I mean, it's better than nothing, right?"
        a "This is true."
        show chris casual
        b_o "What is?"
        pause 0.1
        show chris at close_right_c
        show brit p2 straight casual grin at twoleft
        with easeinleft
        pause 0.1
        "Almost on cue, Ms. Usher made her appearance."
        a "Christeena got Donald a gift card, which is better than nothing."
        $ b_partial = True
        b raised blank "Barely."
        $ c_blush = True
        c_s mad "..."
        a "Anyway, what did you get, Brittney?"
        $ b_partial = False
        show brit p1 straight casual grin at twoleft
        b "I got him a baseball glove."
        $ c_blush = False
        show chris p2 straight raised blank at close_right_c
        c "So you got him something for you to use?"
        b p2 mad blank "Hey, he kept saying how we was missing his, so I'm just trying to help him out!"
        c right level "If you say so..."
        a "Alright, enough chatter; let's eat!"
        b p1 sad opened_smile "Don't gotta tell me twice!"

label eatatfc:
    scene bg mall_fc with dissolve
    pause 0.1
    $ c_blush = False
    if persistent.choices["17"] == 0:
        "I then looked around to see where I should eat. It was a pretty small food court, but there still seemed to be a decent variety of choices."

        "Where should I eat?{nw}"

        menu:
            "Where should I eat?{fast}"

            "Taco Jack's":
                $ persistent.choices["17"] = 1

            "Uncle Ulmer's Pretzels":
                $ persistent.choices["17"] = 2

            "Pizza Shack":
                $ persistent.choices["17"] = 3

            "McDaniel's":
                $ persistent.choices["17"] = 4

            "P.J. Chong's":
                $ persistent.choices["17"] = 5

    window hide dissolve
    scene bg fade with wipeleft
    pause 0.5
    scene bg mall_fc with wipeleft
    window show dissolve
    pause 0.1

    if persistent.choices["17"] == 1:
        $ food_court_food = "tacos"
    elif persistent.choices["17"] == 2:
        $ food_court_food = "pretzel"
    elif persistent.choices["17"] == 3:
        $ food_court_food = "pizza"
    elif persistent.choices["17"] == 4:
        $ food_court_food = "burger"
    elif persistent.choices["17"] == 5:
        $ food_court_food = "sweet and sour chicken"

    "As I ate my [food_court_food], the girls talked about this and that; I honestly wasn't paying too much attention."
    "By the time I finished eating, they were only halfway done with their meals."
    show brit p2 straight casual blank at twoleft
    show chris p1 straight casual blank at tworight
    with dissolve
    pause 0.1
    a "Heh. Not very hungry, I see."
    $ b_wink = True
    b mad tongue "Oh, hush."
    $ b_wink = False
    b p1 straight raised opened_smile "I'm just a naturally slow eater."
    a "Excuses, excuses."
    b p2 level grin "Call it what you will, but eating too fast isn't good for you, you know."
    b raised "Ask Christeena; she sometimes shovels her food down so fast that she'll be burping like a trucker for the rest of the night."
    $ c_blush = True
    c p2 mad "Brittney!!"
    b right level huhu "What? You do!"
    c hanging "God fucking dammit, Brittney!!"
    "Christeena threw her fork at the table and glared at her sister with rage."
    c "You've been pulling this shit all day, and I'm sick of it!!"
    show brit p1 straight casual blank
    "Brittney stared at her with a look of genuine confusion."
    b "What shit?"
    c p1 blank "Saying a bunch of embarrassing and insulting shit about me!!"
    "Naturally, people were starting to look our direction to see what was going on."
    b level "So what? I do it all the time, and you never seem to have an issue."
    c right "Y-Yeah, well..."
    "Brittney paused, looked at me, then grew a smile and looked at Christeena."
    b p2 raised huhu "It wouldn't happen to be an issue today because we're in front of Alex, is it?"
    c_s straight "..."
    b p1 opened_smile "Because that's the only difference I see!"
    c_s "..."
    a "Seriously, Christeena; what's up? You've been acting this way all day."
    c_s p2 right "..."
    b mad blank "I know, right? She's never been THIS moody on her period!"
    c straight p1 scream "ARE!! {w=.5}YOU!!{w=.5} FUCKING!!{w=.5} SERIOUS?!?!"
    b_s blank casual "..."
    $ current_track = "None"
    stop music fadeout(3)
    stop loop fadeout(3)
    play sound table_slam
    "Christeena then quickly stood up and slammed her hands onto the table, leaning towards Brittney with a furious, almost inhuman expression."
    c "FUCK YOU, BRITTNEY!!! THIS IS WHY PEOPLE CAN'T FUCKING STAND YOUR STUPID ASS!!"
    show chris:
        ease 0.25 offscreenright
    pause 0.25
    hide chris
    pause 1
    show brit at middle with easeinleft
    pause 1
    show brit sad
    pause 0.1
    $ c_blush = False
    b_s "..."
    "As Christeena stormed off to the restrooms and everyone turned back to their meals now that the show was over, Brittney leaned back in her chair and let out a small sigh."
    $b_blink = False
    b closed_sad p2 "Fuck..."
    "She said that so quietly, I only understood what she said because I could read her lips."
    a_s "..."
    a "I'm sorry. I shouldn't have said anything."
    b "Alex..."
    $b_blink = True
    b straight "Alex...{fast}it's not your fault. I promise.{w} It's MY fault."
    $ b_wince = True
    b left "It's ALWAYS my fault..."
    "Her voice gave a small crack as she said that."
    a "Brittney...!"
    $ b_wince = False
    b level "I, uh..."
    b straight "I-I'm just gonna walk around for a bit. I need to clear my head."
    hide brit with easeoutleft
    pause 1
    "..."
    "Well, this wasn't exactly how I thought my Sunday afternoon would go."
    "I looked back at Brittney and saw she was wiping her eyes while walking out of the food court and towards the end of the mall."
    "As much as I wanted to go after her and try and help, I feel like I might just make it worse."
    "Sighing, I finished up my drink and pulled out my phone, scrolling through social media to kill time until one or both of the girls comes back."
    window hide dissolve
    scene bg fade with wipeleft
    pause 0.5
    scene bg mall_fc with wipeleft
    window show dissolve
    pause 0.1
    play sound chair
    "It must've been about 10 minutes before I heard the chair next to me being pulled back."
    "I turned to find the one responsible."
    $ current_track = "\"Reflection\""
    play music reflection
    show chris p1 straight sad blank at close_c with dissolve
    pause 0.1
    c "Where's Brit...?"
    a "She said she needed to walk and clear her head."
    c p2 right "Oh..."
    a_s "..."
    a "Hey, I'm sorry that I--{nw}"
    c straight "Don't."
    c p1 "It's my fault; I shouldn't have snapped on her like that. I know how sensitive she can get when..."
    c_s left "..."
    c grin "...{fast}heh. No point in being shy about it at this point."
    c straight "I know how sensitive she can get when she's on HER period."
    a "Oh.{w} So, you both are...?"
    $ c_blush = True
    $c_blink = False
    c closed_happy "What are the odds, right?"
    a "Yeesh."
    $c_blink = True
    $ c_blush = False
    show chris p1 left sad grin at close_c
    c "Yeah..."
    show chris blank
    "She then let out a sigh."
    c "I'm such a bitch."
    a "Hey, now; I get why you were upset. I wouldn't want to constantly be belittled and humiliated like that, either."
    c straight "Still, I could've handled that a bit better."
    a "Well...{w} Yeah, you could've."
    c p2 right "I don't know what's wrong with me... I always end up doing things like this, especially to Brittney..."
    c straight "I'm sorry that you had to see all of this... I promise you we're better than that."
    c right "It's just been one of those days."
    a "I hear ya."
    "With an awkward grimace on my face, I gave Christeena a quick pat on the back."
    a "We all have those days. Lord knows I certainly have."
    c_s "..."
    b_o "H-Hey..."
    pause 0.1
    show chris straight:
        ease 0.5 close_right_c
    show brit p2 straight sad grin at twoleft with easeinleft
    pause 0.5
    b blank "Listen, I--{w=.25}{nw}"
    show chris:
        parallel:
            ease 0.25 zoom 0.75
        parallel:
            ease 0.25 xalign 0.39 yalign 0.5
    pause .25
    show brit small casual hanging zorder 2
    show chris zorder 1
    "Christeena quickly stood up and hugged her sister, sobbing loudly as she buried her face in her shoulder."
    $c_blink = False
    c tightly_shut sad scream p1 "I'M SO SORRY, BRITTNEY!! I SWEAR I DIDN'T MEAN IT!!"
    b sad straight p1 grin "Hey, hey..."
    "Brittney hugged Christeena back and sighed."
    b "I'm sorry, too."
    "The two stood there and hugged for a few seconds before Christeena let go, tears flowing down her face."
    with Pause(.1)
    $c_blink = True
    show chris tears straight blank at tworight with easeinleft
    with Pause(.1)
    b p2 "Let's just...{w=0.5} forget about this, okay?"
    c grin "Y-Yeah... *sniff* I'm okay with that."
    a "Same here."
    b p1 opened_smile "Heh. Sorry for making your day really awkward, Al."
    a "You kidding? Any day where I can hang out with a couple of girls is a good day, in my book."
    b p2 raised grin "You're such an asshole at times."
    a "That's rich coming from you."
    $ b_wink = True
    b tongue mad "Nyeh."
    c p2 straight sad grin -tears "So, uh...{w=.5} are we ready to head home?"
    $ b_wink = False
    b p1 straight sad grin "I am."
    a "Ditto."
    $ daydesc = 0
    $ replay = False
    $ renpy.end_replay()
    $ progress += 1
    jump progress
