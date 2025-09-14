class Solution:
    vovels = set('aeiou')

    def templating(self, word: str) -> str:
        return ''.join('*' if c.lower() in self.vovels else c.lower() for c in word)

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = set(wordlist)
        case_insensitive, vovel_errors = {}, {}
        for word in wordlist:
            if word.lower() not in case_insensitive:
                case_insensitive[word.lower()] = word
            if (template := self.templating(word)) not in vovel_errors:
                vovel_errors[template] = word
        result = []
        for query in queries:
            if query in words:
                result.append(query)
            elif query.lower() in case_insensitive:
                result.append(case_insensitive[query.lower()])
            elif (template := self.templating(query)) in vovel_errors:
                result.append(vovel_errors[template])
            else:
                result.append('')
        return result
