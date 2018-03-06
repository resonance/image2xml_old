#XML_CONVERTER This is to go through and standardize various variables in an XML file in order to decrease tokens and make it easier to train.
    #Should be able to take a file or folder and iterate through all files in the folder
    #Should take a hard coded value and iterate through all occurences swapping it out for a second hard coded value

#Outputfile has to have different name than input file or else it won't work

import sys
import os
import argparse

replaceSpline = "NO"

VARIABLES_TO_CHANGE = ["mx=", "my=", "x=", "y="]
VARIABLES_TO_INSERT = ["mx=\".1\"", "my=\".1\"", "x=\".1\"", "y=\".1\""]
VARIABLE_TO_AVOID =  "blank"

INPUT_DIR_NAME = "/Users/theodoreseem/ResonanceHub/image2XML/image2XML/Data/Vector_XML/"
OUTPUT_DIR_NAME = "/Users/theodoreseem/ResonanceHub/image2XML/image2XML/Data/Vector_XMLProcessed/"

#INPUT_DIR_NAME = "/Users/theodoreseem/ResonanceHub/image2XML/Full_XML_model/image2XML/Vector_XML/Edited/"
#OUTPUT_DIR_NAME = "/Users/theodoreseem/ResonanceHub/image2XML/Full_XML_model/image2XML/Vector_XML/Edited/"

def replaceFolder():
    dirItems = os.listdir(INPUT_DIR_NAME)
    dirItems.remove('.DS_Store')
    files = [item for item in dirItems if os.path.isfile(os.path.join(INPUT_DIR_NAME, item))]
    for file in files:
        Out_File_Name = file#[:-4]  + "_4.val"
        replaceFile(file, Out_File_Name)

def replaceLine(line, outfile, counter, outputDict):
    replacement_line = "Spline" + str(counter)
    outputDict.write(replacement_line + " : " + line + "\n")
    print(replacement_line)
    for char in line:
        if char == ' ': outfile.write(char)
        else: break;
    outfile.write(replacement_line + "\n")

def replaceFile(inputFile, outputFile):
    outputFileEditable = open(OUTPUT_DIR_NAME+outputFile, "w")
    inputFileEditable = open(INPUT_DIR_NAME+inputFile, "r")

    #Ignore if not replacing Spline
    DictName = "/Users/theodoreseem/Desktop/Teddy_XML/Spline_Out/" + outputFile[:-4] + "_Dict.py"
    outputDict = open(DictName, "w")


    for counter, line in enumerate(inputFileEditable):
        if "spline" in line and replaceSpline is "YES":
            replaceLine(line, outputFileEditable, counter, outputDict)
        else:
            for char in line:
                if char == ' ': outputFileEditable.write(char)
                else: break;
            wordList = line.split()
            for word in wordList:
                changed = False
                for position, variable in enumerate(VARIABLES_TO_CHANGE):
                    if variable in word and VARIABLE_TO_AVOID not in word and changed is False:
                        changed = True
                        outputFileEditable.write(VARIABLES_TO_INSERT[position])
                        if '/>' in word:
                            outputFileEditable.write('/>')
                if changed is False:
                    outputFileEditable.write(word)
                outputFileEditable.write(' ')
        outputFileEditable.write('\n')


def simplifyName(directory):
    for afile in os.listdir(directory):
            os.rename(afile, afile[:-12] + '.val')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('FILE_OR_FOLDER', type=int, help='1 for file, 2 for folder')
    parser.add_argument('INPUT_NAME', help='To accept the input folder name or file name')
    args = parser.parse_args()

    if args.FILE_OR_FOLDER == 1:                                #FILE
        OUTPUT_FILE = args.INPUT_NAME[:-4]  + "_edit.val"
        replaceFile(args.INPUT_NAME, OUTPUT_FILE)
    elif args.FILE_OR_FOLDER == 2:                              #FOLDER
        replaceFolder()
    elif args.FILE_OR_FOLDER == 3:                              #RENAME
        simplifyName(args.INPUT_NAME)
    else:
        print("Incorrect input, expected 1: (File) or 2: (Folder)")
        sys.exit()
