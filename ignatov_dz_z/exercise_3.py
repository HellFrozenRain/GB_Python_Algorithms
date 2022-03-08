"""Design Add and Search Words Data Structure"""

"""Design a data structure that supports adding new words
and finding if a string matches any previously added string."""


class WordDictionary:

    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str) -> None:
        current = self.dictionary
        if not self.search(word):
            for i in range(len(word)):
                if word[i] not in current:
                    current[word[i]] = {}
                current = current[word[i]]
            current['#'] = {}

    def search(self, word: str) -> bool:
        current = self.dictionary

        def rec(start, current):
            if start >= len(word):
                if "#" in current:
                    return True
                else:
                    return False

            if word[start] == ".":
                for k, v in current.items():
                    if rec(start + 1, v):
                        return True
                return False
            elif word[start] in current:
                if rec(start + 1, current[word[start]]):
                    return True
            else:
                return False

        return rec(0, current)
