import math


def __find_next_alive(people, i):
    n = len(people)
    for j in range(n):
        i = (i + 1) % n
        if people[i] is None:
            return i


def moment_when_each_person_dies(num_people):
    people = [None] * num_people
    i = 0
    num_alive = num_people
    while num_alive > 1:
        j = __find_next_alive(people, i)
        people[j] = num_people - num_alive
        num_alive -= 1
        i = __find_next_alive(people, j)
    return people


def position_of_survivor(num_people):
    lower_power_of_2 = 2 ** (len(bin(num_people)) - len('0b') - 1)
    return 2 * (num_people - lower_power_of_2) + 1


if __name__ == '__main__':
    for n in range(1, 101):
        final_arrangement = moment_when_each_person_dies(n)
        survivor = final_arrangement.index(None) + 1
        assert position_of_survivor(n) == survivor
        survivor_english = str(survivor) + {1: 'st', 2: 'nd', 3: 'rd'}.get(survivor % 10, 'th')
        print('For %s people, the %s person survives: %s' % (n, survivor_english, final_arrangement))
