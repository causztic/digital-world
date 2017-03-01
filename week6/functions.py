'''Week 6 functions!'''


def reverse(s):
    '''print stuff in reverse'''
    # return s[::-1]
    rev = ""
    for c in s:
        rev = c + rev
    return rev


def check_password(password):
    '''checks if password meets requirements'''
    if len(password) >= 8 and password.isalnum:
        count = 0
        for i in password:
            if i in [str(x) for x in range(0, 10)]:
                count += 1
        return count >= 2
    return False


def longest_common_prefix(s1, s2):
    '''takes two strings and returns the longest common prefix of the two strings.'''
    common = ""
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            break
        common += char1
    return common

f = open('week6/xy.dat', 'r')

class Coordinate(object):
    '''C O O R D I N A T I O N'''
    x = float(0)
    y = float(0)

    def __str__(self):
        return "x: %f, y: %f" % (self.x, self.y)

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.mag = self.get_magnitude()

    def get_magnitude(self):
        """returns the magnitude of the coordinates with respect to the origin at (0,0)"""
        return ((self.x)**2 + (self.y)**2) * 0.5


def get_maxmin_mag(file_object):
    '''
    Gets a file object and returns the Coordinate() with the highest and the lowest magnitude.
    Parameters:
        file_object - A file object
    '''
    pmax = Coordinate(0, 0)
    pmin = Coordinate(0, 0)

    for line in file_object:
        l = [float(item.strip()) for item in line.split(" " * 7)]
        c = Coordinate(l[0], l[1])
        mag = c.mag
        if mag > pmax.mag:
            pmax = c
        if mag < pmin.mag:
            pmin = c

    return pmax, pmin

ppmax, ppmin = get_maxmin_mag(f)
print 'max: (%f, %f)' % (ppmax.x, ppmax.y)
print 'min: (%f, %f)' % (ppmin.x, ppmin.y)
