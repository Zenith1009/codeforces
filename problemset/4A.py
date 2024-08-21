def can_div_melon(w):
    return (w % 2 == 0 and w > 2)

w = int(input())
print("YES" if can_div_melon(w) else "NO")
