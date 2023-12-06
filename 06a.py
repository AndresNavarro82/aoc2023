times = []
distances = []
with open("06.txt") as file:
    times = file.readline().split()[1:]    
    times = [int(i) for i in times]
    distances = file.readline().split()[1:]
    distances = [int(i) for i in distances]

#print(times)
#print(distances)
margin = 1
for t, d in zip(times, distances):
    count = 0
    for i in range(1,t+1):
        if i*(t-i) > d:
            count+=1
    margin*=count
print(margin)
