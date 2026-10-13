def isAnagram( s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(0, len(s)):
            if s[i] not in countS:
                      countS[s[i]] = 1
            
            else:
                countS[s[i]] += 1
        
        for i in range(0, len(t)):
            if t[i] not in countT:
                      countT[t[i]] = 1
            else:
                countT[t[i]] += 1

        for cs in countS:
            if cs in countT and countS[cs] == countT[cs]:
                continue
            else:
                return False
        return True
        

                
        

if __name__ == '__main__':
        s="racecar"
        t="carrace"
        print(isAnagram(s, t))