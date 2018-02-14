#Simple XML to RSL converter.
#These RSL files are created to be fed to the NN to train ont he limited vocabulary size.

import sys
import os
import argparse
__author__ = 'Resonance Companies'


INPUT_DIR_NAME = "/Users/theodoreseem/ResonanceHub/image2XML/Full_XML_model/image2XML/Vector_XML/"
OUTPUT_DIR_NAME = "/Users/theodoreseem/ResonanceHub/image2XML/Full_XML_model/image2XML/guis/"

def addSpaces(spaces, outputFile):
    for x in range(1,spaces):
        outputFile.write(" ")

def read(inputFile, outputFile):
    outputFile = open(OUTPUT_DIR_NAME+outputFile, "w")
    XMLfile = open(INPUT_DIR_NAME+inputFile, "r")
    spaces = 0; firstChar = ''; isStandaloneUnit = False
    for line in XMLfile:
        charList = list(line); word = ""
        if '/>' in line: isStandaloneUnit = True
        if all(x != charList[0] for x in charList) or '<' in charList:
            for char in charList:
                if char == ' ': spaces = spaces + 1
                else:
                    if charList[charList.index(char) + 1] == "/":
                        addSpaces(spaces, outputFile)
                        outputFile.write("}\n")
                    else:
                        for x in charList[charList.index(char)+1:]:
                            if x == '>' or x == ' ': break
                            else: word = word + x
                        addSpaces(spaces, outputFile)
                        if isStandaloneUnit == True or '/'+word in line:
                            outputFile.write(word + "\n")
                        else:
                            outputFile.write(word + "{\n")
                    break
        spaces = 0
        firstChar = 0
        isStandaloneUnit = False


#Enter Filename, or enter ALL for whole Vector_XML directory
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='get input files')
    parser.add_argument('readerFile', help='To accept the input file')
    args = parser.parse_args()

    if args.readerFile == "ALL":
        for f in os.listdir(INPUT_DIR_NAME):
            if '.DS' not in f:
                OUTPUT_FILE_NAME = f[:-3]  + "gui"
                read(f, OUTPUT_FILE_NAME)
    elif len(sys.argv) > 1:
        INPUT_FILE_NAME = args.readerFile #.split("/")[-1]
        OUTPUT_FILE_NAME = INPUT_FILE_NAME[:-3]  + "gui"
        read(args.readerFile, OUTPUT_FILE_NAME)
    else:
        print("Error: not enough arguments supplied:")
        print("RSL_gen.py <path>")
        exit(0)
