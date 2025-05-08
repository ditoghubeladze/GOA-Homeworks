def vowels(word):
    
    vowels = 'aeiou'
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count


