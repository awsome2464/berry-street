label eleanor_guessing:
    # Context:
    # Alex and Eleanor are hanging out at her house early on into her route.
    # One of the first few times they've hung out outside of school.
    # We at one point learn that Eleanor as a boyfriend/sugar daddy in Chicago who pays for her every need, inlucuding house payments.
    python:
        current_track = "Home of One"
        E_Name = "Eleanor"
        outfit_e = "a"
    play music home_of_one
    scene bg living_e
    show elie p1 straight blank raised at close_e
    e "Trust me; I may be an open book, but even I have things about me that nobody believes."
    a "Such as?"
    show elie left level
    "She stared off in thought for a few seconds, taking a long draw from her cigarette as she did."
    show elie straight raised grin
    "Finally, she looked back at me with a sneaky grin while giving the butt a light tap."
    e "Alright, here's one nobody ever gets right:"
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
    a "Hold on."
    a "Are you saying...?"
    e raised "What did I tell you?"
    a "You...{w=0.5} You've seriously only fucked ONE guy in your life?"
    e casual "I may be a cunt, but I'm a loyal cunt."
    a "Wow. I'm impressed."
    e level left blank "Of course, you get those classmates and neighbors who like to think you go around and fuck anything with a cock between its legs."
    a "I mean, can you really blame them?"
    e mad straight frown "Yes."
    a "Um, okay let me rephrase:"
    a "Would you expect them to think anything different?"
    e "Yes."
    e "I'd expect them to mind their own goddamn business and not worry about my sex life."
    a "Uh..."
    "I guess she's not necessarily wrong."
    e raised blank "Besides, what do you mean \"Can you really blame them\"?"
    a "Well, I mean..."
    a "You don't exactly come off as a girl who's loyal to one guy."
    e neutral "Why? Because I wear tops that have a tiny fraction of my tits hanging out?"
    "What exactly is her definition of tiny?"
