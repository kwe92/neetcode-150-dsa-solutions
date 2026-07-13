def isAnagram(s: str, t: str) -> bool:
    countS = {}
    countT = {}

    if len(s) != len(t):
        return False
    
    for i in range(0, len(s)):
        if s[i] not in countS:
            countS[s[i]] = 1
        else:
            countS[s[i]] += 1

        if t[i] not in countT:
            countT[t[i]] = 1
        else:
            countT[t[i]] += 1
    
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True

if __name__ == '__main__':
    # s = "racecar"
    # t = "carrace"
    s="jar"
    t="jam"
    print(isAnagram(s,t))