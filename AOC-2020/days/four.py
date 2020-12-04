import re
def main(filepath):
    with open(filepath) as file:
        rows = [x.strip() for x in file.readlines()]
    passport = {}
    counter1 = 0
    counter2 = 0
    for i in range(len(rows)):
        if rows[i] == "":
            if checkpassport(passport):
                counter1+=1
                if checkvalid(passport):
                    counter2+=1
            passport = {}
        else:
            rows[i] = rows[i].split(" ")
            for j in range(len(rows[i])):
                passport[rows[i][j].split(":")[0]] = rows[i][j].split(":")[1]
    if checkpassport(passport):
        counter1+=1
        if checkvalid(passport):
            counter2+=1
    print("Part a solution: "+ str(counter1))
    print("Part b solution: "+ str(counter2))
    return

def checkpassport(passport):
    if all(keys in passport for keys in ("byr","iyr","eyr","hgt","hcl","ecl","pid")):
        return True
    return False

def checkvalid(passport):
    params = []
    params.append(2002 >= int(passport["byr"]) >= 1920)
    params.append(2020 >= int(passport["iyr"]) >= 2010)
    params.append(2030 >= int(passport["eyr"]) >= 2020)
    params.append(re.match("[#][0-9a-f]{6}",passport["hcl"]))
    params.append(len(passport["hcl"])==7)
    params.append(re.match("(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)",passport["ecl"]))
    params.append(re.match("[0-9]{9}",passport["pid"]))
    params.append(len(passport["pid"]) == 9)
    if passport["hgt"][-2:] == "cm":
        params.append(193 >= int(passport["hgt"][:-2]) >= 150)
    elif passport["hgt"][-2:] == "in":
        params.append(76 >= int(passport["hgt"][:-2]) >= 59)
    else:
        params.append(False)
    return all(params)
