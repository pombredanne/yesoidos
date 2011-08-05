init:    
    # Set up Chapter 1 characters
    $ me = Character('Binyomin', color="#6688ff")
    $ zu = Character('Zusha', color="#ff7777")
    $ ch = Character('Children', color="#aaffaa")
    $ pn = Character('Pinchas', color="#9955cc")
    
    # Characters from the past, like in the Baal Shem Tov story, are in grey
    define storyChar = Character("", color = "#888888")

    $ shout = Character(None,
                     window_align=(0.5,0.5),
                     window_xminimum=0.1,
                     window_xmaximum=0.9,
                     window_yminimum=0,
                     window_left_padding=35,
                     window_right_padding=35,
                     window_top_padding=15,
                     window_bottom_padding=15,
                     what_pos=(0,0),
                     window_xfill=False,
                     window_yfill=False,
                     window_background="#000a")

    # Baal Shem Tov story
    $ hs = Character(None,
                     what_size=70,
                     window_align=(0.5,0.5),
                     window_xminimum=0.1,
                     window_xmaximum=0.9,
                     window_yminimum=0,
                     window_xfill=False,
                     window_yfill=False,
                     window_left_padding=55,
                     window_right_padding=55,
                     window_top_padding=15,
                     window_bottom_padding=15,
                     window_background="#000a",
                     what_prefix="{font=Speedline.ttf}",
                     what_suffix="{/font}",
                     what_outlines=[(3, "#000000", 2, 2),(3,"#111", 2, 2)])
    $ st = storyChar.copy("Satan")
    $ mc = storyChar.copy("Michoël")
    $ el = storyChar.copy("Eliëzer")
    $ sr = storyChar.copy("Sara")
    $ yb = storyChar.copy("Yisroël")
    $ sz = storyChar.copy("Shlomo Zalmen")
    
    # Transitions
    $ mediumDissolve = Dissolve(2.0)
    $ slowDissolve = Dissolve(4.0)
    $ slowFade = Fade(2.0,0,2.0)
    # Art
    image bg forest1 = "Forest1.jpg"
    image bg forest2 = "Forest2.jpg"
    image bg forestCabin1 = "ForestCabin1.jpg"
    image bg soul1 = "soul1.png"
    image satan = "satan.png"
    image michoel = "michoel.png"
