﻿# Welcome to the script for Berry Street!

init -999 python:
    if not persistent.ziphtech:
        persistent.gamename = "Berry Street"
        persistent.ziphtech_label = "gui/textbox.png"
        persistent.game_text = "fonts/libel-suit-rg.ttf"
        persistent.custom_icon = "gui/window_icon.png"
    else:
        persistent.gamename = "ZiphTech"
        persistent.ziphtech_label = "gui/ziphtech_textbox.png"
        persistent.game_text = "fonts/Audiowide-Regular.ttf"
        persistent.custom_icon = "gui/ziphtech_icon.png"

default persistent.playthroughs = 0
default persistent.progress = -1
default persistent.customdialogue = False

style build:
    font "fonts/LibbyRegular.ttf"
    color "#ffffff"
    outlines [(absolute(1), "#000000", absolute(0), absolute(0))]
    size 25

image build = ParameterizedText(style='build')

label splashscreen:
    $ persistent.credits = False

    scene bg fade

    if persistent.ziphtech:
        jump judgement

    if not persistent.agree:
        "WARNING: Berry Street contains content not suitable for younger audiences, including strong language and sexual humor."
        "By proceeding, you acknowledge the potential events that are to come and are at least 15 years old and/or of a mature age."
        "Press {i}'I Agree'{/i} to acknowledge these facts.{nw}"
        menu:
            "Press {i}'I Agree'{/i} to acknowledge these facts.{fast}"

            "I Agree":
                $ persistent.agree = True
                with Pause(1)
            "I Don't Agree":
                $ renpy.quit()

    if persistent.Build_Name != "May 1st, 2019 Build":
        show text "Berry Street is currently in development. Everything you see and hear is subject to change." with dissolve
        $renpy.pause(delay=5)
        hide text with dissolve
        $ persistent.Build_Name = "May 1st, 2019 Build"

    play music main_theme
    with Pause(1)
    show splash at truecenter zorder 2 with dissolve
    with Pause(2)
    hide splash with dissolve
    pause 0.5
    return

label before_main_menu:
    $ persistent.current_track = 'Welcome to Berry Street!'
    scene bg bs zorder 1:
        yalign 0.0
        linear 3.0 yalign 1.0
    with dissolve
    pause 0.5
    show title_logo zorder 4:
        xalign 0.5 yalign -.2
        ease 1.5 yalign 0.03
    if persistent.progress == -1:
        show menu_01 zorder 4:
            xalign 0.5 yalign 1.25
            ease 2.0 yalign 0.9
    else:
        show menu_02 zorder 4:
            xalign 0.5 yalign 1.25
            ease 2.0 yalign 0.9
    show build "[persistent.Build_Name]" zorder 4:
        xalign 0.99 yalign 1.34
        ease 2.0 yalign 0.99
    if persistent.elie_completed:
        show eleanor_title zorder 2:
            alpha 0.0
            xalign -0.2 yalign 0.5
            pause 0.3
            parallel:
                ease 1.5 alpha 1.0
            parallel:
                ease 1.0 xalign 0.0
    if persistent.don_completed:
        show donald_title zorder 2:
            alpha 0.0
            xalign 1.2 yalign 0.5
            pause 0.3
            parallel:
                ease 1.5 alpha 1.0
            parallel:
                ease 1.0 xalign 1.0
    if persistent.chris_completed:
        show christeena_title zorder 2:
            alpha 0.0
            xalign 0.0 yalign 0.1
            pause 0.6
            parallel:
                ease 1.5 alpha 1.0
            parallel:
                ease 1.0 xalign 0.2
    if persistent.brit_completed:
        show brittney_title zorder 2:
            alpha 0.0
            xalign 0.98 yalign 0.2
            pause 0.6
            parallel:
                ease 1.5 alpha 1.0
            parallel:
                ease 1.0 xalign .78
    if persistent.brit_completed and persistent.chris_completed and persistent.don_completed and persistent.elie_completed:
        show alex_title zorder 3:
            alpha 0.0
            xalign 0.5
            ypos 0.2
            pause 0.9
            parallel:
                ease 1.3 alpha 1.0
            parallel:
                ease 1.0 ypos 0.051
    pause 2

    return

label start:
    if persistent.credits:
        $ persistent.credits = False
        return
    if persistent.customdialogue:
        scene bg house_ut
        window hide
        $b_hat = True
        $b_partial = True
        show brit a2 sad right opened_smile at middle
        $renpy.pause()
    # Tracking your progress through the story, with the 'progress' variable being added to as each new section is completed.
    # This system is only here because the call method was glitching for some odd reason, but this seems to be working.
    # \/\/\/
label progress:
    # Moving to Berry Street, Reuniting with Donald, Hanging Out with Brittney
    # \/\/\/ 13_06_03.rpy
    if progress == 0:
        python:
            os.chdir(config.basedir + "/Logs/")
            twentythirteenlogs = glob.glob("2013-*.txt")
            for filename in twentythirteenlogs:
                os.remove(filename)
            twentyfourteenlogs = glob.glob("2014-*.txt")
            for filename in twentyfourteenlogs:
                os.remove(filename)
            persistent.todays_date = "June 3rd, 2013"
        jump firstday
    # elif progress == 7:
    #     call logs from _call_logs
    #     window hide dissolve
    #     stop music fadeout 5
    #     with Pause(1)
    #     show white zorder 3:
    #         alpha 0.0
    #         ease 3.0 alpha 1.0
    #     pause 5
    #     call credits from _call_credits
    #     python:
    #         players = {"Brittney": B_Points, "Christeena": C_Points, "Donald": D_Points}
    #         route = max(players, key=players.get)
    #         if route == "Brittney":
    #             persistent.brit_completed = True
    #         elif route == "Christeena":
    #             persistent.chris_completed = True
    #         elif route == "Donald":
    #             persistent.don_completed = True
    #         if E_Points >= 1:
    #             persistent.elie_completed = True
    #         persistent.playthroughs += 1
    #         persistent.progress = -1
    #         if persistent.playthroughs == 1:
    #             persistent.ziphtech = True
    #     call newgame from _call_newgame
    #     return
    else:
        window hide dissolve
        $ current_track = "None"
        stop music fadeout 3.0
        pause 1.0
        scene bg fade
        with Dissolve(2.0)
        pause 2
        call logs from _call_logs_1

        if progress == 1:
            # Touring the Town
            #\/\/\/ 13_06_04.rpy
            python:
                persistent.progress = 1
                day_2 = True
                June3B = B_Points
                June3C = C_Points
                June3D = D_Points
                June3E = E_Points
                
            jump tour

        elif progress == 2:
            # Shopping with Harry, Lunch at Kelly's, Hang with Brittney
            #\/\/\/ 13_06_11.rpy
            python:
                persistent.progress = 2
                day_3 = True
                June4B = B_Points
                June4C = C_Points
                June4D = D_Points
                June4E = E_Points
                
            jump shoppingwithharry

        elif progress == 3:
            # Unpacking
            #\/\/\/ 13_06_21.rpy
            python:
                persistent.progress = 3
                day_4 = True
                June11B = B_Points
                June11C = C_Points
                June11D = D_Points
                June11E = E_Points
                
            jump unpack0621

        elif progress == 4:
            # Back from church, shopping with Brit and Chris
            #\/\/\/ 13_06_23.rpy
            python:
                persistent.progress = 4
                day_5 = True
                June21B = B_Points
                June21C = C_Points
                June21D = D_Points
                June21E = E_Points
                
            jump churchends

        elif progress == 5:
            # Never Have I Ever
            #\/\/\/ 13_06_30.rpy
            python:
                persistent.progress = 5
                day_6 = True
                June23B = B_Points
                June23C = C_Points
                June23D = D_Points
                June23E = E_Points
                
            jump nhie_start

        elif progress == 6:
            call logs from _call_logs_2
            # Donald's Birthday
            #\/\/\/ 13_07_04.rpy
            python:
                persistent.progress = 6
                day_7 = True
                June30B = B_Points
                June30C = C_Points
                June30D = D_Points
                June30E = E_Points
                current_track = "None"
                
            jump donbirthday

        elif progress == 7:
            # Swimming at the Pond
            #\/\/\/ 13_07_10.rpy
            python:
                persistent.progress = 7
                day_8 = True
                July4B = B_Points
                July4C = C_Points
                July4D = D_Points
                July4E = E_Points
                current_track = "None"
            jump swimming

        elif progress == 8:
            # Baseball Game
            #\/\/\/ 13_07_15.rpy
            python:
                persistent.progress = 8
                day_9 = True
                July10B = B_Points
                July10C = C_Points
                July10D = D_Points
                July10E = E_Points
                current_track = "None"
            jump baseball

default logno = "2013-06-03"
default logdate = "Monday, June 03, 2013"
default logtime = "22:15"
default logmessage = "The new family arrived today, right on schedule.\n\nThe elder son has spent the afternoon with Waters and Usher while the remaining Sprouses moved their belongings into the house.\n\nThey seem to have suspected nothing out of the ordinary.\n\nAs long as it remains that way, the experiment can proceed as planned."

label logs:
    python:
        players = {"Brittney": B_Points, "Christeena": C_Points, "Donald": D_Points}
        route = max(players, key=players.get)
        if progress == 1:
            pass
        elif progress == 2:
            logno = "2013-06-04"
            logdate = "Tuesday, June 04, 2013"
            logtime = "18:25"
            logmessage = "The Sprouse boy has met Truman, and the four teenagers have spent their day touring the town together.\n\nWhile their comments about me being a machine do not bother me in any way, it is worth noting that comment for record's sake.\n\nRather uneventful day for the experiment, other than that, but as long as everything stays according to plan, we should see changes soon."
        elif progress == 3:
            logno = "2013-06-11"
            logdate = "Tuesday, June 11, 2013"
            logtime = "20:45"
            if delihangout:
                logmessage = "How fascinating of a day for the experiment.\n\nWhile Sprouse's grocery trip was relatively boring sans his brief encounter with Yellman, his decision to join Usher for her meal certainly caught my attention.\n\nDid he do it to spend time with her out of pity, friendship, or romantic interest?\n\nTime will tell if he does anything else regarding an interest in Usher going forward."
            else:
                logmessage = "How fascinating of a day for the experiment.\n\nWhile Sprouse's grocery trip was relatively boring sans his brief encounter with Yellman, his decision to not join Usher for her meal certainly caught my attention.\n\nDid he do it to respect her wishes or because he has no interest in her, whether it be romantic or not?\n\nTime will tell if he does anything else regarding rejecting Usher going forward."
        elif progress == 4:
            logno = "2013-06-21"
            logdate = "Friday, June 21, 2013"
            logtime = "21:35"
            if cleaningpartner == "Christeena":
                if route == "Christeena":
                    logmessage = "Sprouse asked Truman to help him today.\n\nA very interesting choice.\n\nHe has proven to be interested in her the most via his previous choices; will he continue to follow this pattern?"
                else:
                    logmessage = "Sprouse asked Truman to help him today.\n\nA very interesting choice.\n\nWhile Truman is not the neighbor he has previously appealed to the most, he still chose her. What could this mean?"
            else:
                if route == "Donald":
                    logmessage = "Sprouse asked Waters to help him today.\n\nA very interesting choice.\n\nHe has proven to be interested in him the most via his previous choices; will he continue to follow this pattern?"
                else:
                    logmessage = "Sprouse asked Waters to help him today.\n\nA very interesting choice.\n\nWhile Waters is not the neighbor he has previously appealed to the most, he still chose him. What could this mean?"
        elif progress == 5:
            logno = "2013-06-23"
            logdate = "Sunday, June 23, 2013"
            logtime = "16:55"
            if persistent.choice_12 == 1:
                messagepart01 = "going alone to a video game store and Sprouse and Usher going together to a sports store.\n\n"
                if persistent.choice_14 == 1:
                    messagepart02 = "The latter two also ran like fools throughout the mall in some sort of race. Waste of energy, I say.\n\n"
                else:
                    messagepart02 = "The latter also ran like a fool throughout the mall in some sort of race while Sprouse didn't follow suit. Quite a pleasure to see him have some sense.\n\n"
            elif persistent.choice_12 == 2:
                messagepart01 = "and Sprouse going to a video game store and Usher going alone to a sports store.\n\nTruman spent time talking about Waters and her not-so subtle dislike of him. One wonders if this could affect Sprouse's thoughts and feelings of him.\n\n"
                messagepart02 = ""
            else:
                messagepart01 = "going to a video game store, Usher going to a sports store, and Sprouse going to an art store.\n\nThe most interesting aspect was Sprouse encountering Yellman for a second time.\n\n"
                if persistent.choice_15 == 1 and persistent.choice_16 == 2:
                    messagepart02 = "He actually had the strength to talk to her, despite her obvious disinterest. This could certainly show that Sprouse is willing to be friendly to those others see unworthy.\n\n"
                else:
                    messagepart02 = "He didn't muster the strength to hold a conversation with her. This could certainly show that Sprouse is perhaps a bit cowardly, or like the other 3, who are unwilling to show compassion for those they don't see worthy of it.\n\n"
            logmessage = "Sprouse, Usher, and Truman went shopping for Waters today. Cute.\n\nThe trio split among themselves at the shopping mall, with Truman " + messagepart01 + messagepart02 + "I suppose I could tell Waters what they all purchased for him, but that time could easily be spent doing other things."
        elif progress == 6:
            logno = "2013-06-30"
            logdate = "Sunday, June 30, 2013"
            logtime = "23:10"
            if persistent.choice_18 == 1:
                messagepart01 = "Usher from the game first.\n\n"
                if persistent.choice_19 == 2:
                    messagepart02 = "However, in a surprise move, he allowed Truman to win. It's currently unclear why this move was made, but it is certainly worth mentioning.\n\n"
                elif persistent.choice_20 == 1:
                    messagepart02 = "In an expected move, Sprouse also won the competition, allowing Usher to perform a dare for him, the dare in question being a kiss. Typical teenage male behavior.\n\n"
                elif persistent.choice_20 == 2:
                    messagepart02 = "In an expected move, Sprouse also won the competition, allowing Usher to perform a dare for him, the dare in question being for her to kiss Waters. Certainly a very interesting move.\n\n"
                elif persistent.choice_20 == 3:
                    messagepart02 = "In an expected move, Sprouse also won the competition, allowing Usher to perform a dare for him, the dare in question being for her to punch Waters. Few things bring me true joy, but I will admit that seeing that brought a small smile to my face.\n\n"
            elif persistent.choice_18 == 2:
                messagepart01 = "Truman from the game first.\n\n"
                if persistent.choice_19 == 1:
                    messagepart02 = "In an expected move, Sprouse also won the competition, allowing Truman to perform a dare for him, the dare in question being a kiss. Typical teenage male behavior.\n\n"
                elif persistent.choice_19 == 2:
                    messagepart02 = "In an expected move, Sprouse also won the competition, allowing Truman to perform a dare for him, the dare in question being for her to show him her bare breasts. Typical teenage male behavior.\n\n"
                elif persistent.choice_19 == 3:
                    messagepart02 = "In an expected move, Sprouse also won the competition, allowing Truman to perform a dare for him, the dare in question being for her to punch Waters. Few things bring me true joy, but I will admit that seeing that brought a small smile to my face.\n\n"
            else:
                messagepart01 = "Waters from the game first.\n\n"
                if persistent.choice_19 == 2:
                    messagepart02 = "However, in a surprise move, he allowed Usher to win. It's currently unclear why this move was made, but it is certainly worth mentioning.\n\n"
                elif persistent.choice_20 == 1:
                    messagepart02 = "In an expected move, Sprouse also won the competition, allowing Waters to perform a dare for him, the dare in question being for him to perform pushups. I have no explanation for the logic behind this decision.\n\n"
                elif persistent.choice_20 == 2:
                    messagepart02 = "In an expected move, Sprouse also won the competition, allowing Waters to perform a dare for him, the dare in question being for him to jump into the local pond. I suppose that given that the average temperature of said pond at this time of night is around 7 degrees Celsius, that is a fair punishment.\n\n"
                elif persistent.choice_20 == 3:
                    messagepart02 = "In an expected move, Sprouse also won the competition, allowing Waters to perform a dare for him, the dare in question being for him to kiss Usher. What a rather interesting turn of events.\n\n"
            logmessage = "After an uneventful morning and afternoon from Sprouse, he, along with Usher, Truman, and Waters, met up in their cabin for a dare game of sorts. I knew from the very beginning that this would only end in disaster.\n\nThe game ended with Sprouse eliminating " + messagepart01 + messagepart02
        elif progress == 7:
            logno = "2013-07-04"
            logdate = "Thursday, July 04, 2013"
            logtime = "22:15"
            realdate = datetime.datetime.now()
            years_in_future = realdate.year - 2013
            logmessage = ("Sensors have indicated that the experiment might not be as fair as I had initially thought.\n\nAs impossible as it might seem, we may be dealing with an outside force, not too dissimilar to a god, although that title would imply they created this world.\n\nNo matter their title, they also appear to be from the future. %s years in the future, to be precise.\n\nIf they ever return, I'll be sure to have a word with them about their meddling." % years_in_future)

        currentlog = "START LOG\n\n\nDATE: " + logdate + "\nTIME: " + logtime + "\n\n" + logmessage + "\n\n\n\nEND LOG"
        open(config.basedir + "/Logs/" + logno + ".txt", "w").write(currentlog)
    return
