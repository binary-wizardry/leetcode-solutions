class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        translate = defaultdict(lambda: '?', {k: v for k, v in knowledge})
        return s.replace('(', '{').replace(')', '}').format_map(translate)
