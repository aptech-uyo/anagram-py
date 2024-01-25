# write the function is_anagram
def is_anagram(test, original):
    test = test.lower().strip()
    original = original.lower().strip()

    if sorted(test) == sorted(original):
        return True
    else:
        return False
