#remove a word from a txt
#open up the txt
f = open('E:\PYTHON REPO\Python_practice\pythonDeleteword\preproinsulin_seq.txt','r')
#what you want to remove
a = ['ORIGIN', '1', '6', '//']
#empty listt your gonna input new data in
lst = []
#reading the lines in the files
for line in f:
    #going through the words
    for word in a:
        #if the word exist delete it
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
#creating new file
f = open('E:\PYTHON REPO\Python_practice\pythonDeleteword\preproinsulin_seq.txtclean','w')
#writing new txt file
for line in lst:
    f.write(line)
f.close()