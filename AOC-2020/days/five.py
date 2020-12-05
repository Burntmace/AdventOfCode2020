def main(filepath):
    with open(filepath) as file:
        rows = [int(x.strip().replace("F","0").replace("B","1").replace("L","0").replace("R","1"),2) for x in file.readlines()]
        rows.sort()
    print("Part a solution: "+ str(rows[-1]))
    for i in range(len(rows)):
        if not rows[i+1] - rows[i] == 1:
            print("Part b solution: "+ str(rows[i]+1))
            break
    return
