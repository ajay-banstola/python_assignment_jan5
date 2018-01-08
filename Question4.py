my_list = list(range(0,100))
fp = open("prime","w")

for num in my_list:
    for i in range(2,num-1):
        if (num%i == 0):
            break
    else:
        fp.write("{}".format(str(num)))
fp.close()