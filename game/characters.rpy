init:    
    # Set up Chapter 1 characters
    $ me = Character('Binyomin', color="#6688ff")
    $ zu = Character('Zusha', color="#ff7777")
    $ ch = Character('Children', color="#ccffcc")
    $ pn = Character('Pinchus', color="#bb55ff")
    
    # Characters from the past, like in the Baal Shem Tov story, are in grey
    define storyChar = Character("", color = "#888888")

    # Set up Baal Shem Tov story characters
    $ hs = storyChar.copy("Hashem")
    $ st = storyChar.copy("Satan")
    $ mc = storyChar.copy("Michoel")
    $ el = storyChar.copy("Eliezer")
    $ sr = storyChar.copy("Sara")
    $ yb = storyChar.copy("Yisroel")
    $ sz = storyChar.copy("Shlomo Zalmen")
    
