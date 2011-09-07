init:
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

    # Satan
    image satan = "satan.png"
    image satan small = "satan.small.png"
    image satan scheming = "satan.scheming.png"
    image satan yearning = "satan.yearning.png"
    image satan angry = "satan.angry.png"
    
    # Michoel
    image michoel = "michoel.png"
    image michoel angry = "michoel.angry.png"
    image michoel small = "michoel.small.png"
    image michoel inspired = "michoel.inspired.png"
