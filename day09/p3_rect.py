# p3_rect.py 第二个子类：Rect(w, h)，注意 3 * 4 出来的是 int 不是 float
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("子类必须实现 area()")

class Rect(Shape):
    def __init__(self, w, h):
        super().__init__("矩形")
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

r = Rect(3, 4)
print(r.name, r.area())
print(r.w, r.h)