namn = input("vad heter du?")
print("Hej " + namn + " och välkommen till spelet!")

import random
hemligt_tal = random.randint(1, 10)
gissning = None
while gissning != hemligt_tal:
    gissning = int(input("Gissa ett tal mellan 1 och 10"))
    if gissning == hemligt_tal:
        print("rätt gissat!")
    else:
        print("Fel gissat.")