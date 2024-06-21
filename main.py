def character_counter(inputs):
    dic= {}
    for i in inputs:
        if i.isalpha():
            if i not in dic:
                dic[i] = 0
            else:
                dic[i] += 1
    return dic
    
def to_lower_case(input):
    lowercase = input.lower()
    return lowercase
def count_words(input):    
    return len(input.split())

def main():
    with open("books/frankenstein.txt") as book:
        f = book.read()
        lowercases = to_lower_case(f)
        words = count_words(f)
        count = character_counter(lowercases)
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        for i in count:
            print(f"The '{i}' character was found {count[i]} times")
        print("--- End report ---")      


main()