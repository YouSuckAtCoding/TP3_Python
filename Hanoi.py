def towerOfHanoi(nDisks, a, b, c):
    if nDisks == 1:
        print("Move disk 1 from source", a, "to destination", c);
        return;
    towerOfHanoi(nDisks - 1, a, b, c);
    print ("Move disk",nDisks,"from source",a,"to destination",c)
    towerOfHanoi(nDisks - 1, a, c, b);


towerOfHanoi(4,"a", "b", "c")