that = ("gafur", "kbtu", "kyzylorda")
print(len(that))

print(that[1])

print(that[0: 3])

that_2 = list(that)
that_2[1] = "the_best_university"
that = tuple(that_2)
print(that)

that_3 = list(that)
that_3.append("kbtu")
that = tuple(that_3)
print(that)

for i in range(len(that)) :
    print(that[i])


