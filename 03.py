# BFC 广度优先搜索
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue = deque()
search_queue += graph["you"]

def person_is_seller(person):
    return person[-1] == "m"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False

search("you")