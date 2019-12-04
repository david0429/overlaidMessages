#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random
from math import floor

parser = argparse.ArgumentParser(description='Hides a message in multiple overlaid pages')
parser.add_argument('--padding', type=float, default=1.5, help='How much extra character padding is added to the longest word')
parser.add_argument('--message', type=str, default="This is an example string", help='The message to hide amongst the sheets')
parser.add_argument('--sheets', type=int, default=5, help='Number of pages to create')

def printSheets(sheets):
    for i in range(len(sheets[0])):
        for j in range(len(sheets)):
            outString = "| "
            for k in sheets[j][i]:
                outString = outString + k
            print(outString + " |")
        print("-------------------")

def getLines(line, line_len, sheets):
    char_locations = []
    while True:
        r_value = random.randint(0, line_len-1)
        if r_value not in char_locations:
            char_locations.append(r_value)
        if len(char_locations) == len(line):
            break

    char_locations = sorted(char_locations)

    sheet_data = []
    for i in range(sheets):
        sheet_data.append( [' '] * line_len )

    for i in range(len(char_locations)):
        sheet_data[random.randint(0, sheets-1)][char_locations[i]] = line[i]

    for i in range(line_len):
        if i not in char_locations:
            sheet_data[random.randint(0, sheets-1)][i] = chr(random.randint(65, 90) + 32 * int(floor(random.randint(0, 5) / 5)))
            sheet_data[random.randint(0, sheets-1)][i] = '█'
    return sheet_data

def main(args):
    message = args.message
    message_data = message.split()

    line_len = int( max(len(x) for x in message_data) * args.padding )

    pages = []
    for line in message_data:
        pages.append(getLines(line, line_len, args.sheets))

    printSheets(pages)

if __name__== "__main__":
    args = parser.parse_args()
    main(args)
