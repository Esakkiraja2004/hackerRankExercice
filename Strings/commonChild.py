def longest_common_subsequence(s1, s2):
    n = len(str1)
    m = len(str2)
    
    # Create a 2D DP array
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill the DP array
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The length of the LCS is in dp[n][m]
    return dp[n][m]

result = longest_common_subsequence(string1, string2)


# def lcs(str1, str2, i=0, j=0):
#     if i == len(str1) or j == len(str2): return 0
#     if str1[i] == str2[j]: return 1 + lcs(str1, str2, i + 1, j + 1)
#     return max(lcs(str1, str2, i + 1, j), lcs(str1, str2, i, j + 1))

# # Example usage
# print(lcs("ABCD", "ABDC"))
