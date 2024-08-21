li = [1, 2, 3]


def modify(a, lst):  # list is passed as reference whereas variable is pass by value
    a = a * 2
    print(a)
    lst.append(100)


if __name__ == "__main__":
    b = 10
    modify(b, li)
    print(b)
    print(li)
