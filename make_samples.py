import random
from german_tokenizer import GermanTokenizer


def main():
    fns = [
        p1,
        p2,
        p3,
        p4,
        p5,
        p6,
        p7,
        p8,
        p9,
        p10,
        p11,
        p12,
        p13
    ]
    with open('train.txt', 'w') as f:
        for _ in range(2):
            for fn in fns:
                lines = fn()
                print_data(f, lines)


def p1():
    # "Rg. 19049481 Kd.-Nr. 42674"
    d1 = rand(8)
    d2 = rand(5)
    str = "Rg. %d Kd.-Nr. %d" %(d1, d2)
    labels = [
        (4, 5, 'INV'),
        (14, 15, 'ADDR')
    ]
    lines = make_label(str, labels)
    return lines


def p2():
    # "KD 13433 19049243 Betrag 33,01"
    d1 = rand(8)
    d2 = rand(5)
    str = "KD %d %d Betrag 33,01" %(d2, d1)
    labels = [
        (3, 4, 'ADDR'),
        (5, 6, 'INV')
    ]
    lines = make_label(str, labels)
    return lines


def p3():
    # "Kd.Nr. 39484 / Fibu 70245 Rg.Nr. 19049614"
    d1 = rand(8)
    d2 = rand(5)
    d3 = rand(5)
    str = "Kd.Nr. %d / Fibu %d Rg.Nr. %d" %(d2, d3, d1)
    labels = [
        (7, 8, 'ADDR'),
        (25, 26, 'INV')
    ]
    lines = make_label(str, labels)
    return lines


def p4():
    # "35676 19049604"
    d1 = rand(8)
    d2 = rand(5)
    str = "%d %d" %(d2, d1)
    labels = [
        (0, 1, 'ADDR'),
        (2, 3, 'INV')
    ]
    lines = make_label(str, labels)
    return lines


def p5():
    # "19049102 31.01.2019"
    d1 = rand(8)
    d2 = rand(5)
    str = "%d 31.01.2019" %(d1)
    labels = [
        (0, 1, 'INV')
    ]
    lines = make_label(str, labels)
    return lines


def p6():
    # "RECH/GUT. VOM 28.02. NR. 19049578"
    d1 = rand(8)
    d2 = rand(5)
    str = "RECH/GUT. VOM 28.02. NR. %d" %(d1)
    labels = [
        (21, 22, 'INV')
    ]
    lines = make_label(str, labels)
    return lines


def p7():
    # "31414/INV/19048261 31.1.2019"
    d1 = rand(8)
    d2 = rand(5)
    str = "%d/INV/%d 31.1.2019" %(d2, d1)
    labels = [
        (0, 1, 'ADDR'),
        (6, 7, 'INV')
    ]
    lines = make_label(str, labels)
    return lines


def p8():
    # "16101/6-19049574"
    d1 = rand(8)
    d2 = rand(5)
    str = "%d/6-%d" %(d2, d1)
    labels = [
        (0, 1, 'ADDR'),
        (4, 5, 'INV')
    ]
    lines = make_label(str, labels)
    return lines


def p9():
    # "/INV/R-19048904 31.1.2019RE 19048904 v. 31.1.19"
    d1 = rand(8)
    d2 = rand(5)
    str = "/INV/R-%d 31.1.2019RE %d v. 31.1.19" %(d1, d1)
    labels = [
        (7, 8, 'INV'),
        (15, 16, 'INV')
    ]
    lines = make_label(str, labels)
    return lines


def p10():
    # "/19049225 28.2.2019/"
    d1 = rand(8)
    d2 = rand(5)
    str = "/%d 28.2.2019/" %(d1)
    labels = [
        (1, 2, 'INV')
    ]
    lines = make_label(str, labels)
    return lines


def p11():
    # "RE 19049673 KN 9282"
    d1 = rand(8)
    d2 = rand(4)
    str = "RE %d KN %d" %(d1, d2)
    labels = [
        (3, 4, 'INV'),
        (8, 9, 'ADDR')
    ]
    lines = make_label(str, labels)
    return lines


def p12():
    # "Rechnung 18043323 - Kunde 17495"
    d1 = rand(8)
    d2 = rand(5)
    str = "Rechnung %d - Kunde %d" %(d1, d2)
    labels = [
        (9, 10, 'INV'),
        (19, 20, 'ADDR')
    ]
    lines = make_label(str, labels)
    return lines


def p13():
    # "E.Kt: I.Kt:5018967 B.Nr:19048871 B.Dt:310119 R.Bt:1579.97 h S.Bt:0.00"
    d1 = rand(8)
    d2 = rand(5)
    str = "E.Kt: I.Kt:%d B.Nr:%d B.Dt:%d R.Bt:%d.%d h S.Bt:0.00" %(rand(7), d1, rand(6), rand(4), rand(2))
    labels = [
        (18, 19, 'INV')
    ]
    lines = make_label(str, labels)
    return lines


def print_data(f, lines):
    f.write('\n')
    f.write('-DOCSTART- -X- O\n')
    f.write('\n')
    for l in lines:
        if l[0] != ' ':
            f.write("%s %s\n" %(l[0], l[1]))


def make_label(string, config):
    chars = [c.lower() for c in GermanTokenizer.tokenize(string)]
    # print(chars)
    lines = []
    for index, c in enumerate(chars):
        found = False
        for l in config:
            if index == l[0]:
                lines.append((c, "B-" + l[-1]))
                found = True
                break
            elif l[0] < index < l[1]:
                lines.append((c, "I-" + l[-1]))
                found = True
                break

        if found is False:
            lines.append((c, "O"))

    return lines


def rand(size):
    left = pow(10, (size - 1))
    right = pow(10, size)
    return random.randint(left, right)


main()
