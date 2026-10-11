import sys
def main():
    s = input().strip()
    left = 0
    right = len(s) - 1
    is_palindrome = True
    while left < right:
        if s[left] != s[right]:
            is_palindrome = False
            break  
        left += 1   
        right -= 1 
    if is_palindrome:
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()      