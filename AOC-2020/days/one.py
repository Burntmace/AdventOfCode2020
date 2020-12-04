def main(filepath):
    rows = []
    #file load
    with open(filepath) as file:
        for line in file:
            rows.append(line)
    #cartesian product
    for i in range(len(rows)):
        for j in range(i,len(rows)):
            if int(rows[i])+int(rows[j]) == 2020:
                print("Part a solution: "+ str(int(rows[i])*int(rows[j])))
            for k in range(j,len(rows)):
                if int(rows[i])+int(rows[j])+int(rows[k]) == 2020:
                    print("Part b solution: "+ str(int(rows[i])*int(rows[j])*int(rows[k])))
    return
