from euler_22_words import words

def find_sum(words):
    total_sum = 0
    
    sorted_words = sorted(words)
    
    for i, word in enumerate(sorted_words):
        word_score = sum(ord(letter) - 64 for letter in word)
        total_sum += word_score * (i + 1)
    
    print(total_sum)

find_sum(words)
