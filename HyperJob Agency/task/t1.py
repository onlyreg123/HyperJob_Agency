from collections import namedtuple
from datetime import time

# Instant = namedtuple("Instant", ['h', 'm', 's'])
#
# # t1 = Instant(int(input()), int(input()), int(input()))
# # t2 = Instant(int(input()), int(input()), int(input()))
# t1 = Instant(1, 2, 3)
# t2 = Instant(4, 5, 6)
#
#
#
# dt1 = time(hour=t1.h, minute=t1.m, second=t1.s)
# dt2 = time(hour=t2.h, minute=t2.m, second=t2.s)
# print(dt1, dt2)


h1, m1, s1, h2, m2, s2 = (int(input()) for _ in range(6))

print((h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1)
