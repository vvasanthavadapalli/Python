read = 4
write = 2
execute = 1
permissions = read | write
print("Permission value:", permissions)
if permissions & write:
    print("Write permission is set")
else:
    print("Write permission is not set")

'''output:
Permission value: 6
Write permission is set'''
