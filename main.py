def main():
    file = "books/frankenstein.txt"

    with open(file) as f:
        file_contents = f.read()

    word_count = get_words(file_contents)

    char_count_dict = get_char_count(file_contents)


    print(f'--- Begin report of {file} ---')
    print(f"{word_count} words found in the document")

    for key, value in char_count_dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def sort_key(dict):
    return dict["num"]

def get_words(string):
    return len(string.split())

def get_char_count(string):
    lower_string = string.lower()
    count_dict = {}

    for char in lower_string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    count_dict_sorted = {k: v for k, v in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)}

    return count_dict_sorted
    

main()