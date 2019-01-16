from  itertools import combinations as comb

def maxDistance(dis, x):
    var=0
    flag="True"
    if sum(dis) <= x :
        return sum(dis)
    for j in range(len(dis)):
        if dis[j] <= x:
            flag="False"
    for u in range(len(dis)):
        dis1 = list(comb(dis, u))
        for i in dis1:
            if sum(i) <= x and sum(i) > var:
                var = sum(i)

    if flag == "True":
        return "Your integer is smaller than your list"
    else:
        return var


s = raw_input("Give 1 or more distance (exp:1 3 2...) : ")
dis = map(int, s.split())
x = input("Give a positive integer (exp:10) : ")
print maxDistance(dis,x)
