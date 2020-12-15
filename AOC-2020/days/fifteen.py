def game(input,max_turns):
    memory = {}
    turncounter = 1
    most_recent_number = int(input[-1])
    for i in range(len(input)):
        memory[int(input[i])] = [turncounter,-1]
        turncounter += 1
    while turncounter <= max_turns:
        if memory[most_recent_number][1] == -1:
            most_recent_number = 0
        else:
            most_recent_number = memory[most_recent_number][0] - memory[most_recent_number][1]
        if most_recent_number in memory:
            memory[most_recent_number] = [turncounter,memory[most_recent_number][0]]
        else:
            memory[most_recent_number] = [turncounter,-1]
        turncounter +=1
    return str(most_recent_number)
def main(filepath):
    with open(filepath) as file:
        rows = [x.strip() for x in file.readlines()]
    input = rows[0].split(",")
    print("Part a solution: "+game(input,2020))
    print("Part b solution: "+game(input,30000000)) #takes a while to run, but less than 1 minute
