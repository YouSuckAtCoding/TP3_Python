def reverse(string, windows_start, windows_end):
    if(windows_start < windows_end):
        if(windows_end == len(string)):
         return;
        string[windows_start], string[windows_end] = string[windows_end], string[windows_start];
        reverse(string, windows_start + 1, windows_end - 1);
    return "".join(str(element) for element in string);

word = "racecar";
print(reverse(list(word), 0, len(word) - 1));

