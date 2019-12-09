label animetalk_b:
    "About halfway there, I turned towards her and gave a sneaky grin."
    show brit a2 casual straight blank at close_b with dissolve
    with Pause(.1)
    a "So..."
    a "...how's the anime watching going?"
    b level "..."
    b right "I don't know..."
    b "I'm just not a fan of that whole Japanese look to it."
    a "That kinda sounds racist."
    $ b_partial = True
    b a1 mad straight "You know what I mean."
    a "I don't think I do."
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    $ b_partial = False
    show brit a1 straight raised blank at close_b
    b "It's so... choppy. And the mouth animations are, like, so simple. It's just them opening and closing their mouth over and over to sync up to the dialogue."
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b a2 casual "Chris said it's to make it easier to dub it into other languages, and I kinda get it..."
    b right level "...but I feel like the whole thing is animated by a guy learning animation."
    a "..."
    a "So, your problems are with the animation style and not the plot?"
    b a1 hanging mad straight "Oh, don't get me started on the plot."
    a "Alright. I won't."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    b a2 sad right blank "I dunno. Maybe I'm just too used to American animated films to get it."
    a "Maybe. I've only seen bits and pieces of anime here and there, but from what I've seen, I can certainly see the appeal."
    b level straight "I'm glad one of us can."
    b grin "Thankfully, we're almost done with this season, apparently, so I only have to suffer for a little longer."
    a "Kind of a negative way of putting it."
    b "It is what it is."
    jump britreturns

label kisstalk_b:
    "About halfway there, she turned towards me with a smug grin."
    $ b_partial = True
    show brit a2 straight level huhu at close_b with dissolve
    with Pause(.1)
    b "You're not just hanging out with me because we kissed, are you?"
    "Well, that certainly came out of nowhere."
    a "Uh..."
    $ b_partial = False
    show brit a1 straight sad grin at close_b
    b "Hey, don't feel embarrassed! I think it's kinda cute!"
    a "Oh, do you?"
    b casual opened_smile "Yeah!"
    b a2 right level huhu "Plus, I bet it'll make Donnie really jealous."
    a "I actually talked to him about this earlier. He said he was fine with it."
    $ b_partial = True
    b straight casual grin "Oh, I'm sure he DID say that."
    $ b_partial = False
    show brit a1 straight raised opened_smile at close_b
    b "But I know him well enough to know that it's killing him that I kissed you and not him."
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    b mad grin "Oh, well. Sucks to be him."
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b a2 casual blank "But I hope you realize that it was just a kiss and nothing more."
    b level "It's not like we're dating or anything."
    b right "Hell, I can't even really say that I like you romantically, so don't get any weird ideas."
    b "It's bad enough I've got one guy on my ass about that..."
    a "..."
    a "Brit, you're the only one who's implied anything of the sort. {w=.5}All I wanted was a soda."
    b a1 straight sad "Sorry, sorry.{w=.5} You're right."
    a "But for the record, I understand that we're not dating or anything."
    b level grin "Alright. Good."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    a "Anyway, I couldn't help but notice your enjoyment at the idea of Donald getting jealous."
    b a2 raised closed_smile "What can I say? I'm just that kind of girl."
    b right level huhu "I mean, yeah, it's probably wrong, but I just like teasing Donald about his crush, making him upset by reminding him that I'm not his."
    b a1 straight sad blank "Though, as you can imagine, it sometimes does go a bit too far..."
    if persistent.choice_12 == 1:
        b level grin "...but it's like I told you: I've made it clear to him that I don't feel that way about him, and that he's setting himself up for disappointment by pursuing the impossible."
    else:
        b level grin "...but I've made it clear to him that I don't feel that way about him, and that he's setting himself up for disappointment by pursuing the impossible."
    a "I guess..."
    jump britreturns

label kisstalk_b_d_b:
    "About halfway there, I turned to her and told her something that had been on my mind."
    show brit a2 straight casual blank at close_b with dissolve
    with Pause(.1)
    a "Anyway, Brit... There's something I've been meaning to ask you."
    b raised grin "Oh? And what would that be?"
    a "It's about that night in the cabin..."
    b casual blank "..."
    a "...and that dare I suggested..."
    b level "..."
    a "You're not mad at me for that, are you?"
    b a1 raised hanging "Mad? Why would I be mad?"
    a "You just looked so uninterested and upset about the whole thing."
    b a2 blank level "...well..."
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    b left "...it's not easy to admit this, but... yeah. I wasn't exactly keen on the idea of kissing my best friend, even as a dare."
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b straight casual "But!"
    b a1 grin "You were just acting as a wingman of sorts, and I can't be mad at you for that."
    b a2 right level huhu "After all, it could've been a lot worse, right?"
    b "You totally had the chance to dare me to fuck him or something crazy like that and didn't take it."
    "Well, when she puts it like that, it sounds like a wasted opportunity."
    "Though it's an opportunity that I would kindly not want to witness."
    if persistent.choice_21 == 2:
        b a1 straight casual grin "Plus, you changed your mind, and I didn't have to do it, in the end, anway, which I really appreciate."
    b a1 straight casual grin "So, yeah. No hard feelings."
    a "Alright, then. Glad to know that."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    a "..."
    a "So, um..."
    b blank "What?"
    a "If I'm not getting too personal here..."
    if persistent.choice_21 == 1:
        a "Did you... you know...{w} enjoy it?"
    else:
        a "If you had actually kissed him, do you think you would... you know... {w} enjoy it?"
    b level hanging "...!"
    a "Sorry, I'm just curious. You don't have to answer if--"
    b a2 grin "Nah, you're cool. I just wasn't expecting that question."
    b casual blank "But to answer it..."
    b level left "...well..."
    b straight "I mean, after you've kissed enough people enough times, the 'magical' effect wears off."
    a "Is that right?"
    "I could see Brittney being the kind of person to have some...{w=.5} experience,{w=.5} but that's besides the current point."
    a "So, if kissing really doesn't mean anything to you, then what's the big deal with kissing Donald?"
    b right "..."
    b "Can we just...{w=.5}{nw}"
    b straight "Can we just...{fast} drop this, please?"
    a "..."
    a "Yeah, sure. Sorry."
    b grin "Thanks."
    "Wow."
    "I think I may have found Brittney's weak spot."
    jump britreturns

label punchtalk_b_b:
    "About halfway there, I turned towards her and started a conversation."
    show brit a1 casual straight blank at close_b with dissolve
    with Pause(.1)
    a "It's good to see that you and Donald are cool after that night at the cabin."
    b a2 level grin "Oh, yeah. Totally."
    a "What even happened after you left, anyway?"
    b right huhu "Well, I knew he would be at the pond; it's his go-to place to hide when the cabin's unavailable."
    a "Was he upset to see you?"
    b straight blank sad "...{w=.5}a little."
    b level right "But I must've looked more upset than he did, because he quickly asked if I was okay, as if he was the one who hurt ME."
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    b a1 casual straight "I told him that I was fine, and that I was just checking up on him."
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b a2 sad grin "It was your typical makeup scenario."
    b level right huhu "I apologized, he forgave me, we hugged it out..."
    b a1 straight casual grin "...and that's when you and Chris showed up."
    a "Gotcha."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    a "So does this kind of thing happen often, or...?"
    b a2 level blank "...{w=.5}yeah, more than I'd like to admit."
    b "The problem seems to stem from the fact that I'm a bit of a hypocrite."
    a "How so?"
    b right "I'm always getting on Don's case about not thinking before doing, and then there's me, who's even worse at not doing it."
    a "Like that day at the mall?"
    b straight raised "Exactly like that day at the mall."
    b level grin right "I mean, I guess we're all guilty of it, when you think about it..."
    b blank "I dunno. I guess some things will never change..."
    a "..."
    "Hearing Brittney go semi-philosophical is a bit strange, I'll admit."
    b a1 straight casual grin "But we always seem to find a way to get over it, so there's a silver lining for ya."
    a "I guess so."
    jump britreturns

label kisstalk_b_c_t:
    "About halfway there, she turned towards me with a smug grin."
    $ b_partial = True
    show brit a2 level huhu straight at close_b with dissolve
    with Pause(.1)
    b "I'm honestly shocked you chose to not spend time with your girlfriend."
    a "Brittney, you and I both know that Christeena is not my girlfriend."
    b casual grin a1 "But you kissed, and you both seemed to enjoy it, so the ball is already in motion."
    a "It was just a dare!"
    $ b_partial = False
    show brit a1 straight mad grin at close_b
    b "Yeah, a dare YOU made!"
    a "Your point being?"
    b a2 level "Geez, do I need to spell everything out for ya, dum-dum?"
    b opened_smile "Why would you dare her to kiss you if you didn't have any sort of romantic feelings for her?"
    a "Have you considered that maybe I just wanted to kiss a girl?"
    b grin raised "So then why not get ME out so I could be the one you kissed?"
    b "After all, I obviously would be the more-willing girl out of the two."
    a "..."
    $ b_partial = True
    b level huhu "Exactly."
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    $ b_partial = False
    show brit a1 level straight grin at close_b
    b "But, hey. Don't feel embarrassed about it."
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b raised closed_smile a2 "She feels the same way."
    a "..."
    a "She does...?"
    b level right huhu "I probably shouldn't be telling you this..."
    b a1 straight raised grin "...but she has a total crush on you. Like, ever since she met you, she's talked about how handsome you are."
    a "And why do I get the feeling that you're lying to me?"
    b a2 left derp level "Probably because I do tend to lie a lot to mess with people."
    b raised straight grin "But I swear on my mother's life that I would never kid around with something like this."
    a "I see..."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    a "And so what exactly do you expect me to do with this information?"
    b a1 casual blank "I'm not really 'expecting' you do to anything."
    b level grin "I'm simply giving you the facts. You can do whatever you want with said facts."
    b a2 right "If you wanna ask her out, go for it. If not, that's cool, too."
    b straight blank "Just don't lead her on if you're gonna go with the latter option."
    a "I'll certainly keep that in mind."
    "I mean, I've only known Christeena for a month, and even then, I can't really say I know too much about her."
    "But I guess it's nice to know that the option is supposedly available if I'm interested..."
    jump britreturns

label kisstalk_b_c_f:
    "About halfway there, she turned towards me with a smug grin."
    $ b_partial = True
    show brit a2 straight level huhu at close_b with dissolve
    with Pause(.1)
    b "You're not trying to avoid Christeena, are you?"
    a "And why would I do a thing like that?"
    $ b_partial - False
    show brit a1 straight level grin at close_b
    b "Because you two didn't actually kiss because she didn't want to, and now you feel embarrassed about it."
    a "..."
    b a2 "Here's a life lesson for ya: sisters tell each other EVERYTHING."
    a "...noted..."
    b right derp "I feel like I should be disappointed in her for not going through with the dare..."
    b raised straight grin "...but I'm actually more proud of you for suggesting that you fake it."
    a "Proud...?"
    b a1 level huhu "Did I stutter?"
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    b sad grin "It shows you've got a heart in you, and I respect that heavily."
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b a2 raised "Maybe if you showed that heart around her more often, she'd actually want to kiss you."
    a "Seems like a large leap of assumption."
    b right level huhu "Well, I probably shouldn't be telling you this..."
    b straight raised a1 grin "...but Christeena has a small crush on you."
    a "And why do I get the feeling that you're lying to me?"
    b a2 left derp level "Probably because I do tend to lie a lot to mess with people."
    b raised straight grin "But I swear on my mother's life that I would never kid around with something like this."
    a "I see..."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    b a1 casual blank "Look, I'll be serious for a second."
    a "Yes?"
    b level "I have a feeling you may feel the same way in return. You don't gotta tell me if I'm right or not."
    b right "But if you do and actually do want to pursue something with her..."
    b straight "...then you gotta spend more time with her."
    a "We already do spend a lot of time together."
    b raised a2 "I mean without me and Donald around. Talk to her. Get to know her better."
    b level "And above else, don't be a dick."
    b sad a1 grin "It's not too late to try and get a ball rolling,{nw}"
    b mad blank "It's not too late to try and get a ball rolling,{fast} but you gotta play your cards right from this point on."
    a "Good to know, I suppose."
    b level grin a2 "Take it from me. I know her better than anyone."
    jump britreturns

label flashtalk_b_c:
    "About halfway there, Brittney turned towards me with a smug grin."
    show brit a2 straight level huhu at close_b with dissolve
    $ b_partial = True
    with Pause(.1)
    b "You're not trying to avoid Christeena, are you?"
    a "And why would I do a thing like that?"
    $ b_partial = False
    show brit a1 straight level grin at close_b
    if persistent.choice_20 == 1:
        b "Because you tried to make her show you her tits, and now you're embarrassed."
    else:
        b "Because you tried to make her show you her tits, and now she's pissed at you."
    a "..."
    b a2 "Here's a life lesson for ya: sisters tell each other EVERYTHING."
    a "...noted..."
    b right derp "I feel like I should be disappointed in her for not going through with the dare..."
    b straight raised grin "...but, honestly, I'm actually a bit proud of her."
    a "Proud...?"
    b a1 level huhu "Did I stutter?"
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    b a1 casual blank "As much as I try to get her to 'open up' more, so to speak, I'm actually a bit glad she's adamant about her beliefs."
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b a2 level "I might not always share those beliefs..."
    b grin "...but I respect that she won't just agree with whatever makes her look good, you know?"
    a "Yeah, I guess."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    b mad blank "That said, showing a little skin ain't gonna kill her, especially to a guy she has a crush on."
    a "...!"
    b level right huhu a1 "...oops."
    a "She...{w=.5} does...?"
    if persistent.choice_20 == 1:
        b a2 level straight grin "Well, she certainly thinks a little less of you because of that dare, but yeah. She's mentioned it a few times."
    else:
        b a2 level straight grin "Well, she certainly thinks you're a perverted asshole because of that dare, but yeah. She's mentioned it a few times."
    a "Oh..."
    a "So, in other words, I screwed up?"
    b blank "Well, probably."
    b a1 casual grin "But it's not too late to try and redeem yourself. Just try and be nice and respectful to her from now on, and maybe she'll change her mind."
    b a2 level right derp "Or you could keep having her think less of you, if you really want. That's up to you, at the end of the day."
    b straight grin "Who am I to tell you what to do with your life?"
    jump britreturns

label punchtalk_b_c:
    "About halfway there, Brittney turned towards me with a grin."
    show brit a1 straight raised closed_smile at close_b with dissolve
    with Pause(.1)
    b "You know, just for the record, it was pretty cool what you did at the cabin that night."
    a "Huh?"
    b level a2 grin "Letting Chris slap Donald?"
    b right huhu "That was actually pretty clever of you."
    a "Well, thanks, I suppose."
    a "I guess it truly was one of those things we can look back and laugh at."
    a "Though I must admit it wasn't really that funny in the moment."
    b casual straight blank "Oh, no doubt."
    b a1 raised grin "But Donald seems to be cool with it now, so that's a relief."
    a "Yeah, that's what he told me earlier."
    a "He also mentioned something about how Chris is more violent than she lets on."
    b right level huhu "Huhuhu..."
    a "Is that true?"
    b a2 straight raised grin "Well, technically, yes."
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    b a1 level "But that doesn't mean she just resorts to violence at a moment's notice."
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b a2 casual blank "But it DOES mean that she can get pretty uncontrollable if she gets pissed enough."
    b level right "I've only seen it happen a few times, and it was not pretty."
    a "What got her that pissed?"
    b a1 straight "Eleanor."
    a "Ah. Should've guessed."
    a "So how 'not pretty' are we talking?"
    $ current_track = "None"
    stop music fadeout(3)
    b a2 sad "Well..."
    b level right "Most of the time, it's just verbal abuse."
    b "But every now and then, punches are thrown outside of school..."
    a "Seriously?!"
    b straight "I joke about a lot of things, but this is not one of those things, Alex."
    $ current_track = "\"Reflection\""
    play music reflection
    b a1 sad "Thankfully, there haven't been any broken bones or lawsuits."
    a "Yeah, thankfully, indeed."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    b a2 right "I just..."
    b "...I'm worried about her.{w=.5} Worried she'll end up getting herself killed..."
    a "You think Eleanor is capable of doing that?"
    b mad straight "From what I know about her, absolutely."
    b raised "She certainly has the physical strength for it..."
    b sad right "...but that doesn't mean she would never try to fight dirty with a knife or something..."
    a "Eleanor's that bad, huh?"
    b a1 level straight "I mean, I don't really know her on a personal level, but..."
    b sad "...I can imagine she would be."
    a "Damn..."
    b a2 "Well, at the end of the day, there's only so much I can do to protect Christeena..."
    a "..."
    b right "..."
    b straight level huhu "...but, hey. At least Chris has enough strength in her to avoid getting raped or something."
    a "...!"
    b sad a2 right grin "Sorry, just...{w=.5} trying to lighten the mood, I guess."
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    jump britreturns

label tampontalk_b:
    "About halfway there, I turned towards her and started a conversation."
    show brit a1 straight casual blank at close_b with dissolve
    with Pause(.1)
    a "So, is Donald really going to go through with his dare?"
    $ b_partial = True
    b a2 level grin "Oh, he will, whether he wants to or not."
    $ b_partial = False
    show brit straight a1 level grin at close_b
    b "I mean, when you think about it, it's the perfect dare."
    a "How so?"
    b right level huhu "Well, nobody got hurt, doing it will embarrass him, and I benefit heavily from the actions of the dare."
    a "...huh.{w=.5} I guess you have a point."
    b a2 raised straight grin "Plus, he won't need to make that many shopping trips for it throughout the year, since I'm not that much of a heavy bleeder."
    a "Ok{cps=*0.25}aaaaay{/cps}. {w=.5}Did not need to know that."
    $ b_wink = True
    b tongue "Well, it made you blush, so you kinda did."
    a "Do you ever get tired of flustering people?"
    $ b_wink = False
    show brit a2 level straight grin at close_b
    b "If I did, I wouldn't keep doing it, dum-dum."
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    b a1 raised blank "Although I'm still curious about one thing."
    a "What's that?"
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b a2 "Why did you let me win?"
    b left "I mean, you totally could have won and made Donald do a dare, but you didn't."
    a "Eh. Honestly, I couldn't really think of anything I could have Donald do.{w=.5} Plus, I figured you would enjoy the opportunity to make him do a dare."
    b a1 straight casual "Oh, don't get me wrong, I did enjoy it."
    b level grin "Oh, don't get me wrong, I did enjoy it.{fast} Like, a lot."
    b a2 raised blank "I guess I was just wondering what your reasoning was, that's all."
    a "Alright, then..."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    b a1 casual grin "Well, anyway, thanks for that."
    a "What, letting you win?"
    b level "I was actually thinking of that time you saved me from the fire-breathing dragon, but yeah, letting me win was also pretty nice of you."
    "I wiped some of the condensation off of my soda can and flicked it at her."
    $ b_wink = True
    show brit tongue
    "She just wiped it off her face and stuck out her tongue."
    a "Well, you're welcome for the dare. Glad you could find use out of it."
    $ b_wink = False
    show brit a2 raised straight grin at close_b
    b a2 raised "But, you know, something else has been on my mind..."
    a "...yes?"
    b opened_smile "What would you have made Donald do if you were gay?"
    "I stopped dead in my tracks and looked at her with the most confused and weirded-out look I feel like I've ever given to someone."
    a "What the fuck kind of a question is that?!"
    b a1 casual "An honest one!"
    b level grin "I mean, I'm not judging. I'm just curious what you think you would do."
    "I continued to stare at her, waiting for any sign that she was joking.{w} Unfortunately, I couldn't find one."
    a "I'm not having this discussion."
    "I continued walking towards Christeena, with Brittney quickly speed walking to catch up."
    $b_blink = False
    b a1 closed sad closed_smile "Ehehehe! Your face is blood red! That's a new personal record!"
    "I groaned and slowly shook my head."
    jump britreturns

label pushuptalk_b:
    "About halfway there, Brittney turned towards me with a grin."
    show brit a2 straight raised closed_smile at close_b with dissolve
    with Pause(.1)
    b "I still can't believe he managed to do all of those push-ups."
    a "Who, Donald?"
    $ b_partial = True
    b level grin "No, I meant Fat Albert."
    "I guess I deserved that sarcasm."
    a "Well, that certainly would be impressive to see."
    $ b_partial = False
    show brit a2 left level derp at close_b
    b "Hm. Fair enough."
    a "But I'll admit that Donald did a pretty good job."
    b a1 straight casual grin "Has he said anything about his arms being sore?"
    a "Not to me."
    b a2 level left huhu "Well, he hasn't said anything to me, either."
    b straight raised grin "Then again, telling me that would make him look less manly than he already feels."
    a "Yeah, I can see that. He's always seemed to have had an issue with things like that."
    b a1 casual blank "Really?"
    a "Really."
    b a2 level right "...huh."
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    b a1 straight sad "Has it ever, like, bothered him really badly?"
    a "What do you mean?"
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b a2 "Like, has he ever gotten really upset and embarrassed because he looked weak?"
    a "Well, not that I can really recall."
    a "He never really tried to make himself feel or look like the strongest man on Earth, but he's certainly seemed to have felt upset when someone did better than him."
    b right "...{w}I see."
    a "..."
    a "You okay?"
    b straight casual "Yeah, of course."
    a "..."
    b sad "..."
    b "Well..."
    b left "I mean, I always like to pick on him about how I'm stronger than him, so..."
    b a1 straight "...I guess now I'm starting to wonder if maybe it's actually hurting him more than I'd like."
    a "Hm..."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    a "Well, if it means anything to you, I think you're fine."
    b straight casual "You think so?"
    a "Donald isn't the kind of guy to continue to hang out with someone who makes him legitimately feel terrible."
    a "I'm sure he knows that you're just teasing and nothing more."
    b sad right a2 "..."
    a "And, hey. In a way, it kinda helps him."
    b raised straight "Huh?"
    a "I'm willing to bet anything that he only did those 50 push-ups the way he did because he wanted to impress you."
    b right "..."
    b grin "...yeah, I suppose that's possible."
    b a1 straight "I guess he does tend to go outside his comfort zone a bit when I tell him he can't do something."
    a "Exactly. So, I think you're alright."
    b "..."
    b a2 "Thanks, Al."
    a "No problem."
    jump britreturns

label pondtalk_b:
    $ current_track = "None"
    stop music fadeout(3)
    "About halfway there, Brittney turned towards me with a serious expression."
    show brit a2 sad straight blank at close_b with dissolve
    with Pause(.1)
    $ current_track = "\"Reflection\""
    play music reflection
    b "Hey..."
    a "Yeah?"
    b a1 "Have you talked to Donald about that night at the cabin?"
    a "Yeah. He said everything was good."
    b a2 right "You sure?"
    a "To quote the man, himself, he said we were {i}'as 'no beef' as a vegetarian buffet'{/i}."
    $b_blink = False
    b closed opened_smile "Heh."
    $b_blink = True
    b straight grin "Well, that's good to hear for you, but..."
    b right blank "...I don't know how he feels about me, still."
    a "What do you mean? Haven't you talked to him about it?"
    b casual a1 straight "Of course I have."
    b sad "But..."
    b a2 left "...I'm just scared that he might not fully forgive me."
    a "Why wouldn't he? He's the kind of guy who would forgive someone who slaughtered his parents."
    b "...{w}I don't know. Maybe I'm just freaking myself out."
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    b a1 straight "Like, as much as I think I know him, I sometimes can't read how he feels."
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b a2 "I can't tell if he's really forgiving and forgetting..."
    b right "...or if he's just pretending so I'll feel better..."
    a "Why would he do that?"
    b a1 "Why wouldn't he?"
    b straight "I've done things like this to him all the time. Anyone would be sick of it."
    a "..."
    "I'm admittedly taken back. I've never seen Brittney get this concerned or emotional."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    a "Hey, I assure you everything's fine."
    a "Look, if it'll make you feel better, I'll talk to Donald if you want."
    b straight casual hanging "..."
    b a2 blank "N-No. You don't have to do that."
    a "Maybe I want to."
    b sad "Alex, please."
    b right grin "I appreciate it, but you're right. Everything will be fine."
    b a1 "Again, just freaking myself out. That's all. Ehehe..."
    a "..."
    $ current_track = "None"
    stop music fadeout(1)
    b "..."
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    jump britreturns

label kisstalk_b_d_d:
    "About halfway there, Brittney turned towards me with a warm grin."
    show brit a1 straight sad grin at close_b with dissolve
    with Pause(.1)
    b "Hey, Al?"
    a "Yeah?"
    b a2 right "For the record, that was pretty cool what you did for Donald."
    a "Huh?"
    b a1 level straight "You know, daring him to kiss me?"
    a "You...{w=.5} thought that was 'cool'?"
    b casual a2 "Yeah!"
    b sad "Having his back, trying to help him get what he wants..."
    b left "I really meant it when I said that I wish I had someone who could do something like that for me..."
    a "Not to sound stupid, but doesn't Donald already kinda fill that position?"
    b casual straight blank "Huh?"
    a "Donald seems like he'd do anything to help you."
    b level "Well, yeah, but..."
    b right "I dunno. It's hard to explain."
    a "Try me."
    b "..."
    $ current_track = "None"
    stop music fadeout(3)
    "We had reached the coolers. She opened up one of them, revealing it to be nothing but water bottles."
    "She grabbed one of them, closed the lid, and continued to speak as she opened the one next to it."
    $ current_track = "\"Reflection\""
    play music reflection
    b raised straight a1 "I guess what I mean is that even though Donald and I are close, I kinda don't trust him with everything."
    a "That doesn't seem like the kind of thing you can 'kinda' do. Either you do or you don't."
    $ b_partial = True
    b level "..."
    b a2 raised "Fine. I don't trust him with everything."
    a "Why not?"
    $ b_partial = False
    show brit a1 straight sad blank at close_b
    b "I don't know..."
    "After grabbing a Hilly Dew from the cooler, she closed that lid and turned to face me."
    b a2 right "...{w}I guess there are some things about me that I don't want him to know..."
    b a1 straight casual blank "I mean, I trust Donald, don't get me wrong."
    b sad "...but..."
    b right "...there are some things that I'm just not sure he'd take well if he found them out."
    "As tempted as I was to ask what exactly she was getting at, I had a feeling it might just be better to let her ramble on."
    "After all, if she won't tell Donald, why would she tell me?"
    "Although hearing her vent like this at all seems a bit out of character for her..."
    b a2 "He knows I'm not perfect, and he doesn't expect me to be, either, but..."
    $b_blink = False
    b closed_sad "*sigh* I don't know..."
    a "..."
    "I grabbed a Hilly Dew for myself, and we started to walk back towards Christeena, who was standing by herself awkwardly in the middle of the yard."
    a "So, why don't you find a friend that you CAN talk to about this stuff with? One that won't judge?"
    $b_blink = True
    show brit a2 straight casual blank at close_b
    b "I do."
    a "..."
    a "I thought you said--"
    b level "I said I didn't have anyone to help me out with certain stuff."
    b a1 "But I talk to Christeena about this stuff all the time."
    b "She just doesn't..."
    b a2 right "...help."
    a "..."
    a "So, may I ask why exactly you're telling me all of this?"
    $ b_partial = True
    b straight level huhu "Because who would ever believe you?"
    a "...!"
    "I feel like I should be offended right now, but I'm too confused to really understand what to feel."
    $ b_partial = False
    show brit a1 straight level grin at close_b
    b "Anyway, enough depressing stuff."
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    jump britreturns

################################################################################

label animetalk_c:
    "Christeena and I stood there somewhat awkwardly in silence before I struck up a conversation."
    show chris b1 straight casual blank
    a "So..."
    a "...how's the anime watching going?"
    $c_blink = False
    c closed_happy smile sad "Great!"
    $c_blink = True
    c straight raised b2 grin "Honestly, I'm just amazed that Brittney is really going through with it."
    c level left dot "Although, she clearly doesn't seem to be enjoying it."
    a "Well, wasn't the whole dare idea supposed to be a punishment?"
    c b1 sad straight blank "I guess, but..."
    c b2 right "...I guess I was hoping she'd maybe be into it just a little bit."
    a "Ah. I see."
    c straight mad "She really does seem to be close-minded about certain stuff and won't give it a chance."
    c b1 sad "There are only so many things we can do together and have in common..."
    c left "...I guess I just thought that maybe this could be another one we could do together."
    a "Yeah, tell me about it. Harry and I hardly have anything in common besides video games and some shows."
    c straight "And doesn't that bother you?"
    a "Eh. Not really."
    c casual "Really?"
    a "I dunno. Maybe it's a male thing, but Harry and I have this mutual understanding that we're a bit different from each other."
    a "So, we use that to our advantage and just pick on each other a lot."
    c level "..."
    a "But it's all in good fun, I promise."
    a "Besides, we both know if we ever went too far, Mom would find out."
    $c_blink = False
    c closed_happy smile sad "Ahahaha!"
    $c_blink = True
    c b2 straight raised grin "And I thought Brittney was the most immature person I knew!"
    a "What can I say? I'm just full of surprises."
    c level "Yeah, apparently."
    jump britreturns

label kisstalk_c:
    "Christeena and I stood there somewhat awkwardly in silence before she struck up a conversation."
    c level blank "So, I know this isn't really any of my business, but I'm curious..."
    c b2 raised "Why did you dare Brittney to kiss you?"
    a "..."
    "Well, I certainly wasn't expecting her to ask that."
    a "I, uh...{nw}"

    menu:
        a "I, uh...{fast}"

        "'I think she's attractive.'":
            $ persistent.choice_23_ = 1
            jump thinkshesattractive

        "'I wanted to make Donald jealous.'":
            $ persistent.choice_23_ = 2
            jump makedonaldjealous

    label thinkshesattractive:
        a "Okay, this stays between us, but..."
        a "...I think she's attractive."
        c b1 sad grin "Really?"
        "I could feel my face getting warmer as I looked to see where Brittney was."
        "She had just made it to the coolers and was digging around in one of them."
        "I quickly turned back to Christeena and gave an awkward smile."
        a "Yeah, really."
        $c_blink = False
        c closed_happy "Well, that's a little cute."
        a "But I just...{w=.5} don't want her to know."
        $c_blink = True
        c straight b2 "I don't blame you, Alex. It's not easy to tell someone you think they're attractive when you've only known them for a month."
        a "Exactly."
        c level blank "And I kinda hate to break it to you, but..."
        a "Oh, no. {w=.5}What is it?"
        $ c_blush = True
        c sad hanging "N-Nothing bad, I promise!"
        $ c_blush = False
        show chris b1 straight sad blank at close_c
        c "It's just that she's, well..."
        c right level "...not exactly into relationships right now."
        a "...oh."
        c straight "Yeah."
        a "Is there a specific reason, or...?"
        c straight sad "..."
        c left b2 "I don't think that's my place to say."
        a "Alright, then. Fair enough."
        jump britreturns

    label makedonaldjealous:
        a "Okay, this stays between us, but..."
        a "...I kinda wanted to make Donald jealous."
        c level b1 "...really?"
        a "Yeah, as dickish as that sounds."
        c raised "Why, though?"
        a "I mean, I guess my thought process was that I was going to punish him for trying to add the dare punishment by having his crush kiss me."
        c sad dot "Well, that certainly is quite the punishment."
        a "Yeah, but we talked it over earlier, and he seems okay about it."
        c b2 blank "Are you sure?"
        a "Well..."
        a "He doesn't hate me, I can say that much."
        c left grin "Heh. I suppose that's a good sign, then."
        c straight casual blank "So, does that mean you don't have any romantic feelings towards her, then?"
        a "..."
        $ c_blush = True
        c b1 sad dot "S-Sorry! That was too personal!"
        c b2 left blank "I-I mean, it's none of my business. I shouldn't have asked that!"
        a "Chris, you're okay, I promise."
        c straight "You're sure?"
        a "Positive."
        $ c_blush = False
        show chris b1 grin straight sad at close_c
        c "O-Okay, then..."
        jump britreturns

label kisstalk_b_d_c:
    "Christeena and I stood there somewhat awkwardly in silence before she struck up a conversation."
    c level blank "So, uh..."
    c b2 raised "Can I talk to you about something?"
    a "I don't see why not."
    c sad "It's about Brittney."
    a "Okay...?"
    c b1 left "And that dare..."
    a "..."
    "I really don't like the way this is headed."
    c straight grin "Look, I know you just wanted to help Donald."
    c level blank "But..."
    c right "Well, it takes a lot to get under Brittney's skin."
    c "And the idea of kissing Donald is very high on the list of things that get her upset."
    a "Oh..."
    c straight sad b1 "Yeah..."
    if persistent.choice_21 == 2:
        a "I mean, at least I changed my mind, right?"
        c grin "Yeah, you did."
        c level blank "Still, she really was upset that it was suggested, nonetheless..."
    a "What exactly is her issue with kissing Donald?"
    c raised "She told you: she's uncomfortable kissing a close friend that she has no romantic feelings for."
    a "That's all it is, though?"
    c mad b2 "What other reason would there be?"
    a "Well...{w=.5} I don't know. {w=.25}I guess I assumed she was the kind of person who wouldn't let something like that bother her."
    a "She said she'd be fine kissing a total stranger like me, yet kissing someone she knows and trusts is an issue."
    a "That doesn't make sense to me."
    c level "It doesn't have to make sense to you. At the end of the day, it's how she feels, whether you understand why or not."
    a "..."
    a "Yeah, I guess..."
    a "But she doesn't hate me or anything, right?"
    $ c_blush = True
    c sad b1 hanging "No, of course not!"
    $ c_blush = False
    show chris b1 sad grin straight at close_c
    c "But I think it would just be better to take things like this into consideration from now on if you want to be on her good side."
    a "Alright, then."
    jump britreturns

label punchtalk_b_c_c:
    "Christeena and I stood there somewhat awkwardly in silence before I struck up a conversation."
    show chris blank casual
    a "So, I take it everything's good between Donald and Brittney?"
    c sad b2 grin "Seems like it!"
    a "That's a relief..."
    c b1 left "Yeah..."
    a "..."
    c straight casual blank "..."
    "More awkward silence."
    "I looked towards the coolers and saw Brittney digging around in one of them."
    "I turned back to Christeena and asked something that had been on my mind since that night in the cabin."
    a "So, do things like that happen often?"
    c b1 dot "You mean the whole 'fight and forgive' thing?"
    a "Yeah."
    c level blank "..."
    c right "Sometimes."
    c straight sad "But that's just how people are, right?"
    a "I suppose."
    c level blank right "I mean...{w=.5} There was that day at the mall, for example."
    c raised b2 "There were several variables that led to the argument that had happened..."
    c straight sad grin "But, in the end, we both realized we were being stupid and made up."
    a "And that's essentially what happened with Brit and Don?"
    c casual blank b1 "More or less."
    a "Huh."
    jump britreturns

label kisstalk_c_c_:
    $ current_track = "None"
    stop music fadeout(3)
    c blank "..."
    a "..."
    "We both seemed to reach the same realization that we were alone."
    "We hadn't really talked since that night in the cabin."
    if C_Kiss == False:
        "I mean, nothing ended up happening, and she didn't seem mad at me or anything..."
    elif C_Kiss == True:
        "I mean, we both seemed to enjoy it, but how exactly are we supposed go forward from this?"
    $ current_track = "\"Reflection\""
    play music reflection
    c sad grin "So..."
    "I'm snapped into reality by her attempt to start a conversation."
    a "So..."
    c b1 "How've you been?"
    a "Pretty good."
    c left "That's good."
    a "Yeah."
    c "..."
    a "..."
    "Well, that got us nowhere."
    "I guess if I wanna avoid more conversations like this, I better say something about the issue at hand."
    a "So, uh... about that dare..."
    c straight level blank "Alex, stop."
    a "..."
    $ c_blush = True
    c sad dot b2 "S-Sorry. I didn't mean to sound so harsh..."
    $ c_blush = False
    show chris b2 sad left blank at close_c
    c "It's just..."
    if C_Kiss == False:
        c straight "I hardly know you, let's be real."
        c right "I've only known you for a month, and we've barely really done anything together in that time."
        a "Yeah, I guess that's true."
        c straight grin b1 "But, you are a pretty good guy, I can tell."
        c level blank "I just..."
        c left "Well..."
        c straight sad "I just want my first kiss to be more special than that."
        a "Oh."
        c right level b2 "Sorry to disappoint."
        a "No, I understand completely, Christeena."
        "Well, I'm glad we somewhat got that sorted out."
        "I wonder if it's not too late to try and be closer to Christeena, though..."
    elif C_Kiss == True:
        c straight b1 "Yeah, we kissed."
        c right grin "And, yeah... I enjoyed it."
        c straight level blank "But..."
        c "I hardly know you, let's be real."
        c right b2 sad "I've only known you for a month, at the end of the day."
        c straight "And even though we've spent a lot of time together, that's still hardly enough time to properly know someone."
        a "Yeah, I guess that's true."
        c straight grin b1 "But, you are a pretty good guy, I can tell."
        c level blank "I just..."
        c left "Well..."
        c straight sad "I don't wanna insinuate anything, but..."
        c b2 left "..."
        c "I dunno..."
        a "..."
        "I was going to ask about this more, but I was interrupted by a familiar voice."
        $ cutoff = True
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    jump britreturns

label flashtalk_c_t:
    $ current_track = "None"
    stop music fadeout(3)
    c level blank "..."
    a "..."
    "We both seemed to reach the same realization that we were alone."
    "We hadn't really talked since that night in the cabin."
    if persistent.choice_20 == 1:
        "Yeah, we both agreed to never mention it again, but we weren't really sure what to talk about, instead."
    elif persistent.choice_20 == 2:
        "I was personally too scared to bring it up, and she was most likely too angry to mention it."
    "I guess some old-fashioned small talk will have to do for now."
    $ current_track = "\"Reflection\""
    play music reflection
    a "So..."
    a "How've you been?"
    c sad grin "Good, I guess."
    a "That's good."
    c blank "..."
    a "..."
    "I looked towards the coolers and saw Brittney digging around in one of them."
    "I turned back to Christeena and sighed and crossed my arms with embarrassment."
    if persistent.choice_20 == 2:
        a "...look. About that dare..."
        c level "...yeah?"
        a "I'm sorry. I really am."
        c "..."
        a "I was being stupid."
        c b2 mad "Yes. Yes, you were."
        a "..."
        a "Do you hate me? Because I wouldn't blame you if you did."
        c level "No, I don't hate you, Alex."
        c left b1 "I just thought you were...{w=1} Well..."
        c straight raised "Better than that."
        a "Oh."
        c level "But..."
        c grin "...I appreciate the fact you apologized."
        a "So, do you forgive me, then?"
        c level blank "..."
    elif persistent.choice_20 == 1:
        a "Look, I just wanna make sure everything's good between us."
        c level "..."
        a "I'll admit I was being stupid that night in the cabin."
        c b2 mad "Yes. Yes, you were."
        a "..."
        c raised "But..."
        c level grin b1 "...I appreciate that you backed out and apologized."
        c sad b2 "I already told you I forgive you, and I'm not retracting that forgiveness any time soon."
        c level blank "Just..."
        c mad "...please, please, {b}PLEASE{/b} never do anything like that again."
        a "I won't."
        c casual grin b1 "Alright, then. Things are good between us."
        a "Just like that?"
        c raised smile b2 "What, would you prefer to get on your knees and beg?"
        a "Uh...{w} Not really, no."
        $c_blink = False
        c closed_happy grin sad "Ehehe!"
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    jump britreturns

label punchtalk_c_c:
    "Christeena and I stood there somewhat awkwardly in silence before I struck up a conversation."
    show chris casual blank b1 straight
    a "So..."
    a "Donald told me something earlier."
    c raised dot "Oh?"
    a "Something about how you're more violent than you let on."
    $ current_track = "None"
    stop music fadeout(3)
    c level blank "...{w}oh."
    a "I'm not judging or anything. I'm just curious if there's any truth to that, that's all."
    a "You just don't strike me as the kind of person who would resort to that kind of thing."
    c left "..."
    a "..."
    "Well, she didn't deny it the second she had a chance."
    $ current_track = "\"Reflection\""
    play music reflection
    c sad straight b2 "Look, it's not as bad as you're probably thinking."
    c mad "It's just..."
    $ c_blush = True
    c right "...that fucking bitch..."
    a "...I'm sorry?"
    c straight "Eleanor."
    a "Ah."
    $ c_blush = False
    show chris b1 raised straight blank at close_c
    c "She just really knows how to get under my skin."
    a "And that results in you punching her or something?"
    c casual b2 "Most of the time, no."
    c level left "It's usually just your typical insults and screaming, but..."
    c sad "..."
    $ c_blush = True
    c "...sometimes, we do get into fist fights after school ends..."
    "She said that really quietly, as if she was ashamed of herself."
    a "Geez."
    c straight b1 "I'm sorry if you hate me now."
    a "I don't hate you, Christeena."
    c b2 dot "Are you sure?"
    a "Positive. {w=.5}Though, I am curious:"
    a "Who usually starts it? You or her?"
    $ c_blush = False
    show chris b1 straight level blank at close_c
    c "Well..."
    c b2 right "Do you mean who starts the punching, or who starts the whole confrontation in the first place?"
    a "..."
    a "You mean they're not the same person?"
    c sad "..."
    "Oh, boy."
    "I wanted to comment further on this, but that's when I heard a voice behind me."
    $ cutoff = True
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    jump britreturns

label tampontalk_c:
    "Christeena and I stood there somewhat awkwardly in silence before she struck up a conversation."
    c b2 straight smile sad "I haven't gotten the chance to tell you this yet, but it was pretty cool of you to let Brittney win that night."
    a "Oh, it was no problem. I honestly couldn't think of anything I could make Donald do as a dare, and she seemed like she'd enjoy the chance more than me."
    $ c_blush = True
    $c_blink = False
    c closed_happy grin "Oh, she certainly did."
    $ c_blush = False
    $c_blink = True
    show chris b2 left mad blank at close_c
    c "Although her dare easily could've been a lot less embarrassing."
    a "Uh, last I checked, DONALD was supposed to be the one embarrassed by the dare."
    c level "Well, yeah, I know."
    c b1 straight raised "Still, I don't understand how she can talk about things like this like they're no big deal."
    c mad "Case in point: the mall."
    a "I mean, personally, I don't see a big issue with girls talking about that stuff."
    a "It's no different than talking about burping or farting or other 'gross' things the human body does."
    c level "Well..."
    c b2 right "I guess you're kinda right, but it's still not something I just wanna go and talk about all the time."
    a "Well, I don't, either."
    if persistent.choice_12 == 2:
        a "Still, it's like I told you: you shouldn't let things like that bother you. She's clearly just doing it for a reaction."
    else:
        a "Still, you shouldn't let things like that bother you. She's clearly just doing it for a reaction."
    c b1 straight mad "You say that like it's so easy to not be bugged by something."
    a "Let me rephrase:{w=.5} You shouldn't let her see how much she's bothering you."
    c level "That's still not easy to do."
    $ c_blush = True
    c right "When something bothers me, I can't just sit silently and take it."
    a "Hm."
    c sad b2 "That's kinda why I always..."
    c "..."
    a "Always...?"
    $ c_blush = False
    show chris b1 straight sad blank at close_c
    c "N-Nevermind."
    a "..."
    "Before I could attempt to press her for more information, I heard a voice behind me."
    $ cutoff = True
    jump britreturns

label pushuptalk_c:
    "Christeena and I stood there somewhat awkwardly in silence before I struck up a conversation."
    show chris casual blank b1 straight
    a "Man, what a night that was in the cabin."
    c b2 sad grin "I know, right?"
    $c_blink = False
    c closed_happy smile "We found out embarrassing things about each other, and we saw Donald nearly pass out!"
    $ c_blush = True
    $c_blink = True
    c b1 straight hanging "Uh...{w} I-I didn't mean to sound so happy about that last part..."
    a "Heh heh heh. You're good."
    c b2 blank "Are you sure?"
    a "Positive."
    c left grin "O-Okay."
    a "..."
    c straight blank "..."
    "Well, this got awkward."
    $ c_blush = False
    show chris b1 straight sad blank at close_c
    c "S-Sorry."
    a "For what?"
    c right "Being awkward."
    a "..."
    "Did I say that out loud?"
    a "You don't have to apologize for being yourself, Christeena."
    c level straight "Wow. What cheesy children's story did you pull that one from?"
    a "I'm serious! I kinda like when you just say what's on your mind."
    c sad dot b2 "Why?"
    $ c_blush = True
    c left blank "Whenever I do, it's usually something stupid or hurtful."
    a "Says who?"
    $ c_blush = False
    show chris b2 straight level blank at close_c
    c "Says common sense."
    c sad b1 right "Like just now, I acted so happy that I watched my friend exhaust himself out to the point of not being able to move his arms!"
    a "Well, to be fair, at this point, it is pretty funny to look back at and laugh at."
    a "It's not like you said that right after he did the push-ups, right?"
    c straight "Well, yeah, but still..."
    c b2 left "I don't know."
    $ cutoff = True
    jump britreturns

label pondtalk_c:
    $ current_track = "None"
    stop music fadeout(3)
    "Christeena and I stood there somewhat awkwardly in silence before she struck up a conversation."
    $ current_track = "\"Reflection\""
    play music reflection
    c blank "So, uh..."
    c b2 "Have you talked to Donald about what happened that night at the pond?"
    a "Yeah, I have. Just before you got here, actually."
    c dot "And?"
    a "He said everything's good."
    c b1 blank "Are you sure?"
    a "Mhm."
    a "To quote the man, himself, he said we were 'as 'no beef' as a vegetarian buffet'."
    c left grin "I see."
    c "Well, that's good to hear, then."
    a "Yeah."
    a "What about Brittney? How's she handling it?"
    c blank "..."
    a "I mean, she HAS talked to him, right?"
    c b2 straight mad hanging "Of course she has!"
    a "And Donald forgave her, I hope?"
    c b1 level blank "Yeah, he did."
    a "So..."
    c "..."
    c right b2 sad "She's...{w}still not taking it well."
    a "Why?"
    c level straight "Well..."
    c raised b1 "I'm sure you remember that little incident at the mall, right?"
    "As tempted as I was to make a sarcastic remark..."
    a "Yeah, I remember."
    c level left dot "And how even after we agreed to just let that whole thing go, she still didn't seem to be acting like her usual self?"
    a "Right."
    c sad straight blank b2 "Well, it's basically the same thing as that."
    c right "Yeah, everything's all good and sorted away, with the person she wronged forgiving her..."
    c "...but..."
    a "But...?"
    c "She can't seem to forgive HERSELF, no matter what."
    a "Oh..."
    c straight b1 "Yeah."
    c left "It's been that way for a few years, ever since--"
    $ c_blush = True
    c small hanging casual "Ah!!"
    a "Since what?"
    $ c_blush = False
    show chris right sad blank b2 at close_c
    c "N-N-Nothing!{w=.5} F-Forget I said that last part!"
    a "..."
    "Before I could attempt to press her for more information, I heard a voice behind me."
    $ cutoff = True
    $ current_track = "\"Relaxation in the Country\""
    play music relaxation_in_the_country
    jump britreturns

label kisstalk_c_d_d:
    "Christeena and I stood there somewhat awkwardly in silence before she struck up a conversation."
    c casual blank "So, I'm curious..."
    c "Why were you willing to help Donald get a kiss from Brittney?"
    a "What do you mean?"
    c b2 level "How many things could I possibly mean?"
    "Fair point."
    a "Well, I just wanted to help out my friend."
    a "I figured he would've enjoyed it, you know?"
    c left dot "I guess..."
    a "Though, clearly, I was mistaken, right?"
    c straight sad grin b1 "I think we all were."
    c right "Still, I'm glad he decided to turn it down after seeing how little she wanted to do it."
    c mad b2 blank straight "Yeah, he can be a bit of a jerk at times..."
    c sad grin "...but he's a nice guy, at the end of the day."
    a "A jerk? How?"
    c level "Heh."
    c left b1 "Just try telling him anything he disagrees with."
    a "Such as...?"
    c mad small hanging b2 "{i}'I don\'t think God is real!'{/i} or {i}'There's nothing wrong with being gay!'{/i}"
    c raised straight blank b1 "You know. Things like that."
    $c_blink = False
    c sad closed_happy smile "Honestly, seeing him get defensive over an opinion like that is kinda funny."
    a "..."
    $ c_blush = True
    $c_blink = True
    c straight sad dot "Oh, no..."
    c blank "S-Sorry."
    a "For what?"
    c left b2 "I probably just offended you. I know you at least think God is real..."
    a "Unless it's about me, it's gonna take more than an opinion to offend me, Christeena."
    $ c_blush = False
    show chris b2 straight sad grin at close_c
    c "O-Okay, good."
    c level blank "Still, I guess that makes you more understanding than Donald..."
    a "Hm..."
    "Donald always was the kind of guy to hold true to his thoughts and beliefs no matter what, which I always admired about him."
    "Though now, if what Christeena is saying is true, this might be more serious than I had thought."
    jump britreturns
