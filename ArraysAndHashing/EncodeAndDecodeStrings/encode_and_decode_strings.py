def encode(strs: list[str]) -> str:
    result = []
    for s in strs:
        result.append(str(len(s)))
        result.append('#')
        result.append(s)
    return "".join(result)


def decode(s: str) -> list[str]:
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        first_char = j + 1
        result.append(s[first_char:first_char + length])
        i = first_char + length
        j = i
    return result


if __name__ == '__main__':
    # strs = ["Hello", "World"]
    strs = [""]

    print(decode(encode(strs)))


#! Initial brute force: Passing
def encode_brute_force(strs: list[str]) -> str:
    sep = ","
    empty_sep = "*"
    word_sep = "**"

    encoded = ''
    for s in strs:
        if len(s) == 0:
            encoded = encoded + empty_sep + sep
        else:
            for c in s:
                encoded = encoded + str(ord(c)) + sep
        encoded = encoded + word_sep
    return encoded


def encode_brute_force_slight_refactor(strs: list[str]) -> str:
    sep = ","
    empty_sep = "*"
    word_sep = "**"

    encoded_list = []
    for s in strs:
        if len(s) == 0:
            encoded_list.append(empty_sep + sep)
        else:
            for c in s:
                encoded_list.append(str(ord(c)) + sep)
        encoded_list.append(word_sep)

    return "".join(encoded_list)  # "".join() is always strictly O(N)


def decode_brute_force(s: str) -> list[str]:
    encoded_strs = s.split('**')
    filtered_encoded_strs = [s for s in encoded_strs if len(s) > 0]
    result = []
    for s in filtered_encoded_strs:
        encoded_str = s[:-1]
        encoded_str_array = encoded_str.split(',')
        decoded_word = ''
        for c in encoded_str_array:
            if c == '*':
                result.append('')
            else:
                decoded_word = decoded_word + chr(int(c))
        if decoded_word:
            result.append(decoded_word)
    return result
