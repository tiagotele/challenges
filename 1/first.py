from os import listdir
from os.path import isfile
import sys


def get_files_only(suffix, path):
    final_files=[]

    for f in listdir(path):
        if isfile(path+f):
            final_files.append(path+f)
        else:
            final_files.extend(get_files_only(suffix, path+f+"/"))
    return [f for f in final_files if f.endswith(suffix)]

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Missing arguments")

    suffix = sys.argv[1]
    path = sys.argv[2]

    final_files=get_files_only(sys.argv[1], sys.argv[2])
    for f in final_files:
        print(f)