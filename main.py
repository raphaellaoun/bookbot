def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        words = file_contents.split()
        print(f"Total number of words: {len(words)}")
        count_char ={}
        for char in file_contents:
            if char in count_char:
                count_char[char] += 1
            else:
                count_char[char] = 1
        sorted_char_count = sorted(count_char.items(), key=lambda x: x[0])
        char_count_dict = dict(sorted_char_count)
        alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
        for i in sorted(alphabet):
            print(f"the '{i}' character was found {char_count_dict[i]} times")
main()