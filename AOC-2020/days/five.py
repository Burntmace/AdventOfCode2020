def main(filepath):
    with open(filepath) as file:
        rows = [x.strip() for x in file.readlines()]
    max = 0
    dict = {}
    missing_IDs = []
    for i in range(len(rows)):
        row = list(range(0,128))
        for char in rows[i][0:7]:
            if char == "F":
                row = row[:len(row)//2]
            if char == "B":
                row = row[len(row)//2:]
        column = list(range(0,8))
        for char in rows[i][7:10]:
            if char == "L":
                column = column[:len(column)//2]
            if char == "R":
                column = column[len(column)//2:]
        if 8*row[0]+column[0] > max:
            max = 8*row[0]+column[0]
        dict[8*row[0]+column[0]] = True
    print("Part a solution: "+ str(max))
    for i in range(0,128*8+8):
        if not i in dict.keys():
            missing_IDs.append(i)
    for i in range(len(missing_IDs)):
        if not missing_IDs[i+1] == missing_IDs[i]+1:
            print("Part b solution: "+ str((missing_IDs[i+1])))
            break
    return
