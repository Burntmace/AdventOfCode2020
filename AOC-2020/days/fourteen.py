import itertools
def main(filepath):
    with open(filepath) as file:
        rows = [x.strip() for x in file.readlines()]
    memory = {}
    mask_memory = {}
    for i in range(len(rows)):
        if rows[i][1] == "a":
            mask = rows[i].split("= ")[1]
        else:
            value = int(rows[i].split("= ")[1])
            mask_value = str(bin(value))[2:]
            address = int(rows[i].split("[")[1].split("]")[0])
            mask_address = str(bin(address))[2:]
            while len(mask_value) < len(mask):
                mask_value = "0"+mask_value
            while len(mask_address) < len(mask):
                mask_address = "0"+mask_address
            for n in range(len(mask)):
                if not mask[n] == "X":
                    mask_value = mask_value[:n] + mask[n] + mask_value[n+1:]
                if not mask[n] == "0":
                    mask_address = mask_address[:n] + mask[n] + mask_address[n+1:]
            memory[address] = int(mask_value,2)
            powerset = list(itertools.product([0, 1], repeat=mask_address.count("X")))
            for i in range(len(powerset)):
                address_copy = mask_address
                for n in range(len(address_copy)):
                    if address_copy[n] == "X":
                        address_copy = address_copy[:n] + str(powerset[i][0]) + address_copy[n+1:]
                        powerset[i] = powerset[i][1:]
                mask_memory[address_copy] = value
    print("Part a solution: "+str(sum(memory.values())))
    print("Part b solution: "+str(sum(mask_memory.values())))
