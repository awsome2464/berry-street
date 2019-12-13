##############
# Characters #
##############

# Main
define a = Character("Alex", callback=a_voice, what_prefix='"', what_suffix='"')
define b = Character("[B_Name]", callback=b_voice, image="brit", what_prefix='"', what_suffix='"')
define bc = Character("Brit and Chris", what_prefix='"', what_suffix='"')
define bd = Character("Brit and Don", callback=bd_voice, what_prefix='"', what_suffix='"')
define c = Character("[C_Name]", callback=c_voice, image="chris", what_prefix='"', what_suffix='"')
define ct = Character("Mr. Truman", callback=ct_voice, image="chad", what_prefix='"', what_suffix='"')
define da = Character("Daniel", callback=da_voice, image="daniel", what_prefix='"', what_suffix='"')
define d = Character("Donald", callback=d_voice, image="don", what_prefix='"', what_suffix='"')
define e = Character("[E_Name]", callback=e_voice, image="elie", what_prefix='"', what_suffix='"')
define f = Character("Dad", callback=f_voice, image="fred", what_prefix='"', what_suffix='"')
define g = Character("Mom", callback=g_voice, image="ginger", what_prefix='"', what_suffix='"')
define gr = Character("Greeter", what_prefix='"', what_suffix='"')
define h = Character("Harry", callback=h_voice, image="harry", what_prefix='"', what_suffix='"')
define hr = Character("Mr. Rodriguez", image="hector", what_prefix='"', what_suffix='"')
define j = Character("Mrs. Waters", callback=j_voice, image="janice", what_prefix='"', what_suffix='"')
define k = Character("[K_Name]", callback=k_voice, image="kelly", what_prefix='"', what_suffix='"')
define l = Character("Mr. Waters", callback=l_voice, image="latrell", what_prefix='"', what_suffix='"')
define mu = Character("[M_Name]", callback=m_voice, image="martha", what_prefix='"', what_suffix='"')
define p = Character("[P_Name]", callback=p_voice, image="percy", what_prefix='"', what_suffix='"')
define ump = Character("Umpire", what_prefix='"', what_suffix='"')
define unknown = Character(" ???", what_prefix='"', what_suffix='"')
define wo = Character("Woman", what_prefix='"', what_suffix='"')

# Offscreen
define b_o = Character("[B_Name]", callback=b_offscreen, what_prefix='"', what_suffix='"')
define c_o = Character("[C_Name]", callback=c_offscreen, what_prefix='"', what_suffix='"')
define da_o = Character("Daniel", callback=da_offscreen, what_prefix='"', what_suffix='"')
define d_o = Character("Donald", callback=d_offscreen, what_prefix='"', what_suffix='"')
define e_o = Character("[E_Name]", callback=e_offscreen, what_prefix='"', what_suffix='"')
define f_o = Character("Dad", callback=f_offscreen, what_prefix='"', what_suffix='"')
define g_o = Character("Mom", callback=g_offscreen, what_prefix='"', what_suffix='"')
define h_o = Character("Harry", callback=h_offscreen, what_prefix='"', what_suffix='"')
define m_o = Character("[M_Name]", callback=m_offscreen, what_prefix='"', what_suffix='"')
define p_o = Character("[P_Name]", callback=p_offscreen, what_prefix='"', what_suffix='"')

# Silent
define a_s = Character("Alex", what_prefix='"', what_suffix='"')
define b_s = Character("[B_Name]", image="brit", what_prefix='"', what_suffix='"')
define c_s = Character("[C_Name]", image="chris", what_prefix='"', what_suffix='"')
define d_s = Character("Donald", image="don", what_prefix='"', what_suffix='"')
define e_s = Character("[E_Name]", image="elie", what_prefix='"', what_suffix='"')
define h_s = Character("Harry", image="harry", what_prefix='"', what_suffix='"')
define mu_s = Character("[M_Name", image="martha", what_prefix='"', what_suffix='"')

# Texting
define narrate = nvl_narrator
define a_nvl = Character("Alex", what_color="#d7d400", what_outlines=[(1, "#000000")], kind=nvl)
define b_nvl = Character("Brittney", what_color="#7c0000", what_outlines=[(1, "#000000")], kind=nvl)
define c_nvl = Character("Christeena", what_color="#5a00ae", what_outlines=[(1, "#000000")], kind=nvl)
define d_nvl = Character("Donald", what_color="#ff0000", what_outlines=[(1, "#000000")], kind=nvl)
define unknown_nvl = Character("???", what_color="#424242", what_outlines=[(1, "#ffffff")], kind=nvl)

###############
# Backgrounds #
###############

image bg fade = "#000000"
image bg white = "#ffffff"
image bg car:
    "BG/Backseat View.png"
    zoom 0.75
image bg house_s:
    zoom 0.75
    "BG/Sprouse House.png"
image bg house_ut:
    zoom 0.75
    "BG/Usher Truman House.png"
image bg house_w:
    "BG/Waters House.png"
    zoom 0.75
image bg house_w_s:
    "BG/Waters House Sunset.png"
    zoom 0.75
image bg living_w:
    "BG/Waters Living Room.png"
    zoom 0.75
image bg basketball_w:
    "BG/Waters Basketball Hoop.png"
    zoom 0.75
image bg living_s_m:
    "BG/Living Room Moving.png"
    size(1920, 1080)
image bg bedroom_a_m:
    "BG/Alex Bedroom Moving.png"
    zoom 0.75
image bg living_ut:
    "BG/Usher Truman Living Room.png"
    zoom 0.75
image bg house_ro:
    "BG/Rodriguez House.png"
    zoom 0.75
image bg house_z:
    "BG/Ziphon House.png"
    zoom 0.75
image bg house_re:
    "BG/Reagan House.png"
    zoom 0.75
image bg house_y:
    zoom 0.75
    "BG/Yellman House.png"
image bg house_n:
    "BG/Nanner House.png"
    zoom 0.75
image bg pond:
    zoom 0.75
    "BG/Pond.png"
image bg pond_n:
    zoom 0.75
    "BG/Pond Night.png"
image bg cabin_e:
    "BG/Cabin Exterior.png"
    zoom 0.75
image bg cabin_e_s:
    "BG/Cabin Exterior Sunset.png"
    zoom 0.75
image bg cabin_i:
    "BG/Cabin Interior.png"
    zoom 0.75
    xalign 0.5
image bg cabin_i_s:
    "BG/Cabin Interior Sunset.png"
    zoom 0.75
    xalign 0.5
image bg cabin_i_n:
    "BG/Cabin Interior Night.png"
    zoom 0.75
    xalign 0.5
image bg mainstreet:
    "BG/Main Street.png"
    zoom 0.75
image bg deli_e:
    "BG/Kelly's Deli Exterior.png"
    zoom 0.75
image bg deli_i_e:
    "BG/Kelly's Deli Entrance.png"
    zoom 0.75
image bg deli_i_wb:
    "BG/Kelly's Deli Window Booth.png"
    zoom 0.75
    xalign 0.0
image deli_table:
    "BG/Kelly's Deli Window Booth Table.png"
    zoom 0.75
    xalign 0.0
image bg porch_ut:
    "BG/Porch Usher Truman.png"
    zoom 0.75
image bg bs:
    "BG/Berry Street.png"
    yalign 1.0
    zoom 0.75
image bg school_e:
    "BG/School Entrance.png"
    zoom 0.75
image bg dolmart_e:
    "BG/Dolmart Exterior.png"
    zoom 0.75
image bg dolmart_i:
    "BG/Dolmart Interior.png"
    zoom 0.75
image bg game_menu:
    "BG/game_menu.png"
    zoom 0.75
image bg church_e:
    "BG/Church Exterior.png"
    zoom 0.75
image bg mall_e:
    "BG/Mall Exterior.png"
    zoom 0.75
image bg mall_i:
    "BG/Mall Interior.png"
    zoom 0.75
image bg sports:
    "BG/Sport Store.png"
    zoom 0.75
image bg games:
    "BG/Game Store.png"
    zoom 0.75
image bg art:
    "BG/Art Store.png"
    zoom 0.75
image bg mall_fc:
    "BG/Food Court.png"
    zoom 0.75
image bg backyard_w:
    "BG/Backyard_Waters.png"
    zoom 0.75
image bg anna:
    "CG/CG 03/CG_03.png"
    zoom 0.75
image bg woods:
    zoom 0.75
    "BG/Woods.png"
image bg baseball:
    "BG/Baseball Field.png"
    zoom 0.75
image baseball_overlay:
    "BG/Baseball Field Overlay.png"
    zoom 0.75
image bg conveniencestore:
    "BG/Convenience Store.png"
    zoom 0.75

##########
# Images #
##########

image splash:
    "Good Tales Transparent.png"
    size(1920, 1080)
image title = "Title.png"
image title_logo:
    "gui/logo.png"
    size(479, 120)
image main_menu = "gui/main_menu.png"
image fade = "#000000"
image white = "#ffffff"
image nhie = "NHIE.png"
image start_button = "gui/start_idle.png"
image start_locked = "gui/start_locked.png"
image load_button = "gui/load_idle.png"
image load_locked = "gui/load_locked.png"
image options_button = "gui/options_idle.png"
image extras_button = "gui/extras_idle.png"
image quit_button = "gui/quit_idle.png"
image menu_01 = "gui/menu_intro_01.png"
image menu_02 = "gui/menu_intro_02.png"
image record = "gui/record.png"
image phone_base = "Phone/base.png"
image phone_bg = "Phone/bg.png"
image phone_receiver = "Phone/receiver.png"
image phone_sender = "Phone/sender.png"

image pond_foreground:
    "BG/Pond_02.png"
    zoom 0.75
image deli_entrance_sign:
    "BG/Kelly's Deli Entrance Sign.png"
    zoom 0.75

image calendar_circle:
    size(136.5, 121.5)
    "Calendars/Circle/Circle_00.png"
    pause 1.0
    "Calendars/Circle/Circle_01.png"
    pause 0.025
    "Calendars/Circle/Circle_02.png"
    pause 0.025
    "Calendars/Circle/Circle_03.png"
    pause 0.025
    "Calendars/Circle/Circle_04.png"
    pause 0.025
    "Calendars/Circle/Circle_05.png"
    pause 0.025
    "Calendars/Circle/Circle_06.png"
    pause 0.025
    "Calendars/Circle/Circle_07.png"
    pause 0.025
    "Calendars/Circle/Circle_08.png"
    pause 0.025
    "Calendars/Circle/Circle_09.png"
    pause 0.025
    "Calendars/Circle/Circle_10.png"
    pause 0.025
    "Calendars/Circle/Circle_11.png"
    pause 0.025
    "Calendars/Circle/Circle_12.png"
    pause 0.025
    "Calendars/Circle/Circle_13.png"
    pause 0.025
    "Calendars/Circle/Circle_14.png"
    pause 0.025
    "Calendars/Circle/Circle_15.png"
    pause 0.025
    "Calendars/Circle/Circle_16.png"
    pause 0.025
    "Calendars/Circle/Circle_17.png"
    pause 0.025
    "Calendars/Circle/Circle_18.png"
    pause 0.025
    "Calendars/Circle/Circle_19.png"
    pause 0.025
    "Calendars/Circle/Circle_20.png"

image full_circle:
    size(136.5, 121.5)
    "Calendars/Circle/Circle_20.png"

layeredimage calendar:
    group months:
        attribute june:
            size(783, 783)
            "Calendars/June.png"
        attribute july:
            size(783, 672.75)
            "Calendars/July.png"
    group Xs:
        attribute june_03:
            size(783, 783)
            "Calendars/June/June_03.png"
        attribute june_04:
            size(783, 783)
            "Calendars/June/June_04.png"
        attribute june_11:
            size(783, 783)
            "Calendars/June/June_11.png"
        attribute june_21:
            size(783, 783)
            "Calendars/June/June_21.png"
        attribute june_23:
            size(783, 783)
            "Calendars/June/June_23.png"
        attribute june_30:
            size(783, 783)
            "Calendars/June/June_30.png"
        attribute june_31:
            size(783, 783)
            "Calendars/June/June_31.png"
        attribute july_04:
            size(783, 672.75)
            "Calendars/July/July_04.png"
        attribute july_10:
            size(783, 672.75)
            "Calendars/July/July_10.png"
        attribute july_15:
            size(783, 672.75)
            "Calendars/July/July_15.png"

image eleanor_title:
    "gui/title/Eleanor.png"
    size(540, 1080)
image christeena_title:
    "gui/title/Christeena.png"
    size(600, 1200)
image brittney_title:
    "gui/title/Brittney.png"
    size(600, 1200)
image donald_title:
    "gui/title/Donald.png"
    size(540, 1080)
image alex_title:
    "gui/title/Alex.png"
    size(540, 1080)

#########
# Music #
#########

define audio.new_life = "<loop 14.769>audio/music/New Life.ogg" # Opening
define audio.oddball = "audio/music/Oddball.ogg" # Brittney
define audio.ivories_and_ebony = "<loop 3>audio/music/Ivories and Ebony.ogg" # Gang All Together
define audio.home_life = "<to 112 loop 5.32>audio/music/Home Life.ogg" # Slow Moments @ Home
define audio.relaxation_in_the_country = "<loop 5.333>audio/music/Relaxation in the Country.ogg" # Mellow Moments
define audio.violet_wonder = "<loop 9.6>audio/music/Violet Wonder.ogg" # Christeena
define audio.dinin_in = "<loop 9.6>audio/music/Dinin' In.ogg" # Kelly's Deli
define audio.reflection = "audio/music/Reflection.ogg" # Sad
define audio.cabin_fever = "<loop 8>audio/music/Cabin Fever.ogg" # Cabin
define audio.friendly_competition = "audio/music/Friendly Competition.ogg" # Heavy Workout
define audio.outside_the_street = "audio/music/Outside the Street.ogg" # Downtown
define audio.the_pond = "audio/music/The Pond.ogg" # Pond
define audio.scrapbook = "audio/music/Scrapbook.mp3" # School
define audio.sunday_service = "audio/music/Sunday Service.ogg" # Church
define audio.generic_80s_song = "audio/music/Generic 80s Song.ogg" # Generic 80's Song
define audio.different_yet_equal = "audio/music/Different Yet Equal.ogg" # Sisters
define audio.donald = "<to 68 loop 12>audio/music/Brotato Chips.ogg" # Donald
define audio.main_theme = "<to 76 loop 8>audio/music/Welcome to Berry Street.ogg"
define audio.the_mall = "<loop 15>audio/music/The Mall.ogg" # Mall
define audio.chaotic_evil = "audio/music/Chaotic Evil.ogg" # Eleanor
define audio.chillaxin = "<loop 18>audio/music/Chillaxin.ogg" # Slow, happy moments
define audio.judgement = "audio/se/judgement.mp3" # ???
define audio.credits = "<from 14.769>audio/music/New Life.ogg"


#################
# Sound Effects #
#################

define audio.phone_vibrate = "audio/se/phone_vibrate.mp3"
define audio.phone_vibrate_call = "audio/se/phone_vibrate_call.mp3"
define audio.deli_door = "audio/se/deli_door.mp3"
define audio.deli_crowd = "audio/se/deli_crowd.mp3"
define audio.door_knock = "audio/se/door_knock.mp3"
define audio.door_open = "audio/se/door_open.mp3"
define audio.door_slam = "audio/se/door_slam.mp3"
define audio.punch = "audio/se/punch.mp3"
define audio.truck_start = "audio/se/truck_start.mp3"
define audio.van_start = "audio/se/van_start.mp3"
define audio.mall = "audio/se/mall.mp3"
define audio.dolmart = "audio/se/dolmart.mp3"
define audio.shopping_cart = "audio/se/shopping_cart.mp3"
define audio.woosh = "audio/se/woosh.mp3"
define audio.table_slam = "audio/se/table_slam.mp3"
define audio.chair = "audio/se/chair.mp3"
define audio.bag_hit = "audio/se/bag_hit.mp3"
define audio.fireworks = "audio/se/fireworks.mp3"
define audio.begin_judgement = "audio/se/begin_judgement.mp3"
define audio.light_flicker = "audio/se/light_flicker.mp3"
define audio.splash = "audio/se/splash.mp3"
define audio.forest_daytime = "audio/se/forest_daytime.mp3"
define audio.forest_nighttime = "audio/se/forest_nighttime.mp3"
define audio.stomach = "audio/se/stomach.mp3"
define audio.doorbell = "audio/se/doorbell.mp3"
define audio.twig_snap = "audio/se/twig_snap.mp3"
define audio.scare_and_scream = "audio/se/scare_and_scream.mp3"

#############
# Variables #
#############

default persistent.choices = {"1": 0, "2": 0, "3": 0,
    "4": 0, "5": 0, "6": 0, "7": 0,
    "8": 0,
    "9": 0, "10": 0,
    "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
    "18": 0, "19": 0, "20": 0, "21": 0, "22": 0,
    "23": 0, "23_": 0, "24": 0, "25": 0, "26": 0,
    "27": 0, "28": 0, "29": 0, "30": 0,
    "31": 0, "32": 0}

default persistent.tour = {"1": 0, "2": 0, "3": 0, "4": 0}

default marthatruman = False

default currentmonth = "June"
default warning_selector = 0
default progress = 0
default nextchoice = 0
default choicevbox = 1
default B_Name = "???"
default C_Name = "???"
default K_Name = "Waitress"
default M_Name = "Waitress"
default B_Points = 0
default C_Points = 0
default D_Points = 0
default E_Points = 0
default B_Kiss = False
default C_Kiss = False
default d_buy_stuff = False
default B_Basketball = False
default delifoodorder = ""
default acceptsandwich = False
default britnotpretty = False

default tour_town = 0
default tour_berrystreet = False
default tour_pond = False
default tour_downtown = False
default tour_school = False
default first_tour_pick = False

default b_blink = True
default b_hat = 0
default b_hair = 0
default b_hairtie = renpy.random.randint(0, 2)
default b_partial = False
default b_wink = False
default b_wince = False
default c_blink = True
default c_blush = False
default c_hair = 0
default d_blink = True
default e_blink = True
default e_hair = 0
default e_glasses = True
default h_blink = True
default h_hair = True
default k_hair = 0
default m_glasses = True
default m_partial = False
default p_glasses = 1

default outfit_b = "b"
default outfit_ch = "a"
default outfit_c = "a"
default outfit_da = "a"
default outfit_d = "b"
default outfit_e = "a"
default outfit_f = "a"
default outfit_g = "a"
default outfit_h = "a"
default outfit_j = "a"
default outfit_k = "a"
default outfit_l = "a"
default outfit_m = "a"
default outfit_p = "a"

default nhie_a_points = 5
default nhie_b_points = 5
default nhie_c_points = 5
default nhie_d_points = 5

default replay = False
default dayselectmenuvalue = "June, 2013"

default daydesc = 0

default current_track = "None"

default day = 1

default monthpoints = {"June3B": 0, "June3D": 0, 
"June4B": 0, "June4C": 0, "June4D": 0, 
"June11B": 0, 
"June21C": 0, "June21D": 0, 
"June23B": 0, "June23C": 0, "June23E": 0, 
"June30B": 0, "June30C": 0, "June30D": 0, 
"July4B": 0, "July4C": 0, "July4D": 0, 
"July10B": 0, "July10C": 0, "July10D": 0, "July10E": 0}

#####################
# Character Sprites #
#####################

# Brittney
image brit_blink:
    "Characters/Brittney/Brittney_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Brittney/Brittney_Blinking_04.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_03.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_02.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_01.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_00.png"
        repeat

image brit_talking:
    choice:
        "Characters/Brittney/Brittney_Lip_A.png"
    choice:
        "Characters/Brittney/Brittney_Lip_E.png"
    choice:
        "Characters/Brittney/Brittney_Lip_O.png"
    choice:
        "Characters/Brittney/Brittney_Lip_U.png"
    pause 0.09
    repeat

layeredimage brit:
    if b_hair == 0:
        "Characters/Brittney/Brittney_Ponytail.png"
    elif b_hair == 1:
        "Characters/Brittney/Brittney_Hair_Back.png"
    if b_hairtie == 0:
        "Characters/Brittney/Brittney_HairTie_01.png"
    elif b_hairtie == 1:
        "Characters/Brittney/Brittney_HairTie_02.png"
    else:
        "Characters/Brittney/Brittney_HairTie_03.png"
    group body:
        attribute p1:
            "Characters/Brittney/Brittney_Body_[outfit_b]01.png"
        attribute p2:
            "Characters/Brittney/Brittney_Body_[outfit_b]02.png"
    group eyes:
        attribute straight:
            "Characters/Brittney/Brittney_Pupils_01.png"
        attribute left:
            "Characters/Brittney/Brittney_Pupils_02.png"
        attribute right:
            "Characters/Brittney/Brittney_Pupils_03.png"
        attribute small:
            "Characters/Brittney/Brittney_Pupils_04.png"
        attribute closed:
            "Characters/Brittney/Brittney_Eyelids_02.png"
        attribute closed_sad:
            "Characters/Brittney/Brittney_Eyelids_04.png"
    if b_blink:
        "brit_blink"
    if b_partial:
        "Characters/Brittney/Brittney_Eyelids_01.png"
    if b_wink:
        "Characters/Brittney/Brittney_Eyelids_03.png"
    if b_wince:
        "Characters/Brittney/Brittney_Eyelids_05.png"
    group mouth:
        attribute closed_smile:
            "Characters/Brittney/Brittney_Mouth_01.png"
        attribute grin:
            "Characters/Brittney/Brittney_Mouth_02.png"
        attribute blank:
            "Characters/Brittney/Brittney_Mouth_03.png"
        attribute dot:
            "Characters/Brittney/Brittney_Mouth_04.png"
        attribute frown:
            "Characters/Brittney/Brittney_Mouth_05.png"
        attribute huhu:
            "Characters/Brittney/Brittney_Mouth_06.png"
        attribute derp:
            "Characters/Brittney/Brittney_Mouth_07.png"
        attribute opened_smile:
            "Characters/Brittney/Brittney_Mouth_08.png"
        attribute hanging:
            "Characters/Brittney/Brittney_Mouth_09.png"
        attribute tongue:
            "Characters/Brittney/Brittney_Mouth_10.png"
    group lips:
        attribute talking:
            "brit_talking"
        attribute notalking:
            "Characters/Brittney/Brittney_Lip_None.png"
    if b_hair == 0:
        "Characters/Brittney/Brittney_Hair_01.png"
    elif b_hair == 1:
        "Characters/Brittney/Brittney_Hair_02.png"
    group eyebrows:
        attribute raised:
            "Characters/Brittney/Brittney_Eyebrows_01.png"
        attribute casual:
            "Characters/Brittney/Brittney_Eyebrows_02.png"
        attribute mad:
            "Characters/Brittney/Brittney_Eyebrows_03.png"
        attribute sad:
            "Characters/Brittney/Brittney_Eyebrows_04.png"
        attribute level:
            "Characters/Brittney/Brittney_Eyebrows_05.png"
    group misc:
        attribute blush:
            "Characters/Brittney/Brittney_Blush.png"
    group crying:
        attribute tears:
            "Characters/Brittney/Brittney_Tears_01.png"
    group headwear:
        attribute sunglasses:
            "Characters/Brittney/Brittney_Sunglasses.png"
    if b_hat == 1:
        "Characters/Brittney/Brittney_Hat_01.png"
    elif b_hat == 2:
        "Characters/Brittney/Brittney_Hat_02.png"
    group pants:
        attribute shorts:
            "Characters/Brittney/Brittney_Shorts.png"

# Chad Truman
image chad_blink:
    "Characters/Brittney/Brittney_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Chad/Chad_Blink_04.png"
        pause 0.025
        "Characters/Chad/Chad_Blink_03.png"
        pause 0.025
        "Characters/Chad/Chad_Blink_02.png"
        pause 0.025
        "Characters/Chad/Chad_Blink_01.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_00.png"
        repeat

image chad_talking:
    choice:
        "Characters/Chad/Chad_Lip_A.png"
    choice:
        "Characters/Chad/Chad_Lip_E.png"
    choice:
        "Characters/Chad/Chad_Lip_O.png"
    choice:
        "Characters/Chad/Chad_Lip_U.png"
    pause 0.1
    repeat

layeredimage chad:
    group body:
        ypos 0.1
        attribute p1:
            "Characters/Chad/Chad_Body_[outfit_ch]01.png"
    group mouth:
        ypos 0.1
        attribute grin:
            "Characters/Chad/Chad_Mouth_01.png"
        attribute blank:
            "Characters/Chad/Chad_Mouth_02.png"
    group lip:
        ypos 0.1
        attribute talking:
            "chad_talking"
        attribute notalking:
            "Characters/Brittney/Brittney_Lip_None.png"
    group eyes:
        ypos 0.1
        attribute straight:
            "Characters/Chad/Chad_Pupils_01.png"
        attribute left:
            "Characters/Chad/Chad_Pupils_02.png"
        attribute right:
            "Characters/Chad/Chad_Pupils_03.png"
    always:
        "chad_blink"
        ypos 0.1
    group eyebrows:
        ypos 0.1
        attribute sad:
            "Characters/Chad/Chad_Eyebrows_01.png"
        attribute casual:
            "Characters/Chad/Chad_Eyebrows_02.png"
        attribute mad:
            "Characters/Chad/Chad_Eyebrows_03.png"
        attribute raised:
            "Characters/Chad/Chad_Eyebrows_04.png"
        attribute level:
            "Characters/Chad/Chad_Eyebrows_05.png"

# Christeena
image chris_blink:
    "Characters/Christeena/Christeena_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Christeena/Christeena_Blinking_04.png"
        pause 0.025
        "Characters/Christeena/Christeena_Blinking_03.png"
        pause 0.025
        "Characters/Christeena/Christeena_Blinking_02.png"
        pause 0.025
        "Characters/Christeena/Christeena_Blinking_01.png"
        pause 0.025
        "Characters/Christeena/Christeena_Blinking_00.png"
        repeat

image chris_talking:
    choice:
        "Characters/Christeena/Christeena_Lip_A.png"
    choice:
        "Characters/Christeena/Christeena_Lip_E.png"
    choice:
        "Characters/Christeena/Christeena_Lip_O.png"
    choice:
        "Characters/Christeena/Christeena_Lip_U.png"
    pause 0.09
    repeat

layeredimage chris:
    if c_hair == 0:
        "Characters/Christeena/Christeena_Hair_Down_02.png"
        ypos 0.1
    elif c_hair == 1:
        "Characters/Christeena/Christeena_Hair_Up_02.png"
        ypos 0.1
    group body:
        ypos 0.1
        attribute p1:
            "Characters/Christeena/Christeena_Body_[outfit_c]01.png"
        attribute p2:
            "Characters/Christeena/Christeena_Body_[outfit_c]02.png"
    group eyes:
        ypos 0.1
        attribute straight:
            "Characters/Christeena/Christeena_Pupils_01.png"
        attribute right:
            "Characters/Christeena/Christeena_Pupils_02.png"
        attribute left:
            "Characters/Christeena/Christeena_Pupils_03.png"
        attribute up:
            "Characters/Christeena/Christeena_Pupils_04.png"
        attribute small:
            "Characters/Christeena/Christeena_Pupils_05.png"
        attribute closed_happy:
            "Characters/Christeena/Christeena_Eyelids_01.png"
        attribute closed_sad:
            "Characters/Christeena/Christeena_Eyelids_02.png"
        attribute tightly_shut:
            "Characters/Christeena/Christeena_Eyelids_03.png"
    if c_blink:
        "chris_blink"
        ypos 0.1
    group mouth:
        ypos 0.1
        attribute grin:
            "Characters/Christeena/Christeena_Mouth_01.png"
        attribute blank:
            "Characters/Christeena/Christeena_Mouth_02.png"
        attribute dot:
            "Characters/Christeena/Christeena_Mouth_03.png"
        attribute smile:
            "Characters/Christeena/Christeena_Mouth_04.png"
        attribute hanging:
            "Characters/Christeena/Christeena_Mouth_05.png"
        attribute scream:
            "Characters/Christeena/Christeena_Mouth_06.png"
    group lips:
        ypos 0.1
        attribute talking:
            "chris_talking"
        attribute notalking:
            "Characters/Christeena/Christeena_Lip_None.png"
    if c_blush:
        "Characters/Christeena/Christeena_Blush_01.png"
        ypos 0.1
    if c_hair == 0:
        "Characters/Christeena/Christeena_Hair_Down_01.png"
        ypos 0.1
    elif c_hair == 1:
        "Characters/Christeena/Christeena_Hair_Up_01.png"
        ypos 0.1
    group eyebrows:
        ypos 0.1
        attribute sad:
            "Characters/Christeena/Christeena_Eyebrows_01.png"
        attribute casual:
            "Characters/Christeena/Christeena_Eyebrows_02.png"
        attribute mad:
            "Characters/Christeena/Christeena_Eyebrows_03.png"
        attribute level:
            "Characters/Christeena/Christeena_Eyebrows_04.png"
        attribute raised:
            "Characters/Christeena/Christeena_Eyebrows_05.png"
    group crying:
        ypos 0.1
        attribute tears:
            "Characters/Christeena/Christeena_Tears_01.png"

# Daniel
image daniel_blink:
    "Characters/Christeena/Christeena_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Daniel/Daniel_Blinking_04.png"
        pause 0.025
        "Characters/Daniel/Daniel_Blinking_03.png"
        pause 0.025
        "Characters/Daniel/Daniel_Blinking_02.png"
        pause 0.025
        "Characters/Daniel/Daniel_Blinking_01.png"
        pause 0.025
        "Characters/Christeena/Christeena_Blinking_00.png"
        repeat

image daniel_talking:
    choice:
        "Characters/Daniel/Daniel_Lip_A.png"
    choice:
        "Characters/Daniel/Daniel_Lip_E.png"
    choice:
        "Characters/Daniel/Daniel_Lip_O.png"
    choice:
        "Characters/Daniel/Daniel_Lip_U.png"
    pause 0.09
    repeat

layeredimage daniel:
    group body:
        attribute p1:
            "Characters/Daniel/Daniel_Body_[outfit_da]01.png"
    group eyes:
        attribute straight:
            "Characters/Daniel/Daniel_Pupils_01.png"
    always:
        "daniel_blink"
    group mouth:
        attribute grin:
            "Characters/Daniel/Daniel_Mouth_01.png"
        attribute blank:
            "Characters/Daniel/Daniel_Mouth_02.png"
        attribute smile:
            "Characters/Daniel/Daniel_Mouth_03.png"
    group lip:
        attribute talking:
            "daniel_talking"
        attribute notalking:
            "Characters/Brittney/Brittney_Lip_None.png"
    group eyebrows:
        attribute casual:
            "Characters/Daniel/Daniel_Eyebrows_01.png"
        attribute level:
            "Characters/Daniel/Daniel_Eyebrows_02.png"
        attribute mad:
            "Characters/Daniel/Daniel_Eyebrows_03.png"

# Donald
image don_blink:
    "Characters/Donald/Donald_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pause 0.0
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Donald/Donald_Blinking_04.png"
        pause 0.025
        "Characters/Donald/Donald_Blinking_03.png"
        pause 0.025
        "Characters/Donald/Donald_Blinking_02.png"
        pause 0.025
        "Characters/Donald/Donald_Blinking_01.png"
        pause 0.025
        "Characters/Donald/Donald_Blinking_00.png"
        repeat

image don_talking:
    choice:
        "Characters/Donald/Donald_Lip_A.png"
    choice:
        "Characters/Donald/Donald_Lip_E.png"
    choice:
        "Characters/Donald/Donald_Lip_O.png"
    choice:
        "Characters/Donald/Donald_Lip_U.png"
    pause 0.08
    repeat

layeredimage don:
    group body:
        attribute p1:
            "Characters/Donald/Donald_Body_[outfit_d]01.png"
        attribute p2:
            "Characters/Donald/Donald_Body_[outfit_d]02.png"
    group eyes:
        attribute straight:
            "Characters/Donald/Donald_Pupils_01.png"
        attribute left:
            "Characters/Donald/Donald_Pupils_02.png"
        attribute right:
            "Characters/Donald/Donald_Pupils_03.png"
        attribute small:
            "Characters/Donald/Donald_Pupils_04.png"
        attribute closed:
            "Characters/Donald/Donald_Eyelids_01.png"
    if d_blink:
        "don_blink"
    group mouth:
        attribute grin:
            "Characters/Donald/Donald_Mouth_01.png"
        attribute blank:
            "Characters/Donald/Donald_Mouth_02.png"
        attribute dot:
            "Characters/Donald/Donald_Mouth_03.png"
        attribute smile:
            "Characters/Donald/Donald_Mouth_04.png"
        attribute wide:
            "Characters/Donald/Donald_Mouth_05.png"
    group lip:
        attribute talking:
            "don_talking"
        attribute notalking:
            "Characters/Donald/Donald_Lip_None.png"
    group eyebrows:
        attribute casual:
            "Characters/Donald/Donald_Eyebrows_01.png"
        attribute raised:
            "Characters/Donald/Donald_Eyebrows_02.png"
        attribute mad:
            "Characters/Donald/Donald_Eyebrows_03.png"
        attribute level:
            "Characters/Donald/Donald_Eyebrows_04.png"
        attribute sad:
            "Characters/Donald/Donald_Eyebrows_05.png"
    group misc:
        attribute blush:
            "Characters/Donald/Donald_Blush.png"


# Eleanor
image elie_blink:
    "Characters/Brittney/Brittney_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Eleanor/Eleanor_Blinking_04.png"
        pause 0.025
        "Characters/Eleanor/Eleanor_Blinking_03.png"
        pause 0.025
        "Characters/Eleanor/Eleanor_Blinking_02.png"
        pause 0.025
        "Characters/Eleanor/Eleanor_Blinking_01.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_00.png"
        repeat

image elie_talking:
    choice:
        "Characters/Eleanor/Eleanor_Lip_A.png"
    choice:
        "Characters/Eleanor/Eleanor_Lip_E.png"
    choice:
        "Characters/Eleanor/Eleanor_Lip_O.png"
    choice:
        "Characters/Eleanor/Eleanor_Lip_U.png"
    pause 0.1
    repeat

layeredimage elie:
    if e_hair == 0:
        "Characters/Eleanor/Eleanor_Hair_Bottom.png"
    group body:
        attribute a1:
            "Characters/Eleanor/Eleanor_Body_[outfit_e]01.png"
    group eyes:
        attribute straight:
            "Characters/Eleanor/Eleanor_Pupils_01.png"
        attribute right:
            "Characters/Eleanor/Eleanor_Pupils_02.png"
        attribute left:
            "Characters/Eleanor/Eleanor_Pupils_03.png"
        attribute small:
            "Characters/Eleanor/Eleanor_Pupils_04.png"
    if e_blink:
        "elie_blink"
    group mouth:
        attribute blank:
            "Characters/Eleanor/Eleanor_Mouth_01.png"
        attribute frown:
            "Characters/Eleanor/Eleanor_Mouth_02.png"
        attribute scream:
            "Characters/Eleanor/Eleanor_Mouth_03.png"
        attribute grin:
            "Characters/Eleanor/Eleanor_Mouth_04.png"
    group lips:
        attribute talking:
            "elie_talking"
        attribute notalking:
            "Characters/Brittney/Brittney_Lip_None.png"
    if e_glasses:
        "Characters/Eleanor/Eleanor_Glasses_01.png"
    if e_hair == 0:
        "Characters/Eleanor/Eleanor_Hair.png"
    group eyebrows:
        attribute neutral:
            "Characters/Eleanor/Eleanor_Eyebrows_01.png"
        attribute casual:
            "Characters/Eleanor/Eleanor_Eyebrows_02.png"
        attribute level:
            "Characters/Eleanor/Eleanor_Eyebrows_03.png"
        attribute raised:
            "Characters/Eleanor/Eleanor_Eyebrows_04.png"
        attribute mad:
            "Characters/Eleanor/Eleanor_Eyebrows_05.png"
        attribute sad:
            "Characters/Eleanor/Eleanor_Eyebrows_06.png"

# Fred
image fred_blink:
    "Characters/Brittney/Brittney_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Fred/Fred_Blink_04.png"
        pause 0.025
        "Characters/Fred/Fred_Blink_03.png"
        pause 0.025
        "Characters/Fred/Fred_Blink_02.png"
        pause 0.025
        "Characters/Fred/Fred_Blink_01.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_00.png"
        repeat

image fred_talking:
    choice:
        "Characters/Fred/Fred_Lip_A.png"
    choice:
        "Characters/Fred/Fred_Lip_E.png"
    choice:
        "Characters/Fred/Fred_Lip_O.png"
    choice:
        "Characters/Fred/Fred_Lip_U.png"
    pause 0.1
    repeat

layeredimage fred:
    group body:
        attribute p1:
            "Characters/Fred/Fred_Body_[outfit_f]01.png"
    group mouth:
        attribute grin:
            "Characters/Fred/Fred_Mouth_01.png"
        attribute blank:
            "Characters/Fred/Fred_Mouth_02.png"
    group lip:
        attribute talking:
            "fred_talking"
        attribute notalking:
            "Characters/Brittney/Brittney_Lip_None.png"
    group eyes:
        attribute straight:
            "Characters/Fred/Fred_Pupils_01.png"
    always:
        "fred_blink"
    group eyebrows:
        attribute casual:
            "Characters/Fred/Fred_Eyebrows_01.png"
        attribute mad:
            "Characters/Fred/Fred_Eyebrows_02.png"
        attribute raised:
            "Characters/Fred/Fred_Eyebrows_03.png"
        attribute sad:
            "Characters/Fred/Fred_Eyebrows_04.png"
        attribute level:
            "Characters/Fred/Fred_Eyebrows_05.png"
    group eyewear:
        attribute glasses:
            "Characters/Fred/Fred_Glasses.png"

# Ginger
image ginger_blink:
    "Characters/Brittney/Brittney_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Ginger/Ginger_Blink_04.png"
        pause 0.025
        "Characters/Ginger/Ginger_Blink_03.png"
        pause 0.025
        "Characters/Ginger/Ginger_Blink_02.png"
        pause 0.025
        "Characters/Ginger/Ginger_Blink_01.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_00.png"
        repeat

image ginger_talking:
    choice:
        "Characters/Ginger/Ginger_Lip_A.png"
    choice:
        "Characters/Ginger/Ginger_Lip_E.png"
    choice:
        "Characters/Ginger/Ginger_Lip_O.png"
    choice:
        "Characters/Ginger/Ginger_Lip_U.png"
    pause 0.1
    repeat

layeredimage ginger:
    group body:
        attribute p1:
            "Characters/Ginger/Ginger_Body_[outfit_g]01.png"
        attribute p2:
            "Characters/Ginger/Ginger_Body_[outfit_g]02.png"
    group mouth:
        attribute grin:
            "Characters/Ginger/Ginger_Mouth_01.png"
        attribute blank:
            "Characters/Ginger/Ginger_Mouth_02.png"
        attribute wide:
            "Characters/Ginger/Ginger_Mouth_03.png"
    group lip:
        attribute talking:
            "ginger_talking"
        attribute notalking:
            "Characters/Brittney/Brittney_Lip_None.png"
    group eyes:
        attribute straight:
            "Characters/Ginger/Ginger_Pupils_01.png"
    always:
        "ginger_blink"
    group eyebrows:
        attribute casual:
            "Characters/Ginger/Ginger_Eyebrows_01.png"
        attribute raised:
            "Characters/Ginger/Ginger_Eyebrows_02.png"
        attribute mad:
            "Characters/Ginger/Ginger_Eyebrows_03.png"
        attribute sad:
            "Characters/Ginger/Ginger_Eyebrows_04.png"
        attribute level:
            "Characters/Ginger/Ginger_Eyebrows_05.png"

# Harry
image harry_blink:
    "Characters/Brittney/Brittney_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Harry/Harry_Blinking_04.png"
        pause 0.025
        "Characters/Harry/Harry_Blinking_03.png"
        pause 0.025
        "Characters/Harry/Harry_Blinking_02.png"
        pause 0.025
        "Characters/Harry/Harry_Blinking_01.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_00.png"
        repeat

image harry_talking:
    choice:
        "Characters/Harry/Harry_Lip_A.png"
    choice:
        "Characters/Harry/Harry_Lip_E.png"
    choice:
        "Characters/Harry/Harry_Lip_O.png"
    choice:
        "Characters/Harry/Harry_Lip_U.png"
    pause 0.09
    repeat

layeredimage harry:
    if h_hair:
        "Characters/Harry/Harry_Hair_02.png"
    group body:
        attribute p1:
            "Characters/Harry/Harry_Body_[outfit_h]01.png"
    group mouth:
        attribute blank:
            "Characters/Harry/Harry_Mouth_01.png"
        attribute grin:
            "Characters/Harry/Harry_Mouth_02.png"
        attribute closed_smile:
            "Characters/Harry/Harry_Mouth_03.png"
        attribute frown:
            "Characters/Harry/Harry_Mouth_04.png"
        attribute scream:
            "Characters/Harry/Harry_Mouth_05.png"
        attribute dot:
            "Characters/Harry/Harry_Mouth_06.png"
    group lips:
        attribute talking:
            "harry_talking"
        attribute notalking:
            "Characters/Brittney/Brittney_Lip_None.png"
    group eyes:
        attribute straight:
            "Characters/Harry/Harry_Pupils_01.png"
        attribute left:
            "Characters/Harry/Harry_Pupils_02.png"
        attribute right:
            "Characters/Harry/Harry_Pupils_03.png"
        attribute small:
            "Characters/Harry/Harry_Pupils_04.png"
    if h_blink:
        "harry_blink"
    if h_hair:
        "Characters/Harry/Harry_Hair_01.png"
    group eyebrows:
        attribute casual:
            "Characters/Harry/Harry_Eyebrows_01.png"
        attribute mad:
            "Characters/Harry/Harry_Eyebrows_02.png"
        attribute level:
            "Characters/Harry/Harry_Eyebrows_03.png"
        attribute raised:
            "Characters/Harry/Harry_Eyebrows_04.png"
        attribute sad:
            "Characters/Harry/Harry_Eyebrows_05.png"

# Janice Waters
image janice_blink:
    "Characters/Brittney/Brittney_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Janice/Janice_Blink_04.png"
        pause 0.025
        "Characters/Janice/Janice_Blink_03.png"
        pause 0.025
        "Characters/Janice/Janice_Blink_02.png"
        pause 0.025
        "Characters/Janice/Janice_Blink_01.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_00.png"
        repeat

image janice_talking:
    choice:
        "Characters/Janice/Janice_Lip_A.png"
    choice:
        "Characters/Janice/Janice_Lip_E.png"
    choice:
        "Characters/Janice/Janice_Lip_O.png"
    choice:
        "Characters/Janice/Janice_Lip_U.png"
    pause 0.1
    repeat

layeredimage janice:
    group body:
        attribute p1:
            "Characters/Janice/Janice_Body_[outfit_j]01.png"
    group mouth:
        attribute grin:
            "Characters/Janice/Janice_Mouth_01.png"
        attribute blank:
            "Characters/Janice/Janice_Mouth_02.png"
    group lip:
        attribute talking:
            "janice_talking"
        attribute notalking:
            "Characters/Brittney/Brittney_Lip_None.png"
    group eyes:
        attribute straight:
            "Characters/Janice/Janice_Pupils_01.png"
    always:
        "janice_blink"
    group eyebrows:
        attribute casual:
            "Characters/Janice/Janice_Eyebrows_01.png"
        attribute sad:
            "Characters/Janice/Janice_Eyebrows_02.png"
        attribute mad:
            "Characters/Janice/Janice_Eyebrows_03.png"

# Kelly Magson
image kelly_blink:
    "Characters/Brittney/Brittney_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Kelly/Kelly_Blink_04.png"
        pause 0.025
        "Characters/Kelly/Kelly_Blink_03.png"
        pause 0.025
        "Characters/Kelly/Kelly_Blink_02.png"
        pause 0.025
        "Characters/Kelly/Kelly_Blink_01.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_00.png"
        repeat

image kelly_talking:
    choice:
        "Characters/Kelly/Kelly_Lip_A.png"
    choice:
        "Characters/Kelly/Kelly_Lip_E.png"
    choice:
        "Characters/Kelly/Kelly_Lip_O.png"
    choice:
        "Characters/Kelly/Kelly_Lip_U.png"
    pause 0.1
    repeat

layeredimage kelly:
    if k_hair == 0:
        "Characters/Kelly/Kelly_Hair_02.png"
    group body:
        attribute p1:
            "Characters/Kelly/Kelly_Body_[outfit_k]01.png"
        attribute p2:
            "Characters/Kelly/Kelly_Body_[outfit_k]02.png"
    group eyes:
        attribute straight:
            "Characters/Kelly/Kelly_Pupils_01.png"
    always:
        "kelly_blink"
    group mouth:
        attribute grin:
            "Characters/Kelly/Kelly_Mouth_01.png"
        attribute blank:
            "Characters/Kelly/Kelly_Mouth_02.png"
    group lips:
        attribute talking:
            "kelly_talking"
        attribute notalking:
            "Characters/Brittney/Brittney_Lip_None.png"
    if k_hair == 0:
        "Characters/Kelly/Kelly_Hair_01.png"
    group eyebrows:
        attribute casual:
            "Characters/Kelly/Kelly_Eyebrows_01.png"
        attribute raised:
            "Characters/Kelly/Kelly_Eyebrows_02.png"
        attribute mad:
            "Characters/Kelly/Kelly_Eyebrows_03.png"
        attribute level:
            "Characters/Kelly/Kelly_Eyebrows_04.png"
        attribute sad:
            "Characters/Kelly/Kelly_Eyebrows_05.png"

transform k_middle:
    size (810, 1080)
    xalign 0.5 yalign 0.5

transform k_twoleft:
    size (810, 1080)
    xalign 0.25 yalign 0.5

transform k_tworight:
    size (810, 1080)
    xalign 0.75 yalign 0.5

transform k_threeleft:
    size (810, 1080)
    xalign 0.1 yalign 0.5

transform k_threeright:
    size (810, 1080)
    xalign 0.9 yalign 0.5

transform k_four3:
    size (810, 1080)
    xalign 0.7 yalign 0.5

# Latrell Waters
image latrell_blink:
    "Characters/Latrell/Latrell_Blink_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Latrell/Latrell_Blink_04.png"
        pause 0.025
        "Characters/Latrell/Latrell_Blink_03.png"
        pause 0.025
        "Characters/Latrell/Latrell_Blink_02.png"
        pause 0.025
        "Characters/Latrell/Latrell_Blink_01.png"
        pause 0.025
        "Characters/Latrell/Latrell_Blink_00.png"
        repeat

image latrell_talking:
    choice:
        "Characters/Latrell/Latrell_Lip_A.png"
    choice:
        "Characters/Latrell/Latrell_Lip_E.png"
    choice:
        "Characters/Latrell/Latrell_Lip_O.png"
    choice:
        "Characters/Latrell/Latrell_Lip_U.png"
    pause 0.11
    repeat

layeredimage latrell:
    group body:
        attribute p1:
            "Characters/Latrell/Latrell_Body_[outfit_l]01.png"
    group mouth:
        attribute grin:
            "Characters/Latrell/Latrell_Mouth_01.png"
    group lip:
        attribute talking:
            "latrell_talking"
        attribute notalking:
            "Characters/Latrell/Latrell_Lip_None.png"
    group eyes:
        attribute straight:
            "Characters/Latrell/Latrell_Pupils_01.png"
    always:
        "latrell_blink"
    group eyebrows:
        attribute casual:
            "Characters/Latrell/Latrell_Eyebrows_01.png"
        attribute level:
            "Characters/Latrell/Latrell_Eyebrows_02.png"

transform l_middle:
    size(627.75, 1080)
    xalign 0.5 yalign 0.5

transform l_tworight:
    size(627.75, 1080)
    xalign 0.75 yalign 0.5

transform l_threeright:
    size(627.75, 1080)
    xalign 0.9 yalign 0.5

# Martha Truman
image martha_blinking:
    "Characters/Martha/Martha_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Martha/Martha_Blinking_04.png"
        0.025
        "Characters/Martha/Martha_Blinking_03.png"
        0.025
        "Characters/Martha/Martha_Blinking_02.png"
        0.025
        "Characters/Martha/Martha_Blinking_01.png"
        0.025
        "Characters/Martha/Martha_Blinking_00.png"
        repeat

image martha_talking:
    choice:
        "Characters/Martha/Martha_Lip_A.png"
    choice:
        "Characters/Martha/Martha_Lip_E.png"
    choice:
        "Characters/Martha/Martha_Lip_O.png"
    choice:
        "Characters/Martha/Martha_Lip_U.png"
    pause 0.09
    repeat

layeredimage martha:
    group body:
        ypos 40
        attribute p1:
            "Characters/Martha/Martha_Body_[outfit_m]01.png"
    group eyes:
        ypos 40
        attribute straight:
            "Characters/Martha/Martha_Pupils_01.png"
    always:
        "martha_blinking"
        ypos 40
    if m_partial:
        "Characters/Martha/Martha_Eyelids_01.png"
        ypos 40
    group mouth:
        ypos 40
        attribute grin:
            "Characters/Martha/Martha_Mouth_01.png"
        attribute blank:
            "Characters/Martha/Martha_Mouth_02.png"
        attribute smile:
            "Characters/Martha/Martha_Mouth_03.png"
    group lips:
        ypos 40
        attribute talking:
            "martha_talking"
        attribute notalking:
            "Characters/Martha/Martha_Blinking_00.png"
    if m_glasses:
        "Characters/Martha/Martha_Glasses_01.png"
        ypos 40
    group eyebrows:
        ypos 40
        attribute casual:
            "Characters/Martha/Martha_Eyebrows_01.png"
        attribute raised:
            "Characters/Martha/Martha_Eyebrows_02.png"
        attribute mad:
            "Characters/Martha/Martha_Eyebrows_03.png"
        attribute sad:
            "Characters/Martha/Martha_Eyebrows_04.png"
        attribute level:
            "Characters/Martha/Martha_Eyebrows_05.png"

transform m_middle:
    size (540, 1080)
    xalign 0.5

transform m_twoleft:
    size (540, 1080)
    xalign 0.25

transform m_tworight:
    size (540, 1080)
    xalign 0.75

transform m_threeleft:
    size (540, 1080)
    xalign 0.1

transform m_threeright:
    size (540, 1080)
    xalign 0.9

transform m_four2:
    size (540, 1080)
    xalign 0.3

transform m_four4:
    size (540, 1080)
    xalign 1.0

# Percy
image percy_blink:
    "Characters/Brittney/Brittney_Blinking_00.png"
    block:
        pause 2.0
        choice:
            pass
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 1.5
        choice:
            pause 2.0
        choice:
            pause 2.5
        choice:
            pause 3.0
        "Characters/Percy/Percy_Blink_04.png"
        pause 0.025
        "Characters/Percy/Percy_Blink_03.png"
        pause 0.025
        "Characters/Percy/Percy_Blink_02.png"
        pause 0.025
        "Characters/Percy/Percy_Blink_01.png"
        pause 0.025
        "Characters/Brittney/Brittney_Blinking_00.png"
        repeat

image percy_talking:
    choice:
        "Characters/Percy/Percy_Lip_A.png"
    choice:
        "Characters/Percy/Percy_Lip_E.png"
    choice:
        "Characters/Percy/Percy_Lip_O.png"
    choice:
        "Characters/Percy/Percy_Lip_U.png"
    pause 0.09
    repeat

layeredimage percy:
    group body:
        attribute p1:
            "Characters/Percy/Percy_Body_[outfit_p]01.png"
    group mouth:
        attribute grin:
            "Characters/Percy/Percy_Mouth_01.png"
        attribute blank:
            "Characters/Percy/Percy_Mouth_02.png"
    group lip:
        attribute talking:
            "percy_talking"
        attribute notalking:
            "Characters/Brittney/Brittney_Lip_None.png"
    group eyes:
        attribute straight:
            "Characters/Percy/Percy_Pupils_01.png"
    always:
        "percy_blink"
    if p_glasses == 1:
        "Characters/Percy/Percy_Glasses_01.png"
    group eyebrows:
        attribute casual:
            "Characters/Percy/Percy_Eyebrows_01.png"
        attribute raised:
            "Characters/Percy/Percy_Eyebrows_02.png"
        attribute mad:
            "Characters/Percy/Percy_Eyebrows_03.png"
        attribute level:
            "Characters/Percy/Percy_Eyebrows_04.png"

#######
# CGs #
#######

layeredimage cg_01:
    always:
        "CG/CG 01/CG_01.png"
        size (1920, 1080)
    group alex_eyebrows:
        size (1920, 1080)
        attribute a_level:
            "CG/CG 01/Alex_Eyebrows_01.png"
        attribute a_raised:
            "CG/CG 01/Alex_Eyebrows_02.png"
        attribute a_casual:
            "CG/CG 01/Alex_Eyebrows_03.png"
    group alex_eyes:
        size (1920, 1080)
        attribute a_right:
            "CG/CG 01/Alex_Eyes_01.png"
        attribute a_left:
            "CG/CG 01/Alex_Eyes_02.png"
    group alex_mouth:
        size (1920, 1080)
        attribute a_grin:
            "CG/CG 01/Alex_Mouth_01.png"
        attribute a_blank:
            "CG/CG 01/Alex_Mouth_02.png"

    group brit_eyebrows:
        size (1920, 1080)
        attribute b_raised:
            "CG/CG 01/Brit_Eyebrows_01.png"
        attribute b_casual:
            "CG/CG 01/Brit_Eyebrows_02.png"
        attribute b_level:
            "CG/CG 01/Brit_Eyebrows_03.png"
        attribute b_mad:
            "CG/CG 01/Brit_Eyebrows_04.png"
    group brit_eyes:
        size (1920, 1080)
        attribute b_right:
            "CG/CG 01/Brit_Eyes_01.png"
    group brit_mouth:
        size (1920, 1080)
        attribute b_grin:
            "CG/CG 01/Brit_Mouth_01.png"
        attribute b_opened_smile:
            "CG/CG 01/Brit_Mouth_02.png"
        attribute b_blank:
            "CG/CG 01/Brit_Mouth_03.png"

    group chris_eyebrows:
        size (1920, 1080)
        attribute c_level:
            "CG/CG 01/Chris_Eyebrows_01.png"
        attribute c_sad:
            "CG/CG 01/Chris_Eyebrows_02.png"
        attribute c_mad:
            "CG/CG 01/Chris_Eyebrows_03.png"
        attribute c_casual:
            "CG/CG 01/Chris_Eyebrows_04.png"
    group chris_eyes:
        size (1920, 1080)
        attribute c_left:
            "CG/CG 01/Chris_Eyes_01.png"
        attribute c_right:
            "CG/CG 01/Chris_Eyes_02.png"
        attribute c_up:
            "CG/CG 01/Chris_Eyes_03.png"
    group chris_mouth:
        size (1920, 1080)
        attribute c_blank:
            "CG/CG 01/Chris_Mouth_01.png"
        attribute c_grin:
            "CG/CG 01/Chris_Mouth_02.png"

image bg cg_02:
    "CG/CG 02/CG_02.png"
    size (1920, 1080)

image firework:
    size (1920, 1080)
    alpha 0.5
    choice:
        "#ff0000"
    choice:
        "#0066ff"
    choice:
        "#42ff00"
    choice:
        "#8a00ff"

##############
# Transforms #
##############
init:
    transform new_default:
        alpha 1 rotate None zoom 1 xzoom 1 yzoom 1 align (0, 0) alignaround (0, 0) subpixel True size None crop None
        xpos 0.5 xanchor 0.5 ypos 1.0 yanchor 1.0

    $ config.default_transform = new_default

transform middle:
    zoom 0.75
    xalign 0.5 yalign 0.5

transform middle_float:
    zoom 0.75
    xalign 0.5 ycenter 0.5
    block:
        ease 1.0 ycenter 0.52
        ease 1.0 ycenter 0.5
        repeat

transform twoleft:
    zoom 0.75
    xalign 0.25 yalign 0.5

transform twoleft_float:
    zoom 0.75
    xalign 0.25 ycenter 0.5
    block:
        ease 1.0 ycenter 0.52
        ease 1.0 ycenter 0.5
        repeat

transform tworight:
    zoom 0.75
    xalign 0.75 yalign 0.5

transform tworight_float:
    zoom 0.75
    xalign 0.75 ycenter 0.5
    block:
        ease 1.0 ycenter 0.52
        ease 1.0 ycenter 0.5
        repeat

transform threeleft:
    zoom 0.75
    xalign 0.1 yalign 0.5

transform threeleft_float:
    zoom 0.75
    xalign 0.1 ycenter 0.5
    block:
        ease 1.0 ycenter 0.52
        ease 1.0 ycenter 0.5
        repeat

transform threeright:
    zoom 0.75
    xalign 0.9 yalign 0.5

transform threeright_float:
    zoom 0.75
    xalign 0.9 ycenter 0.5
    block:
        ease 1.0 ycenter 0.52
        ease 1.0 ycenter 0.5
        repeat

transform four1:
    zoom 0.75
    xalign 0.0 yalign 0.5

transform four2:
    zoom 0.75
    xalign 0.3 yalign 0.5

transform four3:
    zoom 0.75
    xalign 0.7 yalign 0.5

transform four4:
    zoom 0.75
    xalign 1.0 yalign 0.5

transform close_b:
    zoom 1.0
    xalign 0.5 yalign 0.2

transform close_b_float:
    zoom 1.0
    xalign 0.5 yalign 0.2
    block:
        ease 1.0 yalign 0.15
        ease 1.0 yalign 0.2
        repeat

transform close_right_b:
    zoom 1.0
    xalign 0.9 yalign 0.2

transform close_right_b_float:
    zoom 1.0
    xalign 0.9 yalign 0.2
    block:
        ease 1.0 yalign 0.15
        ease 1.0 yalign 0.2
        repeat

transform close_right_b_2:
    zoom 1.0
    xalign 1.0 yalign 0.2

transform close_right_b_2_float:
    zoom 1.0
    xalign 1.0 yalign 0.2
    block:
        ease 1.0 yalign 0.15
        ease 1.0 yalign 0.2
        repeat

transform close_left_b:
    zoom 1.0
    xalign 0.1 yalign 0.2

transform close_c:
    zoom 1.0
    xalign 0.5 yalign 0.4

transform close_c_float:
    zoom 1.0
    xalign 0.5 yalign 0.4
    block:
        ease 1.0 yalign 0.35
        ease 1.0 yalign 0.4
        repeat

transform close_c_float_2:
    zoom 1.0
    xalign 0.5 yalign 0.25
    block:
        ease 1.0 yalign 0.2
        ease 1.0 yalign 0.25
        repeat

transform close_left_c:
    zoom 1.0
    xalign 0.1 yalign 0.4

transform close_left_c_float:
    zoom 1.0
    xalign 0.1 yalign 0.4
    block:
        ease 1.0 yalign 0.35
        ease 1.0 yalign 0.4
        repeat

transform close_right_c:
    zoom 1.0
    xalign 0.9 yalign 0.4

transform close_right_c_2:
    zoom 1.0
    xalign 1.0 yalign 0.4

transform close_d:
    zoom 1.0
    xalign 0.5 yalign 0.2

transform close_d_float:
    zoom 1.0
    xalign 0.5 yalign 0.2
    block:
        ease 1.0 yalign 0.15
        ease 1.0 yalign 0.2
        repeat

transform close_right_d:
    zoom 1.0
    xalign 0.9 yalign 0.2

transform close_right_d_float:
    zoom 1.0
    xalign 0.9 yalign 0.2
    block:
        ease 1.0 yalign 0.15
        ease 1.0 yalign 0.2
        repeat

transform close_left_d:
    zoom 1.0
    xalign 0.1 yalign 0.2

transform close_left_d_float:
    zoom 1.0
    xalign 0.1 yalign 0.2
    block:
        ease 1.0 yalign 0.15
        ease 1.0 yalign 0.2
        repeat

transform close_left_d_2:
    zoom 1.0
    xalign 0.0 yalign 0.2

transform close_left_d_2_float:
    zoom 1.0
    xalign 0.0 yalign 0.2
    block:
        ease 1.0 yalign 0.15
        ease 1.0 yalign 0.2
        repeat

transform close_e:
    zoom 1.0
    xalign 0.5 yalign 0.25

transform close_h:
    zoom 1.0
    xalign 0.5 yalign 0.45

transform close_h_float:
    zoom 1.0
    xalign 0.5 yalign 0.45
    block:
        ease 1.0 yalign 0.4
        ease 1.0 yalign 0.45
        repeat

transform close_left_h:
    zoom 1.0
    xalign 0.1 yalign 0.45

transform close_left_h_float:
    zoom 1.0
    xalign 0.1 yalign 0.45
    block:
        ease 1.0 yalign 0.4
        ease 1.0 yalign 0.45
        repeat

transform close_right_h:
    zoom 1.0
    xalign 0.9 yalign 0.45

transform close_right_h_float:
    zoom 1.0
    xalign 0.9 yalign 0.45
    block:
        ease 1.0 yalign 0.4
        ease 1.0 yalign 0.45
        repeat

transform close_m:
    zoom 1.0
    xalign 0.5 yalign 0.15

transform close_to_left:
    parallel:
        ease 0.5 zoom 0.75
    parallel:
        ease 0.5 xalign 0.25 yalign 0.5

transform close_to_right:
    parallel:
        ease 0.5 zoom 0.75
    parallel:
        ease 0.5 xalign 0.75 yalign 0.5

transform close_to_far:
    ease 0.5 zoom 0.75

transform punchleft:
    zoom 0.75
    xalign 0.25 yalign 0.5
    linear 0.15 xalign 0.6
    pause .05
    linear 0.15 xalign 0.25

transform punchright:
    zoom 0.75
    xalign 0.75 yalign 0.5
    linear 0.15 xalign 0.4
    pause .05
    linear 0.15 xalign 0.75

transform three_to_two_left:
    zoom 0.75
    xalign 0.1 yalign 0.5
    linear 0.5 xalign .25

transform three_to_two_right:
    zoom 0.75
    xalign 0.9 yalign 0.5
    linear 0.5 xalign .75

transform hugtwoleft:
    zoom 0.75
    xalign 0.75 yalign 0.5
    linear .25 xalign 0.4

transform loadgame:
    xalign 0.5 yalign 0.5
    ease 1.0 zoom 1.0

transform record_move:
    size(270, 270)
    xanchor 0.5 yanchor 0.5
    xalign 0.02 yalign 0.79
    rotate 0
    linear 3.0 rotate 360
    repeat

transform record_move_musicroom:
    size(450, 450)
    xanchor 0.5 yanchor 0.5
    xalign 0.15 yalign 0.5
    rotate 0
    linear 3.0 rotate 360
    repeat

transform record_pause:
    size(270, 270)
    xanchor 0.5 yanchor 0.5
    xalign 0.05 yalign 0.75

transform choices(delay):
    alpha 0.0
    xpos 100
    yalign 0.5
    pause delay
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 0.5 xpos 0

transform gallery:
    zoom 0.25

transform fullscreen:
    size(1920, 1080)

##########
# Styles #
##########

style options_menu:
    font "fonts/LibbyRegular.ttf"

#############
# Callbacks #
#############

init -1 python:
# Alex
    def a_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/alex.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

# Brittney
    def b_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("brit talking")
            renpy.sound.play("audio/voice/brittney.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("brit notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

    def b_offscreen(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/brittney.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

# Chad
    def ct_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("chad talking")
            renpy.sound.play("audio/voice/chad.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("chad notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

# Christeena
    def c_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("chris talking")
            renpy.sound.play("audio/voice/christeena.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("chris notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

    def c_offscreen(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/christeena.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Daniel
    def da_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("daniel talking")
            renpy.sound.play("audio/voice/daniel.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("daniel notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

    def da_offscreen(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/daniel.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Donald
    def d_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("don talking")
            renpy.sound.play("audio/voice/donald.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("don notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

    def d_offscreen(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/donald.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Brittney and Donald
    def bd_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/brit_and_don.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Eleanor
    def e_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("elie talking")
            renpy.sound.play("audio/voice/eleanor.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("elie notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

    def e_offscreen(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/eleanor.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Fred
    def f_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("fred talking")
            renpy.sound.play("audio/voice/fred.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("fred notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

    def f_offscreen(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/fred.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Ginger
    def g_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("ginger talking")
            renpy.sound.play("audio/voice/ginger.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("ginger notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

    def g_offscreen(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/ginger.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Harry
    def h_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("harry talking")
            renpy.sound.play("audio/voice/harry.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("harry notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

    def h_offscreen(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/harry.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Janice
    def j_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("janice talking")
            renpy.sound.play("audio/voice/janice.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("janice notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Kelly
    def k_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("kelly talking")
            renpy.sound.play("audio/voice/kelly.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("kelly notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Latrell
    def l_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("latrell talking")
            renpy.sound.play("audio/voice/latrell.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("latrell notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Martha
    def m_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("martha talking")
            renpy.sound.play("audio/voice/martha.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("martha notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

    def m_offscreen(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/martha.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()


# Percy
    def p_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.show("percy talking")
            renpy.sound.play("audio/voice/percy.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.show("percy notalking")
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()

    def p_offscreen(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voice/percy.ogg", loop=True, channel="blip")
        elif event == "slow_done":
            renpy.sound.stop(channel="blip")
            renpy.restart_interaction()



#########
# Misc. #
#########

init -1 python:
    mr = MusicRoom(channel="music", fadeout=0.5, loop=True, single_track=True)

    mr.add("<to 76 loop 8>audio/music/Welcome to Berry Street.ogg", always_unlocked=True)
    mr.add("audio/music/Oddball.ogg")
    mr.add("<loop 9.6>audio/music/Violet Wonder.ogg")
    mr.add("<to 68 loop 12>audio/music/Brotato Chips.ogg")
    mr.add("audio/music/Chaotic Evil.ogg")
    mr.add("<loop 3>audio/music/Ivories and Ebony.ogg")
    mr.add("<loop 5.333>audio/music/Relaxation in the Country.ogg")
    mr.add("audio/music/Reflection.ogg")
    mr.add("<loop 18>audio/music/Chillaxin.ogg")
    mr.add("audio/music/Different Yet Equal.ogg")
    mr.add("<to 112 loop 5.32>audio/music/Home Life.ogg")
    mr.add("audio/music/The Pond.ogg")
    mr.add("audio/music/Outside the Street.ogg")
    mr.add("<loop 9.6>audio/music/Dinin' In.ogg")
    mr.add("audio/music/Friendly Competition.ogg")
    mr.add("<loop 8>audio/music/Cabin Fever.ogg")
    mr.add("audio/music/Sunday Service.ogg")
    mr.add("audio/music/Generic 80s Song.ogg")
    mr.add("<loop 14.769>audio/music/New Life.ogg")
    mr.add("<loop 15>audio/music/The Mall.ogg")

init python:
    gal = Gallery()
    gal.transition = dissolve
    gal.locked_button = "gui/gallery/locked.png"
    gal.idle_border = "gui/gallery/idle.png"
    gal.hover_border = "gui/gallery/hover.png"

    gal.button("cg_1")
    gal.condition("persistent.cg_1")
    gal.image("cg1_gal")
    gal.transform(fullscreen)
    
    gal.button("cg_2")
    gal.unlock_image("bg cg_02")

image cg1_gal:
    "cg_01 a_right a_level a_blank b_raised b_right b_grin c_left c_casual c_blank"
    size(2560, 1440)

image idle = "gui/gallery/idle.png"

init python:
    renpy.music.register_channel('blip', mixer="voice")
    renpy.music.register_channel("loop","sfx",True,tight=True)

# Move the images in and out while dissolving. (This is a fairly expensive transition.)
define moveinoutdissolve = ComposeTransition(dissolve, before=moveoutleft, after=moveinright)

define config.enter_yesno_transition = dissolve


init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['help'].remove('K_F1')
