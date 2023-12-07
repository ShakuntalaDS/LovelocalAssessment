# shortest palindrome
def shortest_palindrome(s):
    def is_palindrome(string):
        return string == string[::-1]

    if not s:
        return ""

    for i in range(len(s), -1, -1):
        if is_palindrome(s[:i]):
            return s[i:][::-1] + s

    return s  # If the input string is already a palindrome

# Test cases
input_1 = "aacecaaa"
input_2 = "abcd"

output_1 = shortest_palindrome(input_1)
output_2 = shortest_palindrome(input_2)

print(f"Input: {input_1}\nOutput: {output_1}")
print(f"Input: {input_2}\nOutput: {output_2}")
