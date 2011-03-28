import renpy.exports as renpy

def bookText(text, author = None, title = None):        
    if author and title:
        return "{i}%s{/i}\n\n- {i}%s{/i}, %s" % (text, author, title)
    elif title:
        return "{i}%s{/i}\n\n- %s" % (text, title)
    elif title:
        return "{i}%s{/i}\n\n- {i}%s{/i}" % (text, author)
    else:
        return "{i}%s{/i}" % text


def chapterText(number = None, title = None):
    if not title and not number:
        raise Exception("chapterText() requires at least one argument")
    if not title:
        return "{size=+20}{i}Chapter %d{/i}{/size}" % number
    elif not number:
        return "{size=+20}{i}%s{/i}{/size}" % title
    else: # have both a number and a title
        return "{size=+10}{i}Chapter %d{/size}{size=+20}\n\n%s{/i}{/size}" % (number, title)
    
