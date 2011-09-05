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
    image bg forest1 = "Forest1.png"
    image bg forest2 = "Forest2.png"
    image bg flowerField1 = "FlowerField1.png"
    transform panFlowerField:
        "FlowerField1.png"
        dissolve
        xalign 0.0
        linear 2.0 xalign 1.0

    image bg forestCabin1 = "ForestCabin1.png"
    image bg forestCreek1 = "ForestCreek1.png"
    image bg forestClearing1 = "ForestClearing1.png"
    image bg forestClearing2 = "ForestClearing2.png"
    image bg forestPavedPath1 = "ForestPavedPath1.png"
    image bg forestPathUp1 = "ForestPathUp1.png"
    image bg soul1 = "soul1.png"

    image satan = "satan.png"
    image satan scheming = "satan.scheming.png"
    image satan yearning = "satan.yearning.png"
    image michoel = "michoel.png"


    # Chapter 2 stuff

    $ ys = Character("Yosef", color="#ffcc99")
