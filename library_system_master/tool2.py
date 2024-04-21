import tkinter as tk

def do_that_and_close(top):
    print('doing that')
    top.destroy()

def launch_top():
    top = tk.Toplevel(root)
    lbl = tk.Label(top, text='this is top')
    lbl.pack()
    btn = tk.Button(top, text='do this and quit', command=lambda: do_that_and_close(top))
    btn.pack()

root = tk.Tk()
lbl = tk.Label(root, text='this is root')
lbl.pack()
root_btn = tk.Button(root, text='launch top', command=launch_top)
root_btn.pack()
quit_btn = tk.Button(root, text='quit', command=root.destroy)
quit_btn.pack()

root.mainloop()