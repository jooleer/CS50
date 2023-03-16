from PIL import Image, ImageOps
import sys


def main():
    # check command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # check if input and output images have the same extension
    if sys.argv[1].lower().endswith(".png") and not sys.argv[2].lower().endswith(".png"):
        sys.exit("Input and output have different extensions")
    if sys.argv[1].lower().endswith((".jpg", ".jpeg")) and not sys.argv[2].lower().endswith((".jpg", ".jpeg")):
        sys.exit("Input and output have different extensions")

    # send before/after arguments to pshirt function
    pshirt(sys.argv[1], sys.argv[2])


def pshirt(before, after):
    # open shirt overlay image
    shirt = Image.open("shirt.png")
    # get shirt image size
    size = shirt.size

    try:
        # open input/before image
        input = Image.open(before)
        # copy input to output
        output = input.copy()
        # resize output to shirt size
        output = ImageOps.fit(output, size)
        # paste shirt on top of output
        output.paste(shirt, shirt)
        # save output image
        output.save(after)

    # before/input file does not exist
    except IOError:
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()
