###############
# Phone Stuff #
###############

label showphone(who):
    window hide dissolve
    pause 0.1
    show screen alex_phone(who)
    pause 0.5
    return

label showtext(who, what):
    show screen text_message(who, what)
    pause
    hide screen text_message
    pause 0.1
    return

label hidephone:
    hide screen alex_phone
    pause 0.5
    window show dissolve
    pause 0.1
    return


style textname:
    outlines [(1.0, "#000000", 0.0, 0.0)]
    font "fonts/LemonMilk.otf"
    italic True
    size 25

style textmessage:
    outlines [(1.0, "#000000", 0.0, 0.0)]
    font "fonts/LemonMilk.otf"
    italic True
    size 40

style contact:
    outlines [(1.0, "#000000", 0.0, 0.0)]
    size 90


transform pick_up_phone:
    xalign 0.5 yalign 0.5
    alpha 0.0
    yoffset 1000
    ease 0.5 yoffset 0 alpha 1.0
    on hide:
        ease 0.5 yoffset 1000 alpha 0.0

transform contact_name:
    xalign 0.834 yalign 0.21
    alpha 0.0
    yoffset 1000
    ease 0.5 yoffset 0 alpha 1.0
    on hide:
        ease 0.5 yoffset 1000 alpha 0.0

transform new_message:
    yoffset 100
    alpha 0
    easein 0.1 alpha 1 yoffset 0
    on hide:
        ease 0.1 yoffset 30 alpha 0


screen alex_phone(who):
    zorder 100
    add "phone.png" at pick_up_phone
    frame at contact_name:
        background None
        xsize 829 ysize 162
        xalign 0.832 yalign 0.25
        text who style "contact" xalign 0.5 yalign 0.5

screen text_message(who, what):
    zorder 100
    frame:
        background None
        xsize 829 ysize 728
        xalign 0.832 yalign 1.0
        vbox:
            if who == "Alex":
                xalign 0.99 yalign 0.1
            else:
                xalign 0.015 yalign 0.1
            frame at new_message:
                if who == "Alex":
                    background Solid("d8ff00")
                else:
                    if groupchat:
                        if who == "Brittney":
                            background Solid("8d002c")
                        elif who == "Christeena":
                            background Solid("ca7bff")
                    else:
                        background Solid("00ccff")
                xpadding 10 ypadding 5
                if who == "Alex":
                    vbox:
                        text what style "textmessage" xalign 1.0
                else:
                    vbox:
                        if groupchat:
                            text who style "textname" xalign 0.0
                            null height 5
                        text what style "textmessage" xalign 0.0

