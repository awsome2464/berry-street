# Never Have I Ever Screens and Styles

style nhie_top_points:
    xalign 0.015
    yalign 0.5

style nhie_bot_points:
    xalign 0.01
    yalign 0.25

screen timer_c():
    hbox:
        xalign 0.95
        yalign 0.95
        frame:
            xysize(300, 75)
            hbox:
                xalign 0.5
                yalign 0.5
                text "[hours] hour(s), [minutes] minute(s), [seconds] second(s)"

screen don_points():
    hbox:
        style "nhie_top_points"
        text "[nhie_d_points]" size 75

screen finger_points():
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

screen char_points():
    hbox:
        xalign 0.05
        yalign 0.95
        text "[B_Points] [C_Points] [D_Points]"

screen route_select():
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
        xalign 0.25 yalign 0.5
        spacing 5
        frame:
            xysize(240,128)
            xalign 0.5 yalign 0.5
            text "{size=+10}[dayselectmenuvalue]{/size}" xalign 0.5 yalign 0.5
        frame:
            xysize(450,525)
            vbox:
                xalign 0.5 yalign 0.5
                spacing 5
                if dayselectmenuvalue == "June, 2013":
                    if day >= 2:
                        textbutton "{size=+5}{b}June 3rd, 2013{/b}{/size}":
                            hovered SetVariable("daydesc", 1)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("firstdayreplay", scope={"B_Points": 0, "D_Points": 0, "h_hair": True, "replay": True})
                    else:
                        textbutton "{size=+20}{font=fonts/libel-suit-rg.ttf}???{/font}{/size}" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day >= 3:
                        textbutton "{size=+5}{b}June 4th, 2013{/b}{/size}":
                            hovered SetVariable("daydesc", 2)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("tour", scope={"B_Points": monthpoints["June3B"], "D_Points": monthpoints["June3D"], "h_hair": True, "b_hat": True, "replay": True, "progress": 1})
                    else:
                        textbutton "{size=+20}{font=fonts/libel-suit-rg.ttf}???{/font}{/size}" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day >= 4:
                        textbutton "{size=+5}{b}June 11th, 2013{/b}{/size}":
                            hovered SetVariable("daydesc", 3)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("shoppingwithharry", scope={"B_Points": monthpoints["June4B"], "delifoodorder": delifoodorder, "acceptsandwich": acceptsandwich, "britnotpretty": britnotpretty, "b_hat": False, "replay": True, "progress": 2})
                    else:
                        textbutton "{size=+20}{font=fonts/libel-suit-rg.ttf}???{/font}{/size}" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day >= 5:
                        textbutton "{size=+5}{b}June 21st, 2013{/b}{/size}":
                            hovered SetVariable("daydesc", 4)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("unpack0621", scope={"C_Points": monthpoints["June3B"], "D_Points": monthpoints["June3D"], "delihangout": delihangout, "replay": True, "progress": 3})
                    else:
                        textbutton "{size=+20}{font=fonts/libel-suit-rg.ttf}???{/font}{/size}" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day >= 6:
                        textbutton "{size=+5}{b}June 23rd, 2013{/b}{/size}":
                            hovered SetVariable("daydesc", 5)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("churchends", scope={"B_Points": monthpoints["June11B"], "C_Points": monthpoints["June21C"], "B_Basketball": B_Basketball, "britnotpretty": britnotpretty, "cleaningpartner": cleaningpartner, "b_hat": False, "replay": True, "progress": 4})
                    else:
                        textbutton "{size=+20}{font=fonts/libel-suit-rg.ttf}???{/font}{/size}" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day >= 7:
                        textbutton "{size=+5}{b}June 30th, 2013{/b}{/size}":
                            hovered SetVariable("daydesc", 6)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("nhie_start", scope={"B_Points": monthpoints["June23B"], "C_Points": monthpoints["June23C"], "D_Points": monthpoints["June21D"], "b_hat": False, "replay": True, "progress": 5})
                    else:
                        textbutton "{size=+20}{font=fonts/libel-suit-rg.ttf}???{/font}{/size}" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                elif dayselectmenuvalue == "July, 2013":
                    if day >= 8:
                        textbutton "{size=+5}{b}July 4th, 2013{/b}{/size}":
                            hovered SetVariable("daydesc", 1)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("donbirthday", scope={"B_Points": monthpoints["June30B"], "C_Points": monthpoints["June30C"], "D_Points": monthpoints["June30D"], "h_hair": True, "b_hat": True, "replay": True})
                    else:
                        textbutton "{size=+20}{font=fonts/libel-suit-rg.ttf}???{/font}{/size}" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
                    if day >= 9:
                        textbutton "{size=+5}{b}July 10th, 2013{/b}{/size}":
                            hovered SetVariable("daydesc", 2)
                            unhovered SetVariable("daydesc", 0)
                            action Replay("swimming", scope={"B_Points": monthpoints["July4B"], "C_Points": monthpoints["July4C"], "D_Points": monthpoints["July4D"], "b_hat": False, "c_hair": 1, "replay": True})
                    else:
                        textbutton "{size=+20}{font=fonts/libel-suit-rg.ttf}???{/font}{/size}" xalign 0.5:
                            hovered SetVariable("daydesc", -1)
                            unhovered SetVariable("daydesc", 0)
                            action NullAction()
    vbox:
        xalign 0.85 yalign 0.55
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


    if day >= 8 and dayselectmenuvalue != "July, 2013":
        hbox:
            xalign 0.95
            yalign 0.95
            frame:
                xysize(150, 75)
                textbutton "{b}Next{/b}":
                    if dayselectmenuvalue == "June, 2013":
                        action ToggleVariable('dayselectmenuvalue', "July, 2013") xalign 0.5 yalign 0.5

# Music Room

screen music_room():
    tag menu
    add 'gui/main_menu.png'
    add 'gui/pause_bg.png' xalign 0.5 yalign 0.5
    frame:
        xpadding 50 ypadding 25
        xalign 0.8 yalign 0.5
        vbox:
            xalign 0.5 yalign 0.5
            null height 5
            textbutton "01. Welcome to Berry Street!" action [ToggleVariable('persistent.current_track', 'Welcome to Berry Street!'), mr.Play("<to 76 loop 8>audio/music/Welcome to Berry Street.ogg")]
            textbutton "02. New Life" action [ToggleVariable('persistent.current_track', 'New Life'), mr.Play("<loop 14.769>audio/music/New Life.ogg")]
            textbutton "03. Oddball" action [ToggleVariable('persistent.current_track', 'Oddball'), mr.Play("audio/music/Oddball.ogg")]
            textbutton "04. Violet Wonder" action [ToggleVariable('persistent.current_track', 'Violet Wonder'), mr.Play("<loop 9.6>audio/music/Violet Wonder.ogg")]
            textbutton "05. Brotato Chips" action [ToggleVariable('persistent.current_track', 'Brotato Chips'), mr.Play("<to 68 loop 12>audio/music/Brotato Chips.ogg")]
            textbutton "06. Chaotic Evil" action [ToggleVariable('persistent.current_track', 'Chaotic Evil'), mr.Play("audio/music/Chaotic Evil.ogg")]
            textbutton "07. Ivories and Ebony" action [ToggleVariable('persistent.current_track', 'Ivories and Ebony'), mr.Play("<loop 3>audio/music/Ivories and Ebony.ogg")]
            textbutton "08. Different Yet Equal" action [ToggleVariable('persistent.current_track', "Different Yet Equal"), mr.Play("audio/music/Different Yet Equal.ogg")]
            textbutton "09. Home Life" action [ToggleVariable('persistent.current_track', "Home Life"), mr.Play("<to 112 loop 5.32>audio/music/Home Life.ogg")]
            textbutton "10. Relaxation in the Country" action [ToggleVariable('persistent.current_track', 'Relaxation in the Country'), mr.Play("<loop 5.333>audio/music/Relaxation in the Country.ogg")]
            textbutton "11. Reflection" action [ToggleVariable('persistent.current_track', 'Reflection'), mr.Play("audio/music/Reflection.ogg")]
            textbutton "12. Chillaxin\'" action [ToggleVariable('persistent.current_track', 'Chillaxin\''), mr.Play("<loop 18>audio/music/Chillaxin.ogg")]
            textbutton "13. The Pond" action [ToggleVariable('persistent.current_track', 'The Pond'), mr.Play("audio/music/The Pond.ogg")]
            textbutton "14. Outside the Street" action [ToggleVariable('persistent.current_track', 'Outside the Street'), mr.Play("audio/music/Outside the Street.ogg")]
            textbutton "15. Dinin' In" action [ToggleVariable('persistent.current_track', 'Dinin\' In'), mr.Play("<loop 9.6>audio/music/Dinin' In.ogg")]
            textbutton "16. Getting Educated" action [ToggleVariable('persistent.current_track', 'Getting Educated'), mr.Play("<to 108 loop 4>audio/music/Getting Educated.ogg")]
            textbutton "17. The Mall" action [ToggleVariable('persistent.current_track', 'The Mall'), mr.Play("<loop 15>audio/music/The Mall.ogg")]
            textbutton "18. Friendly Competition" action [ToggleVariable('persistent.current_track', 'Friendly Competition'), mr.Play("audio/music/Friendly Competition.ogg")]
            textbutton "19. Cabin Fever" action [ToggleVariable('persistent.current_track', 'Cabin Fever'), mr.Play("<loop 8>audio/music/Cabin Fever.ogg")]
            textbutton "20. Sunday Service" action [ToggleVariable('persistent.current_track', 'Sunday Service'), mr.Play("audio/music/Sunday Service.ogg")]
            textbutton "21. Generic 80s Song" action [ToggleVariable('persistent.current_track', 'Generic 80s Song'), mr.Play("audio/music/Generic 80s Song.ogg")]

            null height 20

            textbutton "Back" action ShowMenu('extras')

            null height 5

    add "gui/record.png" at record_move_musicroom

screen gallery():
    tag menu
    add "gui/main_menu.png"
    add "gui/pause_bg.png" xalign 0.5 yalign 0.5
    frame:
        xpadding 50 ypadding 25
        xalign 0.5 yalign 0.5
        hbox:
            xalign 0.5 yalign 0.5
            spacing 50
            add gal.make_button("cg_1", "cg1_gal", xalign=0.5, yalign=0.5) at gallery
            add gal.make_button("cg_2", "CG/CG 02/CG_02.png", xalign=0.5, yalign=0.5) at gallery
    frame:
        xalign 0.5 yalign 0.99
        xpadding 5 ypadding 5
        textbutton "Back" action ShowMenu('extras') xalign 0.5 yalign 0.5

screen extras():
    tag menu
    add "gui/pause_bg.png" xalign 0.5 yalign 0.5
    frame:
        xpadding 50 ypadding 25
        xalign 0.5 yalign 0.5
        vbox:
            xalign 0.5 yalign 0.5
            spacing 25
            textbutton "Music Room" action ShowMenu('music_room')
            textbutton "Gallery" action ShowMenu('gallery')
            textbutton "Good Tales Social Media" action ShowMenu('social_media')
            textbutton "Patreon" action OpenURL('https://www.patreon.com/goodtalesvn')
            textbutton "Credits" action [ToggleVariable('persistent.credits', True), Jump('credits')]
            null height 10
            textbutton "Back" action ShowMenu('main_menu')

screen social_media():
    tag menu
    add 'gui/main_menu.png'
    add "gui/pause_bg.png"
    frame:
        xysize(450,300)
        xalign 0.5 yalign 0.5
        vbox:
            xalign 0.5 yalign 0.5
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
