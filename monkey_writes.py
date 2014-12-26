import random
import string

target = "methinks it is like a weasel"
target_len = len(target)
source_string = string.lowercase + ' '


def generator(input, positions):
    if input is None or len(positions) == target_len:
        return ''.join(random.choice(source_string) for i in range(target_len))

    input = list(input)

    for position in positions:
        input[position] = random.choice(source_string)

    return ''.join(input)


def comparer(input):
    difference = []
    range_list = range(target_len)

    for i in range_list:
        input_letter = input[i]
        target_letter = target[i]

        if input_letter is not target_letter:
            difference.append(i)

    return difference


def process(generated_in, difference_in, tries_count):
    generated_out = generator(generated_in, difference_in)
    difference_out = comparer(generated_out)

    tries_count += 1

    if len(difference_out) != 0:
        tries_count = process(generated_out, difference_out, tries_count)

    return tries_count


def processor():
    tries_count = 0
    start_difference = range(target_len)

    return process(None, start_difference, tries_count)


if __name__ == "__main__":
    print ('RESULT: {result}'.format(result=processor()))
