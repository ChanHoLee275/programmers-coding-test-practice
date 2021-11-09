def solution(n, words):
    beforeWord = words[0]
    checker = set()
    checker.add(beforeWord)
    for i in range(1, len(words)):
        if words[i][0] != beforeWord[-1]:
            return [i%n + 1, i//n + 1]
        else:
            beforeLength = len(list(checker))
            checker.add(words[i])
            if beforeLength == len(list(checker)):
                return [i%n + 1, i//n + 1]
            beforeWord = words[i]
    return [0,0]