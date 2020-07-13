label shoppingwithharry:
    python:
        B_Name = "Brittney"
        C_Name = "Christeena"
        E_Name = "???"
        b_hat = 0
        b_hairtie = renpy.random.randint(0, 2)
        outfit_b = "a"
    show text "{size=+50}June, 2013{/size}":
        xalign 0.5 yalign 0.05
    show screen calendarOs
    show calendar june june_11:
        xalign 0.5 yalign 0.6
    show calendar_circle:
        xalign 0.435 yalign 0.53
    with dissolve
    if replay == False:
        $ persistent.todays_date = "June 11th, 2013"
        $ renpy.notify("Game saved!")
        $ renpy.save("1-1")
    pause 4
    hide text
    hide screen calendarOs
    hide calendar
    hide calendar_circle
    with dissolve
    pause 1
    scene bg bedroom_a_m with dissolve
    $ current_track = "\"Home Life\""
    play music home_life
    nvl show dissolve
    $ renpy.block_rollback()
    narrate "Despite my first couple days living here, my first full week has been pretty standard."
    narrate "It mostly consisted of unboxing; Mom said she was lenient for the first few days, but now I really had to put some work into straightening up my room."
    narrate "Though I'm not a prisoner or anything; if I get enough work done, she rewards me with some time to hang out with the guys."
    narrate "It's weird. Donald, Christeena, Brittney and I always seem to be in a group of some sort; it's either all of us, three of us, or none of us."
    narrate "I mean, yeah, I spent some one-on-one time with Donald when I first moved, and there was that brief moment when I met Christeena, but for the most part, we're all together."
    narrate "I wonder if I'll ever get the opportunity to hang out with just one of them, though. Just us two..."
    nvl clear
    g_o "Alex?"
    "I'm awoken from my daydream by the familiar call of Ginger Sprouse."
    a "Yeah?"
    g_o "Can you come here for a second?"
    "Uh-oh.{w=0.5} That's mother-speak for {i}'You're in big trouble, young man!'{/i}"
    "Regardless, I followed orders and went downstairs to the living room."
    scene bg living_s_m with dissolve
    pause 0.1
    show ginger p2 straight casual grin at close_c with dissolve
    pause 0.1
    "When I got downstairs, I saw Mom looking at me with a smile."
    "On the bright side, that's a sign that she wasn't angry at me.{w} On the dark side, that's a sign that she wants me to do a favor that I probably won't enjoy."
    a "What's up?"
    g level "Here."
    "She then proceeds to hand me a $100 bill."
    "I don't take it right away, though; I sense something isn't right here."
    a "What's this for?"
    g sad "I need you to head into town and grab some groceries."
    "I knew it was too good to be true."
    g "I'll text you the list of everything I need. I did the math and that hundred bucks should be more than enough to pay for everything."
    g casual "And that remaining money you can spend on yourself."
    a "Seriously??"
    g grin "Seriously. Consider it a bonus for working so hard to unbox everything."
    "Huh.{w} Perhaps it wasn't too good to be true, after all."
    show ginger blank
    h_o "Hey!!"
    show ginger at close_left_c
    show harry p1 small mad scream at tworight
    with easeinright
    pause 0.1
    "It didn't take long for my younger brother to rush in at the mention of spending money because of good behavior."
    h "I did a lot of unboxing, too! Why don't I get to buy something?"
    g grin "Perfect timing, Harry; I was just about to ask you if you wanted to go with your brother to help him."
    h straight blank "I'll go with, but only because I feel like I deserve a reward, too!"
    a "Everything's always gotta be fair with you, doesn't it?"
    h scream "Easy to say when you're the favorite!"
    g level blank "Now, Harry, you know that there is no 'favorite'; your father and I love you both very equally!"
    h blank level right "Whatever you say, Mom."
    g mad wide "Harold Michael Sprouse!"
    h sad small "*gulp*"
    h "S-sorry, Mom."
    g level grin "That's more like it.{w} Now, run along, boys, before it gets too dark!"
    a "Will do."
    scene bg living_s_m with dissolve
    pause 0.1
    window show
    "I took the $100 bill from Mom and put it safely in my wallet.{w} She also handed me the keys to the minivan, making me swear to drive carefully."
    "I understand her worry, but I don't think they give driver's licenses to people who don't know how to drive."
    "Granted, I've only had my license for around a month, but if I can survive driving in Chicago, I can survive Smalltown."
    "Regardless, I promised to drive safely, if for no other reason than to appease her.{w} She looked relieved enough."
    scene bg house_s with dissolve
    pause 0.1
    $ current_track = "\"Outside the Street\""
    play music outside_the_street
    show harry p1 straight closed_smile casual at close_h with dissolve
    pause 0.1
    h "I call shotgun!"
    a "Darn, and here I was hoping I could get shotgun so YOU could drive, instead!"
    h grin raised "Hey, I'm a better driver than you are!"
    a "As much as I'd love to test that claim, Mom would kill us both if I let that happen."
    h level "You're no fun."
    a "I'm fun, just not around you."
    h raised closed_smile "Whatever."
    hide harry with dissolve
    pause 0.1
    "Harry then ran towards the passenger door, opening it up and hopping inside."
    "I was about to enter the driver's door before someone caught my attention."
    unknown "Good afternoon, Alexander!"
    "I turned around towards the other side of the street, where I could see the source."
    "It was Mr. Rodriguez waving at me from his front lawn."
    a "Hi, Mr. Rodriguez!"
    "I called back with a quick wave."
    "He gave a quick nod of acknowledgment before pushing his lawnmower into his garage."
    "He had been mowing for about a half hour now. At least, that's when I started hearing the mower run."
    "Yeah, yeah. A Mexican mowing a lawn. I wish I was making this up."
    "Jokes aside, he's actually pretty cool. All the Rodriguezes are."
    "They came over and introduced themselves a few days after we moved in. Brittney was right: their Mexican accents are next to nonexistent!"
    "She was also right when she said that Mrs. Rodriguez's cookies were amazing; she had brought a tray of them over as a housewarming gift."
    "They were snickerdoodles, aka the best cookies to have ever been created, period!"
    "And Daniel was pretty cool, too. As advertised, energetic, but not annoying."
    "He and Harry seemed to get along pretty well. Granted, they're only 3 years apart, but it's still cool to see Harry making a new friend like I did."
    play sound van_start
    "Anyway, I then got into the van, started it up, and went on my way to the grocery store."
    scene bg dolmart_e with dissolve
    pause 0.1
    "While Smalltown did have a grocery store, it didn't really have anything big with everything we needed."
    "So, we had to resort to the next town over, Trenburg, which was slightly bigger than Smalltown, but not too far away to where it felt like a trek."
    "It was certainly a lot closer than Chicago, that's for sure."
    "Anyway, they had a Dolmart there that basically sold anything on God's Green Earth, and that's where Harry and I found ourselves."
    show harry p1 straight casual blank at close_h with dissolve
    pause 0.1
    a "Now, remember, we have to get everything on the list, THEN we can buy the stuff for us, so I don't wanna see you run straight to the videogame aisle."
    h mad "I know that!"
    a "I can never tell with you."
    h right "Hmph."
    hide harry with dissolve
    pause 0.5
    play loop dolmart fadein(0.5)
    scene bg dolmart_i with dissolve
    pause 0.1
    "It seemed like a pretty busy day, judging by the amount of people in the store."
    "I had only been in this building once before now, so I wasn't fully lost, but I certainly didn't remember where everything was."
    "Still, all the groceries seemed to be on one side of the store, aka the side we were in, so there's a start."
    "Harry grabbed an empty cart and rushed over next to me."
    show harry p1 straight casual blank at close_h with easeinleft
    pause 0.1
    h "So, what's on the list?"
    a "Let's see..."
    "I pulled out my phone and looked at the text Mom had sent."
    a "First, there's '2 packages of chicken breasts'."
    h mad closed_smile "Heh."
    a "You're so dirty-minded."
    h raised grin "And yet you knew what I was laughing at."
    a "Let's just go get it."
    hide harry with dissolve
    pause 0.1
    "We walked over to the meats section. It wasn't hard to miss, since it seemed to take up a good portion of the far wall."
    "I couldn't believe just how many different kinds of meat there were. Things like ground beef and chicken legs make sense..."
    "...but pig hooves and chicken paws? People really eat those? Is there really enough meat on those things that you can eat??"
    "Ah, whatever. For now, I just grabbed two packages of the chicken and threw them into our cart."
    show harry p1 straight casual blank at close_h with dissolve
    pause 0.1
    h "Okay. Now what?"
    a "Next up is Alfredo sauce."
    h sad closed_smile "Yes! That means we're having chicken Alfredo!"
    a "Gee, what could've possibly tipped you off?"
    h mad blank "Jerk."
    a "What'd I do?"
    h raised "Treat me like an idiot."
    a "It's called sarcasm, Harold. Look it up."
    h level right "Whatever. Let's just go."
    hide harry with easeoutright
    pause 0.1
    "Harry then grabbed the cart and bolted towards the next aisle."
    a "Harry, watch where you're--!"
    $ current_track = "None"
    stop music
    stop loop
    play sound shopping_cart
    "But it was too late; Harry ran the cart right into someone."
    e_o "{b}{i}OWW!{/i}{/b}"
    show elie p1 straight mad blank at middle with dissolve
    pause 0.1
    $ current_track = "\"Chaotic Evil\""
    play music chaotic_evil
    "It was a young woman that looked around her early twenties, and her expression was rightfully a furious one."
    show harry p1 small sad scream at twoleft
    show elie at tworight
    with easeinleft
    pause 0.1
    h "I'm so sorry!"
    e scream "Oh, yeah, that totally makes my legs stop hurting, dickhead!"
    a "Hey! Calm down! It was an accident!"
    e straight frown "Whatever! Just watch where the fuck you're going!"
    $ E_Name = "Eleanor"
    hide elie with easeoutleft
    $ current_track = "None"
    stop music fadeout 3.0
    pause 1
    "She stormed off before we could say anything else."
    "The people around us were staring at her, and then us. A few seconds later, they just went back to doing what they were doing."
    "We're fine, really. Thanks, everyone."
    show harry straight blank:
        ease 0.5 close_h
    pause 0.6
    h_s "..."
    a "You okay?"
    h right "...let's just go get the sauce."
    "His tone was soft. I could barely make out what he said."
    a "Alright. It should be right over here."
    a "And hey...{w} don't let her bother you. She just overreacted."
    h_s "..."
    a "Besides, what are the odds of seeing her ever again?"
    h_s "..."
    a "*sigh*"
    "I guess there isn't really anything I could say to cheer him up at the moment, but I'm sure he'll get over it pretty quickly."
    window hide dissolve
    scene bg fade with wipeleft
    pause 1
    scene bg dolmart_i with wipeleft
    $ current_track = "\"Outside the Street\""
    play music outside_the_street
    play loop dolmart
    window show dissolve
    a "Okay, we've got the chicken, the Alfredo sauce, the cheese, the noodles, the pesto, and the milk.{w} I believe that's everything."
    show harry p1 straight raised blank at close_h with dissolve
    pause 0.1
    h "I'd hope so; you're the one with the list."
    a "So, I suppose now that we have that out of the way, it's time to decide what to do with the rest of the money."
    h mad closed_smile "Ah, the moment we've all been waiting for!"
    a "Any suggestions?"
    h raised grin "We could always check out the video games!"
    a "You're too predictable."
    h level blank "What, do you have a better idea?"
    a "Well...{w} We could always... {w}Uh..."
    h grin "Yeah, that's what I thought."
    a "Fine. We'll do it your way."
    h closed_smile sad "Yay!"
    hide harry with dissolve
    pause 0.1
    "Harry then pushed the cart of groceries towards the other side of the store, making sure to go slowly and carefully."
    "Even though he seemed to be in a better mood, he still had that bitchy woman on his mind, and I can't really fault him for that."
    "Regardless, we made it to the electronics section with no issues. The game cabinet had quite a large selection, I must admit."
    show harry p1 straight casual blank at close_h with dissolve
    pause .1
    h "How much money do we have left to spend?"
    a "Taking tax into consideration, I'd say maybe...{w=0.5}$45?"
    h sad right "Aww...that's not enough for a VexBox game..."
    a "What a shame.{w} Though that's still enough for a TS game."
    h straight mad "When was the last time you saw me play my TS?"
    a "I was just offering a suggestion."
    h level left "Hm..."
    h casual "Hey! Didn't you used to play these games?"
    "I looked at the game he was pointing at."
    "{i}Doctor Letton and the Magic Mask.{/i}"
    a "Oh, yeah! I had completely forgotten that the new one was out!"
    h straight grin "So, let's buy it!"
    a "Well, we might not be able to afford two games. You sure you wanna buy a game just for me?"
    h raised blank "Who said it was just for you? Maybe I wanna play, too."
    a "Since when have you had an interest in Doctor Letton?"
    a "Also, you yourself just said you don't even play on your TS anymore!"
    h sad small "Uh..."
    h straight mad scream "The point is Mom said we could spend the money on anything we wanted, so I wanna spend it on this!"
    a "Well, alright, then. Just know that you're going to have to play all the other games, first, before this one."
    h level grin "I'm fine with that."
    a "Well, alrighty then!"
    hide harry with dissolve
    pause 0.1
    "We tracked down a Dolmart employee who managed to get the game out of the case."
    "After we checked out and bought both the game and groceries, not adding anything else to the list, our leftover amount was around $20."
    stop loop fadeout 0.5
    scene bg dolmart_e with dissolve
    show harry p1 straight casual blank at close_h with dissolve
    pause 0.1
    h "So, now what?"
    a "Well, Mom didn't say we had to spend ALL the money, so we could always just head home and give her the rest."
    play sound stomach
    show harry sad small
    "That's when I heard a loud rumbling from Harry's stomach area."
    a "...or, we could grab some food."
    h straight casual "From where?"
    a "I know a place back in Smalltown. You'll like it."
    h level "I better..."
    a "If nothing else, you'll love the owner."
    window hide dissolve
    scene bg fade with wipeleft
    scene bg deli_i_e
    show deli_entrance_sign zorder 2
    with wipeleft
    play sound deli_door
    play loop deli_crowd
    $ current_track = "\"Dinin' In\""
    play music dinin_in
    window show dissolve
    "By the time we arrived at Kelly's, the lunch rush was almost over."
    "That said, it was still a bit crowded, but we managed to get the greeter's attention pretty quickly."
    gr "Table for two?"
    a "Yes, Ma'am."
    gr "I'll let you know when a table is available. Please wait here patiently."
    a "No problem."
    "She gave a relieved smile and nod as she walked away to the main dining area."
    show harry p1 straight level dot at close_h with dissolve
    pause 0.1
    h "Wow. It's really busy in here."
    a "Indeed. It's nothing like when I first came here a week ago with Donald and the girls."
    a "Though, it's only my third time here, so who am I to know how busy this place normally gets?"
    show harry casual left blank
    unknown "Excuse me, waitress!"
    hide harry with dissolve
    pause 0.1
    "Harry and I turned towards a table nearby, where we could see a middle-aged woman holding her hand in the air, looking at a waitress passing by."
    show kelly p2 straight casual blank at k_middle with dissolve
    pause 0.1
    k "Can I help you?"
    wo "Yes, I just want to say that you've passed by my table twice now and haven't refilled my drink, even though my glass is clearly empty."
    k sad "I'm sorry, Ma'am; it's really busy, and we've all got our minds in several places at once."
    wo "I don't care. If I come to a restaurant, I expect good service."
    k mad "Well, when I come into work, I expect all of the customers to be kind, patient, and understanding, yet I always seem to get the selfish bitches like you."
    "The woman was flabbergasted, to say the least, though that look of shock was quickly replaced by a look of anger."
    wo "Is there a manager here? I'd very much like to speak to them."
    k raised grin "Certainly. Just give me a second."
    show kelly at k_threeright with easeinleft
    "The waitress then started walking towards the kitchen area. {w}Halfway there, though, she did an exaggerated 180 turn and walked back to the table, putting on an innocent yet cunning smile."
    show kelly casual p1 at k_middle with easeinright
    k "Hi! I'm Kelly, the manager of Kelly's Deli. I heard you wanted to speak with me?"
    $ K_Name = "Kelly"
    "The woman just glared at her face for a second before shifting her eyes to her name tag."
    "Sure enough, it clearly read 'Kelly, Manager'."
    k raised "Something about how you're unsatisfied with your service?"
    "The woman continued to stare at Kelly, though her anger was clearly growing."
    wo "If this is how you run your restaurant, then I'm leaving and never coming back!"
    k level blank "Aw, what a shame."
    "Her sarcasm was so strong, it could beat Dwayne Johnson in arm wrestling."
    "Nevertheless, the woman stormed up from her seat and exited the building, nearly bumping into Harry and I in the process."
    show kelly mad grin
    "As soon as she did, though, Kelly started laughing her ass off."
    k "Good riddance!"
    a "Nice one, Kelly!"
    show kelly casual blank
    "She turned towards me in confusion, but it didn't take long for her to recognize me."
    k grin "Oh, hey! You're Donald's friend, right?"
    extend raised " Alan, is it?"
    a "Alex."
    k sad "Alex! Right!"
    k casual "And who's this with you?"
    a "This is my brother, Harry. Thought I'd treat him to lunch."
    k "Well, it's certainly nice to make your acquaintance, Harry."
    show kelly at k_twoleft
    show harry p1 straight mad closed_smile at tworight
    with easeinright
    pause 0.1
    h "Do you always treat rude customers like that?"
    k level "Not always. {w}Well, let me rephrase that: I'm not always that kind to them."
    k sad "Honestly, with as many times as I've hinted at owning a shotgun, it's a miracle I haven't been sued or arrested!"
    h sad "Seriously?? That's crazy!"
    k mad "Not from where I'm from, Sonny."
    k raised "Anyway..."
    "She then glanced over at the table the angry woman was just sitting at."
    k "...it looks like a table just opened up. Would you boys like a seat?"
    a "Yes, please."
    hide harry
    hide kelly
    with dissolve
    pause .1
    scene bg deli_i_wb
    show deli_table zorder 2
    with dissolve
    pause 0.1
    "Kelly quickly cleaned up the table, clearly not bothered by the obvious dine-and-dash that had occurred, and handed us our menus."
    "She said that the deli was a little understaffed today, so service might not be fast.{w} Harry and I both told her that there was no problem."
    "She gave us a thumbs-up and told us to call her over when we're ready to order."
    show harry p1 straight closed_smile sad at middle zorder 1 with dissolve
    pause 0.1
    h "Man, that woman is awesome!"
    a "I told you you'd love the owner."
    "I had the pleasure of meeting Kelly a few days ago, when Donald, Christeena, and I all came here for lunch (Brittney was at work)."
    "She's certainly a character, but you can tell that she loves both her career in food and showing how little she'll be pushed around."
    h raised grin "I gotta ask: is her accent real?"
    a "It would take a lot of dedication to constantly fake a southern accent like that. But judging by her attitude, I don't doubt her southernness."
    a "Anyway, we should probably order something."
    h level blank "Hmm..."
    "Harry looked at the menu, nothing seeming to catch his attention."
    h "I don't know. What do you usually get?"
    a "Well, I got [delifoodorder] the first time I was here, but I tried a Swiss Miss last time, since Brittney and Donald made such a big deal about it."
    a "Honestly, it's all amazing food, so I'd say just go with whatever sounds the most appetizing."
    "I somehow don't feel like that response helped him figure out what to eat, but he looked back at the menu."
    h casual grin "I guess I'll go for the Ham and Cheddar thing. It sounds good."
    if acceptsandwich:
        a "Yeah, it is pretty good; Christeena let me try a bite of hers."
        a "Though I should warn you that it's going to be HOT."
        h raised closed_smile "I think I can handle it."
        a "If you say so, buddy."
    else:
        a "Yeah, that's what Christeena usually gets."
        a "If she gets it a lot, then it must be pretty good, right?"
        h raised blank "I guess so."
    hide harry with dissolve
    pause 0.1
    "I got Kelly's attention, and she took our orders."
    "It was a tough choice, but I decided on the Tuna Melt; it was different, and my curiosity was tingling."
    "She let us know that our sandwiches and soda would be out soon, to which we thanked her and she was on her way."
    "After a few minutes of silence between Harry and I, I spoke up, trying to make conversation."
    show harry p1 straight casual blank at middle with dissolve
    pause 0.1
    a "So, Harry, what do you think of Smalltown so far?"
    h level right "Eh. It's not as bad as I thought it would be."
    a "Well, that's good to hear. I'm glad we moved here in the beginning of summer and not right before school started or something."
    h raised grin straight "Yeah, no kidding!"
    extend mad blank " Though it sucks that we have to spend part of our summer unboxing everything."
    a "Fair enough. But it's still better than unboxing when you also have homework to do."
    h small frown "Ugh. Don't even remind me that homework exists."
    a "Heh. You sound just like Brittney."
    h casual straight blank "You sure do talk about those girls a lot."
    a "I do not."
    h raised "Yeah, you kinda do."
    a "Well, maybe because they're so cool."
    h level grin "What kind of cool people would hang out with you?"
    a "Well, that just stings, Harold. Just for that, I won't let you play that Doctor Letton game we bought."
    h mad small scream "Hey!! That game belongs to both of us!!"
    a "Not anymore."
    h straight frown "Jerk!"
    a "Apologize, and I may reconsider it."
    h_s blank ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
    h right level "...{fast}whatever. It's just a dumb game, anyway."
    "Wow. Now THAT'S hurtful."
    a "Well, I still think you should be properly introduced to the girls."
    h raised straight "Why?"
    a "Don't you wanna see why I like them so much?"
    h level grin "Isn't it because they're the first girls that want to be around you?"
    a "Ah, screw you. I'd like them even if they were both dudes."
    h casual "Oh, so you're gay now?"
    a "I- NO!! You know what I mean!"
    h level closed_smile "Do I?"
    "I was about to make a rebuttal, but I was spared by Kelly coming over with our order."
    show bg deli_i_wb:
        ease 0.5 xalign 1.0
    show deli_table:
        ease 0.5 xalign 1.0
    show harry:
        ease 0.5 twoleft
    show kelly p2 casual straight grin at k_threeright with easeinright
    pause 0.1
    k "Here you boys are!"
    a "That was quicker than I expected."
    k raised "What can I say? My cooks know how to handle busy days."
    k sad "Let me know what you think of the food, will ya, Larry?"
    h level blank "Harry."
    k level "Right. I knew that."
    show bg deli_i_wb:
        ease 0.5 xalign 0.0
    show deli_table:
        ease 0.5 xalign 0.0
    show harry:
        ease 0.5 middle
    hide kelly with easeoutright
    pause 0.1
    "And with that, she rushed over to the booth next to ours."
    h raised "She's not good with names, is she?"
    a "Well, she's only barely met us, plus she's clearly having a busy day."
    a "Anyway, let's eat up!"
    h mad "Hold it!"
    a "What?"
    h "We have to pray, first."
    a "Oh.{w=.5} Right.{w=.5} My bad."
    hide harry with dissolve
    pause 0.1
    "Harry folded his hands together, bowed his head, and closed his eyes, with me following suit."
    scene bg fade with dissolve
    pause 0.1
    h_o "Dear, Jesus, we thank you for this food, and we ask that you bless it to our bodies. Amen."
    a "Amen."
    scene bg deli_i_wb
    show deli_table zorder 2
    show harry p1 straight casual grin at middle zorder 1
    with dissolve
    pause 0.1
    h "There! NOW we can eat!"
    a "If you say so!"
    "I took a bite out of my tuna melt. I gotta say, it wasn't what I was expecting, but it was still very good!"
    "I don't know how everything in this deli tastes like it was touched by the hand of God, but it truly is incredible."
    h sad small scream "AHHH!!!"
    "Harry spat his bite onto his plate."
    if acceptsandwich:
        a "I told you it was hot!"
        h straight mad blank "I know, I know!"
    else:
        a "What's wrong?"
        h straight mad blank "It's hot!!"
    "He then blew on the sandwich, trying to cool it down."
    a "Glad I got a cold sandwich today, then!"
    "Harry took a large gulp of his Hilly Dew with a glare on his face."
    hide harry with dissolve
    pause 0.1
    "By the time his sandwich cooled down enough to be safely consumed, I was almost done with mine."
    "We didn't talk much while we ate, just the occasional 'Wow, this is good!' or asking Kelly for drink refills."
    "Though based on the expressions on Harry's face, he certainly seemed to enjoy his meal, as predicted."
    "This was confirmed when Kelly stopped by after we had eaten."
    show bg deli_i_wb:
        ease 0.5 xalign 1.0
    show deli_table:
        ease 0.5 xalign 1.0
    pause 0.6
    show harry p1 straight casual grin at twoleft
    show kelly p1 straight raised grin at k_threeright
    with dissolve
    pause 0.1
    k "Well?"
    h closed_smile "It was delicious!"
    k sad "Glad to hear!"
    k level "You boys take care, now. Y'hear?"
    a "We hear."
    "I paid for the meal and used the remaining money as a tip. With that, we were off."
    stop loop fadeout 0.5
    scene bg deli_e with dissolve
    $ current_track = "\"Outside the Street\""
    play music outside_the_street
    show harry p1 straight raised grin at close_h with dissolve
    pause .1
    h "Okay, I'll admit it: that was pretty good."
    a "What's this? Harold Sprouse admitting that I'm right? Next you'll tell me that Satan had a snow day!"
    h level blank "Jerk."
    a "I'm your big brother. I'm supposed to be a jerk."
    $ B_Name = "???"
    b_o "Is that so?"
    show harry casual
    "I jumped what felt like a mile in the air as that voice spoke from right by my ear! I turned around and found the source."
    $b_blink = False
    hide harry with easeoutright
    show brit p1 closed opened_smile sad at close_b with easeinleft
    pause .1
    $ B_Name = "Brittney"
    b "Hehehe! Did I scare you?"
    "Now that my heart rate was slowly going back to normal, I cracked a joking grin."
    a "Nah, I just felt like jumping and screaming."
    $b_blink = True
    b p2 left derp level "Darn. I'll just have to try harder next time."
    a "Anyway, what are you doing here?"
    b p1 straight casual grin "I just got done with work, so I thought I'd grab a quick bite."
    a "What, does sitting in a chair and blowing a whistle all day build up an appetite?"
    b p2 level "I'll remember that when you start drowning on my watch."
    a "Don't you mean 'if'?"
    $ b_partial = True
    b closed_smile mad "I know what I said."
    $ b_partial = False
    show brit p2 right casual grin
    b "Oh, hey! Who's this?"
    show brit at close_left_b
    show harry p1 straight blank casual at tworight
    with easeinright
    pause 0.1
    "Oh, yeah; Harry's here."
    show brit:
        ease 0.5 twoleft
    pause .6
    a "This is Harry, my brother. Harry, this is Brittney, our next-door neighbor."
    b straight p1 opened_smile "Nice to meet ya!"
    h raised left grin "Yeah, same here, with as much as Alex talks about you!"
    b p2 straight raised grin "Is that so? What does he say?"
    h straight closed_smile mad "He said that he thinks you're cute!"
    a "Hey!! I said no such thing!!"
    if britnotpretty:
        b level "Oh, I know you haven't, Alex. I believe the exact words you DID say were 'Brittney is not pretty'!"
        a "You're never going to let that go, are you?"
        $ b_partial = True
        b mad opened_smile "Nope."
        $ b_partial = False
    else:
        b p1 sad blank "Aww, so you don't think I'm cute?"
        a "Hey! I-I didn't say that, either!"
        b p2 raised grin "So you DO think I'm cute?"
        a "I...! {w}Ugh..."
        $b_blink = False
        b p2 sad closed opened_smile "Ehehe. Your face is so red right now!"
        a "*urk*"
        $b_blink = True
    show brit p1 straight casual grin
    b "Anyway, did you guys just finish eating?"
    a "Yep. Which sucks; if I had known you were coming, I would've made sure to meet you here at the same time."
    b p2 sad "Oh, that's okay, Alex. I'm fine with eating alone."
    a "You sure? I wouldn't mind hanging out with you so you don't feel lonely."
    h blank "But I wanna go home!"
    a "Harry, that's rude!"
    $ choicevbox = 5
    b p1 opened_smile "No, it's fine. You don't have to inconvenience yourselves on my account. I'll be fine."
    if persistent.choices["8"] == 1:
        "Hmm..."
        jump brithangout
    elif persistent.choices["8"] == 2:
        "Hmm..."
        jump leavebritalone
    else:

        menu:

            "Hmm..."

            "Hang out with Brittney.":
                $ persistent.choices["8"] = 1
                jump brithangout

            "Leave Brittney alone.":
                $ persistent.choices["8"] = 2
                jump leavebritalone

    label brithangout:
        $ B_Points += 1
        $ delihangout = True
        a "Okay, how's this: I'll drop Harry off at home, then head back to the deli?"
        b small level hanging "Alex, I just said-"
        a "Don't worry, it's not an inconvenience."
        hide screen skipchoice
        b p2 straight sad blank "I told you I'm fine eating alone."
        a "I know, but I still wanna hang out with you. Is that a problem?"
        b_s "..."
        b p1 level grin "I guess not."
        a "The deli's not too far from home, anyway. I'll be right back."
        b p2 raised "If you insist. But I'm not waiting until you get back to order."
        a "I'm not eating, anyway, so go for it."
        b "Alrighty, then!"
        scene bg deli_e with dissolve
        pause 0.1
        "Brittney then walked into the deli as Harry and I got back into the van."
        "After heading home and unloading the groceries into the house, I let Mom know that I was heading back out and drove back to the deli."
        scene bg deli_i_e
        show deli_entrance_sign zorder 2
        with dissolve
        play sound deli_door
        play loop deli_crowd
        $ current_track = "\"Dinin' In\""
        play music dinin_in
        "By the time I got back to Kelly's, Brittney was already eating her food. She waved at me as she saw me enter."
        "Waving back, I walked over to the booth she was sitting in."
        scene bg deli_i_wb
        show deli_table zorder 2
        with dissolve
        show brit p2 straight raised grin at middle zorder 1 with dissolve
        pause .1
        b "And here I thought you had changed your mind!"
        a "What do you take me for, a liar?"
        b left level huhu "Maybe not a 'liar'; more of a 'dum-dum'."
        a "Don't you know any insults other than that one?"
        b p1 straight raised opened_smile "Sure, but they're not as effective."
        a "If you say so, Miss Usher."
        $b_blink = False
        show brit p2 closed sad grin
        "She gave a small giggle before she took a sip of her water."
        a "So, can I ask why you always drink water with your meals?"
        $ b_blink = True
        $ b_partial = True
        b straight raised "What, do you have something against water?"
        a "No, I'm just curious."
        $ b_partial = False
        show brit straight level p1 grin
        b "Well, I'm not a fan of soda, to start with."
        a "Why?"
        b p2 right blank "I just don't like how unhealthy it is. The sugar, the caffeine, the who-knows-what..."
        b straight raised "I'm no health nut by any means, but I wanna make sure what I'm putting in my body doesn't hurt me, you know?"
        a "I guess so. Athletes certainly do like to pay attention to what's in their bodies, right?"
        b level grin "Right."
        b raised "And you can't get much healthier than water, can you?"
        a "I suppose not."
        b p1 casual "You know, you may wanna pay attention to what you're eating and drinking, yourself."
        a "What do you mean?"
        b p2 level "Well, not to be offensive, but you seem out of shape and unhealthy."
        a "Which part of that wasn't supposed to be offensive?"
        b p2 left huhu level "Well, okay, maybe I was being a little offensive, but my point still remains!"
        b p1 straight casual blank "I've seen how out of breath you get when you walk for a while. You get exhausted too quickly."
        b p2 sad "At the very least, you could try exercising a little bit to build your stamina up."
        a "Yeah, I'll consider that."
        b p1 raised opened_smile "Is that sarcasm I hear, Alexander?"
        a "Not at all, Brittney."
        b p2 left huhu level "If you say so."
        hide brit with dissolve
        pause 0.1
        "She then continued to eat her Turkey Takeover, leaving us both in silence for a little bit."
        "Kelly had come over to ask if I wanted anything, but I passed.{w} Even if I wanted something, I didn't have any money on me, anyway, and I wasn't going to make Brittney pay for me."
        "Brittney finally finished her food and looked at the time."
        show brit p1 straight casual grin at middle zorder 1 with dissolve
        pause 0.1
        b "It's getting pretty late. I better head home."
        a "Yeah, same here. Still, it was nice to hang out with you."
        b p2 raised "Even if most of it was just watching me eat?"
        a "Hey, even you can make that entertaining, Miss Messy-Eater."
        b p1 mad opened_smile "It was a couple drops of cheese on my pant leg!"
        a "Still a mess, albeit a small one."
        $ b_wink = True
        show brit p2 tongue
        "She stuck her tongue out at me and picked up the check."
        hide brit with dissolve
        pause 0.1
        $ b_wink = False
        "After that, we said our goodbyes and both headed back to Berry Street."
        stop loop fadeout(0.5)
        scene bg house_s with dissolve
        $ current_track = "\"Relaxation in the Country\""
        play music relaxation_in_the_country
        "Brit and I got home at around the same time. We waved to each other before entering our houses."
        jump meeteleanor

    label leavebritalone:
        $ delihangout = False
        a "Well, alright, if you insist. Have a good night, Brittney!"
        b p2 level grin "You, too, Al! And it was nice to meet you, Harry!"
        h casual grin "Nice to meet you, too!"
        hide screen skipchoice
        hide brit
        hide harry
        with dissolve
        pause 0.1
        "With that, Brittney entered Kelly's, and I drove Harry and myself home."
        scene bg house_s with dissolve
        $ current_track = "\"Relaxation in the Country\""
        play music relaxation_in_the_country
        "When we got home, we unloaded the groceries into the house. Mom thanked us for the shopping, as well as not killing each other."

    label meeteleanor:
        $ choicevbox = 1
        scene bg living_s_m with dissolve
        pause 0.1
        "As deduced, we were having chicken Alfredo tonight, which instantly got Harry excited."
        "I offered to help Mom make it, but she insisted she was fine."
        show ginger p2 straight casual grin at middle with dissolve
        pause 0.1
        g "Though, if you want to be helpful, would you mind taking the garbage out for me? They're picking it up tomorrow morning."
        a "I don't mind at all."
        g sad "Thanks, Alex!"
        hide ginger with dissolve
        pause 0.1
        scene bg house_s with dissolve
        pause 0.1
        "I took the trash out to the garbage can next to the driveway. I looked around and saw that a few of the other houses on the street had their cans out, as well."
        "That's when I saw movement at the far end of the street, right across from Donald's house. It looks like they were dragging their garbage can out, too."
        "...{w}wait a minute..."
        $ current_track = "None"
        stop music fadeout 3.0
        "...{w}no...!"
        pause 1
        show elie p1 straight casual blank at middle with dissolve
        pause 1
        $ current_track = "\"Chaotic Evil\""
        play music chaotic_evil
        "The person in front of the house was the same woman from Dolmart."
        "It was in that moment where everything clicked."
        window hide
        play sound woosh
        scene bg white with dissolve
        scene bg house_y
        show don p1 straight grin casual at middle
        with dissolve
        window show dissolve
        pause .1
        d "Over here, we have the Yellman house."
        d "There's only one resident, Eleanor. She's in Brittney's class."
        d raised blank "It's really no secret that not a lot of people like her, ourselves included."
        hide don
        show chris p2 straight mad blank at middle
        with dissolve
        pause 0.1
        c "She's a slut who will constantly treat everyone like useless garbage."
        window hide
        play sound woosh
        scene bg white with dissolve
        scene bg house_s with dissolve
        window show dissolve
        "Well, well, well. I guess earlier today was my first run-in with our neighbor, Eleanor."
        "Part of me wants to run right over to her and call her out on her bullshit from earlier, but honestly, I doubt she'd even remember me."
        "If that's the case, maybe it's best it stays that way."
        "But if she's supposed to be in Brittney's class, why does she look so old? Is that just how she looks? But if that's the case, why does she live alone?"
        "I guess this raises more questions than answers. I'll have to ask someone about this soon."
        "With that, I went back into the house. Dinner should be ready soon, but before that, maybe I'll get a chance to lie down for a bit; it's been a busy day."
        $ daydesc = 0
        $ replay = False
    label progressday03:
        $ progress += 1

        jump progress
