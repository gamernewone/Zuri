# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    handle = open(filename)

    return handle


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    counts = dict()
    for line in text:
        words = line.split()

        for word in words:
            counts[word] = counts.get(word, 0) + 1

    return counts


answer = count_words()
print(answer)
