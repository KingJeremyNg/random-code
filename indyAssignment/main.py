file = open('q4_distance.txt', 'r+')
arr = file.readlines()
arr.pop(0)
rows = []

data = {
    "house1": [],
    "house2": [],
    "house3": [],
    "house4": [],
    "apartment1": [],
    "apartment2": [],
    "apartment3": [],
    }

for r in arr:
    temp = r.split('\t')
    temp.pop(0)
    temp[len(temp) - 1] = temp[len(temp) - 1].replace('\n', '')
    
    for n in range(0, len(temp)) :
        data.get(list(data)[n]).append(temp[n])

print(data)