#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import math
import sys


if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input().split()))
    F = []
    R = []
    # Если список пуст, завершить программу.
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    for x in A:
        if 8 < x and x < 18:
            F.append(x)
        t=0
        m =10
    for i in F:
        if i % 10 == 0:
            t +=1
    R.append(i)
    from functools import reduce
    reduce(lambda x, y: x * y, R)
print(R)
print(t)
print(m)
