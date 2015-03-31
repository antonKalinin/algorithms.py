import math

COST_MOVE = 5  # char is in another position
COST_DELETE = 20  # delete char
COST_ADD = 20  # add char
COST_CHANGE = 40  # delete and add new char


def char_cost(char, position, destination):
    if char in destination:
        positions = []
        last = 0

        while last != -1:
            last = destination.find(char, last)
            if last != -1:
                positions.append(last)
                last += 1

        min_shift = min([math.fabs(position-i) for i in positions])

        return min_shift * COST_MOVE
    else:
        if position > (len(destination)-1):
            return COST_DELETE
        else:
            return COST_CHANGE


def string_distance(source, destination):
    total_distance = 0
    len_diff = len(destination) - len(source)

    for i in range(len(source)):
        distance = char_cost(source[i], i, destination)
        total_distance += distance
        print('Distance for {0}: {1}'.format(source[i], distance))

    if len_diff > 0:
        total_distance += COST_ADD * len_diff

    return math.ceil(total_distance)


if __name__ == "__main__":
    string_a, string_b = 'alligatoor', 'alligator'
    print('Distance between {0} & {1}'.format(string_a, string_b))
    print('Distance is {0}'.format(string_distance(string_a, string_b)))
