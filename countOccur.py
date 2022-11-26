s = "this this this this is what you came for"
a = s.split(' ')

map = {}

for i in a:
    count = 1
    if i not in map:
        map[i] = count
    else:
        count+=1
        map.update({i:map[i]+1})
        

print(map)