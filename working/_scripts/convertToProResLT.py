import os, subprocess, shutil, re

#Finding the file locaiton of the master folder
current_dir = os.path.realpath(__file__)
master_path = os.path.sep.join(current_dir.split(os.path.sep)[:-3])

#file paths for the different folders
watch_path = master_path+'/download_here/'
in_process_path = master_path+'/working/inProcess/'
staging_path = master_path+'/working/temp/'
processed_path = master_path+'/working/processed/'
finished_path = master_path+'/ProRes/'

#simple lists for names and paths
file_path_array = []
file_name_array = []

#Functions

#building arrays of files.
def buildList(l):
    file_path_array.append(os.path.join(r,l))
    file_name_array.append(os.path.join(l))

#cleans file name
def cleanString(file_name):
    file_name_no_extention = os.path.splitext(file_name)
    space_to_dash = file_name_no_extention[0].replace(' ', '_').lower()
    clean_name = re.sub(r'[\W-]+', '', space_to_dash)
    return  clean_name

def move_to(move_from, move_to):
    os.rename(move_from, move_to)

def converToProRes(movie_file_name, current_path):
    clean_name = cleanString(movie_file_name)
    final_name = staging_path + clean_name + "_ProResLT.mov"
    ff_command = "ffmpeg -i '" + current_path + "' -vcodec prores_ks -profile:v 1 -qscale:v 9 -vendor ap10 -pix_fmt yuv422p10le -acodec pcm_s16le '" + final_name + "'"

    print("### " + ff_command)
    subprocess.call(ff_command, shell=True)

def finalize():
    source = staging_path
    destination = finished_path

    files = os.listdir(source)

    for f in files:
        shutil.move(source+f, destination)


#Video file type to look for
for r, d, f in os.walk(watch_path):
    for file in f:
        if '.MP4' in file:
            buildList(file)
        elif '.mp4' in file:
            buildList(file)
        elif '.mov' in file:
            buildList(file)
        elif '.MXF' in file:
            buildList(file)
        elif '.mxf' in file:
            buildList(file)
        elif '.webm' in file:
            buildList(file)
        elif '.avi' in file:
            buildList(file)
        elif '.flv' in file:
            buildList(file)
        elif '.wmv' in file:
            buildList(file)
        elif '.ogg' in file:
            buildList(file)

#Moving files to inProcess
for index, movie_file in enumerate(file_name_array):
    source = file_path_array[index]
    to_in_process = in_process_path + movie_file

    move_to(source, to_in_process)
    print('Moving' + movie_file + 'to inProcess')


#start converting process
for movie_file in file_name_array:
    movie_file_path = in_process_path + movie_file
    destination = processed_path + movie_file

    print("#####CALLING FFMPEG FUNCTION######")
    converToProRes(movie_file, movie_file_path)

    #move completed movie to processed folder
    move_to(movie_file_path, destination)

finalize()
