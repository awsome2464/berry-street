label eleanor_phone_number:
    # Context:
    # Alex and Eleanor were just paired up in a school project
    # Alex approaches Eleanor after class ends
    python:
        current_track = "Getting Educated"
        E_Name = "Eleanor"
        outfit_e = "d"
    play music getting_educated
    scene bg school_hall
    a "Hey!"
    show elie p1 left neutral blank at middle with dissolve
    pause 0.1
    "She was still within view, but moving away quickly."
    "I picked up the pace and caught up."
    show elie:
        ease 0.5 close_e
    pause 0.6
    a "Hey, Eleanor?"
    show elie casual straight
    "She turned around and stopped that time."
    e level "Oh.{w=0.2} What do you want?"
    "The amount of hatred radiating off of this woman, I swear..."
    a "Well, we're gonna be partners, so it would help if we had a way to keep in touch."
    e neutral left "It's not like you don't know where I live."
    a "I mean, yeah, but still. Can I at least have your number so we can work out a time to meet?"
    e_s "..."
    e right level "Alright, whatever."
    a "Thanks."
    "I took out my phone and opened up a new contact."
    "It's weird to be getting THE Eleanor Yellman's phone number, but a guy's gotta do what a guy's gotta do."
    a "Alright, go."
    e straight "It's eight-six-seven..."
    a "Eight-six-seven..."
    e "Five-three-oh-nine."
    a "Five-th--"
    "I stopped before looking up at her with annoyance."
    a "C'mon, I'm being serious here."
    e casual "Wait, you actually know what that means?"
    a "You do realize I'm only, like, 2 years younger than you, right?"
    "Not that that really matters, since that song is older than both of us by over a decade."
    e left level "Hm.{w=0.2} Alright, fine."
    "She then told me her ACTUAL number.{w=0.2} I made sure to text her as a test first just to verify she wasn't fucking with me again."
    a "Alright, cool.{w=0.2} Thanks."
    e straight neutral "Sure."
    hide elie with dissolve
    pause 0.1
    "With that, she continued down the hall to her next class."


label eleanor_guessing:
    # Context:
    # Alex and Eleanor are hanging out at her house early on into her route.
    # One of the first few times they've hung out outside of school.
    # We at one point learn that Eleanor as a boyfriend/sugar daddy in Chicago who pays for her every need, inlucuding house payments.
    python:
        current_track = "Home of One"
        E_Name = "Eleanor"
        outfit_e = "a"
        e_cig = True
    play music home_of_one
    scene bg living_e
    show elie p1 straight blank raised at close_e
    e "Trust me; I may be an open book, but even I have things about me that nobody knows."
    a "Such as?"
    show elie left level
    "She stared off in thought for a few seconds, taking a long draw from her cigarette as she did."
    show elie straight raised grin
    "Finally, she looked back at me with a sneaky grin while giving the butt a light tap."
    e "Alright, here's one you'll never get:"
    e "How many guys do you think I've fucked?"
    "Well, that question came straight out of left field."
    a "Uh..."
    e mad "C'mon, be honest. In my 18 years of living, how many guys do you think I've fucked?"
    a "Uh...{nw}"
    menu:
        a "Uh...{fast}"

        "2 or 3":
            a "2 or 3?"
            e raised left "Hm. Reasonable guess."
        "5 to 10":
            a "5 to 10?"
            e level "Heh. That's what most people guess."
        "More than 10":
            a "More than 10?"
            e level right blank "Well, I wasn't aware I looked like THAT much of a slut."

    e straight raised grin "Wanna know the answer?"
    a "Sure."
    "I mean, it's none of my business, but if she's insisting on telling me..."
    show elie mad
    "She then gave a small chuckle."
    e "You'll never believe it."
    a "We'll see about that."
    "She then looked at me in silence for a moment before holding up one finger."
    "I stared at her hand for a few seconds."
    a "..."
    a "No way."
    e raised "What did I tell you?"
    a "You...{w=0.5} You've seriously only fucked ONE guy in your life?"
    e casual "I may be a cunt, but I'm a loyal cunt."
    a "Wow. I'm impressed."
    e level left blank "Of course, you get those classmates and neighbors who like to think you go around and fuck anything with a cock between its legs."
    a "I mean, can you really blame them?"
    e mad straight frown "Yes."
    a "...{w=0.5}um, okay let me rephrase:"
    a "Would you expect them to think anything different?"
    e "Yes.{w=0.2} I'd expect them to mind their own goddamn business and not worry about my sex life."
    a "Uh..."
    "I guess she's not necessarily wrong."
    e raised blank "Besides, what do you mean \"Can you really blame them\"?"
    a "Well, I mean..."
    a "You don't exactly come off as a girl who's loyal to one guy."
    e neutral "Why? Because I wear tops that have a tiny fraction of my tits hanging out?"
    "What exactly is her definition of tiny?"
