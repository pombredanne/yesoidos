# Yesoidos
# chapter1.rpy
#
# All rights reserved.
# Literary content Copyright (c) 2010 by Musashi <astrochess@gmail.com>
#
# This file is part of Yesoidos.
#
# The non-literary content of Yesoidos is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public License as 
# published by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

label chapter1:
    scene black
    with dissolve
    
    show text chapterText(1, "Early Years") with dissolve
    pause
    scene black with dissolve
    show text(bookText(
        "Tsadikim are motivated [solely] by their good nature, as it is written, \"My heart is a void within me,\" i.e., void of an evil nature....", 
        "Rabbi Shneur Zalmen of Liadi", 
        "Likkutei Amarim")) with dissolve
    pause
    scene black with dissolve
    
    # me = Binyomin, "Benny"
    me "Teacher, why are we here?" 

    "The walls of the teacher's home are simple drywall, painted a plain white. Here and there, crayon marks, cracks and dents color and texture the surface."
    "A chart of Hebrew letters hangs from a plastic hook near the door, around which my friends sit. There are about ten of us crowded in the tiny room, between three and five years old."

# [prz] Most of what's said in the above two lines will be visible on the background art anyway, so it's a bit redundant to state it in words as well. Just be sure to instruct your artist ;]
# --[mus] Agreed. I'll leave this in for now, as a note for the artist. As graphics are put in, these picture descriptions will disappear. 

    # zu = Zusha, the teacher
    zu "Why are you here? You're here to learn how to be good people, like your Mamas and Tatties. Alrright?"

    "I giggle at how he emphasizes and rolls his 'r' - {i}alrright!{/i}"
    "Zusha didn't give me the answer I was looking for." 
    "But, I forgot what I really wanted to ask. I'm only three, after all."

    zu "{i}Alrright!{/i} We're learning some more letters today! This is a {i}zayin{/i}. Can everyone say {i}zayin?{/i}"

    # ch = the children
    ch "{i}Zayin!{/i}"

    zu "Good! The {i}zayin{/i} makes a z- z- sound like a bee. Can everyone make the z- z- sound?"

    "... And the lesson continues."
    "We all love Zusha the teacher."
    "Especially when he tells us stories."
    "If we learn our letters well, sometimes he'll tell us about really special people called {i}tsadikim.{/i}"
    "A {i}tsadik{/i} helps other people and cares for them, and he never does anything bad."
    "This is because his {i}yeitser hora{/i}, his evil inclination, is completely defeated."
    "All that's left is his desire to do good: the {i}yeitser hatov{/i}."

    # pn = Pinchus, "Pinny"
    pn "Oh! Benny, I think he's gonna start!"

    zu "Alkay. This is a story about the Baal Shem Tov. Ready? Here we go."
    
    "Everyone quiets down and shifts to see Zusha better."
    
    zu "A long time ago, there lived a married couple in a village called Okup. Eliezer and Sara were their names."
    "They were {i}tsadikim{/i}, but they were lonely because they had no child."
    "They {i}davened{/i} and {i}davened{/i} for a child, crying out to Hashem."
    "And Hashem heard their prayers."
    "He went to His treasury, carefully looked through it, and chose - a special soul for Eliezer and Sara to raise as a son."
    "He was just about to send the soul down to Earth, when a certain angel saw the soul that was chosen and spoke up."
    
    # st = Satan, the angel
    st "Wait!"
    st "How do we know that those two really deserve to raise this soul as their child?"
    st "A soul like this may {i}not{/i} be given to just anybody!"
    # mc = Michoel, the angel
    mc "Be quiet! Who here doesn't know that you have been blocking this soul's way, for centuries now?"
    mc "You're just afraid that its radiance and holiness could threaten your power!"
    st "And what of that?"
    mc "If the soul were to be sent down, it could bring the era of {i}Moshiach!{/i} The culmination of all God's efforts in Creation!"
    mc "No one would die, no wars would be fought, and no one would wrong another again. The world would be filled with holy light and knowledge of God!"
    st "Of course. But if that was all the Holy One wanted, wouldn't He have created the Earth that way from the start?"
    st "Actually, why create the Earth at all? Here in Heaven, we already have the Divine Light and knowledge of God. Why bother creating the lower worlds?"
    st "Because - \"The light born out of darkness itself is superior to any other light!\" Hashem wants mankind to fight the darkness and {i}transform{/i} it to light! Not just have it drop down on their laps!"
    mc "And your point is?"
    st "To merit such a great light, an equal amount of darkness must be subdued. Eliezer and Sarah are not ready for this soul yet."
    mc "Oh, come now! Haven't you seen how they welcome guests to their house? They {i}hire{/i} people to bring visitors to their house - all year round, for crying out loud!"
    mc "And, haven't you seen how much charity they give? They hardly have a kopek left for themselves!"
    st "It's still not enough. Serving God with money is just one way. They must also show that they serve God with all their heart and soul!"
    # hs = Hashem, God. 
    hs "Silence!"
    "The angelic court stood, trembling in awe as God spoke."
    hs "The Satan is right. A soul like this may not be given without the parents proving their worthiness."
    hs "Since the Satan was created to test mankind, it is hereby decreed that he shall design a test to prove the worthiness of Eliezer and Sara."
    hs "It is further decreed that if Eliezer and Sara pass the test, this soul shall be given to them, immediately, to raise as their son!"
    "And so it happened."
    "In the test, Eliezer and Sara were separated for many years in distant lands, enduring grueling trials of moral strength."
    "In the end, they passed the test, remaining faithful to each other and to God."
    "And so, that radiant soul was finally sent down to Earth."
    "This was the soul of the Holy Rabbi Yisroel Baal Shem Tov."
    "For nine months, Sara carried him in her belly. But all that time, the baby was unusually still."
    "A baby usually kicks in his mother's belly, but not this one."
    "He was so eager to start doing {i}mitzvos{/i} that even inside his mother's womb, he fulfilled the {i}mitzvah{/i} of honoring his parents."
    "He was still, to avoid bothering his mother as she carried him."
    "That's the kind of {i}tsadik{/i} he was."
    "When he was finally born, he was healthy and sound. At eight days old, his circumcision was a joyous affair."
    # el = Eliezer, the Baal Shem Tov's father
    el "... be saved for the sake of His Covenant, which we set in our flesh. Blessed are You, Lord, Who makes the Covenant!"
    # sr = Sara, the Baal Shem Tov's mother
    sr "{i}Amein!{/i}"
    el "Our God and God of our forefathers, sustain this boy to me and my wife, and let his name be called in Israel - Yisroel, son of Eliezer!"
    el "May his heart be open to Your Holy Torah like the entrance to the Temple - to learn, to teach, to guard and to do it...."
    "The joy and peace, however, was not to last."
    st "The boy grows fast."
    st "Too fast."
    st "I must slow his progress. I can't have him threaten my power over mankind!"
    st "By God's decree, I cannot take the boy's life. But..."
    st "It is the mother who instills love in the child. Maybe by taking her away, I can halt the boy's progress."
    st "Wisdom comes from the father. I can wait a bit to claim him; the boy is too young to learn Torah right now."
    "And so, while Yisroel was still a small child, first his mother, then his father passed into {i}Oilom HoEmes.{/i}"
    "The poor child Yisroel was on his own."
    "However, that did not stop his learning and growth."
    "His childhood was an intensely Godly experience. Having learned to read the Holy Tongue as fluently as an adult, {i}seforim{/i} like the Tehillim, Gemara and the Zohar came alive for him as he mouthed their teachings."
    "When he read \"You are my son - I have begotten you today,\" in the Tehillim of King Dovid, he heard God telling him that he was God's son."
    "When he read how God called out to Shmuel the prophet, he longed for God to call to him the same way. For him, learning was life, and life was learning."
    "But, even though he learned and felt more than probably anyone alive today, that was just a small part of who the Baal Shem Tov was."
    "Before Yisroel's father Eliezer left this world, there were two things he told his beloved son."
    
    el "Yisroelik..."
    # yb = Yisroel, Baal Shem Tov
    yb "Yes, Tatti?"
    el "Before I go, there are two... things..."
    el "...tell you, before I go."
    yb "Tatti, you can't go!"
    el "Listen, Yisroelik..."
    el "Love... every Jew. Who he is, what he is... doesn't matter. Love them all.... as brothers."
    yb "Yes, Tatti."
    el "Don't be afraid of... anything. Only fear... Hashem..."
    yb "Yes, Tatti."
    el "... and nothing else."
    yb "Yes."
    el "It's time for... me, now."
    yb "Tatti!"
    el "Yisroelik. Don't cry."
    yb "Tatti! No! Stay!"
    el "Shema, Yisro-eil... Adoynoy Eloiheinu... Adoynoy... echod...."
    yb "Tatti?"
    yb "TATTIII!!! No! Nooooo!"

    "Little Yisroel carried those lessons with him for the rest of his life." 
    "He treated everyone nicely and made friends with everyone. He would smile and cheer everyone up."
    "He loved everyone and everything, because they were all creations of HaKodosh Boruch Hu - the Holy One, Blessed Be He."
    "Another thing little Yisroel loved was meditating on the wonders of Creation. Since he wasn't afraid of the forest, he liked going there alone to think about these things."
    "Now, there are 36 hidden {i}tsadikim{/i} in the world at all times. These {i}tsadikim{/i} make sure that there is always enough good to fight evil."
    "Rabbi Shlomo Zalmen was one of them, and he met little Yisroel one day as the boy wandered in the forest."
    
    yb "{i}Sholom aleichem!{/i}"
    # sz = Shlomo Zalmen
    sz "{i}Aleichem sholom!{/i} What are you doing in the forest alone?"
    yb "Just hiking a bit."
    sz "Hiking? There are wild animals here. Aren't you afraid?"
    yb "No. Tatti told me not to be afraid of anything, except for HaKodosh Boruch Hu."
    sz "Oh? Where is your tatti?"
    yb "......"
    sz "What's his name?"
    yb "... E- Eliezer."
    sz "Oh... Eliezer. I'm sorry."
    yb "It's alright."
    sz "He was a great man, and a good friend."
    yb "......"
    sz "Do you want to learn something with me?"
    yb "Yes! Yes!"
    sz "Let's sit over here, by the creek. So, here. Go ahead and read."
    yb "Hmm... {i}Rabi Chizkiya posach, k'siv k'shoishana bayn ha-choichim...{/i}"
    
    "Seeing that Yisroel had such a special soul, Rabbi Shlomo decided to take care of Yisroel. From then on, wherever Rabbi Shlomo Zalmen went, little Yisroel went, too."
    zu "In time, Yisroel learned the keys to finding the Secret of Secrets."
    pn "Teacher?"
    zu "Hmm?"
    pn "What was the Secret?"
    zu "What was the Secret, you ask?"
    zu "... I can't tell you. It's a Secret!"
    pn "Aww..."
    zu "I'm sorry, Pinny."
    zu "Maybe you'll grow up and learn the Secret yourself!"
    pn "... Oh!"
    "Pinny brightens up."
    zu "Later, when Yisroel became the Baal Shem Tov, he spread holy knowledge, good deeds and happiness all over the world. Those things sustain and illuminate the Earth today!"
    zu "The story, though, doesn't end there. His mission was to bring the {i}Moshiach.{/i}"
    zu "{i}Melech HaMoshiach{/i} didn't come then."
    zu "But, he is very close today."
    zu "Just do one more {i}mitzvah,{/i} and you could tip the scales to bring {i}Moshiach{/i} right now!"
    zu "Alkay, {i}kinderlech.{/i} That's all for today! You can go!"

    "All my friends run to the field to play soccer."
    "I'm about to join them, when I remember my question from earlier."

    me "Teacher?"
    zu "Ai?"
    me "My question from before... I meant, why did God put me here? I mean, not {i}here{/i}, but... in the world..."
    "Zusha smiles."
# [prz] This would be better served by a character emotion than narration. "Show, don't tell". You will have emotions for the characters anyway.
# -- [mus] Ditto before. Since I think almost every character will have a smile emotion, this is just a note to myself to switch from "attentive/stroke beard" to "smile".
    zu "Where do you get all these pesky questions?"
    "I giggle."
    zu "That's a gooood question. Everyone has a different mission here."
    zu "Like Yakov the policeman. He has to make sure everyone's homes are safe, day and night."
    zu "And Mendel the butcher! You know? He gives the poor people a share of meat every week, {i}kaynahora.{/i}"
    zu "Your mission, though. Hmmm-hm."

    "Zusha strokes his short, red beard."
# [prz] Same as my previous comment (stroke_beard will be an amusing emotion to have :D but I think it will probably occur often enough to have your artist draw it!)
# -- [mus] ditto previous.

    zu "Well, what would {i}you{/i} like to do?"

    me "I wanna be {i}tsadik{/i} just like little Yisroel!"

    "Zusha's eyes twinkle and he laughs. I pout."

    me "But I {b}do{/b} so wanna be a {i}tsadik!{/i}"

    "Zusha stops laughing, but he is still smiling. He puts his hand on my shoulder."

    zu "You want you should be a {i}tsadik?{/i}"

    "I nod eagerly."

    zu "Your mommy and tatti should be proud."
    zu "Go for it!"

    "I beam at him. Then I chase after my friends."

    me "Oi! Pinny! Yossi! Wait up!" 

#########################

    scene black with slowDissolve
    show text bookText("[The Torah] is more precious than pearls; all your desires cannot compare to it.... It is a tree of life to those who grasp onto it, and praiseworthy are all who support it.", "Proverbs 3:15, 18") with dissolve
    pause
    scene black with dissolve
    show text chapterText(title="The Tree") with dissolve
    pause
    scene black with dissolve
    
    show text "{i}Time passes...{/i}" with dissolve
    pause
    scene black with dissolve
    
    pn "Let's go climb that one over there."
    me "The one with the split trunk?"
    pn "Yeah, the magnolia."
    me "That looks like a great one!"
    
    "We are in the park, carrying some rope we got at the hardware store. We race each other to the tree and climb up several feet."
    
    pn "Heh heh heh! O-kay."
    "Pinny tests a branch and puts his weight on it."
    me "Wouldn't it be really cool to be a prophet?" 
    pn "And see angels and stuff?"
    me "Yeah."
    "Pinny seems satisfied with the branch's strength. He thinks, then rubs his hands."
    me "I wanna know what goes on in Heaven."
    pn "Well, I want to know everything, Heaven {i}and{/i} Earth!"
    me "Well, I want to know all that, plus infinity!"
    pn "Aaargh! You got me!"
    pn "... Well, I want that, too!"
    
    "While Pinny ties an end of the rope around a sturdy branch, I search for another branch on about the same level."

    me "Think this branch is good?"
    pn "Yeah. Test it, then go ahead and tie it."
    me "How many hammocks do you think we can make?"
    pn "Probably two, maybe three, with the amount of rope we have. You know how to make the knots so they won't slip?"
    me "No, not really."
    pn "Here, lemme show you."

    "Whenever it comes to building things and using tools, Pinny is the expert."
    "Back in kindergarten, he got in trouble because he took apart the teacher's chair with a screwdriver he brought that day."
    "He loves making pranks like that. So that he is always prepared, he carries around a combo tool with pliers, scissors, knives, screwdrivers, and other useful goodies."

    me "Okay. Could you give me another rope? I want to get started on the second level."
    pn "Sure. Here."

    "He tosses me a coil and begins weaving the first hammock."
    
    "Sometime later...."

    me "Finished!"
    pn "Good-good-good! Can I come up?"
    me "Yeah. The entrance hole is over here."

    "He climbs through and leans against the trunk, enjoying the vista of the park below."
    "I let my legs dangle over the edge and gaze up into the tree. It's a great position for letting my mind wander."

    me "Didn't know we could climb this high. How high do you think we are?"
    "Pinny glances down."
    pn "Eighteen feet."
    me "Pretty precise. Why eighteen?"
    pn "Dunno. Chai, I guess."
    "The numerical value for chai, \"life,\" is 18."
    pn "I like being in the tree because I feel like I'm not tied down to the Earth, you know?"
    me "Yeah. I heard that students in the yeshiva will argue over who gets the top bunk, because they feel closer to Heaven that way."
    "Pinny grins."
    pn "I think I'd like the top bunk, too."

    "Pinny picks up a twig, an begins carving it with his knife."
    "We just sit there, me watching, Pinny whittling."

    "I wonder to myself. How can I find God?"
    "Well..."
    "God is a kind of superman in the sky, and that's how He rules over everything."
    "Not."
    "Seriously this time, if you ask where God is, the Kotzker Rebbe once said, \"He is, wherever you let Him in.\""
    "So, how do I let Him in? Mitzvos."
    "My thoughts wander some more."
    "It seems that physical heights and spiritual heights are kind of the same."
    "The higher you go, the more clearly you can see things all around. It's the same on mountains, the same in the Higher Worlds."
    "Maybe this is why those older kids like the top bunk so much. The spritual parallel."
    "And..."
    "Maybe that's why we like climbing trees."
    
    "I look over at Pinny's work. It looks like he made a case for a {i}mezuzah{/i} scroll."
    
    me "Hey, Pinny?"
    pn "Hm?"
    me "Let's do this again next week!"
    pn "You're on!"
    
    return