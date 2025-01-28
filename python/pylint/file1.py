"""
pylint :: to check quality of python code
to execute :: pylint file_name.py

"""
def starting(list1):
    for i in list1:
        for j in list1:
            if j > i:
                break
        else:
            return i
    return None

l = [10,20,30]
print(starting(l))
