import os
import subprocess
import shutil

master_path = "/share/CACHEDEV1_DATA/R2 Working/python/qnap-prores-watch-folder-master"

watch_path = master_path+'/download_here/'
in_process_path = master_path+'/working/inProcess/'
staging_path = master_path+'/working/temp/'
processed_path = master_path+'/working/processed/'
finished_path = master_path+'/ProRes/'

file_path_array = []
file_name_array = []

def cleanString(file_name):
    just_the_name = os.path.splitext(file_name)
    needs_cleaning = just_the_name[0]
    cleaned = "".join(i for i in needs_cleaning if i not in "\/:*?<>|")
    return cleaned

def buildList(l):
    file_path_array.append(os.path.join(r,l))
    file_name_array.append(os.path.join(l))

def moveToInProcess(path, file_name):
        moveFrom = path
        moveTo = in_process_path+file_name
        os.rename(moveFrom, moveTo)

def moveToProcessed(file):
        moveFrom = in_process_path+file
        moveTo = processed_path+file
        os.rename(moveFrom, moveTo)

def converToProRes(file_name, full_path):
    print("File Name " +file_name)
    cleanName = cleanString(file_name)
    print("clean name " + cleanName)
    finalName = staging_path + cleanName + "_ProResLT.mov"
    ff_command = "ffmpeg -i '" + full_path + "' -vcodec prores_ks -profile:v 1 -qscale:v 9 -vendor ap10 -pix_fmt yuv422p10le -acodec pcm_s16le '" + finalName + "'"

    print("### " + ff_command)
    subprocess.call(ff_command, shell=True)


#making a list
for r, d, f in os.walk(watch_path):
    for file in f:
        if '.MP4' in file:
            buildList(file)
        elif '.mp4' in file:
            buildList(file)

#Moving files to inProcess
for f in file_path_array:
    index = file_path_array.index(f)
    name_of_movie = file_name_array[index]

    print("Moving " + name_of_movie + " to inProcess")
    moveToInProcess(f, name_of_movie)

#start converting process
for file_name in file_name_array:
    fullPath = in_process_path + file_name
    print("#####CALLING FFMPEG FUNCTION######")
    converToProRes(file_name, fullPath)
    moveToProcessed(file_name)

def finalize():
    source = staging_path
    dest1 = finished_path

    files = os.listdir(source)

    for f in files:
        shutil.move(source+f, dest1)

finalize()



# for root, dirs, files in os.walk("."):
#     for filename in files:
#         print(filename)
