'''Use all peices to from a medical term'''

pieces = ['he', 'ta', 'Co', 'iv', 
          'l', 're', 'e', 'bo',
          'mp', 'ns', 'Pa', 'ne',
          'li', 'Me', 'c'
          ]
words = ['nurse', 'sample', 'hosptial', 'metabolic', 'blood', 'comprehensive', 'panel']


# Does not yet return 'comprehsive metabolic panel' in the correct order
# and is not optemized for runtime.
# It does however return the comprehensive, panel, metabolic so I got the
# words :).
def unscrambel_pieces_to_medical_phrase(pieces: list, words: list) -> str:
    target_length = sum([len(piece) for piece in pieces])
    seen = set()
    res = []

    def recursion(new_word: bool, lenght: int):
        if lenght == target_length:
            return True
        for i in range(0, len(pieces)):
            piece = pieces[i].lower()
            if piece in seen:
                continue
            for word in words:
                rec = False
                if new_word and piece == word[0:len(piece)]:
                    res.append(piece)
                    new_word = False
                    rec = True
                elif res:
                    part = res[-1] + piece
                    if part == word:
                        res[-1] = part
                        new_word = True
                        rec = True
                    elif part == word[0:len(part)]:
                        res[-1] = part
                        rec = True
                if rec:
                    seen.add(piece)
                    lenght += len(piece)
                    return recursion(new_word, lenght)
        return False

    if recursion(True, 0):
        return res
    return ''


print(unscrambel_pieces_to_medical_phrase(pieces, words))

# def unscrambel_pieces_to_medical_phrase(pieces: list, words: list) -> str:
#     seen = set()
#     res = []
#     def recursion(new_word: bool):
#         for i in range(0, len(pieces)):
#             piece = pieces[i].lower()
#             if piece in seen:
#                 continue
#             for word in words:
#                 rec = False
#                 if new_word and piece == word[0:len(piece)]:
#                     res.append(piece)
#                     new_word = False
#                     rec = True
#                 elif res:
#                     part = res[-1] + piece
#                     if part == word:
#                         res[-1] = part
#                         new_word = True
#                         rec = True
#                     elif part == word[0:len(part)]:
#                         res[-1] = part
#                         rec = True
#                 if rec:
#                     seen.add(piece)
#                     return recursion(new_word)
#         return

#     recursion(True)
#     return res


# print(unscrambel_pieces_to_medical_phrase(pieces, words))