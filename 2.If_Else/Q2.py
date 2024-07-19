# 2) Write a Program to Check Whether a Character is Vowel or Consonant.

vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
chr = input("Enter a character: ")
print(chr, " is Vowel.") if chr in vowels else print(chr, " is Consonant.")