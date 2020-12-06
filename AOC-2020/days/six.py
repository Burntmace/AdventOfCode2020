def main(filepath):
    with open(filepath) as file:
        rows = [x.strip() for x in file.readlines()]
    count1 = 0
    count2 = 0
    part_a = set()
    part_b = []
    for i in range(len(rows)):
        if rows[i] == "" or i+1 == len(rows):
            count1 += len(part_a)
            count2 += len(set.intersection(*part_b))
            part_a = set()
            part_b = []
            continue
        part_b.append(set())
        for j in range(len(rows[i])):
            part_a.add(rows[i][j])
            part_b[-1].add(rows[i][j])
    print("Part a solution: "+ str(count1))
    print("Part b solution: "+ str(count2))
