#print("Angram code, YAY!")
print("Anagram!" if sorted(input("First word: \n").lower()) ==
      sorted(input("Second word: \n").lower()) else "Not a Anagram")
