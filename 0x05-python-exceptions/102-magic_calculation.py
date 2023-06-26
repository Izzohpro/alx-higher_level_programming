#!/usr/bin/python3


def magic_calculation(a, b):
    zino = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                zino += a ** b / i
        except Exception:
            zino = b + a
            break
    return (zino)

