def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # how to solve: Frequency Array Hashing
    # Why: The total universe of lowercase characters is small 26, so there is no need to sort to match

    result: dict[tuple,list[str]] = {}
    for s in strs:
        frequency_array = [0] * 26 # fixed array the length of lowercase character universe
        for c in s:
            index_state = (ord(c) - ord('a')) # current_unique_id - smallest_unique_id i.e. unique ids increment by one starting at 'a'
            frequency_array[index_state] += 1
        serialized_frequency = tuple(frequency_array) # mutable object -> immutable object
        if serialized_frequency not in result:
            result[serialized_frequency] = [s]
        else:
            result[serialized_frequency].append(s)
    return list(result.values()) # problem statement required a list to be returned


            
if __name__ == '__main__':
    strs = ["act","pots","tops","cat","stop","hat"]

    # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

    print('result:', groupAnagrams(strs))