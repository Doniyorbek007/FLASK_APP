my_list = [1,4,5,"Salom"]
your_list = [1,4,5,"Salom"]


result = my_list is your_list
print(result) # False


if my_list == your_list:
    print("Teng")
else:
    print("Teng emas")