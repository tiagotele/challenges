from os import listdir
from os.path import isfile


def my_func(suffix, path):
    final_files=[]

    for f in listdir(path):
        if isfile(path+f):
            final_files.append(path+f)
        else:
            final_files.extend(my_func(suffix, path+f+"/"))
    return final_files

if __name__ == '__main__':
    mypath="/Users/Tiago/git/cocus/"
    first_level=mypath+"1/first_level_files/"

    final_files=my_func(None, mypath)
    for f in final_files:
        print(f)