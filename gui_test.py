# import matplotlib
# matplotlib.use('Agg')

# import tkinter as tk
# root = tk.Tk()
# root.title('hello world')
# root.geometry('200x150')

# root.mainloop()

import tkinter as tk
from tkinter import font

class CustomGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom GUI")

    def set_window_size(self, width, height):
        self.root.geometry(f"{width}x{height}")

    def set_font_size(self, font_size):
        custom_font = font.Font(size=font_size)
        self.root.option_add("*Font", custom_font)

    def set_font_style(self, font_style):
        custom_font = font.nametofont("TkDefaultFont")
        custom_font.configure(family=font_style)
        self.root.option_add("*Font", custom_font)

    def set_background_color(self, color):
        self.root.configure(bg=color)

    def add_scrollbar(self, orientation):
        scrollbar = tk.Scrollbar(self.root, orient=orientation)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text = tk.Text(self.root, yscrollcommand=scrollbar.set)
        text.pack(expand=tk.YES, fill=tk.BOTH)

        scrollbar.config(command=text.yview)
        
        

# 建立主視窗
root = tk.Tk()

# 建立 CustomGUI 實例
custom_gui = CustomGUI(root)

# 調整視窗大小
custom_gui.set_window_size(500, 300)

# 調整字體大小
custom_gui.set_font_size(16)

# 調整字體風格
custom_gui.set_font_style("Arial")

# 設定背景顏色
custom_gui.set_background_color("lightblue")

# 增加垂直滑動拉桿
custom_gui.add_scrollbar(tk.VERTICAL)

# 啟動主迴圈
root.mainloop()