init:    
    # Set up Chapter 1 characters
    $ me = Character('Binyomin', color="#6688ff")
    $ zu = Character('Zusha', color="#ff7777")
    $ ch = Character('Children', color="#aaffaa")
    $ pn = Character('Pinchas', color="#9955cc")
    
    # Characters from the past, like in the Baal Shem Tov story, are in grey
    define storyChar = Character("", color = "#888888")

    $ shout = Character(None,
                     window_background="#000a",
                     window_align=(0.5,0.5),
                     window_xmargin=0.05,
                     window_yminimum=0,
                     window_xpadding=35,
                     window_ypadding=15,

                     what_textalign=0.5,
                     what_xalign=0.5,
                     what_xfill=True,

                     # screen_width * (1-xmargin*2) - 2*xpadding
                     what_minwidth=852)


    # Baal Shem Tov story
    $ hs = shout.copy(None,
                     window_xpadding=60,

                     # screen_width * (1-xmargin*2) - 2*xpadding
                     what_minwidth=802, 
                     what_size=70,
                     what_prefix="{font=fonts/Speedline.ttf}",
                     what_suffix="{/font}",
                     what_outlines=[(3, "#000000", 2, 2),(3,"#111", 2, 2)])
    $ st = storyChar.copy("Satan")
    $ mc = storyChar.copy("Michoël")
    $ en = storyChar.copy("Eliyahu")
    $ el = storyChar.copy("Eliëzer")
    $ sr = storyChar.copy("Sara")
    $ yb = storyChar.copy("Yisroël")
    $ sz = storyChar.copy("Shlomo Zalmen")
    

    # Chapter 2

    $ inner = Character("Inner Voice", color="#668877")
    $ zu_mem = zu.copy('Zusha', color="#888888", what_prefix="{i}", what_suffix="{/i}")
    $ me_mem = me.copy('Binyomin', color="#888888", what_prefix="{i}", what_suffix="{/i}")
    $ mom = Character("Mom", color="#ff9999")
    $ ys = Character("Yosef", color="#ffcc99")
