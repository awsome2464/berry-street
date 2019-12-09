# Never Have I Ever Screens and Styles

style nhie_top_points:
    xalign 0.015
    yalign 0.5

style nhie_bot_points:
    xalign 0.01
    yalign 0.25

screen timer_c:
    hbox:
        xalign 0.95
        yalign 0.95
        frame:
            xysize(300, 75)
            hbox:
                xalign 0.5
                yalign 0.5
                text "[hours] hour(s), [minutes] minute(s), [seconds] second(s)"

screen don_points:
    hbox:
        style "nhie_top_points"
        text "[nhie_d_points]" size 75

screen finger_points:
    vbox:
        spacing 75
        style "nhie_top_points"
        text "[nhie_d_points]" size 113
        text "[nhie_c_points]" size 113
        text "[nhie_b_points]" size 113
        text "[nhie_a_points]" size 113
    vbox:
        spacing 159
        style "nhie_bot_points"
        text "Donald"
        text "Christeena"
        text "Brittney"
        text "Alex"

# Development Only

screen char_points:
    hbox:
        xalign 0.05
        yalign 0.95
        text "[B_Points] [C_Points] [D_Points]"

screen route_select:
    hbox:
        xalign 0.05
        yalign 0.05
        textbutton "Brittney" action [SetVariable("B_Points", 10), SetVariable("C_Points", 0), SetVariable("D_Points", 1)]
        textbutton "Christeena" action [SetVariable("B_Points", 0), SetVariable("C_Points", 9), SetVariable("D_Points", 2)]
        textbutton "Donald" action [SetVariable("B_Points", 0), SetVariable("C_Points", 1), SetVariable("D_Points", 6)]
        textbutton "Eleanor" action [SetVariable("B_Points", 0), SetVariable("C_Points", 0), SetVariable("D_Points", 0)]

# Calendar

screen calendarOs():
    if currentmonth == "June":
        if progress >= 1:
            add "full_circle" xalign 0.37 yalign 0.41
        if progress >= 2:
            add "full_circle" xalign 0.435 yalign 0.41
        if progress >= 3:
            add "full_circle" xalign 0.435 yalign 0.53
        if progress >= 4:
            add "full_circle" xalign 0.625 yalign 0.65
        if progress >= 5:
            add "full_circle" xalign 0.31 yalign 0.77
    elif currentmonth == "July":
        if progress >= 6:
            add "full_circle" xalign 0.56 yalign 0.39
        if progress >= 7:
            add "full_circle" xalign 0.5 yalign 0.51

# Day Select

screen dayselectmenu():
    tag menu
    add 'gui/pause_bg.png' xalign 0.5 yalign 0.5
    vbox:
        xalign 0.25
        yalign 0.5
        spacing 5
        frame:
            xysize(240,128)
            xalign 0.5
            yalign 0.5
            text "{size=+10}[dayselectmenuvalue]" xalign 0.5 yalign 0.5
        frame:
            xysize(450,525)
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 5
                if dayselectmenuvalue == "June, 2013":
                    if day_2 == True:
                        textbutton "{size=+5}{b}June 3rd, 2013":
                            hovered SetVariable("daydesc", 1)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("firstdayreplay", scope={"B_Points": 0, "D_Points": 0, "h_hair": True, "replay": True})
                    else:
                        textbutton "{size=+20}{font=gui/libel-suit-rg.ttf}???" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day_3 == True:
                        textbutton "{size=+5}{b}June 4th, 2013":
                            hovered SetVariable("daydesc", 2)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("tour", scope={"B_Points": June3B, "C_Points": June3C, "D_Points": June3D, "h_hair": True, "b_hat": True, "replay": True, "progress": 1})
                    else:
                        textbutton "{size=+20}{font=gui/libel-suit-rg.ttf}???" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day_4 == True:
                        textbutton "{size=+5}{b}June 11th, 2013":
                            hovered SetVariable("daydesc", 3)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("shoppingwithharry", scope={"B_Points": June4B, "delifoodorder": delifoodorder, "acceptsandwich": acceptsandwich, "britnotpretty": britnotpretty, "b_hat": False, "replay": True, "progress": 2})
                    else:
                        textbutton "{size=+20}{font=gui/libel-suit-rg.ttf}???" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day_5 == True:
                        textbutton "{size=+5}{b}June 21st, 2013":
                            hovered SetVariable("daydesc", 4)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("unpack0621", scope={"C_Points": June11C, "D_Points": June11D, "delihangout": delihangout, "replay": True, "progress": 3})
                    else:
                        textbutton "{size=+20}{font=gui/libel-suit-rg.ttf}???" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day_6 == True:
                        textbutton "{size=+5}{b}June 23rd, 2013":
                            hovered SetVariable("daydesc", 5)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("churchends", scope={"B_Points": June21B, "C_Points": June21C, "D_Points": June21D, "E_Points": June21E, "B_Basketball": B_Basketball, "britnotpretty": britnotpretty, "cleaningpartner": cleaningpartner, "b_hat": False, "replay": True, "progress": 4})
                    else:
                        textbutton "{size=+20}{font=gui/libel-suit-rg.ttf}???" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day_7 == True:
                        textbutton "{size=+5}{b}June 30th, 2013":
                            hovered SetVariable("daydesc", 6)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("nhie_start", scope={"B_Points": June23B, "C_Points": June23C, "D_Points": June23D, "b_hat": False, "replay": True, "progress": 5})
                    else:
                        textbutton "{size=+20}{font=gui/libel-suit-rg.ttf}???" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                elif dayselectmenuvalue == "July, 2013":
                    if day_8 == True:
                        textbutton "{size=+5}{b}July 4th, 2013":
                            hovered SetVariable("daydesc", 1)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("donbirthday", scope={"B_Points": June30B, "C_Points": June30C, "D_Points": June30D, "h_hair": True, "b_hat": True, "replay": True})
                    else:
                        textbutton "{size=+20}{font=gui/libel-suit-rg.ttf}???" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day_9 == True:
                        textbutton "{size=+5}{b}July 10th, 2013{/b}{/size}":
                            hovered SetVariable("daydesc", 2)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("swimming", scope={"B_Points": July4B, "C_Points": July4C, "D_Points": July4D, "b_hat": False, "c_hair": 1, "replay": True})
                    else:
                        textbutton "{size=+20}{font=gui/libel-suit-rg.ttf}???" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
    vbox:
        xalign 0.85
        yalign 0.55
        frame:
            xysize(750, 225)
            if daydesc == -1:
                text "???" xalign 0.5 yalign 0.5
            if daydesc == 0:
                text ""
            if daydesc == 1:
                if dayselectmenuvalue == "June, 2013":
                    text "The Sprouses move to Smalltown, and Alex reunites with and meets some friends." xalign 0.5 yalign 0.5
                elif dayselectmenuvalue == "July, 2013":
                    text "The gang enjoys a day of fun for Donald's 17th birthday party." xalign 0.5 yalign 0.5
            if daydesc == 2:
                if dayselectmenuvalue == "June, 2013":
                    text "Donald gives Alex a tour of Smalltown with the help of Brittney and Christeena." xalign 0.5 yalign 0.5
                elif dayselectmenuvalue == "July, 2013":
                    text "The gang beats the heat with a day at the pond." xalign 0.5 yalign 0.5
            if daydesc == 3:
                text "Against Alex's will and desire, Alex and Harry go shopping at Dolmart." xalign 0.5 yalign 0.5
            if daydesc == 4:
                text "Donald and Christeena come over to help the Sprouses finish unpacking." xalign 0.5 yalign 0.5
            if daydesc == 5:
                text "Alex, Brittney, and Christeena all go shopping for gifts for Donald's birthday." xalign 0.5 yalign 0.5
            if daydesc == 6:
                text "Donald brings the gang to the cabin for an exciting game of {i}Never Have I Ever{/i}." xalign 0.5 yalign 0.5
            if daydesc == 7:
                text "It's a day of relaxation and celebration for Donald's 17th birthday party." xalign 0.5 yalign 0.5

    hbox:
        xalign 0.05
        yalign 0.95
        frame:
            ysize 75
            textbutton "  {b}Back{/b}  " action ShowMenu('save') xalign 0.5 yalign 0.5

    if dayselectmenuvalue != "June, 2013":
        hbox:
            xalign 0.15
            yalign 0.95
            frame:
                xysize(225, 75)
                textbutton "{b}Previous{/b}":
                    action ToggleVariable('dayselectmenuvalue', 'June, 2013') xalign 0.5 yalign 0.5


    if day_8 == True and dayselectmenuvalue != "July, 2013":
        hbox:
            xalign 0.95
            yalign 0.95
            frame:
                xysize(150, 75)
                textbutton "{b}Next{/b}":
                    if dayselectmenuvalue == "June, 2013":
                        action ToggleVariable('dayselectmenuvalue', "July, 2013") xalign 0.5 yalign 0.5

# Music Room

screen music_room:
    tag menu
    add 'gui/main_menu.png'
    add 'gui/pause_bg.png' xalign 0.5 yalign 0.5
    vbox:
        xalign 0.8 yalign 0.5
        null height 5
        textbutton "1. Welcome to Berry Street!" action [ToggleVariable('persistent.current_track', 'Welcome to Berry Street!'), mr.Play("<to 76 loop 8>music/Welcome to Berry Street.ogg")]
        textbutton "2. New Life" action [ToggleVariable('persistent.current_track', 'New Life'), mr.Play("<loop 14.769>music/New Life.ogg")]
        textbutton "3. Oddball" action [ToggleVariable('persistent.current_track', 'Oddball'), mr.Play("music/Oddball.ogg")]
        textbutton "4. Violet Wonder" action [ToggleVariable('persistent.current_track', 'Violet Wonder'), mr.Play("<loop 9.6>music/Violet Wonder.ogg")]
        textbutton "5. Brotato Chips" action [ToggleVariable('persistent.current_track', 'Brotato Chips'), mr.Play("<to 68 loop 12>music/Brotato Chips.ogg")]
        textbutton "6. Chaotic Evil" action [ToggleVariable('persistent.current_track', 'Chaotic Evil'), mr.Play("music/Chaotic Evil.ogg")]
        textbutton "7. Ivories and Ebony" action [ToggleVariable('persistent.current_track', 'Ivories and Ebony'), mr.Play("<loop 3>music/Ivories and Ebony.ogg")]
        textbutton "8. Different Yet Equal" action [ToggleVariable('persistent.current_track', "Different Yet Equal"), mr.Play("music/Different Yet Equal.ogg")]
        textbutton "9. Home Life" action [ToggleVariable('persistent.current_track', "Home Life"), mr.Play("<to 112 loop 5.32>music/Home Life.ogg")]
        textbutton "10. Relaxation in the Country" action [ToggleVariable('persistent.current_track', 'Relaxation in the Country'), mr.Play("<loop 5.333>music/Relaxation in the Country.ogg")]
        textbutton "11. Reflection" action [ToggleVariable('persistent.current_track', 'Reflection'), mr.Play("music/Reflection.ogg")]
        textbutton "12. Chillaxin\'" action [ToggleVariable('persistent.current_track', 'Chillaxin\''), mr.Play("<loop 18>music/Chillaxin.ogg")]
        textbutton "13. The Pond" action [ToggleVariable('persistent.current_track', 'The Pond'), mr.Play("music/The Pond.ogg")]
        textbutton "14. Outside the Street" action [ToggleVariable('persistent.current_track', 'Outside the Street'), mr.Play("music/Outside the Street.ogg")]
        textbutton "15. Dinin' In" action [ToggleVariable('persistent.current_track', 'Dinin\' In'), mr.Play("<loop 9.6>music/Dinin' In.ogg")]
        textbutton "16. The Mall" action [ToggleVariable('persistent.current_track', 'The Mall'), mr.Play("<loop 15>music/The Mall.ogg")]
        textbutton "17. Friendly Competition" action [ToggleVariable('persistent.current_track', 'Friendly Competition'), mr.Play("music/Friendly Competition.ogg")]
        textbutton "18. Cabin Fever" action [ToggleVariable('persistent.current_track', 'Cabin Fever'), mr.Play("<loop 8>music/Cabin Fever.ogg")]
        textbutton "19. Sunday Service" action [ToggleVariable('persistent.current_track', 'Sunday Service'), mr.Play("music/Sunday Service.ogg")]
        textbutton "20. Generic 80s Song" action [ToggleVariable('persistent.current_track', 'Generic 80s Song'), mr.Play("music/Generic 80s Song.ogg")]

        null height 20

        textbutton "Back" action ShowMenu('extras')

        null height 5

    add "gui/record.png" at record_move_musicroom

screen extras:
    tag menu
    add "gui/pause_bg.png" xalign 0.5 yalign 0.5
    frame:
        xysize(450,450)
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 25
            textbutton "Music Room" action ShowMenu('music_room')
            textbutton "Good Tales Social Media" action ShowMenu('social_media')
            textbutton "Patreon" action OpenURL('https://www.patreon.com/goodtalesvn')
            textbutton "Credits" action [ToggleVariable('persistent.credits', True), Jump('credits')]
            null height 10
            textbutton "Back" action ShowMenu('main_menu')

screen social_media:
    tag menu
    add 'gui/main_menu.png'
    add "gui/pause_bg.png"
    frame:
        xysize(450,300)
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            textbutton "Discord Server" action OpenURL('https://discord.gg/zZhPrkC')
            textbutton "Instagram" action OpenURL('https://instagram.com/goodtalesvn')
            textbutton "Twitter" action OpenURL('https://twitter.com/goodtalesvn')
            null height 10
            textbutton "Back" action ShowMenu('extras')

screen notify(message):
    zorder 100
    text message at _notify_transform
    timer 3.0 action Hide('notify')

transform _notify_transform:
    xalign 0.9 yalign 0.1
    on show:
        alpha 0
        ease 0.25 alpha 1.0
    on hide:
        alpha 1
        ease 0.25 alpha 0.0

image ctc_arrow:
    xalign 0.82 yalign 0.98
    "gui/click_arrow.png"
    block:
        linear 0.15 xalign 0.825
        linear 0.15 xalign 0.82
        repeat

screen ctc():
    zorder 100
    add "ctc_arrow"

screen skipchoice:
    hbox:
        xalign 0.95
        yalign 0.95
        textbutton "Next Choice":
            if nextchoice == 1:
                action Jump("choice2")
            elif nextchoice == 2:
                action Jump("choice3")
            elif nextchoice == 3:
                action Jump("progressday01")
            elif nextchoice == 4:
                action Jump("choice4")
            elif nextchoice == 5:
                action Jump("choice5")
            elif nextchoice == 6:
                action Jump("choice6")
            elif nextchoice == 7:
                action Jump("choice7")
            elif nextchoice == 8:
                action Jump("progressday02")
            elif nextchoice == 9:
                action Jump("choice8")
            elif nextchoice == 10:
                action Jump("progressday03")
            elif nextchoice == 11:
                action Jump("choice9")
            elif nextchoice == 12:
                action Jump("progressday04")

label show_phone:



    show phone_bg zorder 1:
        alpha 0.0
        xalign 0.5
        linear 0.5 alpha 1.0
    show phone_base zorder 3:
        alpha 0.0
        xalign 0.5
        linear 0.5 alpha 1.0
    show phone_sender zorder 2:
        alpha 0.0
        xalign 0.47 yalign 0.98
        linear 0.5 alpha 1.0

# screen reset:
#     hbox:
#         xalign 0.95
#         yalign 0.05
#         textbutton "Reset":
#             action persistent.choice_1 = 0
#             action persistent.choice_2 = 0
#             action persistent.choice_3 = 0
#             action persistent.choice_4 = 0
#             action persistent.choice_5 = 0
#             action persistent.choice_6 = 0
#             action persistent.choice_7 = 0
#             action persistent.choice_8 = 0
#             action persistent.choice_9 = 0
#             action persistent.choice_10 = 0
#             action persistent.choice_11 = 0
#             action persistent.choice_12 = 0

# screen show_char_points:
#     hbox:
#         xalign 0.1
#         yalign 0.95
#         textbutton "Toggle":
#             action Function(incTotal)
#             if char_points_toggle == 0:
#                 hide screen char_points
#                 return
#             if char_points_toggle == 1:
#                 show screen char_points
#                 return
#             if char_points_toggle == 2:
#                 $ char_points_toggle = 0
#                 hide screen char_points
#                 return