import tkinter as tk


class TablesGeneratorAndTestFrame(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__()
        self.controller = controller
        self.parent = parent
        self.frame_container = tk.Frame(self.parent)
