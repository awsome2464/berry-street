# Sentimental moment where we learn more about Brittney and Christeena's thoughts about the other.

# b "C'mon!"
# a "Sure, let's g-"
# b "Not you; her."

# "As she said that, she gestured towards Christeena, who looked like she had stopped in the middle of the sidewalk to tie her shoe."
# "She glanced up at us at the mention of the word 'her'."
# "A second later, she stood up and jogged over to us."

# c "Sorry, my shoe was a little loose."
# c "Plus, I'm not exactly as fast as you."
# b "Tsk. You've always got some sort of reason to slow us down."
# b "Maybe if you actually took care of yourself from time to time, this wouldn't happen."
# c "..."
# c "...S-sorry."
# b "..."
# b "No, I'm the one who should be sorry."
# b "So, uh, sorry."
# c "...okay."

# with Pause(2)

# a "Uh..."
# a "So, are we ready?"
# b "I am."
# c "Yeah, so am I."
# a "Alright. Lead the way."

# "With that, Brittney took the lead and walked us over to the woods, though the awkwardness still lingered."

# with Pause(2)

# # Woods Night

# "I was between Brittney and Christeena, the latter of which seemed to be looking more towards the ground, as if she wanted to avoid any eye contact with anyone."
# "Even Brittney was unusually silent as we walked through the woods, only occasionally saying the simple 'watch your step' or 'should be there quickly'."
# "..."
# "They both look pretty uneasy."
# "I have a feeling that talking to both girls at the same time would probably only cause arguments between them."
# "It won't take too much longer to get to the cabin, so if I'm going to talk to one of them about this, I gotta decide now."

# menu:
#     "What should I do?"

#     "Talk to Brittney.":

#         $ B_Points += 1
#         jump talktobrit

#     "Talk to Christeena.":

#         $ C_Points +=1
#         jump talktochris

#     "Say nothing.":
#         jump talktonobody

# # Talk to Brittney

# label talktobrit:
# "Brittney seems to be the one who's more regretful, so I think I should talk to her."
# "I pick up my pace a bit until I'm next to Brittney."

# a "Hey."

# "She turned around to look at me, but she keeps walking forward."

# b "What's up?"

# "She's trying her best to sound friendly, but there's still a slight awkwardness in her tone."

# a "So..."
# a "What was up with what happened back there?"

# "She gave a shy smile as she turned forward, breaking the eye contact."

# b "Oh, that...?"
# b "I'm sorry you had to see that."
# a "..."
# a "That doesn't answer my question."

# "She gave a small sigh, still sporting that grimace."

# b "I know."
# b "..."
# b "I guess you can say that I'm a little impulsive."
# a "Impulsive?"
# b "Yeah."
# b "I tend to do and say before I think, which can lead to situations like the one you witnessed."
# a "Oh."
# b "Yep."
# b "I suppose the benefit of it being Christeena is that she's aware of that issue, so she knows I don't really mean it half the time."
# b "But it still sucks when I say something stupid and hurtful to her, especially since she's kind of sensitive."
# a "What do you mean?"
# b "Well, I'm sure even you have enough brain cells to notice that she's not exactly an extrovert."
# a "I suppose."
# b "It could be worse."
# b "It's not like she shuts herself away from people."
# b "She really opens up once she gets to know you, or if you're someone that someone close to her knows."
# a "Like me?"
# b "Exactly!"
# b "She's such a sweetheart. It really is a shame that I tend to lash out on her."
# a "Wow."
# a "You really care about her, don't you?"
# b "Of course I do."
# b "Blood or not, she's my sister. My younger sister, at that."
# b "Sure, I may tease her, but I still want her to be happy and do her best."
# a "I gotcha."
# b "Yeah..."
# b "Anyway, looks like we're here!"

# "I look and see the cabin is, indeed, in front of us."
# "There seem to be lights on inside."

# b "Well, let's not keep Donald waiting any longer."
# a "Yeah."

# label talktochris:

# # Christeena's First Kiss

# a "'Kinda'?"
# show chris 10
# c "Well, I mean..."
# show chris 7
# c "...I've never actually... done that... before."


# # Brittney flashing Alex

# label b_dare_flash:
#     a "...flash me."
#     show brit 5
#     b "PFFFFT!"
#     b "Men are so predictable!"
#     show brit 3
#     b "I mean, a girl like Christeena, I'd understand..."
#     show brit 4
#     b "...but why you would want to see a chest that probably looks just like yours just because it belongs to a female is beyond me."
#     a "..."
#     show brit 5
#     b "But, who am I to deny the horndog what he wants?"
#     show brit at tworight
#     show don 1 at twoleft
#     with dissolve
#     d "Even though you deny me of it all the time?"
#     show brit 4
#     b "What, you think I'm the kind of easy girl who will strip for anyone who asks?"
#     a "I mean, I kinda did just ask..."
#     show brit 3
#     b "You {i}DARED{/i}. There's a difference."
#     b "I'm not one to turn down a dare that easily."
#     show don 3
#     d "Noted..."
#     show brit 6
#     b "Alright, freak; leave the cabin."
#     show don 7
#     d "Huh??"
#     show brit 3
#     b "These cupcakes are for Alex's eyes only."
#     b "Run along, now."
#     show don 12
#     d "..."
#     hide don with moveoutright
#     with Pause(1)
#     show chris 7 at twoleft with dissolve
#     c "..."
#     c "You're seriously going to do this?"
#     show brit 2
#     b "Why not?"
#     show chris 8
#     c "Do you have any shame in you?"
#     show brit 3
#     b "What is this thing you call 'shame'? Sounds stupid."
#     show chris 7
#     c "..."
#     c "I'll be going now."
#     show brit 4
#     b "Be a dear and make sure Donald doesn't peek through the window."
#     show chris 9
#     c "*sigh* Will do..."
#     hide chris with moveoutright
#     with Pause(1)
#     show brit 2 at truecenter with moveinright
#     b "Alright, big boy. You ready?"
#     a "I guess."
#     show brit 4
#     b "'You guess'?"
#     show brit 3
#     b "A girl is about to show you her boobs and 'you guess' you're ready?"
#     a "..."
#     show brit 2
#     b "Oh, my God..."
#     show brit 5
#     b "You've never seen a pair of tits before, have you?"
#     a "...!!"
#     a "Uh..."
#     show brit 4
#     b "Seriously? Not even in porn?"
#     a "..."
#     show brit 5
#     b "Oh, my God!!"
#     b "You're even more pathetic than I thought!"
#     a "This was a mistake, wasn't it?"
#     show brit 4
#     b "I don't know if 'mistake' is the right word here..."
#     show brit 6
#     b "...but this certainly is hilarious!"
#     show brit 1
#     b "..."
#     show brit 2
#     b "You know what?"
#     b "As bitchy as this sounds, I'm not going to let you see them."
#     a "Huh??"
#     show brit 4
#     b "You deserve better-looking boobies as your first pair."
#     a "..."
#     show brit 5
#     b "Aww, don't feel so bad."
#     show brit 2
#     b "I'm doing this for your own good."
#     show brit 4
#     b "Which is why I'm going to give you this piece of advice:"
#     show brit 7
#     b "Watch some porn, for crying out loud!"
#     a "...!!!"
#     show brit 2
#     b "Alright, let's get out of here."
#     show brit 4
#     b "Just promise me one thing."
#     a "What's that?"
#     show brit 3
#     b "Tell Donald how perfect they looked; I wanna see his reaction!"
#     a "You really love teasing him, don't you?"
#     show brit 5
#     b "You know it!"
#     $ B_Flash = True

#     return

label brit_sibling_talk:
    python:
        b_hair = 0
        b_hat = 0
        B_Name = "Brittney"
        outfit_b = "a"
        b_blink = True
        current_track = "\"From the Heart\""
        renpy.music.set_volume(0.5, channel='loop')
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
    b p2 casual opened_smile "Yep. She and my dad could hardly believe it."
    b grin "Her having one child was rare enough, but another on top of that?"
    $b_blink = False
    b closed "It was like winning the lottery!"
    a "They really wanted another kid, huh?"
    $b_blink = True
    b level left huhu "It was mostly my dad. He always dreamed of having a big family."
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
    b straight "...Elizabeth's heart stopped beating."
    a "Dang..."
    $b_wince = True
    b left "Yeah."
    b "My mom was warned many times throughout her life that complications could happen during pregnancy, but that still didn't properly prepare her for that moment."
    $b_wince = False
    b straight "I was definitely as hurt as a kid my age could've been at finding out that my little sister wasn't coming, after all, but I obviously didn't really understand everything."
    $b_wince = True
    b right p1 "I still have some faint memories of my mom crying not too long afterwards."
    b grin "I tried anything I could to make her feel happy. Like I said, I didn't fully understand the situation."
    a "Of course."
    $b_wince = False
    b straight blank "I don't remember too many things about my dad at that time, but one thing for sure still sticks in my mind to this day."
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
    $b_wink = True
    b raised tongue "I didn't inherit my stubbornness from my old man, you know."
    $b_wink = False
    b casual grin p1 "But she really was insistent on having another kid."
    b sad left "Giving me a younger sibling to bond with, giving my dad his wish of a bigger family..."
    b p2 "That's something I'll never stop respecting about my mom: she loves her family and is willing to do anything for them."
    a "Yeah, I've certainly noticed."
    a "But still. Wanting to try getting pregnant again right after she--"
    b casual straight blank "Oh, it wasn't right away."
    b "She was still hit pretty hard by the loss of Elizabeth."
    b sad "We all were."
    b grin "But she swore she'd try again when she was ready."
    b right "...of course, by the time she was ready..."
    b "...my dad... you know..."
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
    $b_wince = True
    b p2 sad hanging "Jesus...!"
    b "I thought you meant like he died literally right after he was born!"
    a "Nah. He was around for a while afterwards."
    $b_wince = False
    b blank "I'm so sorry...!"
    a "I mean, I never met him. Like I said, this was years before I was even conceived."
    b p1 "Still..."
    b "I had no idea..."
    a "Like you said, it's not exactly something to randomly bring up."
    a "Plus, it's not like your situation where you can remember firsthand some of the things that happened."
    b p2 left "I suppose..."
    $b_wince = True
    b "Still, though. That had to have been so awful on your parents."
    a "Yeah, I can only imagine."
    a "Honestly, part of me believes that they still haven't really gotten over it even to this day."
    $b_wince = False
    b p1 straight "Well, I don't think pain like that ever goes away completely."
    a "Probably not."
    "We then stared at each other in silence for a few seconds, not really sure where to go from here."
    show brit p2 right level
    "Brittney then turned back towards the pond with a look of heavy thought."
    b "Hey, Alex?"
    a "Yeah?"
    b "So, like..."
    b "You believe in God and Heaven and all that, right?"
    "I was thrown off for a second at the seemingly sudden change of topic."
    a "Yeah. Why?"
    show brit sad
    "She took a deep breath before continuing."
    b "Well, Donald's always told me that everything happens for a reason."
    b "He says that God allows certain things to happen, no matter how painful they may be at the time, to help you in the long run."
    a "He's not necessarily wrong. There are plenty of stories in the Bible where something like that happens."
    b level "So I guess what I'm trying to wrap my head around is..."
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
    b "First Elizabeth, and then my dad..."
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
    b right "It was...{w=1.0} It was nice to talk about that with you. Get a different perspective and all that."
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


label brit_shopping:
    python:
        b_hair = 0
        b_hat = 0
        B_Name = "Brittney"
        outfit_b = "b"
        b_blink = True
        current_track = "None"
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

