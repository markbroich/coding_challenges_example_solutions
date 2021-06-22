# reverse_words in place

# e.g. 
# in:    " one   two  "
# result "  two   one "


# Ot(n)
# Os(1)
def reverse_words(charLst):
    if len(charLst) == 0:
        return ""
    # rev entire charLst
    rev(s=0, e=len(charLst)-1)
    # parse charLst: look for s and e of word
    # s is blank after word
    # e is blank if s is known
    # pass s and e of word to rev
    s = ""
    for i in range(0, len(charLst)):
        if charLst[i] != " ": # not blank
            if s == "": # s empty
                s = i
            elif i == len(charLst)-1: # s filled and at end
                rev(s, i)
        else: # blank 
            if s != "": # s filled
              rev(s, i-1)
              s = ""

    return "".join(charLst)


# rev charLst between s and e
def rev(s, e):
    cnt = 0
    mid = (s+e)//2
    for i in range(s, mid+1):
        charLst[i], charLst[e-cnt] = charLst[e-cnt], charLst[i]
        cnt += 1


# tests
charLst = list(" one   two  ")
exp = "  two   one "
print(reverse_words(charLst) == exp)

charLst = list(" one   two")
exp = "two   one "
print(reverse_words(charLst) == exp)

charLst = list("one   two  ")
exp = "  two   one"
print(reverse_words(charLst) == exp)

charLst = list("one   two")
exp = "two   one"
print(reverse_words(charLst) == exp)

charLst = list("")
exp = ""
print(reverse_words(charLst) == exp)

charLst = list(" one  two   three    four     five")
exp = "five     four    three   two  one "
print(reverse_words(charLst) == exp)