# write the function is_anagram
def is_anagram(test, original):
    test = test.lower().strip()
    original = original.lower().strip()

    if sorted(test) == sorted(original):
        print("Words are anagrams")
    else:
        print("Words are not anagram")



test = "orange"
original = "granoe"

is_anagram(test, original)
