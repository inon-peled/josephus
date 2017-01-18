def __find_next_alive(people, i):
    n = len(people)
    for j in range(n):
        i = (i + 1) % n
        if people[i]:
            return i

def play(n):
    people = [True] * n
    i = 0
    num_alive = n
    while num_alive > 1:
        j = __find_next_alive(people, i)
        people[j] = False
        num_alive -= 1
        i = __find_next_alive(people, j)
    return people

if __name__ == '__main__':
    print(play(40).index(True) + 1)
