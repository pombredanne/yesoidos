init:    
    # Set up Chapter 1 characters
    $ me = Character('Binyomin', color="#6688ff")
    $ zu = Character('Zusha', color="#ff7777")
    $ ch = Character('Children', color="#aaffaa")
    $ pn = Character('Pinchas', color="#9955cc")
    
    # Characters from the past, like in the Baal Shem Tov story, are in grey
    define storyChar = Character("", color = "#888888")

    # Baal Shem Tov story
    $ hs = Character(None,
                     what_style="centered_text",
                     what_size=70,
                     what_xalign=0.5,
                     what_yalign=0.5,
                     window_xalign=0.5,
                     window_yalign=0.5,
                     window_xfill=False,
                     window_yfill=False,
                     window_background="#0008",
                     what_prefix="{font=Speedline.ttf}",
                     what_suffix="{/font}",
                     what_outlines=[(3, "#000000", 2, 2),(3,"#111", 2, 2)])
    $ st = storyChar.copy("Satan")
    $ mc = storyChar.copy("Michoel")
    $ el = storyChar.copy("Eliezer")
    $ sr = storyChar.copy("Sara")
    $ yb = storyChar.copy("Yisroel")
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
