# # # even numbers and odo numbers
# # def count(list2):
# #     even = 0
# #     odd = 0

# #     for i in list2:
# #         if i % 2 == 0:
# #             even += 1
# #         else:
# #             odd += 1
# #     return even, odd

# # list2 = [10,20,30,40,506,342,23243,3112,1,1,21,11,21,32,23,34]
# # e,o = count(list2)
# # print(f"even :{e}, odd : {o}")

# # list1 = []

# # user1 = input("Enter the name: ")
# # user2 = input("Enter the name: ")
# # user3 = input("Enter the name: ")
# # user4 = input("Enter the name: ")
# # user5 = input("Enter the name: ")
# # user6 = input("Enter the name: ")
# # user7 = input("Enter the name: ")
# # user8 = input("Enter the name: ")

# # list1.extend([user1, user2, user3, user4, user5, user6, user7, user8])

# # for i in list1:
# #     if len(i) > 5:
# #         print(f"{i} has more than 5 letters")
# #     else:
# #         print(f"{i} has less than 5 letters.")


# # fibonacci series

# # def fib(n):
# #     a= 0
# #     b = 1

# #     print(a)
# #     print(b)
# #     for i in range(2, n):
# #         c = a + b
# #         a = b
# #         b = c
# #         print(c)

# # fib(15)


# def fib(n):
#     a = 0
#     b = 1

#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             print(c)


# fib(20)

# factioral number ::

# def fact(n):
#     f = 1

#     for i in range(1, n + 1):
#         f = f * i
#     return f

# r = fact(20)
# print(r)

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

p = fact(5)
print(p)