import time

password = input("Enter password: ")
start = time.time()
charset = "abcdefghijklmnopqrstuvwxyz1234567890"
guess = []
for val in range(5):
    a = [i for i in charset]
    for y in range(val):
        a = [x + i for i in charset for x in a]
    guess = guess + a
    if password in guess:
        break
end = time.time()
clock = str(end - start)

print("Your password: " + password)
print("Time taken: " +clock)