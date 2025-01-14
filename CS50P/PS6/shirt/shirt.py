import PIL
from PIL import Image
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    #if not (len(sys.argv[1]) > 3 and len(sys.argv[2]) > 3 and sys.argv[1][-4:] in [".jpg", ".jpeg", ".pgn"] and sys.argv[1][-4:] == sys.argv[2][-4:]):
    #    sys.exit("Input and output have different extensions")

    #    Invalid output
    if sys.argv[1][-4:] not in [".jpg", ".jpeg", ".pgn"]:
        sys.exit("Invalid input")
    elif sys.argv[2][-4:] not in [".jpg", ".jpeg", ".pgn"]:
        sys.exit("Invalid output")
    else:
        try:
            with Image.open(sys.argv[1]) as im:
                im.show()
                shirt = Image.open("shirt.png")

                im2 = PIL.ImageOps.fit(im, shirt.size)
        except FileNotFoundError:
            sys.exit("Input does not exist")
        else:
            im2.paste(shirt, (0, 0), shirt)
            im2.save(sys.argv[2])

