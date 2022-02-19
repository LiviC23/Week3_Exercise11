#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
empty = ''

for x in Belgium :
    hyphen = '-'
    empty += hyphen
print(empty)
print(len(empty))
print(len(Belgium))

print(Belgium.replace(',',':'))

population_addition = Belgium.split(',')
belguim_pop= int(population_addition[1])
brussels_pop= int(population_addition[3])
print(belguim_pop + brussels_pop)



