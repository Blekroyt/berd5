#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import math
import sys


if __name__ == '__main__':

    a = list(map(int, input().split()))
    C = int(input("Введите число"))
    t = 0
    for i in a:
        if i > C:
            t += 1
    answ = 1
    for i in a[a.index(max(a, key=abs)) + 1:]:
        answ *= i
    print(t)
    print(answ)
    a.sort(key=lambda x: x >= 0)
    print(a)
