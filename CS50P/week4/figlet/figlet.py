from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


def main():
    # check if 2 arguments are provided
    if len(sys.argv) == 3:
        # check if first argument is -f to set font style
        if sys.argv[1] == "-f":
            # check if provided font exists
            fonts_list = figlet.getFonts()
            if sys.argv[2] in fonts_list:
                string = input("Input: ")
                print_figlet(string, sys.argv[2])
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    # check for invalid amount of arguments
    elif len(sys.argv) == 2 or len(sys.argv) > 3:
        sys.exit("Invalid usage")
    # if no arguments are provided continue with random font
    else:
        string = input("Input: ")
        print_figlet(string)


# default font is set to 0 if no arguments are provided to generate a random font
def print_figlet(string, font=0):
    # random font
    if font == 0:
        rand_font = random.randint(0, len(figlet.getFonts()))
        rand_font_int = figlet.getFonts()
        rand_font_name = rand_font_int[rand_font]
        figlet.setFont(font=rand_font_name)

    # font name provided by user
    else:
        figlet.setFont(font=font)

    # print string given by user in figlet font
    print("Output: \n" + figlet.renderText(string))


main()
