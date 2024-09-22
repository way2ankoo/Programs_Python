def lcs_len(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0

    if s1[m - 1] == s2[n - 1]:
        return 1 + lcs(s1, s2, m - 1, n - 1)
    else:
        return max(lcs(s1, s2, m - 1, n), lcs(s1, s2, m, n - 1))


def lcs(s1, s2, m, n):
    if m == 0 or n == 0:
        return ""

    if s1[m - 1] == s2[n - 1]:
        # When characters match, add to result
        return lcs(s1, s2, m - 1, n - 1) + s1[m - 1]
    else:
        # If no match, take the longer subsequence
        lcs1 = lcs(s1, s2, m - 1, n)
        lcs2 = lcs(s1, s2, m, n - 1)
        return lcs1 if len(lcs1) > len(lcs2) else lcs2


if __name__ == "__main__":
    s1 = "AXYZ"
    s2 = "BAXZ"
    print(lcs(s1, s2, len(s1), len(s2)))
