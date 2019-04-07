# ProRes Transcode Folder for Qnap
A simple python script that watches a folder for incoming movie files and then automatically converts those files to ProRes and cleans the file names of illegal characters.

#### Tested on QTS 4.3.0

# Description
This project is intended to assist with transcoding video files that were collected from multiple web sources to a common codec and sanitize their files names for use with SMB and Windows.

Qnap NAS devices come with ffmpeg and Python 2.7 installed by default.  This script uses those two technologies and Cron to continually monitor a folder for changes.

It should be noted that ffmpeg does not create an officially sanctioned ProRes file. Therefore, it is not advisable that one would use the files created with this tool for final client deliverables.

However, my testing has shown that the files created with ffmpeg do perform well in both Adobe Premiere and Blackmagic Resolve. So this tool should be useful for creating working files for complicated video edits.  

All of the scripts are under "/working/_scripts/" and are labeled for the flavor of ProRes they will create. They are self-contained and should not need to be edited to function correctly. However, if you wish to change the script to create a different codec it should be simple to modify. The variable 'ffmpeg_recipe' contains the ffmpeg instructions used. By changing this line you will change how the script converts the files.

# Other important notes: 
You can change the main directory name but all the other names in this folder structure are used in this script. Changing their names will break the script. 

because Github will not preserve an empty folder I have placed temp '.txt' files in each folder. Once you have downloaded the project and set it up you can delete the '.txt' files. 

While I specifically built and tested this on a Qnap device, it should run on any Linux box with python and ffmpeg installed. 

# License

PTF for Qnap is distributed under the GPL making it completely open and available for anyone to use.

# Installation
1.) start by downloading this project with the 'Clone or Download' button in the top right of the Github page. 

unzip and move the folder to a location you want it to be on your Qnap NAS device. 

2.) Rename the folder to something that makes sense to you. 

3.) SSH into your device.
Find your Qnap devices IP address and open up a terminal. 
In the terminal type...
```python
ssh admin@(device ip address here)
```
You will want to locate the exact path to the script you want to run. 

Navigate to the shared folders by typing ...
```python
cd /share/CACHEDEV1_DATA/
```
From here use 'cd' or 'ls' command to locate the folder you just copied over.
When you find it save this location for later use.  
example:
/share/CACHEDEV1_DATA/Shared-Folder/qnap-prores-watch-folder/working/_scripts/toLT.py

4.) Ad the script to Crontab
type this into the ssh terminal.
```python
crontab -e
```
or
```python
vi /etc/config/crontab
```
###add this line with the correct directory to the script 
This example will run the script every 2 minutes. 
*/2 * * * * python /share/CACHEDEV1_DATA/100_working/__toProRes/working/_scripts/toLT.py

###save the file
hit escape
```python
esc 
```
Then type
```python
:wq
```

###restart crontab
```python
crontab /etc/config/crontab && /etc/init.d/crond.sh restart
```

Now you should be ready to test the folder. 



