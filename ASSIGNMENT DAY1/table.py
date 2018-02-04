def tab1(num):
    outer_list = []
    for i in range(num):
        inner_list = []
        i += 1
        for x in range(i):
            x+=1
            inner_list.append(i*x)
        outer_list.append(inner_list)
    return outer_list
        
# x = tab1(3)
# print (x)

       
