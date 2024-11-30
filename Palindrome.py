def anagram(word, window_start, window_end):
    
    if(window_start == window_end):
        return True;
    if word[window_start] == word[window_end]:
        return anagram(word, window_start + 1, window_end - 1); 
    return False;

word = "amoreroma";
start = 0;
end = len(word) - 1;

print(anagram(word, start, end));