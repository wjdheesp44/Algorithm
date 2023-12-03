def lps(pattern):
    lps = [0] * len(pattern)
    length = 0

    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return max(lps)

kmp_input = input()
answer = 0
for i in range(len(kmp_input)):
    answer = max(answer, lps(kmp_input[i:len(kmp_input)]))

print(answer)