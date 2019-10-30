n1 = int(input("Enter number of friends: "))
friends1 = list(map(str, input("\nEnter the friends through comma: ").strip().split(',')))[:n1]
n2 = int(input("Enter number of friends: "))
friends2 = list(map(str, input("\nEnter the friend through comma: ").strip().split(',')))[:n2]

mutial = []
others = []

for i in friends2:
    if i in friends1:
        mutial.append(i)
    else:
        others.append(i)

print("All friends:")
for x in range(len(friends1)):
    print(friends1[x])

print('-' * 20)
print("Mutual Friends:")
for y in range(len(mutial)):
    print(mutial[y])

print('-' * 20)
print("Also Friend of: ")
for z in range(len(others)):
    print(others[z])
print('-' * 20)