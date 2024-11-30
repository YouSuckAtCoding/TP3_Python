def countStringChars(string, selected, n):
    if(n == len(string)):
        return 0;
    if(string[n] == selected):
        return 1 + countStringChars(string, selected, n + 1);
    else:
        return 0 + countStringChars(string, selected, n + 1);
    

print(countStringChars("banana", "o", 0));