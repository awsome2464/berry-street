transform credit_scroll:
    xalign 0.5 yalign 1.3
    linear 15.0 yalign -0.2

style credit_text:
    font "fonts/libel-suit-rg.ttf"
    color "#ffffff"
    text_align 0.5
    outlines [(absolute(2), "#000000", absolute(2), absolute(2))]

image credit_text_1 = ParameterizedText(style="credit_text")
image credit_text_2 = ParameterizedText(style="credit_text")
image credit_text_3 = ParameterizedText(style="credit_text")
image credit_text_4 = ParameterizedText(style="credit_text")
image credit_text_5 = ParameterizedText(style="credit_text")
image credit_text_6 = ParameterizedText(style="credit_text")
image credit_text_7 = ParameterizedText(style="credit_text")
image credit_text_8 = ParameterizedText(style="credit_text")
image credit_text_9 = ParameterizedText(style="credit_text")
image credit_text_10 = ParameterizedText(style="credit_text")
image credit_text_11 = ParameterizedText(style="credit_text")
image credit_text_12 = ParameterizedText(style="credit_text")
image credit_text_13 = ParameterizedText(style="credit_text")
image credit_text_14 = ParameterizedText(style="credit_text")
image credit_text_15 = ParameterizedText(style="credit_text")
image credit_text_16 = ParameterizedText(style="credit_text")
image credit_text_17 = ParameterizedText(style="credit_text")
image credit_text_18 = ParameterizedText(style="credit_text")
image credit_text_19 = ParameterizedText(style="credit_text")
image credit_text_20 = ParameterizedText(style="credit_text")

label credits:
    $config.skipping = False
    $config.allow_skipping = False
    play music credits
    scene bg bs:
        xalign 0.5 yalign 0.0
    show title:
        size (843.04, 211.2)
        xalign 0.5 yalign 0.5
    with Dissolve(1.0)
    pause 4.0
    show bg bs:
        linear 62.0 yalign 1.0
    show title:
        linear 20.0 yalign -2.0
    show credit_text_1 "{size=+10}Writing, Art, and Development{/size}" at credit_scroll
    pause 1.0
    show credit_text_2 "Cole Goodrich" at credit_scroll
    pause 3.0
    show credit_text_3 "{size=+10}Custom Music{/size}" at credit_scroll
    pause 1.0
    show credit_text_4 "Cole Goodrich and Cara Richman" at credit_scroll
    pause 3.0
    show credit_text_5 "{size=+10}Placeholder Music{/size}" at credit_scroll
    pause 1.0
    show credit_text_6 "{size=+5}'Scrapbook'{/size}" at credit_scroll
    pause 0.5
    show credit_text_7 "by Silent Partner" at credit_scroll
    pause 3.0
    show credit_text_8 "{size=+10}Sound Effects{/size}" at credit_scroll
    pause 1.0
    show credit_text_9 "FreeSound.org" at credit_scroll
    pause 3.0
    show credit_text_10 "{size=+10}Placeholder Backgrounds{/size}" at credit_scroll
    pause 1.0
    show credit_text_11 "Google Images" at credit_scroll
    pause 3.0
    show credit_text_12 "{size=+10}Testers{/size}" at credit_scroll
    pause 1.0
    show credit_text_13 "Silas Stewart" at credit_scroll
    pause 0.5
    show credit_text_14 "Cara Richman" at credit_scroll
    pause 0.5
    show credit_text_15 "LaddieCruz" at credit_scroll
    pause 0.5
    show credit_text_16 "Luchiini" at credit_scroll
    pause 0.5
    show credit_text_17 "Maddy" at credit_scroll
    pause 0.5
    show credit_text_18 "Skytigers456" at credit_scroll
    pause 0.5
    show credit_text_19 "WiggleJiggle" at credit_scroll
    pause 0.5
    show credit_text_20 "Tsuri" at credit_scroll
    pause 0.5
    show credit_text_1 "Yurishii" at credit_scroll
    pause 0.5
    show credit_text_2 "HazardSquare" at credit_scroll
    pause 0.5
    show credit_text_3 "SlightlySimple" at credit_scroll
    pause 3.0
    show credit_text_4 "{size=+10}Made with Ren'Py 7.2.2{/size}" at credit_scroll
    pause 3.0
    show credit_text_5 "{size=+10}Special Thanks{/size}" at credit_scroll
    pause 1.0
    show credit_text_6 "{size=+5}God{/size}" at credit_scroll
    pause 0.5
    show credit_text_7 "For blessing me with everything He has provided" at credit_scroll
    pause 1.5
    show credit_text_8 "{size=+5}Tom \"PyTom\" Rothamel{/size}" at credit_scroll
    pause 0.5
    show credit_text_9 "For creating the Ren'Py engine" at credit_scroll
    pause 1.5
    show credit_text_10 "{size=+5}Team Salvato{/size}" at credit_scroll
    pause 0.5
    show credit_text_11 "Whose first visual novel inspired the creation of this one" at credit_scroll
    pause 1.5
    show credit_text_12 "{size=+5}Silas Stewart{/size}" at credit_scroll
    pause 0.5
    show credit_text_13 "For being Berry Street's #1 fan!" at credit_scroll
    pause 1.5
    show credit_text_14 "{size=+5}The Ren'Py Discord Server and Devtalk+{/size}" at credit_scroll
    pause 0.5
    show credit_text_15 "For being helpful, supportive, and aw{s}e{/s}some places to be!" at credit_scroll
    pause 1.5
    show credit_text_16 "{size=+5}My Family and Friends{/size}" at credit_scroll
    pause 0.5
    show credit_text_17 "For being so supportive, no matter what." at credit_scroll
    pause 1.5
    show credit_text_18 "{size=+5}You{/size}" at credit_scroll
    pause 0.5
    show credit_text_19 "For playing this demo. Hope to see you back at the full release!" at credit_scroll
    pause 0.5
    show credit_text_20 "If you wish to support Berry Street's development, check out its Patreon page! (link in the 'Extras' menu!)" at credit_scroll
    pause 13.0
    show white zorder 4:
        alpha 0.0
        ease 2.0 alpha 1.0
    pause 3
    show fade zorder 1
    show splash zorder 2:
        size(1536, 864)
        xalign 0.5 yalign 0.6
    show credit_text_1 "{size=+15}Made with love by{/size}" zorder 3:
        xalign 0.5 yalign 0.05
    show white:
        ease 2.0 alpha 0.0
    stop music fadeout(7)
    pause 5
    scene bg fade
    with Dissolve(3)
    pause 1
    $ config.allow_skipping = True
    return
