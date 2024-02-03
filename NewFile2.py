color_list = ['Black', 'White', 'Gold']
phone_list = ['iphone', 'samsung', 'blackberry']

a = [(i, j) for i in color_list for j in phone_list]
print(a)
for i in color_list:
    for j in phone_list:
        print(i, j)