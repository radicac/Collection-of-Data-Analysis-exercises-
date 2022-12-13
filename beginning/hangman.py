def enter_word():
    return input()


def enter_letter():
    return input()


def print_word(marker, word, counter):
    for i, j in zip(marker, word):
        if i:
            print(j, end=" ")
        else:
            print("_", end=" ")
    print(" - ", counter)


def marker_true(marker):
    for i in marker:
        if not i:
            return False
    return True


def update_marker(word, marker, letter):
    for i, j in enumerate(word):
        if letter == j:
            marker[i] = True

def get_initial_marker(word):
    length = len(word)
    marker = [False] * length
    marker[0] = True
    marker[-1] = True
    update_marker(word, marker, word[0])
    update_marker(word, marker, word[-1])
    return marker

def start_game():
    print("enter a word")
    x = enter_word()
    marker = get_initial_marker(x)
    counter = 0
    while not marker_true(marker):
        print_word(marker, x, counter)
        y = enter_letter()
        update_marker(x, marker, y)
        counter = counter + 1
    print()
    print("u did it in", counter, "times")
    print(x)


start_game()
