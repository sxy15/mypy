from os import listdir
from os.path import isfile, join
from collections import deque

def printnames(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)

    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(fullpath)
            else:
                search_queue.append(fullpath)

printnames("pics")

# pics/odayssey.png
# pics/2001/a.png
# pics/2001/space.png