def listsum(list, n):
   
    if(len(list) == n):
        return 0;
    return list[n] + listsum(list, n + 1);

list = [1,2,3,4,5];
print(listsum(list,  0))


