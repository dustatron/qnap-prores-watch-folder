import os
import re

test_string = 'MVI_?0662|.MP4'

watch_path = '/share/CACHEDEV1_DATA/R2 Working/python/qnap-prores-watch-folder-master/working/processed'
file_path_array = []
file_name_array = []

def buildList(l):
    file_path_array.append(os.path.join(r,l))
    file_name_array.append(os.path.join(l))

def cleanString(file_name):
    file_name_no_extention = os.path.splitext(file_name)
    space_to_dash = file_name_no_extention[0].replace(' ', '_').lower()
    clean_name = re.sub(r'[\W-]+', '', space_to_dash)
    return  clean_name

for r, d, f in os.walk(watch_path):
    for file in f:
        if '.MP4' in file:
            buildList(file)
        elif '.mp4' in file:
            buildList(file)

for i in file_name_array:
    new_name = cleanString(i)
    print(new_name)






# line = re.sub('[!@#$|?]', '', test_string)
#
#
# space_to_dash = line.replace(' ', '-').lower()
#
# # artistName = ''.join(e for e in line if e.isalnum() or e == '-')
#
#
#
# print(space_to_dash)

# print(bool(re.match("^[A-Za-z0-9_-]*$", test_string)))
# print(bool(re.match("^[A-Za-z0-9_-]*$", 'inv@lid')))
