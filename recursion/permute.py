# Given a set (or string) with n distinct characters, print all permutations (no repetitions allowed)
def phelper(slate, array):
    if len(array) == 0:
        print(slate)
    else:
        for i in range(len(array)):
            phelper(slate=slate + array[i], array=array[:i] + array[i+1:])


def printpermutations(s):
    phelper("", s)


printpermutations("abc")
