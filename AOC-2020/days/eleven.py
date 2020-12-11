from copy import deepcopy
def main(filepath):
    #file input
    with open(filepath) as file:
        rows = [x.strip() for x in file.readlines()]
    rows = appendBarrier(rows)
    rows1 = gameOfLife(rows,True)
    rows2 = gameOfLife(rows,False)
    count1 = 0
    count2 = 0
    for i in range(len(rows1)):
        count1 += rows1[i].count("#")
        count2 += rows2[i].count("#")
    print("part a solution: "+str(count1))
    print("part b solution: "+str(count2))

def appendBarrier(rows):
    blanks = ""
    for i in range(len(rows[0])):
        blanks = blanks + "!"
    rows.insert(0,blanks)
    rows.append(blanks)
    for i in range(len(rows)):
        rows[i] = "!"+rows[i]+"!"
    for i in range(len(rows)):
        rows[i] = list(rows[i])
    return rows

def gameOfLife(rows,is_part_a):
    while True:
        rows_copy = deepcopy(rows)
        for j in range(1,len(rows[0])-1): #i is horizontal
            for i in range(1,len(rows)-1): #j is horizontal
                if rows[i][j] == "L":
                    new_state = computeCell(rows,i,j,False,is_part_a)
                elif rows[i][j] == "#":
                    new_state = computeCell(rows,i,j,True,is_part_a)
                elif rows[i][j] == ".":
                    new_state = "."
                rows_copy[i][j] = new_state
        if rows == rows_copy:
            break
        rows = rows_copy
    return rows

def computeCell(rows,i,j,is_occupied,is_part_a):
    list = []
    if is_part_a:
        for n in range(i-1,i+2):
            for m in range(j-1,j+2):
                list.append(rows[n][m])
    else:
        directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        for direction in directions:
            x=i
            y=j
            while True:
                x += direction[0]
                y += direction[1]
                if not rows[x][y] == ".":
                    list.append(rows[x][y])
                    break
    count = list.count("#")
    if is_occupied:
        if count >= 5:
            return "L"
        else:
            return "#"
    else:
        if count == 0:
            return "#"
        else:
            return "L"
