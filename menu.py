from oled import disp

STATUS = {}

def set_status(k ,v):
    global STATUS
    STATUS[k] = v
    
def get_status():
    return STATUS.get("kde", "No kde") + " " + STATUS.get("wifi", "No wifi")

class Menu:
    def __init__(self, title, parent=None, on_enter=None):
        self.parent = parent
        self.title = title
        self.items = []
        self.on_enter = on_enter
        if parent is not None:
            parent.add(self)
    
    def add(self, item):
        self.items.append(item)
        
    def enter(self):
        print("Entering ", self.title)
        if self.on_enter is not None:
            self.on_enter()
            return False
        return True
        
    def show(self):
        disp.fill(0)
        disp.text(self.title.upper(), 0, 0, 1)
        for idx, item in enumerate(self.items):
            disp.text(str(idx+1) + " " + item.title, 0, 9*(idx+1)+3, 1)
        disp.text(get_status(), 0, 63-18, 1)
        if self.parent:
            disp.text("# Back: " + self.parent.title.upper(), 0, 63-8, 1)
        disp.show()
        
    def _handle(self, key):
        if key == "#" and self.parent is not None:
            self.parent.enter()
            return self.parent, None
        if not key:
            return self, None
        if key and key in "123456789":
            idx = int(key) - 1
            if idx < len(self.items):
                return None, idx
        return self, None
        
    def handle(self, key):
        item, idx = self._handle(key)
        if item:
            return item
        submenu = self.items[idx]
        if submenu.enter():
            return submenu
        return self

    def __str__(self):
        return "Menu '" + self.title + "'"