from os import listdir
from os.path import isfile, join, isdir

filetxt = open("testing_list.txt", "w+")

onlydir = [name for name in listdir("audio/") if name != ".DS_Store"]

for directories in onlydir:
    mypath = "audio/" + directories
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for i in range(21):
        name = directories + "/" + onlyfiles[i]
        filetxt.write( name + "\n")
        print(name)

filetxt.close()


filetxt2 = open("validation_list.txt", "w+")

onlydir = [name for name in listdir("audio/") if name != ".DS_Store"]

for directories in onlydir:
    mypath = "audio/" + directories
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for i in range(22, 32):
        name = directories + "/" + onlyfiles[i]
        filetxt2.write( name + "\n")
        print(name)

filetxt2.close()