files = ['cats.txt', 'dogs.txt']

def file_reader(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

for file in files:
    file_reader(file)

