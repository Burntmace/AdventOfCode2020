def main(filepath):
    with open(filepath) as file:
        rows = [int(x.strip())for x in file.readlines()]
    for i in range(25,len(rows)):
        condition_met = False
        for j in range(i-25,i):
            for k in range(i-25,i):
                if (rows[k] + rows[j]) == rows[i] and not rows[k] == rows[j]:
                    condition_met = True
        if not condition_met:
            b_target = rows[i]
            print("Part a solution: "+ str(b_target))
            break
    for i in range(len(rows)):
        for j in range(i,len(rows)):
            if sum(rows[i:j]) == b_target and not len(rows[i:j])==1:
                print("Part a solution: "+ str(max(rows[i:j])+min(rows[i:j])))
