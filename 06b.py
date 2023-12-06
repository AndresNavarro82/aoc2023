time = 0
distance = 0
with open("06.txt") as file:
    time = ''.join(file.readline().split()[1:])    
    time = int(time)
    distance = ''.join(file.readline().split()[1:])
    distance = int(distance)

#print(time)
#print(distance)

count = 0
for i in range(1,time+1):
    if i*(time-i) > distance:
        count+=1
print(count)
