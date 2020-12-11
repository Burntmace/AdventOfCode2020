def main(filepath):
    with open(filepath) as file:
        rows = [int(x.strip()) for x in file.readlines()]
        rows.append(0)
        rows.sort()
        rows.append(rows[-1]+3)
        current_volts = 0
        one_volts = 0
        three_volts = 0
        for i in range(len(rows)):
            if rows[i] - current_volts == 0:
                continue
            if rows[i] - current_volts == 1:
                current_volts = rows[i]
                one_volts += 1
                continue
            if rows[i] - current_volts == 2:
                current_volts = rows[i]
                continue
            if rows[i] - current_volts == 3:
                current_volts = rows[i]
                three_volts += 1
                continue
        print("Part a solution: "+ str(three_volts*one_volts))
        rows.reverse()
        memo = {}
        memo[rows[0]] = 1
        for i in range(1,len(rows)):
            memo[rows[i]] = memo.get(rows[i] + 1, 0) + memo.get(rows[i] + 2, 0) + memo.get(rows[i] + 3, 0)
        print("Part b solution: "+ str(memo[0]))
