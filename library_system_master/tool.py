# import tkinter as tk
#
# class Window(tk.Toplevel):
#     def __init__(self, root, label):
#         super().__init__(root)
#         self.root = root
#         label = tk.Label(self, text=label)
#         label.pack(padx=20, pady=20)
#
#         self.bind("<Destroy>", self.kill_root)
#
#     def kill_root(self, event):
#         if event.widget == self and self.root.winfo_exists():
#             self.root.destroy()
#
# root = tk.Tk()
# label = tk.Label(root, text="Root window")
# label.pack(padx=20, pady=20)
#
# w1 = Window(root, "This is a toplevel window")
#
# root.mainloop()
from tkinter import *
import tkinter.messagebox
root = Tk()
root.geometry("400x200")
root.title("父窗口")
root.withdraw() # 隐藏父窗口#给主界面添加一个标签内容
Label(root,text="欢迎进入主界面").pack()
top = Toplevel()
top.geometry("400x200")
top.title("登录注册")
# 登录
def login():
    top.destroy() # 登入成功后销毁 登录注册窗口
    root.deiconify() # 显示窗口
    tkinter.messagebox.showinfo("提示","登录成功")# 退出
def logout():
    answer = tkinter.messagebox.askyesno("提示","确定直接退出吗？")
    if answer: # 如果点击确定，会返回一个True的值，否则False
        root.destroy()# 销毁主窗口
# 如果直接点击右上角关闭按钮，会直接关闭，通过这个方法，可以直接绑定logout函数top.protocol("WM_DELETE_WINDOW", logout)
Button(top, text="登录", command=login).pack()
Button(top, text="退出", command=logout).pack()
mainloop()