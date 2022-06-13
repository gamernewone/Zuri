# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):

  # [assignment] Add your code here

    if (sorted(word.lower().replace(" ", "")) != sorted(anagram.lower().replace(" ", ""))):
        return False
    else:
        return True