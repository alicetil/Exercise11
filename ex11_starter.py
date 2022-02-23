#!/usr/bin/python
# variables - best practice is lower case

belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print('-' * len(belgium))
# orrrrr could do:
# for character in belgium:
#     print("-", end="")
# print()


belgium = belgium.replace(',', ':')
print(belgium)

belgium = belgium.split(':')
# print(Belgium)
# population1 = Belgium[1]
# population2 = Belgium[3]
# print(int(population1)+int(population2))
print(int(belgium[1]) + int(belgium[3]))