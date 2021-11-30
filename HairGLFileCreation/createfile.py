from sys import byteorder
from scipy.spatial import Delaunay
from struct import *
import numpy as np

def writeToHGL(guidesCount, verticesPerStrand, ifilename, ofilename, objfilename):
    myfile = open(ifilename, 'r')
    points = []
    rootPoints = []
    stepSize = int(100 / verticesPerStrand)

    print("stepSize: " + str(stepSize))

    guideStepSize = 900 / guidesCount
    guideArr = []
    for i in range(guidesCount):
        guideArr.append(i * guideStepSize)

    for i in range(901):
        if i in guideArr:
            count = 0
            for j in range(100):
                line = myfile.readline()
                if (j % stepSize != 0 or count == verticesPerStrand):
                    continue
                print("i: " + str(i) + " j: " + str(j))
                point = line.strip().split(' ')[1:4]
                point = [float(i) for i in point]
                points.append(point)
                if count == 0:
                    rootPoints.append(point[0:2])
                count += 1
                # if count == verticesPerStrand:
                #     break
        else:
            for j in range(100):    
                line = myfile.readline()
    myfile.close()

    tri = Delaunay(np.array(rootPoints))

    ofile = open(ofilename, 'wb')
    objfile = open(objfilename, 'w+')

    segmentsCount = verticesPerStrand - 1
    trianglesCount = len(tri.simplices)

    ofile.write(pack('i', guidesCount))
    ofile.write(pack('i', segmentsCount))
    ofile.write(pack('i', trianglesCount))


    for point in points:
        line = "v"
        for xyz in point:
            ofile.write(pack('f', xyz))
            line += " " + str(xyz)
        objfile.write(line + "\n")


    for triangle in tri.simplices:
        for num in triangle:
            ofile.write(pack('i', num))

    ofile.close()


    for i in range(guidesCount):
        line = "l"
        for j in range(verticesPerStrand):
            line += " " + str(j+1 + i * verticesPerStrand)
        objfile.write(line + "\n")
    # ofile2 = open(ofilename, 'rb')
    # for i in range(3):
    #     byte = unpack('i', ofile2.read(4))
    #     print(byte)
    # for i in range(len(points) * 3):
    #     print(i)
    #     byte = unpack('f', ofile2.read(4))
    #     print(byte)


writeToHGL(50, 16, "hair10.obj", "hairtest.hgl", "hairtest.obj")
