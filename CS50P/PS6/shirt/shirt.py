from PIL import Image
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if not (len(sys.argv[1]) > 3 and len(sys.argv[2]) > 3 and sys.argv[1][-4:] in [".jpg", ".jpeg", ".pgn"] and sys.argv[1][-4:] == sys.argv[2][-4:]):
        sys.exit("Input and output have different extensions")
    else:
        try:
            with Image.open(sys.argv[1]) as im:
                im.show()
        except:
            sys.exit("The specified input does not exist")


