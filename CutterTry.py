import os
from pydub import AudioSegment


def get_audio(speech_file_name):
    speech = AudioSegment.from_wav(speech_file_name)
    return speech


def parse_audio(b_time_stamps, e_time_stamps, words, speech):
    entire_folder = os.listdir(os.getcwd())
    for i in range(len(b_time_stamps)):
        start = int(1000 * b_time_stamps[i]);
        end = int(1000 * e_time_stamps[i]);
        word = speech[start:end]
        word_string = words[i].lower() + '.wav';
        word.export(word_string, format="wav")


"""Not sure how the data will be imported"""


def parse_file(beginning_timestamps, end_timestampswords, words, speech):
    original_path = os.getcwd()
    path_of_words = original_path + "/trump_words"
    path_of_speech_file = original_path + "/trump_speech_files"
    os.chdir(path_of_speech_file)
    audio = get_audio(speech)
    os.chdir(path_of_words)
    parse_audio(beginning_timestamps, end_timestampswords, words, audio)
    os.chdir(original_path)

"""
data = []
beginning_timestamps = []
end_timestamps = []
words = []
percentage = []
for i in range(len(data)):
    if (data[i]['Confidence'] < 0.8):
        continue
    else:
        beginning_timestamps.append(data[i]['Start_Timestart'])
        end_timestamps.append(data[i]['End_Timestart'])
        words.append(data[i]['Transcript'])
        percentage.append(data[i]['Confidence'])
parse_file(beginning_timestamps, end_timestamps, words, "Trimmed.wav")
"""