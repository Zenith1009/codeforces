def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(s.lower()) >= alphabet

n = int(input())
print("YES" if is_pangram(input().strip()) else "NO")
