def main(filepath):
    with open(filepath) as file:
        rows = [x.strip() for x in file.readlines()]
    current_direction = 90
    current_position = 0
    waypoint = 10 + 1j
    waypoint_position = 0
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
    for i in range(len(rows)):
        magnitude = int(rows[i][1:])
        if rows[i][0] in directions:
            current_position += magnitude*directions[rows[i][0]]
            waypoint += magnitude*directions[rows[i][0]]
        elif rows[i][0] == "L":
            current_direction = (current_direction - magnitude) % 360
            for n in range(int(magnitude/90)):
                waypoint = complex(-waypoint.imag, waypoint.real)
        elif rows[i][0] == "R":
            current_direction = (current_direction + magnitude) % 360
            for n in range(int(magnitude/90)):
                waypoint = complex(waypoint.imag, -waypoint.real)
        elif rows[i][0] == "F":
            current_position += magnitude*directions[turning[current_direction]]
            waypoint_position += magnitude*waypoint
    print("Part a solution: "+str(int(abs(current_position.real)+abs(current_position.imag))))
    print("Part b solution: "+str(int(abs(waypoint_position.real)+abs(waypoint_position.imag))))
