def one_iteration(rows,is_part_a):
    has_been_executed = {}
    accumulator = 0
    current_instruction = 0
    try:
        while not current_instruction in has_been_executed.keys():
            instruction = rows[current_instruction][0]
            instruction_value = rows[current_instruction][1]
            has_been_executed[current_instruction] = True
            if instruction == "acc":
                accumulator += int(instruction_value)
                current_instruction+=1
                continue
            if instruction == "jmp":
                current_instruction += int(instruction_value)
                continue
            if instruction == "nop":
                current_instruction +=1
                continue
    except IndexError:
        return accumulator
    if is_part_a:
        print("Part a solution: "+ str(accumulator))
    return prune(rows,has_been_executed)

def prune(rows,has_been_executed):
    for i in has_been_executed.copy().keys():
        if rows[i][0] == "acc":
            del has_been_executed[i]
    return has_been_executed

def main(filepath):
    with open(filepath) as file:
        rows = [x.strip().split(" ") for x in file.readlines()]
    list_of_nor_jmp_instr = one_iteration(rows,True)
    for i in list_of_nor_jmp_instr:
        if rows[i][0] == "jmp":
            temp = "jmp"
            rows[i][0] = "nop"
        elif rows[i][0] == "nop":
            temp = "nop"
            rows[i][0] = "jmp"
        has_terminated = one_iteration(rows,False)
        if isinstance(has_terminated,int):
            print("Part b solution: "+ str(has_terminated))
            break
        else:
            rows[i][0] = temp
