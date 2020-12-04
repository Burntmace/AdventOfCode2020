def calculation(filepath,down,across):
    with open(filepath) as file:
        rows = [x.strip() for x in file.readlines()]
    end = len(rows)
    currentrow = 0
    currentcolumn = 0
    count = 0
    while currentrow < (end-1):
        currentrow = currentrow+down
        currentcolumn = (currentcolumn+across)%len(rows[0])
        if rows[currentrow][currentcolumn] == "#":
            count+=1
    return count

def main(filepath):
    a = calculation(filepath,1,1)
    b = calculation(filepath,1,3)
    c = calculation(filepath,1,5)
    d = calculation(filepath,1,7)
    e = calculation(filepath,2,1)
    print("Part a solution: "+ str(b))
    print("Part b solution: "+ str(a*b*c*d*e))
    return
