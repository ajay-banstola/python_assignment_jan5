#using context manager
my_list=list(range(2,100))
new_list=[]
with open("prime.txt","w") as fp:
    for num in my_list:
        for i in range(2, num - 1):
            if (num % i == 0):
                break
        else:
            new_list.append(num)

    fp.write(str(new_list))


#reading the file
with open("prime.txt","r")as fp:
    print(fp.read())