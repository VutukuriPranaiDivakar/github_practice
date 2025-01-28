# read() − Reads the entire file.

# readline() − Reads one line at a time.

# readlines − Reads all lines into a list.

# f = open("general.txt", "r")
# # a = f.read()
# # print(a)
# # print("")
# b = f.readline()
# print(b)

# c = f.readlines()
# print(c)

# with open ::
# with open("general.txt", "r") as f:
#     a = f.read()
#     print(a)


# write ::
# w = open("create.txt", "w")
# z = w.write("jkrfkdsfsfsf")
# print(z)
# s = w.writelines("jksedafnsafnsjhfdanjkfsflfdkfadsd")
# print(s)

# with open("another.txt", "w") as z:
#     a = z.writelines("afavaacadadadadada")
#     print(a)


# append ::

a = open("general.txt", "a")
z = a.write("ajkdakdjkada")
print(z)