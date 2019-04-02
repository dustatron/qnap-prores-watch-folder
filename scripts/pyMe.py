import os
import subprocess
import shutil

source_Path = '/mnt/c/scripts/toProRes/working'
convert_Path = '/mnt/c/scripts/toProRes/working/inProcess/'
staging_Path = '/mnt/c/scripts/toProRes/working/staging/'
processed_Path = '/mnt/c/scripts/toProRes/working/processed/'
finished_Path = '/mnt/c/scripts/toProRes/ProRes/'

filePath = []
fileName = []


def buildList(l):
    filePath.append(os.path.join(r,l))
    fileName.append(os.path.join(l))

def moveToProcessed(file):
        moveFrom = convert_Path+file
        moveTo = processed_Path+file
        os.rename(moveFrom, moveTo)

def finalize():
    source = staging_Path
    dest1 = finished_Path

    files = os.listdir(source)

    for f in files:
        shutil.move(source+f, dest1)


def converToProRes(fileName, fullPath):
    finalName = staging_Path+fileName+"_ProResLT_3.mov"
    ff_command = "ffmpeg -i " + fullPath + " -vcodec prores_ks -profile:v 3 -qscale:v 9 -vendor ap10 -pix_fmt yuv422p10le -acodec pcm_s16le "+ finalName

    print("### " + ff_command)
    subprocess.call(ff_command, shell=True)

    # command = [
    #     'ffmpeg',
    #     '-i',
    #     fullPath,
    #     '-c:v prores_ks -profile:v 1',
    #     staging_Path+fileName+"_ProResLT.mov",
    # ]
    # print(command)
    #
    # ffmpeg_run = subprocess.Popen( 'ffmpeg', '-i', fullPath, '-c:v prores_ks -profile:v 1', finalName, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    # output, _ = ffmpeg_run.communicate()
    # print(_)

    # subprocess.call(['ffmpeg', '-i', fullPath, staging_Path+fileName+'_ProResLT.mov'])
    # os.system("ffmpeg -i "+fullPath" -c:v prores_ks -profile:v 1 "+staging_Path+fileName+"_ProResLT.mov")
    # subprocess.call()
#making a list
for r, d, f in os.walk(source_Path):
    for file in f:
        if '.MP4' in file:
            buildList(file)
        elif '.mp4' in file:
            buildList(file)


#Moving files to inProcess
for f in filePath:
    index = filePath.index(f)
    name = fileName[index]
    print(fileName)
    print("Moving " + name + " to inProcess")
    os.rename(f, convert_Path+name)

#start converting process
for f in fileName:
    fullPath = convert_Path + f
    print(fullPath)
    converToProRes(f, fullPath)
    moveToProcessed(f)


finalize()



# for root, dirs, files in os.walk("."):
#     for filename in files:
#         print(filename)
