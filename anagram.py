from collections import defaultdict

def group_anagrams(words):
    anagram_groups = defaultdict(set) 
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].add(word)
    return list(anagram_groups.values())

words = ["cat", "dog", "tac", "god", "act"]
result = group_anagrams(words)
print(result)  # [["cat", "tac", "act"], ["dog", "god"]]
