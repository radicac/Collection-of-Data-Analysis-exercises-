import random


def generate_random_boolean():
    if random_integer(0, 1) == 1:
        return True
    else:
        return False


def generate_three_random_booleans():
    x = [generate_random_boolean(), generate_random_boolean(), generate_random_boolean()]
    return x


def generate_random_doors():
    x = generate_three_random_booleans()
    while not x.count(False) == 2:
        x = generate_three_random_booleans()
    return x


def fast_generate_random_doors():
    x = [False, False, False]
    y = random_integer(0, 2)
    x[y] = True
    return x


def stubborn_user_selection(doors):
    y = random_integer(1, 3) - 1
    # print(y)
    return doors[y]


def random_integer(start, end):
    return random.randint(start, end)


def smart_user_selection(doors):
    y = random_integer(1, 3) - 1
    return not doors[y]


def simulate_n_times(n, doors_generator_function, user_selection_function):
    count = 0
    for i in range(n):
        a = doors_generator_function()
        b = user_selection_function(a)
        if b:
            count = count + 1
    return count


number_of_simulations = 200000
c = simulate_n_times(number_of_simulations, generate_random_doors, stubborn_user_selection)
print(c)
d = simulate_n_times(number_of_simulations, generate_random_doors, smart_user_selection)
print(d)

c = simulate_n_times(number_of_simulations, fast_generate_random_doors, stubborn_user_selection)
print(c)
d = simulate_n_times(number_of_simulations, fast_generate_random_doors, smart_user_selection)
print(d)
# a = generate_random_doors()
# print(a)
# b = stubborn_user_selection(a)
# #print(b)


# print([random_integer(1,3) for i in range(1000)].count(2))
# print(generate_random_doors())
