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