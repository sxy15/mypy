# 深度优先搜索

from os import listdir
from os.path import isfile, join

def printnames(start_dir):
    for file in sorted(listdir(start_dir)):
        fullpath = join(start_dir, file)
        if isfile(fullpath):
            print(fullpath)
        else:
            printnames(fullpath)

printnames("pics")

# pics/2001/a.png
# pics/2001/space.png
# pics/odayssey.png