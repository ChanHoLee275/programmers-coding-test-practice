def addPath(route, beforeLocation, location):
    route.add(tuple(beforeLocation + location))
    route.add(tuple(location + beforeLocation))

def solution(dirs):
    answer = 0
    route = set()
    location = [0, 0]
    for i in list(dirs):
        beforeLocation = location[:]
        if i == "U" and location[1] < 5:
            location[1] += 1
            addPath(route, beforeLocation, location)
        elif i == "D" and location[1] > -5 :
            location[1] -= 1
            addPath(route, beforeLocation, location)
        elif i == "L" and location[0] > -5:
            location[0] -= 1
            addPath(route, beforeLocation, location)
        elif i == "R" and location[0] < 5:
            location[0] += 1
            addPath(route, beforeLocation, location)
    return int(len(list(route))/2)