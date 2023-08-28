with open('books/frankenstein.txt') as f:
    file_contents = f.read()

def num_words(contents):
    words = contents.split()
    number = 0
    for word in words:
        number +=1
    return number
def num_letters(contents):
    all_freq = {}
    test_str = contents.lower()
    for i in test_str:
        if i.isalpha():
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
    return all_freq
print(f'--- Begin report of books/frankenstein.txt ---')
words = num_words(file_contents)
print(f'{words} words found in the document')
letter_dict = num_letters(file_contents)
letter_list = list(sorted(letter_dict.items()))
for letter in letter_list:
    print(f'The {letter[0]} character was found {letter[1]} times')

print(f'--- End report ---')

