import sys
from os import listdir
from os.path import isfile, join

import numpy as np
import matplotlib.pyplot as plt
import skimage as ski

DEBUG = False

def getFilesToFilter(inDirectory, outDirectory) -> list[str]:
    inFiles = [f for f in listdir(inDirectory) if isfile(join(inDirectory, f))]
    outFiles = [f for f in listdir(outDirectory) if isfile(join(outDirectory, f))]
    imagesToFilter = [file for file in inFiles if file not in outFiles]
    if DEBUG:
        skippedFiles = [file for file in inFiles if file not in outFiles]
        print(inFiles)
        print(outFiles)
        print(imagesToFilter)
        print(skippedFiles)
    return inFiles

def getImagesToFilter(inDirectory, listOfFiles):
    imagesToFilter = []
    for file in listOfFiles:
        imagesToFilter.append(ski.io.imread(inDirectory + "/" + file))


    return imagesToFilter

def toGray(image):
    return ski.color.rgb2gray(ski.color.rgba2rgb(image))

def toInt(image):
    return (image * 255.99).astype(np.uint8)

def filterImagesTo(imagesToFilter):
    plt.imshow(imagesToFilter[0])
    plt.show()

    plt.imshow(imagesToFilter[1])
    plt.show()
    grayImages = [toGray(image) for image in imagesToFilter]
    normalizedGrayImages = [toInt(image) for image in grayImages]

    return normalizedGrayImages

def save(filesName, filteredImages, outDirectory):
    for (fileName, filteredImage) in zip(filesName, filteredImages):
        ski.io.imsave(outDirectory + "/" + fileName, filteredImage)



def main():
    argv = sys.argv
    if not len(argv) == 3 :
        print("Usage: python ToBlackAndWhite.py <in directory> <out directory>")
        return

    inDirectory = argv[1]
    outDirectory = argv[2]

    filesToFilter = getFilesToFilter(inDirectory, outDirectory)
    imagesToFilter = getImagesToFilter(inDirectory, filesToFilter)
    filteredImages = filterImagesTo(imagesToFilter)
    print(filteredImages)

    save(filesToFilter, filteredImages, outDirectory)

main()
