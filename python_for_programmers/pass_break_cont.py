names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

# pass is used mostly as a placeholder in a loop. Nothing gets executd when pass is placed under
# condition
for name in names:
    if 'j' in name.lower():
        pass
    else:
        print(name)

# break terminates a loop, typically found within conditional statements
for name in names:
    if 'h' in name.lower():
        break
    else:
        print(name)

# continue skips over an iteration if the conditoin is met and goes to next iteration
for name in names:
    if 'm' in name.lower():
        continue
    else:
        print(name)
