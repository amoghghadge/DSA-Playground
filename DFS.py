graph = {'1': ['2', '3'], '2': ['5'], '3': ['4', '6', '2'], '4': ['6'], '5': ['8'], '6': ['3', '7'], '7': ['2'], '8': ['7'], '9': ['8', '7']}

# https://chat.openai.com/share/0b99507d-afe6-4e05-bc88-a51159d0b1c9
def dfs_best(start):
    toVisit = []
    seen = set()

    toVisit.append(start)

    while toVisit:
        curr = toVisit.pop()

        if curr not in seen:
            seen.add(curr)
        
            for nei in graph[curr]:
                if nei not in seen:
                    toVisit.append(nei)

            print(curr, toVisit, seen)

print("Best DFS traversal")
dfs_best('1')

# taught in class, has error in traversal
# https://chat.openai.com/share/9b94586d-a006-44ba-ab44-84403b55451b
def dfs_class(start):
    toVisit = []
    seen = set()

    toVisit.append(start)
    seen.add(start)

    while toVisit:
        curr = toVisit.pop()
        
        for nei in graph[curr]:
            if nei not in seen:
                toVisit.append(nei)
                seen.add(nei)

        print(curr, toVisit, seen)

print("DFS taught in class")
dfs_class('1')