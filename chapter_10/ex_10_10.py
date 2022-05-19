filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

def count_words(filename, key='the'):
    """Подсчет приблизительного количества определенных слов слов в файле."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg) 
    else:
        #Подсчет приблизительного количества слов в файле.
        num_words = contents.lower().count(key)
        print("The file " + filename + " has about " + str(num_words) + 
            " '" + key + "'" + " words.")
            
for filename in filenames:
    count_words(filename, 'george')
