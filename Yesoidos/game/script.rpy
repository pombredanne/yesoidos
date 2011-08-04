init -1:
    # replace the default black to match the theme
    image black = blackColor
    
    # slowDissolves are used at section breaks
    define slowDissolve = Dissolve(1)    
    
    # some functions to format the book quotes and chapter titles
    $ from sections import bookText, chapterText
    
    # set a nicer italic font
    #$ config.font_replacement_map["DejaVuSans.ttf", False, True] = ("DejaVuSans-Oblique.ttf", False, False)

label start:
    call chapter1 from _call_chapter1
    call chapter2 from _call_chapter2
