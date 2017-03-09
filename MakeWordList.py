import os

original_path = os.getcwd()
path_of_words = original_path + "/trump_words"
os.chdir(path_of_words)
entire_folder = os.listdir(path_of_words)

no_extensions = []


for word in entire_folder:
    no_extensions.append(word[:-4])


f = open("trump_words.txt", "w")
for word in no_extensions:
    f.write(" "+word+" \n")

f.close()