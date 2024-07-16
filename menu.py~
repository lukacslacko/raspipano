from oled import disp

STATUS = "Not connected"

def set_status(status):
    global STATUS
    STATUS = status

class Menu:
    def __init__(self, title, parent=None):
        self.parent = parent
        self.title = title
        self.items = []
        if parent is not None:
            parent.add(self)
    
    def add(self, item):
        self.items.append(item)
        
    def enter(self):
        print("Entering ", self.title)
        
    def show(self):
        disp.fill(0)
        disp.text(self.title.upper(), 0, 0, 1)
        for idx, item in enumerate(self.items):
            disp.text(str(idx+1) + " " + item.title, 0, 9*(idx+1)+3, 1)
        disp.text(STATUS, 0, 63-18, 1)
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
        submenu.enter()
        return submenu
