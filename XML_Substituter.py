#XML_CONVERTER This is to go through and standardize various variables in an XML file in order to decrease tokens and make it easier to train.
    #Should be able to take a file or folder and iterate through all files in the folder
    #Should take a hard coded value and iterate through all occurences swapping it out for a second hard coded value

#Outputfile has to have different name than input file or else it won't work

import sys
import re
import os
import argparse
import random

MEASUREMENT_FILE = "/Users/theodoreseem/ResonanceHub/image2XML/image2XML/Data/Vector_Measurements/Tucker-Brianna.vit"

INPUT_DIR_NAME = "/Users/theodoreseem/ResonanceHub/image2XML/image2XML/Data/Vector_XMLProcessed/"
OUTPUT_DIR_NAME = "/Users/theodoreseem/ResonanceHub/image2XML/image2XML/Data/Vector_XMLProcessed/Vector_XMLProcessed2/"

def storeMeasurement():
    measurList = []
    inputFile = open(MEASUREMENT_FILE, "r")
    for count, line in enumerate(inputFile):
        if "<m" in line:
            for word in line.split():
                if "name" in word:
                    ms = re.findall('"([^"]*)"', word)[0]
                    measurList.append(ms)
    return measurList

def replaceFolder(measurList, FileNum):
    dirItems = os.listdir(INPUT_DIR_NAME)
    dirItems.remove('.DS_Store')
    files = [item for item in dirItems if os.path.isfile(os.path.join(INPUT_DIR_NAME, item))]
    for file in files:
        Out_File_Name = "test" + str(FileNum) + ".val"#file
        FileNum = FileNum + 1
        print(Out_File_Name)
        replaceFile(file, Out_File_Name, measurList)

def replaceFile(inputFile, outputFile, measurList):
    outputFileEditable = open(OUTPUT_DIR_NAME+outputFile, "w")
    inputFileEditable = open(INPUT_DIR_NAME+inputFile, "r")

    for counter, line in enumerate(inputFileEditable):
        for char in line:
            if char == ' ': outputFileEditable.write(char)
            else: break;
        for word in line.split():
            if "length" in word:
                randomInt = random.randint(1,len(measurList)-1)
                subMeasure = measurList[randomInt]
                wordEdit = re.sub(r'".*?"', '"' + subMeasure + '"', word)
                outputFileEditable.write(wordEdit)
            elif "angle" in word:
                randomInt = random.randint(1,360)
                wordEdit2 = re.sub(r'".*?"', '"' + str(randomInt) + '"', word)
                outputFileEditable.write(wordEdit2)
            else:
                outputFileEditable.write(word)
            outputFileEditable.write(' ')
        outputFileEditable.write('\n')


if __name__ == "__main__":

        FileNum = 1
        measurement_Dict = storeMeasurement()
        while FileNum < 10000:
            replaceFolder(measurement_Dict, FileNum)
            FileNum = FileNum + 20
