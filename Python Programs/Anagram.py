word1 = input("Enter word 1: ").replace(" ", "").lower()
word2 = input("Enter word 2: ").replace(" ", "").lower()

if sorted(word1) == sorted(word2):
    print("Anagrams")
else:
    print("Not Anagrams")
