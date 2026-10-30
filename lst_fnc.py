num=[12,32,15,24,53,50]

print("ORIGINAL LIST: ",num)

print("LENGTH: ", len(num))

print("APPEND (100): ")
num.append(100)
print(num)

print("SORTED ASC: ")
num.sort()
print(num)

print("SORTED DESC: ")
num.sort(reverse=True)
print(num)

new=[11,22,33,44]
num.extend(new)
print("EXTENDED LIST: ",num)

print("INDEX[3]: ",num[3])

print("POSITION OF 100: ",num.index(100))

print("INSERT 99 at 2nd position: ")
num.insert(1,99)
print(num)

print("SLICING: ", num[2:6])

num.remove(100)
print("REMOVE 100:", num)
