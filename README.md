# ProRes Transcode Folder for Qnap
A simple python script that watches a folder for incoming movie files and then automatically converts those files to ProRes and cleans the file names of illegal characters.

#### Tested on QTS 4.3.0

# Description
This project is intended to assist with transcoding video files that were collected from multiple web sources to a common codec and sanitize their files names for use with SMB and Windows.

Qnap NAS devices come with ffmpeg and Python 2.7 installed by default.  This script uses those two technologies and Cron to continually monitor a folder for changes.

It should be noted that ffmpeg does not create an officially sanctioned ProRes file. Therefore, it is not advisable that one would use the files created with this tool for final client deliverables.

However, my testing has shown that the files created with ffmpeg do perform well in both Adobe Premiere and Blackmagic Resolve. So this tool should be useful for creating working files for complicated video edits.  

All of the scripts are under "/working/_scripts/" and are labeled for the flavor of ProRes they will create. They are self-contained and should not need to be edited to function correctly. However, if you wish to change the script to create a different codec it should be simple to modify. The variable 'ffmpeg_recipe' contains the ffmpeg instructions used. By changing this line you will change how the script converts the files.

#Other important notes: 
You can change the main directory name but all the other names in this folder structure are used in this script. Changing their names will break the script. 

because Github will not preserve an empty folder I have placed temp '.txt' files in each folder. Once you have downloaded the project and set it up you can delete the '.txt' files. 

While I specifically built and tested this on a Qnap device, it should run on any Linux box with python and ffmpeg install. 

# License

PTF for Qnap is distributed under the GPL making it completely open and available for anyone to use.
