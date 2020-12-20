from subprocess import call
import subprocess


def updateVideos():
    #Bash script, removes existing mp4 files from images file
	subprocess.call("./removeOrigVid.sh")
	
	#Converts all h264 files to mp4
	for x in range(0, 3):
    		command = "MP4Box -add ./images/pivid{iter}.h264 ./images/pivid{iter}.mp4"
    		replace = command.format(iter = x)
    		call([replace], shell=True)



updateVideos()
