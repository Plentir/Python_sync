f = open("Holsu.txt", "w")
tot = 0

for l in range(0, 101):
    if l % 2 != 0:
        f.write("%d \n" % l)
        tot = tot + l
        
f.write("홀수의 총 합은 %d이다." % tot)
f.close()
