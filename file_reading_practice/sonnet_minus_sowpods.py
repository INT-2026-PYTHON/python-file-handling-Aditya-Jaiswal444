"""
## 6. Words in sonnet_words.txt but NOT in sowpods.txt  *(Hard)*

=================================================
WORDS UNIQUE TO THE SONNET
=================================================

Problem Statement:
Read the text files `sowpods.txt` and
`sonnet_words.txt`. PRINT every word that
appears in `sonnet_words.txt` but does NOT
appear in `sowpods.txt`.

This problem is about CHOOSING THE RIGHT DATA
STRUCTURE. If you check each sonnet word
against the SOWPODS list with a nested loop,
the work is O(N*M). Using SETS turns the
membership check into O(1), giving you an
overall O(N + M) algorithm.

-------------------------------------------------
Input Example:
sowpods.txt sample:
   thee
   love
   summer
   day
   eyes
   shall
   more

sonnet_words.txt sample:
   shall
   i
   compare
   thee
   to
   a
   summer
   day

Output Example:
Words in sonnet but not in sowpods:
['a', 'compare', 'i', 'to']
Total: 4

-------------------------------------------------
Explanation:
sonnet words -> {'shall', 'i', 'compare',
                 'thee', 'to', 'a', 'summer',
                 'day'}
sowpods set   -> {'thee', 'love', 'summer',
                  'day', 'eyes', 'shall',
                  'more'}
Difference (sonnet - sowpods)
              -> {'i', 'compare', 'to', 'a'}
After sorting -> ['a', 'compare', 'i', 'to'].
=================================================

"""
def main():
      # Step 1: Get sowpods words from user
      print("Enter SOWPODS words (one per line). Press Enter twice to finish:")
      sowpods_words = set()
      while True:
            word = input().strip()
            if word == "":
                  break
            sowpods_words.add(word)
      
      # Step 2: Get sonnet words from user
      print("Enter SONNET words (one per line). Press Enter twice to finish:")
      sonnet_words = set()
      while True:
            word = input().strip()
            if word == "":
                  break
            sonnet_words.add(word)
      
      if not sonnet_words:
            print("No words entered.")
            return
      
      # Step 3: Find words that are in sonnet but not in sowpods
      unique_sonnet_words = sorted(sonnet_words - sowpods_words)
      
      # Step 4: Print the results
      print("Words in sonnet but not in sowpods:")
      print(unique_sonnet_words)
      print(f"Total: {len(unique_sonnet_words)}")
if __name__ == "__main__":
      main()


