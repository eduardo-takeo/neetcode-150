def isAnagram( s: str, t: str) -> bool:
    for letter in s:
        if letter not in t:
            return False

    return True

print(isAnagram("racecar", "carrace"))
print(isAnagram("ham", "jar"))
print(isAnagram("rota", "taro"))
