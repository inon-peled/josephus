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


if __name__ == '__main__':
    for n in (41, 100):
        final_arrangement = moment_when_each_person_dies(n)
        survivor = final_arrangement.index(None) + 1
        survivor_english = str(survivor) + {1: 'st', 2: 'nd', 3: 'rd'}.get(survivor % 10, 'th')
        print('For %s people, the %s person survives: %s' % (n, survivor_english, final_arrangement))
