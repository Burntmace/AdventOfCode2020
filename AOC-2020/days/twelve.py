def main(filepath):
    with open(filepath) as file:
        rows = [x.strip() for x in file.readlines()]
    directions = {
        "N":0 + 1j,
        "E":1 + 0j,
        "S":0 - 1j,
        "W":-1 + 0j
    }
    turning = {
        0:"N",
        90:"E",
        180:"S",
        270:"W"
    }
    part_a = compute(directions,turning,rows,True)
    part_b = compute(directions,turning,rows,False)
    print("Part a solution: "+str(part_a))
    print("Part b solution: "+str(part_b))

def compute(directions,turning,rows,is_part_a):
    current_direction = 90
    current_position = 0
    if is_part_a:
        for i in range(len(rows)):
            magnitude = int(rows[i][1:])
            if rows[i][0] in directions:
                current_position += magnitude*directions[rows[i][0]]
            elif rows[i][0] == "L":
                current_direction = (current_direction - magnitude) % 360
            elif rows[i][0] == "R":
                current_direction = (current_direction + magnitude) % 360
            elif rows[i][0] == "F":
                current_position += magnitude*directions[turning[current_direction]]
        return int(abs(current_position.real)+abs(current_position.imag))
    else:
        waypoint = 10 + 1j
        for i in range(len(rows)):
            magnitude = int(rows[i][1:])
            if rows[i][0] in directions:
                waypoint += magnitude*directions[rows[i][0]]
            elif rows[i][0] == "L":
                for n in range(int(magnitude/90)):
                    waypoint = complex(-waypoint.imag, waypoint.real)
            elif rows[i][0] == "R":
                for n in range(int(magnitude/90)):
                    waypoint = complex(waypoint.imag, -waypoint.real)
            elif rows[i][0] == "F":
                current_position += magnitude*waypoint
        return int(abs(current_position.real)+abs(current_position.imag))
