def good_string(size, chars):
    return "YES" if size > 1 and chars[0] != chars[-1] else "NO"

count = int(input())

for _ in range(count):
    size = int(input())
    chars = input().strip()
    print(good_string(size, chars))
