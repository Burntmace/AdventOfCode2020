def main(filepath):
    rows = []
    #file load
    with open(filepath) as file:
        for line in file:
            rows.append(line)
    counter = 0
    counter2 = 0
    for entry in rows:
        entry = entry.split(" ")
        letter = entry[1][0]
        entry[0] = entry[0].split("-")
        low = entry[0][0]
        high = entry[0][1]
        internalcount = 0
        for char in entry[2]:
            if char == letter:
                internalcount+=1
        if internalcount >= int(low) and internalcount <= int(high):
            counter+=1
        if (entry[2][int(low)-1] == letter) and not entry[2][int(high)-1] == letter:
            counter2+=1
        if not entry[2][int(low)-1] == letter and  entry[2][int(high)-1] == letter:
            counter2+=1
    print("Part a solution: "+ str(counter))
    print("Part b solution: "+ str(counter2))
    return
