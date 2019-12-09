# Resets everything when the game ends
init python:
    import shutil
    import glob

label newgame:
    python:
        
        # 6-03-13
        persistent.choice_1 = 0
        persistent.choice_2 = 0
        persistent.choice_3 = 0

        # 6-04-13
        persistent.choice_4 = 0
        persistent.choice_5 = 0
        persistent.choice_6 = 0
        persistent.choice_7 = 0

        persistent.tour_1 = 0
        persistent.tour_2 = 0
        persistent.tour_3 = 0
        persistent.tour_4 = 0

        # 6-11-13
        persistent.choice_8 = 0

        # 6-21-13
        persistent.choice_9 = 0
        persistent.choice_10 = 0

        # 6-23-13
        persistent.choice_11 = 0
        persistent.choice_12 = 0
        persistent.choice_13 = 0
        persistent.choice_14 = 0
        persistent.choice_15 = 0
        persistent.choice_16 = 0
        persistent.choice_17 = 0

        # 6-30-13
        persistent.choice_18 = 0
        persistent.choice_19 = 0
        persistent.choice_20 = 0
        persistent.choice_21 = 0
        persistent.choice_22 = 0

        # 7-04-13
        persistent.choice_23 = 0
        persistent.choice_23_ = 0
        persistent.choice_24 = 0
        persistent.choice_25 = 0
        persistent.choice_26 = 0

        # 7-10-13
        persistent.choice_27 = 0
        persistent.choice_28 = 0
        persistent.choice_29 = 0
        persistent.choice_30 = 0

        # 7-15-13
        persistent.choice_31 = 0
        persistent.choice_32 = 0

    return
