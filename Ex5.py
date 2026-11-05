t = (12, 32, 15, 24, 53, 50)

print("ORIGINAL TUPLE: ", t)

print("LENGTH: ", len(t))

print("INDEX[2]: ", t[2])

print("SLICING: ", t[1:4])

print("COUNT OF 32: ", t.count(32))

print("POSITION OF 53: ", t.index(53))

print("MAXIMUM: ", max(t))

print("MINIMUM: ", min(t))

print("SUM: ", sum(t))

print("SORTED TUPLE: ", tuple(sorted(t)))

print("CONCATENATION: ", t + (60, 70))

print("REPETITION: ", t * 2)
