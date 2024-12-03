"""
A string s is called a good string if and only if two consecutive letters are not the same. For example, abcab and  cda are 
good while abaa and accba are not.
You are given a string s. Among all the good substrings of s,print the size of the longest one.
"""


NO_OF_CHARS = 256


def longestUniqueSubsttr(string):
    n = len(string)
    cur_len = 1  # To store the lenght of current substring
    max_len = 1  # To store the result
    prev_index = 0  # To store the previous index
    i = 0

    visited = [-1] * NO_OF_CHARS

    visited[ord(string[0])] = 0

    for i in range(1, n):
        prev_index = visited[ord(string[i])]
        if prev_index == -1 or (i - cur_len > prev_index):
            cur_len += 1

        else:
            if cur_len > max_len:
                max_len = cur_len

            cur_len = i - prev_index

        # update the index of current character
        visited[ord(string[i])] = i

    # Compare the length of last NRCS with max_len and update
    # max_len if needed
    if cur_len > max_len:
        max_len = cur_len

    return max_len


if __name__ == "__main__":
    s = input()
    print(longestUniqueSubsttr(s))
