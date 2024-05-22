class Bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

b_code, l_color, b_sec = tuple(input().split())

b = Bomb(b_code, l_color, int(b_sec))

print(f"code : {b.code}")
print(f"color : {b.color}")
print(f"second : {b.sec}")