def main(filepath):
    #file input
    with open(filepath) as file:
        rows = [x.strip().split("contain") for x in file.readlines()]

    #####---start of input parsing---#####
    #hash = {bag: list of contained bags}
    #numberhash = {bag: list of cardinalities of contained bags}
    #numberhash maps onto hash in the expected way.
    numbershash = {}
    for i in range(len(rows)):
        rows[i][0] = rows[i][0].split(" bags")[0]
        rows[i][1] = rows[i][1].split(",")
        numbershash[rows[i][0]] = []
        for j in range(len(rows[i][1])):
            if not rows[i][1][j].split(" ")[1] == "no":
                numbershash[rows[i][0]].append(int(rows[i][1][j].split(" ")[1]))
            rows[i][1][j] = rows[i][1][j].split(" ")[2]+" "+rows[i][1][j].split(" ")[3]
    #row[i] = [upper_bag,[inner_bag_1,inner_bag_1,...]]
    hash = {}
    for i in range(len(rows)):
        hash[rows[i][0]] = []
        for j in range(len(rows[i][1])):
            hash[rows[i][0]].append(rows[i][1][j])
        if hash[rows[i][0]] == ["other bags."]:
            hash[rows[i][0]] = []
    ######---end of input parsing---#####

    count_a = len(countbags(hash,"shiny gold",set(),set()))
    count_b = countbags2(hash,"shiny gold",0,numbershash)-1
    print("Part a solution: "+ str(count_a))
    print("Part b solution: "+ str(count_b))
    return

#recursively counts unique bags starting from smallest bag
def countbags(hash,target,currentset,checkedbags):
    for key in hash.keys():
        if target in hash[key]:
            currentset.add(key) #currentset = all bags that contain gold
    checkedbags.add(target)
    if not currentset == checkedbags:
        for bag in currentset.copy():
            if not bag in checkedbags:
                currentset = countbags(hash,bag,currentset,checkedbags)
    return currentset

#recursively counts bags starting from largest bag
def countbags2(hash,target,count,numbershash):
    if hash[target] == []:
        return 1
    temp = []
    for i in range(len(hash[target])):
        temp.append(numbershash[target][i]*countbags2(hash,hash[target][i],count,numbershash))
    count += sum(temp)
    count = count+1
    return count
