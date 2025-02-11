class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vovels = set('aeiou')
        count, mapping = 0, [0]
        for word in words:
            count += word[0] in vovels and word[-1] in vovels
            mapping.append(count)
        return [mapping[right + 1] - mapping[left] for left, right in queries]

# use a prefix sum to count words starts and ends with vowels
