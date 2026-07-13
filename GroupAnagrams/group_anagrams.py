
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # use Frequency Array Hashing
    result: dict[tuple, list] = {}
    for s in strs:
        freq_array = [0] * 26 # max unique elements of any string is 26
        for c in s:
            freq_array[ord(c) - ord("a")] += 1 # get unique digital identity value of a character and substracted from the smallest unique digital identity value
        serialized = tuple(freq_array)
        if serialized not in result:
            result[serialized] = [s]
        else:
            result[serialized].append(s)
    return list(result.values())
        


if __name__ == '__main__':
    strs = ["act","pots","tops","cat","stop","hat", ""]

    #  Output: [["hat"],["act", "cat"],["stop", "pots", "tops"], [""]]

    print(groupAnagrams(strs))
