import math
def list_notes(n):
    for note in n:
        if note < 40 and note+2 !=40:
            print(f"{note} you failed the test")
            continue
        notes_arrondie = math.ceil(note/5)*5
        if notes_arrondie - note > 3 :
            print(f"{note} you passed the test")
        else:
            print(f"{notes_arrondie} you passed the test")

list_notes([12,37,38,83,76,89,56,37,57,64,87,98])

