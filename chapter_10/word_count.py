def count_words(filename):
    """Подсчет приблизительного количества слов в файле."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)
        #pass
        with open('missing_files.txt', 'a') as missed_files:
            missed_files.write(filename) 
    else:
        #Подсчет приблизительного количества слов в файле.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + 
            " words.")
            
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
