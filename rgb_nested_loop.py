#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: April 25, 2025

# Color code program in python


import time

def main():
    for red in range(0,270,15):
        for green in range(0,270,15):
            for blue in range(0,270,15):
                time.sleep(.001)
                print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(red, green, blue, "RGB(" + str(red) + "," + str(green) + "," + str(blue) + ")"))

if __name__ == "__main__":
    main()