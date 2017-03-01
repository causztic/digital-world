import timeit

f = open('week6/unixdict.txt', 'r')


def find_anagram(f):
    lines = f.readlines()
    max_length = len(lines[-1])
    # this splits the lines based on length of each word.
    sorted_lines = [[i.strip() for i in lines if len(i) == length]
                    for length in range(1, max_length + 1)]
    anagrams = []
    for item in sorted_lines:
        # convert individual words into alphabetical ordered strings to
        # preserve indices.
        converted_to_order = ["".join(sorted(list(i))) for i in item]
        # make a copy of the converted_to_order list and sort it.
        sorted_list = converted_to_order[:]
        sorted_list.sort()
        l = []
        while len(sorted_list) > 1:
            out = sorted_list.pop()
            # since they are sorted and the same, means anagram exist.
            if out == sorted_list[-1]:
                # if there are more than one, get all indices of the matches
                # and get the actual value.
                indices = [i for i, x in enumerate(
                    converted_to_order) if x == out]
                for index in indices:
                    l.append(item[index])
                    # clear the item to prevent duplicates
                    converted_to_order[index] = ' '
            elif l:
                # no more anagrams, append results to anagrams list
                # clear the list to start again.
                anagrams.append(l)
                l = []

    """this will return the anagrams that has the highest combinations.
        required by tutor.
    """
    max_length = len(max(anagrams, key=len))
    return [a for a in anagrams if len(a) == max_length]

test = open("week6/replace.txt", 'r')
# test = open("week6/noob_replace.txt", 'r')

# model answer
def split_sentences(f):
    text = f.read()
    sentences = []
    currentsentence = []
    skip_space = False
    for i, c in enumerate(text):
        currentsentence.append(c)
        if periodcheck(i, c, text):
            # Also .strip() to remove extra whitespace
            sen = "".join(currentsentence).strip()
            sentences.append(sen)
            currentsentence = []
    return sentences


def periodcheck(loc, c, text):
    if loc == len(text) - 1:              # end of sentence.
        return True
    if c in ("?", "!"):                   # ? and ! are always boundaries
        return True
    if c != ".":                         # Not a . is not a boundary
        return False                     # From here on, c only "."
    prev = text[:loc]                    # Partition the text
    after = text[loc + 1:]
    after_strip_space = after.lstrip()   # Remove any whitespace after the .

    # a) followed by whitespace followed by a lower case letter
    if after_strip_space[0].islower():
        return False

    # b) followed by a digit with no intervening whitespace
    if after[0].isdigit():
        return False

    # c) followed by whitespace and then an upper case letter, but preceded by
    # titles. (with more titles!)
    titles = ("Mr", "Ms", "Mrs", "Dr", "Jr", "Mdm", "Phd")
    if after_strip_space[0].isupper() and prev.endswith(titles):
        return False

    # d) Periods internal to a sequence of letters with no adjacent whitespace
    if (not prev[-1].isspace()) and (not after[0].isspace()):
        return False

    # e) Periods followed by certain kinds of punctuation (notably comma and
    # more periods)
    if after[0] in (",", ".", "!"):
        return False

    return True

for sentence in split_sentences(test):
    print sentence + "\n"
