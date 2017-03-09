import os
from pydub import AudioSegment
original_path = os.getcwd()
os.chdir(original_path + "/trump_speech_files")
files_to_cut = ["trump1","trump2","trump3","trump4"]

for file in files_to_cut:
	speech_file_name = file
	speech =AudioSegment.from_wav(speech_file_name +".wav")

	for i in range(len(speech)/600000):
		word = speech[i*600000:(i+1)*600000]
		word.export(speech_file_name+"_part_"+str(i)+".wav", format="wav")
	word = speech[int(len(speech)/600000)*600000:]
	word.export(speech_file_name+"_part_"+str(len(speech)/600000)+".wav", format="wav")