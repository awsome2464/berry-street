init python:
    import webbrowser
    import datetime
    import subprocess
    import os
    process_list = []
    currentuser = ""
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass

image flicker:
    alpha 0.0
    "#000000"
    block:
        pause 1.0
        choice:
            ease 0.05 alpha 0.25
            ease 0.05 alpha 0.0
        choice:
            ease 0.05 alpha 0.25
            ease 0.1 alpha 0.5
            ease 0.1 alpha 0.0
        choice:
            ease 0.2 alpha 1.0
            pause 0.2
            ease 0.2 alpha 0.0
        choice:
            pass
        choice:
            pass
        choice:
            pass
        choice:
            pass
        choice:
            pass
        choice:
            pass
        choice:
            pass
        repeat

image anna_glasses:
    "CG/CG 03/Anna_Glasses.png"
    size (1920, 1080)

label judgement:
    scene bg fade
    with Pause(3)
    python:
        realdate = datetime.datetime.now()
        logno = ("{:%Y-%m-%d}")
        logdate = ("{:%A, %B %d, %Y}")
        logtime = ("{:%H:%M}")
        logmessage = ("I have taken the liberty of speaking directly to %s, the one controlling Sprouse's actions.\n\nIt would appear that perhaps there is more to this world than I had initially thought.\n\nThat perhaps that there truly is a being beyond my comprehension.\n\n\n\n\n\nAnd I do not like that thought." % currentuser)
        currentlog = "START LOG\n\n\nDATE: " + logdate.format(realdate) + "\nTIME: " + logtime.format(realdate) + "\n\n" + logmessage + "\n\n\n\nEND LOG"
        open(config.basedir + "/Logs/" + logno.format(realdate) + ".txt", "w").write(currentlog)
    play sound begin_judgement
    scene bg white
    pause 1
    show white zorder 3
    show anna_glasses zorder 2
    show bg anna zorder 1
    play music judgement
    play loop light_flicker
    show white:
        ease 2.0 alpha 0.0
    pause 2
    show anna_glasses zorder 4
    show flicker zorder 2
    pause 1
    $ show_quick_menu = True
    window show dissolve
    pause .1
    "Hello, [currentuser]."
    "At least, I am assuming that is your name, based on what I can see here."
    "I am sure you are wondering what MY name is."
    "Unfortunately for you, I will not tell you."
    "Although even an inferior mind such as yourself can infer who I am. {w}After all, you have heard my name on several occasions."
    "All of that is not important, however."
    "What IS important is that I am on to you."
    "I may not know who exactly you are."
    "I may not know why exactly you are here."
    "I may not even know how you are able to control my test subject."
    "But I assure you that I know this:"
    "You may think you are the one in control..."
    "...but you're in my territory, not the opposite."
    "So however you think you can meddle with my experiment, I will do everything in my power to stay one step ahead of you."
    "..."
    "That is all. Thank you for your time."
    "Perhaps the next time we meet, it will be under better circumstances."
    hide flicker
    window hide
    pause 2
    show white zorder 3:
        alpha 0.0
        ease 3.0 alpha 1.0
    pause 5
    show anna_glasses:
        ease 2.0 alpha 0.0
    pause 3
    $ persistent.ziphtech = False
    $ renpy.quit()

    #     "Anyway! Onto why we are here."
    #     "Seeing as this is your first time completing the entire story's demo, you have presumably made choices that adhere to what you would do in said situation."
    #     "That being said, allow me to look at your playthrough..."
    #     "..."
    #     if route == "Brittney":
    #         "I see you have gone in favor of the Usher girl."
    #         "That is not the choice I would presume most to make on their first time playing, but that is not an unreasonable choice, either."
    #         "She certainly is a bit of an odd one, I will admit."
    #         "I bet you see her as nothing more than a ridiculous 'tomboy' who cracks adult humor and likes to tease others."
    #         "Is that what you drove you towards her? Is that what interests you?"
    #         "..."
    #         "Well, let me personally assure you that there is more in that mind of hers than meets the eye."
    #         $ persistent.britroute = True
    #     elif route == "Christeena":
    #         "I see you have gone in favor of the Truman girl."
    #         "Typical."
    #         "No, really. Typical."
    #         "More often than not, when given the possible choices of characters to pursue in these sorts of scenarios..."
    #         "...people always go for the shy, quiet girl associated with purple."
    #         "So, congratulations! You are average."
    #         "Just be warned: what you expect to find within her story and what you actually find might just be two different items..."
    #         $ persistent.chrisroute = True
    #     elif route == "Donald":
    #         "I see you have gone in favor of the Waters boy."
    #         "Hm."
    #         "I am curious as to why you would want to pursue him first."
    #         "Perhaps you were curious to see what the only male-oriented route in the game would entail."
    #         "Perhaps you are romantically interested in him."
    #         "Perhaps you simply want to be friends with him."
    #         "Hm."
    #         "Well, whatever your reason, I am sure it will not be quite what you expect to find."
    #         $ persistent.donroute = True
    #     elif route == "Eleanor":
    #         "I see you have gone in favor of the Yellman girl."
    #         "..."
    #         "That can not be right..."
    #         "How on Earth could she be the one you got first?"
    #         "You do not even see her throughout most of the demo!"
    #         "..."
    #         "Well, however you managed to pull it off..."
    #         "...I'm sure you will be in for quite a surprise when the final product is released."
    #         $ persistent.eleanorroute = True
    #     else:
    #         "Hm."
    #         "It appears as though you have strucken a tie..."
    #         "..."
    #         "I suppose there is not much I can say in response to that."
    #         "Moving on."
    #     "That was my brief analysis of your first complete playthrough of {i}Berry Street{/i}."
    #     "If you would like to play again to earn a different outcome, you are within your right to."
    #     "But I do not blame you if you would rather do anything else than play this horrible game."
    #     "Either way, best of luck to you, and thank you for your time."
    #     pause 3
    #     $ config.name = _("Berry Street")
    #     return
    # else:
    #     "Welcome back, [currentuser]."
    #     if persistent.playthroughs == 2:
    #         "That IS your name, correct?"
    #         menu:
    #             "Yes.":
    #                 "As suspected."
    #             "No.":
    #                 "I see."
    #                 "Well, too bad. That is what I will still refer to you as."
    #                 "If you wish for me to call you your proper name, I suggest changing your computer settings."
    #         "Anyway, I see you have decided to play again, after all."
    #         "Why, I am not sure."
    #         "Well, if you are going to waste{nw}"
    #         "Well, if you are going to spend{fast} your time playing this game, I suppose I should do my duty and analyse your results."
    #         "..."
    #         if route == "Brittney":
    #             if persistent.britroute == True:
    #                 "Why would you attempt Usher's route again?"
    #                 "This is only a demo. You can not get a drastically different ending with the same character yet."
    #                 "..."
    #                 "If you want to waste YOUR time, fine."
    #                 "But you had better stop wasting mine."
    #                 "I am a very busy individual."
    #                 "So, either stop playing Usher's route, or stop playing altogether."
    #                 "That is all."
    #                 $ persistent.britplaythroughs = 2
    #                 pause 3
    #                 $config.name = _("Berry Street")
    #                 return
    #             else:
    #                 "I see you have gone in favor of the Usher girl."
    #                 "She certainly is a bit of an odd one, I will admit."
    #                 if persistent.chrisroute == True:
    #                     "I am curious as to who you enjoyed more: Usher or her sister, Truman."
    #                 elif persistent.donroute == True:
    #                     "Did you perhaps pursue her this time because Waters is so interested in her, and you wanted to see what her appeal was?"
    #                 elif persistent.eleanorroute == True:
    #                     "Though not nearly as odd as Yellman."
    #                 "..."
    #                 "Either way..."
    #                 "I bet you see her as nothing more than a ridiculous 'tomboy' who cracks adult humor and likes to tease others."
    #                 "..."
    #                 "Well, let me personally assure you that there is more in that mind of hers than meets the eye."
    #         elif route == "Christeena":
    #             if persistent.chrisroute == True:
    #                 "Why would you attempt Truman's route again?"
    #                 "This is only a demo. You can not get a drastically different ending with the same character yet."
    #                 "..."
    #                 "If you want to waste YOUR time, fine."
    #                 "But you had better stop wasting mine."
    #                 "I am a very busy individual."
    #                 "So, either stop playing Truman's route, or stop playing altogether."
    #                 "That is all."
    #                 $ persistent.chrisplaythroughs = 2
    #                 pause 3
    #                 $config.name = _("Berry Street")
    #                 return
    #             else:
    #                 "I see you have gone in favor of the Truman girl."
    #                 "I had suspected that most people would attempt to appeal to her first, but you clearly proved me wrong."
    #                 if persistent.britroute == True:
    #                     "I am curious as to who you enjoyed more: Truman or her sister, Usher."
    #                 elif persistent.donroute == True:
    #                     "Though to go from Waters to his exact opposite is even more baffling, to say the least."
    #                 elif persistent.eleanorroute == True:
    #                     "I suppose going from Yellman to her nemesis is seemingly understandable, however."
    #                 "..."
    #                 "Either way..."
    #                 "Just be warned: what you expect to find within her story and what you actually find might just be two different items..."
    #         elif route == "Donald":
    #             if persistent.donroute == True:
    #                 "Why would you attempt Waters's route again?"
    #                 "This is only a demo. You can not get a drastically different ending with the same character yet."
    #                 "..."
    #                 "If you want to waste YOUR time, fine."
    #                 "But you had better stop wasting mine."
    #                 "I am a very busy individual."
    #                 "So, either stop playing Water's route, or stop playing altogether."
    #                 "That is all."
    #                 $ persistent.donplaythroughs = 2
    #                 pause 3
    #                 $config.name = _("Berry Street")
    #                 return
    #             else:
    #                 "I see you have gone in favor of the Waters boy."
    #                 "I am curious as to why you would want to pursue him second."
    #                 "Perhaps you were curious to see what the only male-oriented route in the game would entail."
    #                 "Perhaps you are romantically interested in him."
    #                 "Perhaps you simply want to be friends with him."
    #                 "Hm."
    #                 "Well, whatever your reason, I am sure it will not be quite what you expect to find."
    #         elif route == "Eleanor":
    #             if persistent.eleanorroute == True:
    #                 "Why would you attempt Yellman's route again?"
    #                 "This is only a demo. You can not get a drastically different ending with the same character yet."
    #                 "..."
    #                 "If you want to waste YOUR time, fine."
    #                 "But you had better stop wasting mine."
    #                 "I am a very busy individual."
    #                 "So, either stop playing Water's route, or stop playing altogether."
    #                 "That is all."
    #                 $ persistent.eleanorplaythroughs = 2
    #                 pause 3
    #                 $config.name = _("Berry Street")
    #                 return
    #             else:
    #                 "I see you have gone in favor of the Yellman girl."
    #                 "..."
    #                 "That can not be right..."
    #                 "How on Earth could she be the one you appealed to the most?"
    #                 "You do not even see her throughout most of the demo!"
    #                 "..."
    #                 "Well, however you managed to pull it off..."
    #                 "...I'm sure you will be in for quite a surprise when the final product is released."
    #         else:
    #             "..."
    #             "A tie."
    #             "Lovely."
    #         "This concludes this analysis of your second playthrough of {i}Berry Street{/i}."
    #         "Seeing as how you HAVE completed it twice, it is likely that you wish to play again."
    #         "Again, I am not sure why, but that is your choice."
    #         "Once again, thank you for your time."
    #         pause 3
    #         $config.name = _("Berry Street")
    #         return

        #else:
