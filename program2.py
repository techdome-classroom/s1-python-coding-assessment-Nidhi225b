def is_match(message: str, decoder_key: str) -> bool:
    m, n = len(message), len(decoder_key)
    
    # dp[i][j] will be True if the first i characters in message match the first j characters in decoder_key
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty pattern matches empty message
    dp[0][0] = True
    
    # Handle patterns with '*' at the beginning (they can match an empty message)
    for j in range(1, n + 1):
        if decoder_key[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if decoder_key[j - 1] == '?' or decoder_key[j - 1] == message[i - 1]:
                # '?' matches any single character, or exact match
                dp[i][j] = dp[i - 1][j - 1]
            elif decoder_key[j - 1] == '*':
                # '*' can either match no character (dp[i][j-1]) or match one character (dp[i-1][j])
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
    
    return dp[m][n]

# Input from the user
message = input("Enter the secret message: ")
decoder_key = input("Enter the decoder key: ")

# Check if the decoder key matches the message
if is_match(message, decoder_key):
    print("Match: True")
else:
    print("Match: False")
