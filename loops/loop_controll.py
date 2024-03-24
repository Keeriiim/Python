

# break - terminates the loop statement and transfers the execution to the statement immediately following the loop
# continue - causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating
# pass - does nothing, it is used when a statement is required syntactically but you do not want any command or code to execute


# Example 1: break statement
print("loop 1: ")
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))


# Example 2: continue statement
print("loop 2: ")
for a in range (1, 10):
    if a % 2 == 0:
        continue
    print(a)

# Example 3: pass statement , if the statement is in reverse, it will print the nunmber 5
print("loop 3: ")
for a in range (1, 10):
    if a != 5:
        print(a)
    pass