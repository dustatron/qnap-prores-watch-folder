import os.path

master_path = "/share/CACHEDEV1_DATA/R2 Working/python/qnap-prores-watch-folder-master"

watch_Path = master_path+'/ProRes/download_here/'

print("looking in folder")


#
# for r, d, f in os.walk(master_path):
#     for file in f:
#         print(f)

name = "MVI_?0662|.MP4"

def cleanString(file_name):
    just_the_name = os.path.splitext(file_name)
    needs_cleaning = just_the_name[0]
    cleaned = "".join(i for i in needs_cleaning if i not in "\/:*?<>|")
    return cleaned

print( cleanString(name))
