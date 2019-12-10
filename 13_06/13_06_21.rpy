label unpack0621:
    $ C_Name = "Christeena"
    show text "{size=+50}June, 2013{/size}":
        xalign 0.5 yalign 0.05
    show screen calendarOs
    show calendar june june_21:
        xalign 0.5 yalign 0.6
    show calendar_circle:
        xalign 0.625 yalign 0.65
    with dissolve
    if replay == False:
        $ persistent.todays_date = "June 21st, 2013"
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
    $ current_track = "\"Home Life\""
    play music home_life
    nvl show dissolve
    $ renpy.block_rollback()
    narrate """
    I opened up the next box in the living room. More framed photos.

    Now that we have more living space, Mom went and got a lot of our old family photos framed so we could hang them in the walls of our new home.

    Some, I could understand, such as this one of all of us in front of The Bean, or this one of Harry and I from around 10 years ago.

    But was this one of me crying when I was 3 really worth hanging up for our guests to see?

    Ah, whatever. The less I question Mom's motives, the better everyone is.
    """
    play loop phone_vibrate_call
    narrate "My phone then started to ring. I looked and saw that it was Donald."
    nvl clear
    nvl hide dissolve
    window show dissolve
    stop loop
    a "Yeah?"
    d_o "{font=fonts/LemonMilk.otf}{i}Hey, wassup?{/i}{/font}"
    a "Unpacking."
    d_o "{font=fonts/LemonMilk.otf}{i}Again??{/i}{/font}"
    a "Can't help it; Mom wants everything unpacked ASAP."
    d_o "{font=fonts/LemonMilk.otf}{i}Well, that blows.{/i}{/font}"
    a "Yeah, tell me about it."
    d_o "{font=fonts/LemonMilk.otf}{i}Well, how much more do you have?{/i}{/font}"
    a "In the whole house? I mean, not too much more; just some stuff in the living room and then our bedrooms."
    d_o "{font=fonts/LemonMilk.otf}{i}But it's easier said than done?{/i}{/font}"
    a "Heh. Pretty much."
    d_o "{font=fonts/LemonMilk.otf}{i}Hm...{/i}{/font}"
    "Uh oh. {w=.5}I've heard that 'Hm' before; that's Donald's 'I've got an idea' noise."
    d_o "{font=fonts/LemonMilk.otf}{i}Alright, Man. I'll talk to you later.{/i}{/font}"
    a "Alright. See ya!"
    "We then hung up, and I got back to work."
    "It sucks that Mom is forcing Harry and I to do so much unpacking, but I guess it could be worse; we could be doing it alone."
    "Mom and Dad are helping unpack, too, though Dad not as often since he started working. Still, he helps where he can."
    "Now, I should probably ask Mom where to hang this up..."
    window hide dissolve
    scene bg fade with wipeleft
    pause 1
    scene bg living_s_m with wipeleft
    window show dissolve
    play sound door_knock
    "About 15 minutes passed before I heard a knock on the front door."
    a "I got it!"
    "I called out loud as I walked to the door."
    "Opening it up revealed a not-so-surprising surprise."
    play sound door_open
    scene bg house_s with dissolve
    pause 0.5
    show don a1 straight casual grin:
        zoom 1.0
        xalign 0.9 yalign 0.2
    show chris b2 straight casual grin:
        zoom 1.0
        xalign .1 yalign .25
    with dissolve
    pause 0.1
    $ current_track = "\"Ivories and Ebony\""
    play music ivories_and_ebony
    "Donald and Christeena were at the door with excited grins."
    d raised smile "Sup, Man?"
    c b1 smile "Hey, Alex."
    a "Donald, I told you I can't hang out right now; I have to unpack stuff."
    d grin "I know. That's why we're here: we're going to help you!"
    a "You are?"
    c small level dot "We are??"
    c straight mad blank "Donald, you said we were going to Alex's to hang out!"
    d casual smile left "We will!{w=0.5} Right after we help him finish unpacking!"
    c b2 left "Asshole."
    d straight raised "He said there wasn't too much left, so the quicker we help out, the quicker we can all relax!"
    c "..."
    g_o "Who is it, Alex?"
    "My mom called from the kitchen."
    a "It's Donald and Christeena! They're here to help unpack!"
    g_o "Really? Well, how thoughtful of them!"
    d casual grin "Thank you, Mrs. Sprouse! We're both so excited to help!"
    "By the time he finished speaking, Mom had made it to the front door area."
    show chris straight casual dot:
        ease 0.5 threeleft
    show don:
        ease 0.5 middle
    show ginger a2 straight sad grin at threeright with easeinright
    pause 0.1
    g "Oh, Donald, I told you that you don't have to be formal around me; just call me Ginger."
    d level right "Sorry, but I just prefer 'Mrs. Sprouse', if that's alright with you."
    g level "Well, I suppose I don't see a problem with it."
    g casual wide "Ah, where are my own manners?{w=0.5}{nw}"
    show ginger:
        ease 0.25 xalign 0.5
    show don casual straight:
        ease 0.25 xalign 0.9
    pause .26
    g grin "You're the Christeena I've heard about?"
    c b1 grin "Yeah, that's me. Christeena Truman. That's Christeena with two 'e's"
    g sad "Ah, what a cute way of spelling it."
    $ c_blush = True
    c left sad "T-thanks."
    g casual "I'm Ginger, Alex's mother. It's nice to finally meet you."
    $ c_blush = False
    show chris b2 straight casual grin at threeleft
    c "Likewise."
    g "Anyway, come on in!"
    d straight casual smile "Sure thing!"
    hide don
    hide chris
    hide ginger
    with dissolve
    pause 0.5
    scene bg living_s_m with dissolve
    show ginger a2 casual grin straight at middle with dissolve
    pause 0.1
    g "All that really needs to be done now is the rest of the living room in terms of the important stuff, though I'd still like Alex's room to be finished quickly."
    show chris b2 straight casual blank at threeleft
    show don a1 raised grin straight at threeright
    with dissolve
    pause .1
    d "Don't worry, Mrs. Sprouse; we've got this."
    d casual "It'll be easier to split up the work, half of us working on the living room and the other half working on Alex's room."
    a "Well, I think it would be best if I work on my room, for obvious reasons."
    g level "That's fair. And I suppose I would be more fitted for the living room, anyway."
    c b1 level "So, where do Donald and I go?"
    d left level blank "Hmm..."
    d raised straight "Hmm...{fast} Alex, do you have any preference?"
    a "Uh..."
    show don:
        ease 0.5 xalign 0.75
    show chris:
        ease 0.5 xalign 0.25
    hide ginger with dissolve
    pause 0.1
    if persistent.choices["9"] == 1:
        "Hmm...{w} Who do I want to help me work on my room?"
        "Well..."
        jump d_cleanroom
    elif persistent.choices["9"] == 2:
        "Hmm...{w} Who do I want to help me work on my room?"
        "Well..."
        jump c_cleanroom
    else:
        menu:

            "Hmm... Who do I want to help me work on my room?"

            "Donald":
                $ persistent.choices["9"] = 1
                jump d_cleanroom

            "Christeena":
                $ persistent.choices["9"] = 2
                jump c_cleanroom

label c_cleanroom:
    $ C_Points += 1
    $ cleaningpartner = "Christeena"
    a "I guess Christeena could probably be of some good help upstairs."
    hide don
    show chris at middle
    with easeoutright
    pause 0.1
    c b2 sad dot "Are you sure? I mean, I don't think I'd really know where everything in a boy's room would go..."
    a "I've got some boxes of clothes that need unboxed and hung up; you could help with that. It's simple work, nothing too complicated."
    c blank "Well..."
    c b1 grin "Well...{fast}okay. I guess I can handle that."
    show don straight casual smile a1 at tworight
    show chris at twoleft
    with easeinright
    pause .1
    d "Great! Then I'll help your mom in the living room."
    a "Sounds like a plan."
    scene bg living_s_m with dissolve
    pause 0.1
    "Donald and Mom started to open boxes in the living room as I showed Christeena the way to my bedroom."
    "On the way, we ran into Harry as he walked out of the bathroom."
    "I introduced the two and explained that she was going to help me unbox in my room.{w} He was then kind enough to mention how it's the first and last time I'll have a girl in my room."
    "After telling him that at least I could get a girl in my room, unlike him, he laughed and went into his own room to finish his unboxing. Christeena couldn't help but smile a little bit."
    $c_blink = False
    show chris b1 closed_happy sad smile at close_c with dissolve
    pause 0.1
    c "Now I see how you can put up with Brittney!"
    a "Speaking of which, what time does she get off work today?"
    $c_blink = True
    c b2 straight casual grin "5 o'clock, so only a few more hours."
    a "Well, if we're not done by then, I suppose she could always come to help us."
    c left level "Maybe. We'll see."
    scene bg bedroom_a_m with dissolve
    $ current_track = "\"Violet Wonder\""
    play music violet_wonder
    "We then entered my room, which was mostly unpacked, but there were still a handful of boxes left."
    show chris b1 straight dot casual at close_c with dissolve
    pause 0.1
    c "Wow! It looks pretty clean in here, even with the boxes. I expected a boy's room to dirtier than this."
    a "Just give it time; it'll come eventually."
    a "Anyway, all the boxes of clothes are over there, by the closet and dresser."
    c b2 blank "Is there any specific way you want them arranged?"
    a "For the closet, if you could try to keep the T-shirts on one side and the dress shirts on the other, that would be nice."
    a "And for the dresser, socks in the top drawer, then underwear in the next one..."
    c mad "Ew."
    a "Don't worry, they're clean."
    c b1 left "It's still weird."
    a "You'll survive. Anyway, after that, it's jeans, dress pants, and jackets."
    c straight casual "Huh. That seems like a small clothing selection."
    a "What can I say? I'm not a clothing kind of guy."
    c b2 level "Clearly."
    a "So, yeah, that's all you really have to do. I'll work on these boxes over here; it's just stuff for the shelves."
    "I then pointed to the various shelves hanging up around the room, a few above my bed, some by the door, and one right next to the closet."
    a "If we work fast enough, I'd say we could get this done pretty quickly."
    c b1 casual grin "I like the sound of that!"
    hide chris with dissolve
    pause 0.1
    "We each then got to work on a box."
    "At first, Christeena was constantly asking if this was hanging up in the right place or if she was folding these up correctly, but after that, it soon got pretty quiet."
    "Our backs were facing each other for most of the time, so it kinda felt like she wasn't there."
    "Since she certainly wasn't going to start a conversation, it was up to me to break this silence."
    show chris b2 straight casual blank at tworight with dissolve
    pause 0.1
    a "I gotta say, I'm really enjoying it here in Smalltown."
    c sad grin "Really?"
    a "Yeah! I mean, sure, it's only been a few weeks, and it's a drastic change from big-city life, but as far as first impressions go, this is a nice one."
    $ c_blush = True
    $ c_blink = False
    c closed_happy "Well, I'm glad!"
    $ c_blush = False
    $ c_blink = True
    show chris b1 straight casual grin at tworight
    c "Well, I'm glad!{fast} What about the neighbors? How do you like them?"
    a "Well, I gotta say, there are these two annoying girls that live right next door, and they're just the worst."
    c mad "Is that so?"
    a "Yeah, especially the short one with black hair. She sucks so much."
    c b2 smile "Hey, she is not short! She's average height for someone her age!"
    a "Well, she's shorter than me, so that makes her short. {w}And either way, she still sucks."
    show chris b1 grin
    "I could tell she was trying to act offended, but her smile told her true feelings."
    a "Nah, but for real, our neighbors seem like cool people."
    show chris b2 casual
    a "The Rodriguezes are kind, the Reagans are energetic, the Waterses are just as awesome as I remember, and your household is pretty cool, too."
    a "And then there's Eleanor..."
    c b1 left mad blank "Ugh..."
    a "What's her deal, anyway?"
    c straight "No fuckin' clue. It's like she's a robot programmed to piss everyone off."
    c b2 "And how she treated your brother... that's just unacceptable!"
    "I had told the guys about the run-in I had with Eleanor when I was shopping at Dolmart. Their reactions were just as I'd exptected: Donald disappointed, Brittney shocked, and Christeena pissed."
    "I haven't spoken to Eleanor at all since that day, and the longer I can honestly say that, I think the happier I'll be."
    a "Yeah, but Harry seems to have moved on from that. Though if he found out that she was our neighbor..."
    c b1 sad dot "You mean he doesn't know??"
    a "I can't think of a good way to bring it up. Can you?"
    c casual blank "...{w}fair point."
    a "Still, if we've managed to go this long without another run-in, then I think it's safe to say she won't be too much of an inconvenience, right?"
    c b2 left blank level "Well, yeah, maybe for the summer. Once school starts, though..."
    a "Though I'm glad I'm not crazy when I said I think that she looks too old to be a high schooler."
    c b1 straight casual "Yeah, her being held back is crazy! Why would you want to be in high school for longer than necessary??"
    a "I don't think people that get held back WANT to be held back, Christeena."
    c left dot level "Still..."
    a "Anyway, the only neighbor I haven't met yet is that scientist lady. What was her name, again?"
    c b2 straight casual blank "Anna Ziphon. And I'm honestly not surprised you haven't met her yet; she's the biggest hermit I know. Half the time, I forget she even exists."
    a "So does she really have a laboratory in her house or whatever?"
    c b1 dot left level "That's what everyone says, though none of us have actually been in it."
    c straight raised blank "Personally, I don't think there's anything that big in there, but Brittney keeps insisting there's the cure for cancer down there somewhere."
    a "Hehehe..."
    c casual "What?"
    a "It just amuses me how different you and Brittney are, inside and out."
    c b2 left sad grin "Yeah, it truly does baffle me how I got stuck with a sister like her."
    a "Correct me if I'm wrong, but I believe it had something to do with your dad and her mom getting married."
    c straight mad "Smartass."
    $c_blink = False
    show chris closed_happy sad smile
    "We both then gave a hearty laugh before agreeing we should probably get back to focusing on getting my bedroom done."
    window hide dissolve
    scene bg fade with wipeleft
    pause 1
    scene bg bedroom_a_m with wipeleft
    window show dissolve
    $c_blink = True
    "A short while had passed before I heard Christeena walking up next to me."
    show chris b2 straight casual grin at tworight with easeinright
    with pause 0.1
    c "I've got all your clothes put away!"
    "Sure enough, all the boxes that housed my clothing were empty and broken down by the door."
    "Damn. She's quick."
    a "Sweet! I just gotta finish getting these books put up."
    "I grabbed a book from the box and placed it on the nearly-full shelf."
    c b1 dot "You read?"
    "I turned to her in confusion."
    a "You say that like you're surprised."
    c level blank "That doesn't answer the question."
    "Wow.{w} I guess she's taking this pretty seriously."
    a "Occasionally. Not as much as I used to."
    c b2 casual "What kind of things do you read?"
    "She was staring at the shelf as she asked this, leading me to believe that it was more of a rhetorical question."
    a "What's it to ya?"
    c smile "I like to judge people based on what they read."
    a "What, are you a bookworm or something?"
    c b1 left level dot "I don't know about 'bookworm'... I'm not really obsessed with reading or anything like that."
    a "No kidding? I kinda figured you'd spend all your free time absorbed in books."
    c straight raised blank "What gave you that idea?"
    a "I guess I just assumed that all introverted girls were obsessed with books."
    c b2 left level "I...{w=1.0} I'm not sure how to respond to that..."
    a "..."
    "Smooth, Alex. {w=.5}Smooth."
    "I clear my throat and try to get back to the subject at hand."
    a "Well, anyway, I'm more into mystery stories."
    c straight smile casual "Oh, like Agatha Christie?"
    a "Eh. More like {i}The Hardy Boys{/i}."
    c level blank "Oh."
    "The way she said that made me feel like I had insulted her entire family."
    a "Sorry to disappoint."
    $ c_blush = True
    c b1 sad hanging "I-I'm not disappointed!"
    c left grin "I mean, I used to read {i}Nancy Drew{/i}. {w=1.0}You know, when I was younger..."
    a "..."
    a "Well, I mean, I grew up reading horror, too."
    $ c_blush = False
    show chris b2 straight casual blank at tworight
    c "Stephen King?"
    a "R.L. Stine."
    c left grin level "Ah."
    c b1 straight sad "Well, at least you read some decent stories by decent authors."
    "I don't know whether that was a compliment or an insult, but considering it being even from my 'introverted girl' comment, I decide to just nod and finish putting the books up."
    a "Well, I think that's everything! My room is officially done!"
    $c_blink = False
    c b2 closed_happy sad smile "Yes!"
    "We high-five each other in celebration before heading down to the living room."
    scene bg living_s_m with dissolve
    $c_blink = True
    a "Well, we're done in my bedroom!"
    show ginger a2 level blank straight at twoleft
    show don a1 straight blank casual at tworight
    with dissolve
    pause 0.1
    g "Did you ACTUALLY put everything where it belongs, or did you just toss it somewhere out of sight?"
    show ginger at threeleft
    show don at middle
    show chris b1 straight casual grin at threeright
    with easeinright
    pause 0.1
    c "Everything looks like it's where it belongs, Mrs. Sprouse."
    g raised grin "Is that so?{w} Well, then I guess I'll believe you."
    a "Am I really that untrustworthy that you're going to believe the girl you don't know over the guy you've known for 16 years?"
    g level "Indeed, I HAVE known you for 16 years. And because I have, I know how much of a lazy bum you can be."
    a "Eh. I suppose that's fair enough."
    $ c_blush = True
    $ c_blink = False
    c b2 closed_happy sad "Don't worry; we both worked hard to get it all finished."
    d raised grin right "Did I just hear Christeena Renee Truman say, with a confident smile, that she worked hard?"
    $ c_blush = False
    $ c_blink = True
    show chris b2 straight mad grin at threeright
    c "Screw you."
    scene bg living_s_m with dissolve
    pause 0.1
    jump dadcomeshome


label d_cleanroom:
    $ D_Points += 1
    $ cleaningpartner = "Donald"
    a "I guess Donald could help me out; it would make more sense for two guys to be working in a guy's room, right?"
    show don:
        ease 0.5 xalign .9
    show chris:
        ease 0.5 xalign 0.1
    show ginger a2 raised grin straight at middle with dissolve
    pause 0.1
    g "Yes, I suppose that would make more sense."
    g mad "Not that anything would happen if you and Christeena were up there alone, right?"
    c b1 straight mad hanging "Of course not!"
    g raised "Good answer."
    hide ginger
    hide chris
    show don at middle
    with easeoutleft
    pause 0.1
    d straight raised grin "Anyway, shall we go, then?"
    a "Sure thing!"
    hide don with dissolve
    pause .1
    scene bg bedroom_a_m with dissolve
    $ current_track = "\"Brotato Chips\""
    play music donald
    "We walked up the stairs and found myself in my room."
    show don a1 straight raised grin at close_d with dissolve
    d "{cps=*0.5}Niiiiiiice.{/cps}"
    d "Must be great to finally have a bigger room, huh?"
    a "Heh. You have no idea."
    d level "..."
    a "Oh. Right. Duh."
    d raised smile "Anyway, what do you need me to work on?"
    a "I suppose you could put my clothes away for me while I put stuff on the shelves."
    "I then gestured to the various shelves hanging around the room."
    d casual grin "You still the tee-shirt-and-shorts-only guy that I remember?"
    a "Excluding the church shirts, yes."
    $d_blink = False
    d closed sad smile "Well, then how generous of you to give me the easier task."
    a "Hey, you're my guest. I'd be a terrible host if I made you do the hard work."
    $d_blink = True
    d straight grin level "Very true."
    hide don with dissolve
    pause 0.1
    "We then began work on our respective tasks."
    "Despite my simple clothing selection, I was still occasionally glancing over at Donald to make sure everything was arranged correctly."
    "What can I say? I'm OCD like that."
    "As I placed stuff up the shelves and he hung up my clothes, I noticed it was pretty quiet in here. It was actually kinda unsettling."
    "Granted, we were both really focused on our tasks, but it's still weird to not hear Donald talking, as insulting as that probably sounds."
    "To avoid insanity, I started a conversation."
    show don a1 straight blank casual at tworight with dissolve
    pause 0.1
    a "I'm really liking it here in Smalltown so far."
    d grin "Really?"
    a "Yeah! I mean, sure, it's only been a few weeks, and it's a drastic change from big-city life, but as far as first impressions go, this is a nice one."
    d raised smile "Hey, man, that's always good to hear!"
    d casual grin "What about Berry Street in particular, though? I mean, you're gonna be spending a lot of time here."
    a "Sure, sure."
    a "Brittney and Christeena are pretty cool neighbors, as are you."
    d right level "Oh, hush, you; you're gonna make me start blushing."
    a "The Rodriguezes are super friendly, the Reagans are full of energy..."
    a "...the Yellman household, though..."
    d straight blank "Yeah..."
    a "What's her deal, anyway?"
    d sad "Your guess is as good as mine."
    d left "As long as she's been here, Eleanor has acted so inconsiderate of others' feelings."
    d straight level "As I'm sure you and Harry figured out."
    "I had told the guys about the run-in I had with Eleanor when I was shopping at Dolmart. Their reactions were just as I'd exptected: Donald disappointed, Brittney shocked, and Christeena pissed."
    "I haven't spoken to Eleanor at all since that day, and the longer I can honestly say that, I think the happier I'll be."
    a "Yeah, but Harry seems to have moved on from that. Though if he found out that she was our neighbor..."
    d raised "He doesn't know?"
    a "What, do you want me to go 'Oh, Harry, by the way, that woman you pissed off at Dolmart? Yeah, she lives at the end of the street.'"
    d left "Well, no, but..."
    d straight level "He has to find out sooner or later, right?"
    a "Yeah, I guess."
    a "Still, if we haven't really seen her since that day, how often would we realistically see her again?"
    d casual "She's human; she still has errands and such to do."
    d level right "But she realistically doesn't really stay home that often during summer vacation. Where she goes, only God knows."
    d raised straight "Once school starts up, though, expect to see more of her."
    a "Though can I just say that I'm glad I'm not crazy for thinking she's too old to be in high school?"
    d level grin "Yeah, but BARELY too old."
    d "I mean, being held back one year isn't that bad in the grand scheme of things, but you know."
    a "Yeah. I guess she was just unfortunate enough to be held back as well as look older."
    $d_blink = False
    d closed grin sad "Basically."
    a "Anyway, back to the subject of Berry Street, the only neighbor I haven't met yet is that scientist lady."
    $d_blink = True
    d straight casual blank "Oh, Anna? Yeah, that doesn't shock me."
    d level left "The reason we hardly see HER is the exact opposite of Eleanor; she's ALWAYS in her house."
    d straight "They say that she's living off the grid, hiding from someone.{w}.. or someTHING."
    a "Well, she's gotta leave some time, right? She's human, too."
    a "Right?"
    d left "...{w}I don't know, man."
    d "She's... indescribable."
    d straight raised "That experience I had when she called the cops on me... it wasn't a good one."
    a "What happened?"
    d right level "Long story short, she threatened my life after I looked through her window out of curiosity."
    a "Geez! Didn't you tell the cops that?!"
    d mad straight wide "Of course I did!"
    d raised blank "But she denied it, and they believed her."
    a "They believed her just like that?"
    d "Just like that."
    d right "It's highly suspicious, if you ask me, but oh well. That's in the past."
    a "Still, that's not right."
    d straight level "Don't gotta tell ME that!"
    a "..."
    a "You don't think she treated you that way because you're...?"
    $d_blink = False
    d closed sad smile "Hahaha!"
    $d_blink = True
    d straight raised grin "Nah, I think she just hates everyone, no matter who they are or what they look like."
    d left "I guess the positive is that the only way you'd really interact with her is if you brought it on yourself."
    d straight level blank "So when Brittney said to stay away from her, she really means it, though she doesn't know how serious it is..."
    a "Speaking of Brittney, what's the deal with you and her?"
    d casual dot "What do you mean?"
    a "I mean, she keeps talking about how you and her will never be a couple, she constantly hits you, even if her motivations are pure..."
    d level blank "..."
    a "I'm not trying to be rude or invasive, but why do you put up with it? Are you that convinced that she'll magically fall in love with you?"
    d right "..."
    a "Donald?"
    d "I'm thinking about how to word this..."
    d straight raised "I've already told both her and you that I just have this gut feeling that me and her are meant to be together in some way."
    d level "Whether it be romantically or not, I honestly don't know. But being next to her just feels right."
    d grin "Do I wish we could be a couple? Yes. Do I wish we could at least go on a date? Yes. Do my arms hurt after spending a day together? Yes."
    d casual "But you know what? Anything's possible."
    d level blank "I'm not expecting her to just 'magically fall in love with me'..."
    d grin "...but I feel like, with enough time, things could just work out if all the pieces fall into place. I just need to be patient."
    d "Do you understand?"
    if persistent.choices["10"] == 1:
        jump iguess
    elif persistent.choices["10"] == 2:
        jump notreally
    else:

        menu:
            d "Do you understand?{fast}"

            "I guess.":
                $ persistent.choices["10"] = 1
                jump iguess

            "Not really.":
                $ persistent.choices["10"] = 2
                jump notreally

    label iguess:
        a "I guess."
        d raised left "I know it's complicated, but a man can try, right?"
        a "Right..."
        jump finishclean_don

    label notreally:
        a "Not really."
        d level left blank "Hm..."

label finishclean_don:
    a "Anyway, what do you say we finish unpacking my room?"
    d straight casual grin "Good idea."
    hide don with dissolve
    pause 0.1
    "We had been doing a little bit of unpacking while we talked, but now that we were back to silence, we were able to get everything done quicker."
    "After we were done, we fist-bumped and walked downstairs."
    scene bg living_s_m with dissolve
    pause 0.1
    show ginger a2 casual straight blank at tworight
    show chris b1 straight casual blank at twoleft
    with dissolve
    pause 0.1
    a "My room's all done!"
    g level "Did you ACTUALLY put everything where it belongs, or did you just toss it somewhere out of sight?"
    show chris at threeleft
    show ginger at middle
    show don a1 straight raised grin at threeright
    with easeinright
    pause 0.1
    d "Everything's where it's supposed to be, Mrs. Sprouse!"
    g raised grin "Is that so?{w} Well, then I guess I'll believe you."
    a "Am I really that untrustworthy that you're going to believe the guy you haven't seen in 5 years over the guy you've known for 16 years?"
    g level "Indeed, I HAVE known you for 16 years. And because I have, I know how much of a lazy bum you can be."
    a "Eh. I suppose that's fair enough."
    scene bg living_s_m with dissolve
    pause 0.1

label dadcomeshome:
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    play sound door_open
    "It was then when the front door opened up."
    "We turned to see a face familiar to all but one of us in the room."
    show fred a1 straight glasses grin casual at middle with dissolve
    pause 0.1
    f "I'm home!"
    show fred at twoleft
    show ginger a2 straight sad grin at tworight
    with easeinright
    pause 0.1
    g "I can see that!"
    g "How was work?"
    f level "Same old, same old."
    show fred at middle
    show ginger at threeright
    show don a1 straight casual smile at threeleft
    with easeinleft
    pause 0.1
    d "Hey, Mr. Sprouse!"
    f sad "Donald! Nice to see you again."
    f raised "And who's this?"
    hide ginger with easeoutright
    show chris b2 straight casual grin at threeright with easeinright
    pause 0.1
    c "I'm Christeena Truman. That's Christeena with two 'e's."
    a "Sheesh. That's basically a routine at this point, isn't it?"
    $ c_blink = False
    c b1 closed_happy smile sad "Basically."
    f level "Well, it's nice to meet you, Christeena. I'm Fred, Alex's dad."
    $ c_blink = True
    c b2 straight casual grin "Nice to meet you, too."
    c smile "And might I say that it's kinda cool to see parents like you."
    f casual blank "{i}'Parents like me?'{/i}"
    c grin "Yeah! Parents who had kids at an older age!"
    show don blank small
    "Donald and I widened our eyes as we looked at each other."
    c b1 "How old were you when you had Alex, anyway? 35?"
    f mad "24."
    c small sad dot "...!"
    $ c_blush = True
    c b2 straight blank "U-Um..."
    "Well, this introduction went from good to awkward very quickly."
    if C_Points == 3:
        jump defendchris
    elif C_Points == 2 or C_Points == 1:
        jump teasechris
    else:
        jump donothing

label defendchris:
    "I guess it's up to me to get her out of this mess before it escalates."
    a "Dad, it's okay. She wasn't trying to be offensive."
    show don straight
    show fred casual
    $ c_blush = False
    show chris b1 straight casual blank at threeright
    "All eyes were on me as the silence was broken."
    a "She's a really nice girl, I promise."
    d raised smile "Yeah, what he said! Chris is one of the sweetest people I've ever met!"
    $ c_blush = True
    c left sad grin "G-Guys...!"
    "She's speechless once again, only this time from flattery and not embarrassment."
    "Fortunately, my dad seems to believe us; his smile returned and he gave a small chuckle."
    f level grin "Heh. Well, I suppose I can't blame her for thinking what she did."
    "As he said this, he rubbed his hand through his silver hair."
    f mad "It's been this color ever since I put this thing on."
    "He then pointed to his wedding ring, an action that made my mom roll her eyes with a smile as she shook her head."
    jump grayhair

label teasechris:
    "Maybe I can lighten the mood with some playful banter."
    a "C'mon, Chris! If you were gonna guess a high number, at least guess a HIGH number, like 70 or something!"
    $ c_blush = False
    show chris b2 blank straight casual at threeright
    show don straight
    c "Eh?"
    a "That's what you were trying to do, right? Guess a ridiculously high number that couldn't possibly be the correct age?"
    d raised smile "Yeah, that's what I thought you were doin', too! Trying to tease Mr. Sprouse about his hair color?"
    "Thankfully, it looks like Donald caught on to what I was doing. It didn't seem to take long for Christeena to do the same."
    c b1 sad grin "R-Right! That's what I was doing!"
    "Dad was looking at all three of us with suspicious looks, but a smile soon grew on his face."
    f level grin "Well, if that's the case, then it's nice to see someone who's willing to be funny in an introduction."
    $c_blink = False
    c closed_happy sad smile "Yes, sir! That's all I was trying to do! Be funny! I didn't think you'd be so insulted by it, though."
    jump grayhair

label donothing:
    "Honestly, I'm not sure what to do in this situation..."
    "I don't wanna look like the bad guy for just standing here while Christeena feels embarrassed, but I'm at a loss on what to do or say."
    "Fortunately, Donald came to the rescue to get us out of this."
    d straight raised smile "Hey, don't worry about it, Mr. Sprouse; Christeena wasn't trying to be offensive."
    d grin "She's a really nice girl, though she can be a bit awkward around new people."
    c b1 left sad blank "..."
    "Though it looks like it's not working as well as it probably could be."
    "Still, Dad nods his head and smiles at Christeena."
    f level grin "I see."
    $ c_blush = False
    show chris straight b1 sad blank at threeright
    c "I-I really wasn't trying to..."
    f sad "It's alright, I assure you. I'm just a little self-conscious about my hair."

label grayhair:
    "Honestly, as far back as I can remember, my dad's hair has been gray, although family photos reveal that he did, at one point, have black hair."
    "I don't know if it's genetics or not that caused it, but if that's the case, then I better enjoy my blondness while I still can."
    $ c_blink = True
    $ c_blush = True
    hide don
    show chris b2 straight sad grin at tworight
    show fred at twoleft
    with easeoutleft
    pause .1
    c "A-Anyway, sorry about that."
    f casual grin "Apology accepted, then!"
    show fred at threeleft
    show chris at middle
    show ginger a2 straight sad grin at threeright
    with easeinright
    pause 0.1
    g "Anyway, I was about to start making supper, so you can get some rest if you need it, Fred."
    f raised "You know, I may just take you up on that offer."
    "My parents gave each other a quick kiss before Dad went upstairs."
    show fred:
        ease 1.0 offscreenleft
    pause 1.1
    hide fred
    "Now that I could see him walking, it was clear just how exhausted he was, based on his slow movement."
    show don a1 grin straight casual at threeleft with easeinleft
    pause .1
    g casual "Donald, Christeena, would you like to stay for dinner? Consider it a thank you for helping today."
    d smile "I don't see why not; I don't think my parents will mind."
    $ c_blush = False
    c blank straight sad b1 "A-Are you sure it won't be a problem, Mrs. Sprouse?"
    g sad "As long as your parents are okay with it, it won't be!"
    c grin "Well...{w=0.5} Then I guess I can stay."
    a "Hey, Donald did promise you that he'd bring you here to hang out, right? Let's consider this that time!"
    d raised grin "That's a fair point!"
    g casual "Food'll be ready in a couple hours."
    "I gave Mom a thumbs-up, and she went into the kitchen. I would've offered to help, but that would make me a bad host."
    hide ginger with easeoutright
    with pause 0.5
    show don:
        ease 0.5 close_left_d
    show chris:
        ease 0.5 close_right_c
    pause 0.6
    d casual "So, what do you guys wanna do?"
    c left mad blank "I don't know about you, but after all that unpacking, I just wanna sit down and relax."
    a "Nothing wrong with that; we could use a breather."
    a "How about we watch something on TV? I'm sure there must be something on that we all like."
    $ d_blink = False
    d sad closed smile "I'm game."
    c b2 straight casual grin "Sounds good to me!"
    $ current_track = "None"
    stop music fadeout 0.6
    hide don
    hide chris
    with dissolve
    pause 0.1
    $d_blink = True
    nvl clear
    window hide dissolve
    nvl show dissolve
    $ current_track = "\"Chillaxin'\""
    play music chillaxin
    narrate """
    With that, we all sat on the couch and I turned on the TV.

    We eventually settled on an old movie from the early 2000s that was pretty cheesy, but so nostalgic that we couldn't help but love it.

    As promised, dinner was ready in a couple hours. Tonight, it was meatloaf.

    I had texted Brittney and asked if she wanted to join us, even making it clear that her sister and other next-door neighbor were here, but she politely declined.

    {clear}

    It was a little weird sitting around the table with 2 extra people sitting in chairs that didn't match the other 4, but oh well.

    As per usual, Donald was talkative, making most of the dinner conversation between him and my parents.

    Personally, I didn't mind; I'm not the kind of guy who likes to talk while eating a meal.

    Occasionally, he would get me, Christeena, and/or Harry to contribute a bit, but we were silent for the most part.

    Although, at one point, Christeena did ask my dad where he worked.

    He explained that he worked with Mr. Waters at the grain elevators in town. It was busy and tiring, but the pay was decent enough.

    I hadn't really spent much time outside of Chicago before moving to Smalltown, but from what I could see, agriculture and farming are big in the rest of the state.

    It really does continue to amaze me how that one city is so unlike the rest of Illinois.
    """
    nvl clear
    nvl hide dissolve
    window show dissolve
    "Eventually, dinner was done, and it was time for Christeena and Donald to head home."
    show don a1 grin casual straight at twoleft
    show chris b1 straight grin casual at tworight
    with dissolve
    pause 0.1
    a "Well, it was nice to have you guys over. Thanks again for helping with the unpacking!"
    $ d_blink = False
    d closed sad smile "Glad we could be of service!"
    $ d_blink = True
    d right grin level "Even if some of us were not on board at first..."
    c b1 left grin mad "Yeah, yeah..."
    c b2 straight casual "Still, it was pretty cool to meet your family. They seem like nice people."
    a "Indeed, they do."
    c b2 level blank "..."
    a "..."
    a "Anyway, it's a shame that Brittney couldn't at least be here for dinner. Maybe next time?"
    c b1 left grin "Maybe... Depends on if she's in the mood for something like that."
    d straight "Yeah, I don't know if you've noticed, but Brittney isn't exactly as social and outgoing as she seems."
    d "There are times like tonight where she just wants to spend some time alone."
    "I suppose that would explain her behavior that day when Harry and I were at Kelly's...{w=1}{nw}"
    if delihangout:
        extend " Did I really make the right decision by going against her request to eat alone...?"
    else:
        extend " Did I really make the right decision by allowing her to eat alone...?"
    d sad "Anyway, it's getting late; we should really get going."
    c straight grin "Alright, then..."
    a "See you guys later!"
    d raised smile "Later, Man!"
    c casual "Bye, Alex!"
    $ current_track = "None"
    stop music fadeout(2)
    hide don
    hide chris
    with easeoutleft
    pause 0.5
    play sound door_open
    "My friends and neighbors exited my home, and I closed the door behind them."
    $ current_track = "\"Home Life\""
    play music home_life
    "Stretching and yawning, I walked upstairs to my room."
    pause 0.5
    scene bg bedroom_a_m with dissolve
    pause 0.5
    "Lying down in bed, I looked around and smiled."
    "[cleaningpartner] and I did a good job getting my room unpacked and cleaned up, though it's a shame that I know it won't stay this clean forever."
    "Oh, well."
    "I spent the rest of my evening scrolling though funny Internet posts until I got ready for bed."
    "I'd call today a success; the house is unpacked, I got to hang out with friends in my own home, and my parents, at the very least, don't hate Christeena."
    "There's only one way this could've been better:{w} if we had eaten baked spaghetti instead of meatloaf."
    $ replay = False
    $ daydesc = 0
    $ renpy.end_replay()
label progressday04:
    $ progress += 1
    jump progress
