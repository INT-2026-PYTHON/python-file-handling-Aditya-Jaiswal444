"""
## 4. Find All Palindrome Words  *(Medium)*

=================================================
PALINDROME WORDS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every PALINDROME word (a word that reads the
same forwards and backwards).

Write a helper FUNCTION called `is_palindrome`
that takes a single word and returns True if
it is a palindrome, else False. Pass every
word in the file to this function ONE AT A
TIME.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
hello
noon
civic
python
deified
racecar
banana

Output Example:
level
radar
noon
civic
deified
racecar
Total palindromes: 6

-------------------------------------------------
Explanation:
- "level"    reversed -> "level"   -> palindrome
- "radar"    reversed -> "radar"   -> palindrome
- "hello"    reversed -> "olleh"   -> not
- "noon"     reversed -> "noon"    -> palindrome
- "civic"    reversed -> "civic"   -> palindrome
- "python"   reversed -> "nohtyp"  -> not
- "deified"  reversed -> "deified" -> palindrome
- "racecar"  reversed -> "racecar" -> palindrome
- "banana"   reversed -> "ananab"  -> not
=================================================

"""
def is_palindrome(word):
    return word == word[::-1]
def main():
    # Step 1: Get user input
    print("Enter words (one per line). Press Enter twice to finish:")
    words = []
    while True:
        word = input().strip()
        if word == "":
            break
        words.append(word)
    
    if not words:
        print("No words entered.")
        return
    
    # Step 2: Check for palindromes and print them
    palindrome_count = 0
    print("Palindrome words:")
    for word in words:
        if is_palindrome(word):
            print(word)
            palindrome_count += 1
    
    print(f"Total palindromes: {palindrome_count}")

if __name__ == "__main__":
    main()

