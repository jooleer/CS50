import re
import sys


def main():
    # ask user for HTML input and send it to parse function
    print(parse(input("HTML: ")))


def parse(s):
    # check if there is an iframe (including src=) string in the HTML input
    check = re.search(
        r'src="https?://(www\.)?youtube\.com/embed/[a-zA-Z0-9_-]+"', s)

    # if true, extract video id from input and print the cropped url
    if check:
        video = check.group().split("/")
        video = video[len(video)-1]
        video = video.replace("\"", "")
        print("https://youtu.be/", video, sep="")
        sys.exit()
    # if no fitting string is found, exit
    else:
        print("None")
        sys.exit(0)


if __name__ == "__main__":
    main()
