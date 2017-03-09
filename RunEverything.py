from SpeechTry import *
from CutterTry import *

original_path = os.getcwd()
f = open("words_list.txt", "w")


trump_speech_folder = os.getcwd() + "/trump_speech_files/"
names = os.listdir(trump_speech_folder)

for name in names[11:]:
	print("STARTING SPEECH TRANSLATE TO TEXT...")
	theArray=speechaf(name)


	beginning_timestamps=[]
	end_timestamps=[]
	words=[]
	percentage=[]

	for i in range(len(theArray)):
	    if(theArray[i][3] < 0.8):
	        continue
	    else:
	    	b_timestamps = str(theArray[i][1])
	    	e_timestamps = str(theArray[i][2])
	    	word = str(theArray[i][0])
	    	perc = str(theArray[i][3])

	    	line = b_timestamps + " " + e_timestamps + " " + word + " " + perc
	    	
	    	f.write(line+ "\n")

	        beginning_timestamps.append(theArray[i][1])
	        end_timestamps.append(theArray[i][2])
	        words.append(theArray[i][0])
	        percentage.append(theArray[i][3])
	print("STARTING PARSE OF " + name)
	parse_file(beginning_timestamps,end_timestamps,words,name)

f.close()