from oled import disp

class Menu:
    def __init__(self, title, parent=None):
        self.parent = parent
        self.title = title
        self.items = []
        if parent is not None:
            parent.add(self)
    
    def add(self, item):
        self.items.append(item)
        
    def show(self):
        disp.fill(0)
        disp.text(self.title.upper(), 0, 0, 1)
        for idx, item in enumerate(self.items):
            disp.text(str(idx+1) + " " + item.title, 0, 9*(idx+1)+3, 1)
        if self.parent:
            disp.text("# Back: " + self.parent.title.upper(), 0, 63-8, 1)
        disp.show()
    
    def handle(self, key):
        if key and key in "123456789":
            idx = int(key) - 1
            if idx < len(self.items):
                return self.items[idx]
        if key == "#" and self.parent is not None:
            return self.parent
        return self
