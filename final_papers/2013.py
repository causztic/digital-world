# question 1
def init():
    return [["_" for i in range(3)] for i in range(3)]


def show(b):
    s = ""
    for li in b:
        for letter in li:
            s += letter
        s += "\n"
    return s


def movex(b, i, j):
    b[i - 1][j - 1] = "x"


def moveo(b, i, j):
    b[i - 1][j - 1] = "o"


def countmoves(b):
    count = 0
    for li in b:
        for letter in li:
            if letter != "_":
                count += 1
    return count


def getmoves(b):
    d = {'x': [], 'o': []}
    for i_index, li in enumerate(b):
        for j_index, letter in enumerate(li):
            if letter in ["x", "o"]:
                d[letter].append((i_index + 1, j_index + 1))
    return d


def game_check(b, item):
    if b[0][0] == item and b[1][1] == item and b[2][2] == item:
        # diagonal
        return True

    if b[0][2] == item and b[1][1] == item and b[2][0] == item:
        # other diagonal
        return True

    for i in range(3):
        # verticals
        if b[0][i] == item and b[1][i] == item and b[2][i] == item:
            return True

        # horizontal
        elif b[i][0] == item and b[i][1] == item and b[i][2] == item:
            return True

    # if doesn't win
    return False

def winsx(b):
    return game_check(b, "x")

def winso(b):
    return game_check(b, "o")
