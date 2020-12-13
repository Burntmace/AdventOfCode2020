def main(filepath):
    with open(filepath) as file:
        rows = [x.strip() for x in file.readlines()]
    your_time = int(rows[0])
    bus = rows[1].split(",")
    bus_no_x = list(filter(("x").__ne__, bus))
    bus_relative = []
    for i in range(len(bus_no_x)):
        bus_relative.append(-your_time % int(bus_no_x[i]))
    part_a = min(bus_relative)*int(bus_no_x[bus_relative.index(min(bus_relative))])
    print("Part a solution: "+str(part_a))
    #part b
    m = []
    x = []
    for i in range(len(bus)):
        if not bus[i] == "x":
            m.append(int(bus[i]))
            x.append(int(bus[i])-i)
    CRAlgorithm(m,x)

#computes answer using Chinese Remainder Theorem (assumes input is pairwise coprime)
def CRAlgorithm(m,x):
    while True:
        temp1 = inverseMod(m[1],m[0])*x[0]*m[1]+inverseMod(m[0],m[1])*x[1]*m[0]
        temp2 = m[0]*m[1]
        x.remove(x[0])
        x.remove(x[0])
        x = [temp1 % temp2]+x
        m.remove(m[0])
        m.remove(m[0])
        m = [temp2]+m
        if len(x) == 1:
            break
    print("Part a solution: "+str(x[0]))

#computes g,x,y such that gcd(a,b) = g, and ax+by = g
def EEAlgorithm(a,b):
    if a == 0:
        return (b,0,1)
    else:
        gcd, x, y = EEAlgorithm(b % a, a)
        return (gcd, y - (b // a) * x, x)

#returns x such that ax mod m = 1
def inverseMod(a,m):
    x = EEAlgorithm(a,m)[1]
    return x % m
