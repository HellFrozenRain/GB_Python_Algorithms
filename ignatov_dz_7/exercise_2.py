"""
Replace Words

In English, we have a concept called root, which can be followed by
some other word to form another longer word - let's call this word successor.
For example, when the root "an" is followed by the successor word "other",
we can form a new word "another".

Given a dictionary consisting of many roots and a sentence
consisting of words separated by spaces, replace all
the successors in the sentence with the root forming it.
If a successor can be replaced by more than one root,
replace it with the root that has the shortest length.

Return the sentence after the replacement.
"""


class Solution:
    def find_root(self, word, dict_set):
        for head in range(1, len(word)):
            if word[:head] in dict_set:
                return word[:head]
        return word

    def replaceWords(self, dictionary, sentence) -> str:
        set_dict = set(dictionary)
        sentence_in_list = sentence.split(' ')
        result_list = [self.find_root(word, set_dict) for word in sentence_in_list]

        return " ".join(result_list)
