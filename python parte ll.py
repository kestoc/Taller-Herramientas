h = ["a", "a", "a", "a", "c", "a", "d", "d", "a", "a", "z", "z"]


def compr(l):
    """
    """

    lf = []
    c = 0
    num = 0
    a = ""
    while (c < len(l)):
        temp = []
        i = c + 1
        a = l[c]
        while (i < len(l)):
            if (l[c] == l[i]):
                num += 1

            else:
                break
            i += 1

        temp.append(a)
        temp.append(num)
        lf.append(temp)
        c = c + (num + 1)
        num = 0
    return lf


print(compr(h))