num_obj = int(input())

objects = list(map(int, input().split()))
tracks = list(map(int, input().split()))
grau = [0] * num_obj

def findPath(position):
    if grau[tracks[position]-1] > 1:
        return 0#str(position+1)
    if tracks[position] == 0:
        return 0#str(position+1)
    return 1 + findPath(position-1) #str(position+1) + " " + findPath(position-1)
    
for i in range(num_obj):
    if tracks[i] != 0:
        grau[tracks[i]-1] += 1

for i in range(num_obj):
    if objects[i] == 1:
        print(findPath(i))
        
