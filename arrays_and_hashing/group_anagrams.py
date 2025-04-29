def groupAnagrams( strs: list[str]) ->list[list[str]]:
    hash_map = {} 

    for word in strs:
        if sorted(word) not in hash_map:
            hash_map[sorted(word)] = [word]
        else:
         hash_map[sorted(word)].append(word)

    final = []
    for key, value in hash_map:
        final.append(value)
    
    return final

print(groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))