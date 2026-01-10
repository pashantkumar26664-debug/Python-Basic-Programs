# Example 1: Break statement - exits the loop

for i in range(10):
    if i == 5:
        break
    print(i)
print("\n")

# Example 2: Continue statement - skips to next iteration and pass is a placeholder

for i in range(10):
    pass # Placeholder for continue
    # if i == 5:
    #     continue
    # print(i)

# Example 3: Break in while loop

count = 0
while True:
    if count == 3:
        break
    print(count)
    count += 1

# Example 4: Continue in while loop

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)