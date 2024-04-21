import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os
import datetime

book_info = ["名称", "作者", "出版社", "出版日期", "ISBN", "价格", "内容简介"]
book_info1 = ["百年孤独", "加西亚·马尔克斯", "南海出版公司", "1967.6", "9787544218566", "22",
              "是魔幻现实主义文学的代表作，描写了布恩迪亚家族七代人的传奇故事，以及加勒比海沿岸小镇马孔多的百年兴衰，反映了拉丁美洲一个世纪以来风云变幻的历史。"]
book_info2 = ["呐喊", "鲁迅", "浙江文艺出版社", "2010.3", "9787533929855", "12",
              "是中国现代小说的开端与成熟的标志，开创了现代现实主义文学的先河。作品通过写实主义、象征主义、浪漫主义等多种手法，以传神的笔触和“画眼睛”、“写灵魂”的艺术技巧"]
book_info3 = ["活着", "余华", "作家出版社", "2010.10", "9787506355957", "15",
              "地主少爷福贵嗜赌成性，终于赌光了家业，一贫如洗。穷困之中的福贵因为母亲生病前去求医，没想到半路上被国民党部队抓了壮丁，后被解放军所俘虏"]
all_book_info = [book_info1, book_info2, book_info3]

main_window = tk.Tk()
addbook = tk.Tk()
addbook.withdraw()
schbook = tk.Tk()
schbook.withdraw()
mdfbook = tk.Tk()
mdfbook.withdraw()
delbook = tk.Tk()
delbook.withdraw()
showbook = tk.Tk()
showbook.withdraw()


# 主界面
class main_page:
    def addchange(self):
        # self.hello_label.destroy()
        # self.addbt.destroy()
        # self.schbt.destroy()
        # self.mdbt.destroy()
        # self.delbt.destroy()
        # self.showbt.destroy()
        # self.zzr.destroy()
        add_page(addbook)
        addbook.wm_deiconify()
        # main_window.destroy()

    def schchange(self):
        sch_page(schbook)
        schbook.wm_deiconify()

    def mdfchange(self):
        mdf_page(mdfbook)
        mdfbook.wm_deiconify()

    def delchange(self):
        del_page(delbook)
        delbook.wm_deiconify()

    def showchange(self):
        show_page(showbook)
        showbook.wm_deiconify()

    def exit(self):
        main_window.destroy()
        addbook.destroy()
        schbook.destroy()
        mdfbook.destroy()
        delbook.destroy()
        showbook.destroy()

    # 主界面
    def __init__(self, window):
        self.window = window
        self.window.title("图书管理系统（超简陋版）")
        self.window.geometry('1100x700')
        self.hello_label = tk.Label(self.window, text='简陋的图书管理系统', width=20, height=3, font=("隶书", 30))
        self.hello_label.pack(pady=10)
        # 按钮
        self.addbt = tk.Button(self.window, text='增加图书信息', command=self.addchange, width=15, height=1, font=('黑体', 20))
        self.addbt.pack(pady=10)
        self.schbt = tk.Button(self.window, text='查找图书信息', command=self.schchange, width=15, height=1, font=('黑体', 20))
        self.schbt.pack(pady=10)
        self.mdbt = tk.Button(self.window, text='修改图书信息', command=self.mdfchange, width=15, height=1, font=('黑体', 20))
        self.mdbt.pack(pady=10)
        self.delbt = tk.Button(self.window, text='删除图书信息', command=self.delchange, width=15, height=1, font=('黑体', 20))
        self.delbt.pack(pady=10)
        self.showbt = tk.Button(self.window, text='显示图书信息', command=self.showchange, width=15, height=1,
                                font=('黑体', 20))
        self.showbt.pack(pady=10)
        self.exitbt = tk.Button(self.window, text='退出', command=self.exit, width=15, height=1, font=('黑体', 20))
        self.exitbt.pack(anchor='se')

        # 信息
        self.zzr = tk.Label(self.window, text='小组成员：\n蒋经翼\n裘与创\n蔡王榕', width=20, height=60, font=('隶书', 20))
        self.zzr.pack(anchor='sw')


# 页面
class add_page:

    def __init__(self, window):
        self.window = window
        self.window.title("增加图书信息")
        self.window.geometry("1100x700")
        self.blank0 = tk.Label(addbook, height=5)
        self.blank0.pack()
        # 书名
        self.frame1 = tk.Frame(window, height=10)
        self.frame1.pack()
        self.label1 = tk.Label(self.frame1, text='书名:\t')
        self.label1.pack(pady=10, side='left')
        self.bookname = tk.StringVar()
        self.entry1 = tk.Entry(self.frame1, textvariable=self.bookname)
        self.entry1.pack(side='left')
        # 作者
        self.frame2 = tk.Frame(window, height=10)
        self.frame2.pack()
        self.label2 = tk.Label(self.frame2, text='作者:\t')
        self.label2.pack(pady=10, side='left')
        self.author = tk.StringVar()
        self.entry2 = tk.Entry(self.frame2, textvariable=self.author)
        self.entry2.pack(side='left')
        # 出版社
        self.frame3 = tk.Frame(window, height=10)
        self.frame3.pack()
        self.label3 = tk.Label(self.frame3, text='出版社:\t')
        self.label3.pack(pady=10, side='left')
        self.press = tk.StringVar()
        self.entry3 = tk.Entry(self.frame3, textvariable=self.press)
        self.entry3.pack(side='left')
        # 出版时间
        self.frame4 = tk.Frame(window, height=10)
        self.frame4.pack()
        self.label4 = tk.Label(self.frame4, text='出版时间:\n(格式：年.月)')
        self.label4.pack(pady=10, side='left')
        self.date = tk.StringVar()
        self.entry4 = tk.Entry(self.frame4, textvariable=self.date)
        self.entry4.pack(side='left')
        # ISBN号
        self.frame5 = tk.Frame(window, height=10)
        self.frame5.pack()
        self.label5 = tk.Label(self.frame5, text='ISBN号:\t')
        self.label5.pack(pady=10, side='left')
        self.isbn = tk.StringVar()
        self.entry5 = tk.Entry(self.frame5, textvariable=self.isbn)
        self.entry5.pack(side='left')
        # 价格
        self.frame6 = tk.Frame(window, height=10)
        self.frame6.pack()
        self.label6 = tk.Label(self.frame6, text='价格：\t')
        self.label6.pack(pady=10, side='left')
        self.price = tk.StringVar()
        self.entry6 = tk.Entry(self.frame6, textvariable=self.price)
        self.entry6.pack(side='left')
        # 内容简介
        self.frame7 = tk.Frame(window, height=10)
        self.frame7.pack()
        self.label7 = tk.Label(self.frame7, text='内容简介:\t')
        self.label7.pack(pady=10, side='left')
        self.book = tk.StringVar()
        self.entry7 = tk.Entry(self.frame7, textvariable=self.book)
        self.entry7.pack(side='left')
        # 增加按钮
        self.adbt = tk.Button(self.window, text="添加", command=self.addbook, font=('隶书', 20))
        self.adbt.pack()
        # 返回按钮
        self.backbt = tk.Button(self.window, text="返回", command=self.back, font=('隶书', 20))
        self.backbt.pack(anchor='ne', padx=50, pady=50)

    the_add_book = []  # 先设定一个空列表

    # 如何向文件中输入单个书本信息
    def add_book(self, _book_info, mode='a+'):
        f = open(r'lib.txt', mode)
        print(_book_info, file=f)
        f.close()

    def renew_books(self):
        self.add_book(all_book_info)

    # # 将文件中的内容读取出来
    # def read_books(self):
    #     f = open(r'lib1.txt', "r")  # r'lib.txt'中r的存在可以避免防止出现转义字符引起的问题
    #     _books_info = f.read()
    #     _books_info_str = _books_info.split("\n")[:-1]  # 采用split函数读取出text文件中的内容，但读出后的值为字符串类型通过\n进行分割，Split函数可以对字符串按照指定规则分割，并将分割后的字段作为list返回的函数，print函数可以通过\n区别两个字符串，[:-1]是把最后多出来的一个\n给刨去，只取前面几个用的值
    #     _return_info = []
    #     for _book in _books_info_str:
    #         _return_info.append(eval(_book))  # eval将字符串类型转化为列表类型
    #     # print(_books_info_str)
    #     # print(len(_books_info_str))
    #     f.close()
    #     return _return_info
    def addbook(self):
        bookname = self.entry1.get()
        self.the_add_book.append(bookname)
        bookauthor = self.entry2.get()
        self.the_add_book.append(bookauthor)
        bookpress = self.entry3.get()
        self.the_add_book.append(bookpress)
        date = self.entry4.get()
        self.the_add_book.append(date)
        isbn = self.entry5.get()
        self.the_add_book.append(isbn)
        price = self.entry6.get()
        self.the_add_book.append(price)
        book = self.entry7.get()
        self.the_add_book.append(book)
        self.add_book(str(self.the_add_book))
        tk.messagebox.showinfo(title='完成提示框', message='添加成功！')

    def back(self):
        # self.backbt.destroy()
        # self.blank0.destroy()
        # self.frame1.destroy()
        # self.frame2.destroy()
        # self.frame3.destroy()
        # self.frame4.destroy()
        # self.frame5.destroy()
        # self.frame6.destroy()
        # self.frame7.destroy()
        # self.adbt.destroy()
        addbook.withdraw()
        main_page(main_window)


# main_window.title("图书管理系统（超简陋版）")
# main_window.geometry('1100x700')
# hello_label = tk.Label(main_window, text='简陋的图书管理系统', width=20, height=3,font=("隶书",30))
# hello_label.pack(side=tk.TOP)

class sch_page:

    def __init__(self, window):
        # 窗口
        self.window = window
        self.window.title("搜索图书信息")
        self.window.geometry("1100x700")

        self.blank0 = tk.Label(window, height=5)
        self.blank0.pack()

        self.frame1 = tk.Frame(window, height=10)
        self.frame1.pack()
        self.selectw = tk.Label(self.frame1, text='查找方式:', font=('隶书', 15))
        self.selectw.pack(side='left')
        self.select = ttk.Combobox(self.frame1, width=12, textvariable=tkinter.StringVar(), state="readonly")
        self.select.pack(side='left', padx=50)
        self.select["values"] = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN', '价格')
        self.gjc = tk.Label(self.frame1, text="关键词：", font=('隶书', 15))
        self.gjc.pack(side='left')
        self.sch = tk.StringVar()
        self.entry1 = tk.Entry(self.frame1, textvariable=self.sch, width=20)
        self.entry1.pack(side='left', padx=10)
        self.schbt = tk.Button(self.frame1, text='搜索', command=self.find_book, font=('隶书', 20))
        self.schbt.pack(side='right', padx=100)

        self.frame2 = tk.Frame(window, height=10)
        self.frame2.pack()
        lists = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN号', '价格', "简介")
        xscroll = tk.Scrollbar(self.frame2, orient=tk.HORIZONTAL)
        yscroll = tk.Scrollbar(self.frame2, orient=tk.VERTICAL)
        self.xswindow = ttk.Treeview(self.frame2,
                                     height=20,  # 表格显示的行数,height行
                                     columns=lists,  # 显示的列
                                     show='headings',  # 隐藏首列
                                     xscrollcommand=xscroll.set,  # x轴滚动条
                                     yscrollcommand=yscroll.set, )  # y轴滚动条)
        self.xswindow["columns"] = lists

        self.xswindow.column("书名", width=150)  # #设置列
        self.xswindow.column("作者", width=150)
        self.xswindow.column("出版社", width=150)
        self.xswindow.column("出版时间（年、月）", width=150)
        self.xswindow.column("ISBN号", width=150)
        self.xswindow.column("价格", width=150)
        self.xswindow.column("简介", width=150)
        self.xswindow.heading("书名", text="书名")  # #设置显示的表头名
        self.xswindow.heading("作者", text="作者")
        self.xswindow.heading("出版社", text="出版社")
        self.xswindow.heading("出版时间（年、月）", text="出版时间（年、月）")
        self.xswindow.heading("ISBN号", text="ISBN号")
        self.xswindow.heading("价格", text="价格")
        self.xswindow.heading("简介", text="简介")
        self.xswindow.pack()


    def read_books(self):
        f = open(r'lib.txt', "r")
        lists = f.readlines()
        list1 = []
        for item in lists:
            if item != "\n":
                list1.append(eval(item))
        f.close()
        return list1


    def find_book(self):  # 显示书籍信息

        list1 = self.read_books()
        print("你想通过什么方式查询书?\n0.名称\n1.作者\n2.出版社\n3. 出版日期, \n4.ISBN, \n5.价格")
        choice = 0
        # if choice == 0:
        #     print("请输入书本名称")
        # self.select["values"]=('书名','作者','出版社','出版时间（年、月）','ISBN','价格')
        print(self.select.get())
        if self.select.get() == '书名':
            choice = 0
        elif self.select.get() == '作者':
            choice = 1
        elif self.select.get() == '出版社':
            choice = 2
        elif self.select.get() == '出版时间（年、月）':
            choice = 3
        elif self.select.get() == 'ISBN':
            choice = 4
        elif self.select.get() == '价格':
            choice = 5
        print(choice)
        print(list1[2][1])
        self.n = 0
        x = 0
        for i in range(0,len(list1)-1):
            if self.entry1.get() ==list1[i][choice]:
               print(i)
               self.xswindow.insert("", index=self.n, values=list1[i])
               self.n = self.n + 1
            elif i==len(list1):
                 tk.messagebox.showinfo(title='完成提示框', message='查无此书')
                 break


        # 返回按钮
        self.backbt = tk.Button(self.window, text="返回", command=self.back, font=('隶书', 20))
        self.backbt.pack(anchor='se', padx=50, pady=50, side="bottom")

    def back(self):
        schbook.withdraw()
        main_page(main_window)


class mdf_page:
    def __init__(self, window):
        self.window = window
        self.window.title("修改图书信息")
        self.window.geometry("1100x700")
        self.blank0 = tk.Label(window, height=5)
        self.blank0.pack()

        self.frame1 = tk.Frame(window, height=10)
        self.frame1.pack()
        self.selectw = tk.Label(self.frame1, text='查找方式:', font=('隶书', 15))
        self.selectw.pack(side='left')
        self.select = ttk.Combobox(self.frame1, width=12, textvariable=tkinter.StringVar(), state="readonly")
        self.select.pack(side='left', padx=50)
        self.select["values"] = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN', '价格')
        self.gjc = tk.Label(self.frame1, text="关键词：", font=('隶书', 15))
        self.gjc.pack(side='left')
        self.sch = tk.StringVar()
        self.entry1 = tk.Entry(self.frame1, textvariable=self.sch, width=20)
        self.entry1.pack(side='left', padx=10)
        self.schbt = tk.Button(self.frame1, text='搜索', command=self.find_book, font=('隶书', 20))
        self.schbt.pack(side='right', padx=100)

        self.frame2 = tk.Frame(window, height=10)
        self.frame2.pack()
        lists = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN号', '价格', "简介")
        xscroll = tk.Scrollbar(self.frame2, orient=tk.HORIZONTAL)
        yscroll = tk.Scrollbar(self.frame2, orient=tk.VERTICAL)
        self.xswindow = ttk.Treeview(self.frame2,
                                     height=15,  # 表格显示的行数,height行
                                     columns=lists,  # 显示的列
                                     show='headings',  # 隐藏首列
                                     xscrollcommand=xscroll.set,  # x轴滚动条
                                     yscrollcommand=yscroll.set, )  # y轴滚动条)
        self.xswindow["columns"] = lists
        self.xswindow.column("书名", width=150)  # #设置列
        self.xswindow.column("作者", width=150)
        self.xswindow.column("出版社", width=150)
        self.xswindow.column("出版时间（年、月）", width=150)
        self.xswindow.column("ISBN号", width=150)
        self.xswindow.column("价格", width=150)
        self.xswindow.column("简介", width=150)
        self.xswindow.heading("书名", text="书名")  # #设置显示的表头名
        self.xswindow.heading("作者", text="作者")
        self.xswindow.heading("出版社", text="出版社")
        self.xswindow.heading("出版时间（年、月）", text="出版时间（年、月）")
        self.xswindow.heading("ISBN号", text="ISBN号")
        self.xswindow.heading("价格", text="价格")
        self.xswindow.heading("简介", text="简介")
        self.xswindow.pack()
        # 修改
        self.frame3 = tk.Frame(window, height=10)
        self.frame3.pack(pady=20)
        self.changeselectw = tk.Label(self.frame3, text='修改信息种类:', font=('隶书', 15))
        self.changeselectw.pack(side='left')
        self.changeselect = ttk.Combobox(self.frame3, width=12, textvariable=tkinter.StringVar(), state="readonly")
        self.changeselect.pack(side='left', padx=50)
        self.changeselect["values"] = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN', '价格')
        self.xgxx = tk.Label(self.frame3, text="修改信息：", font=('隶书', 15))
        self.xgxx.pack(side='left')
        self.changexx = tk.StringVar()
        self.entry2 = tk.Entry(self.frame3, textvariable=self.changexx, width=50)
        self.entry2.pack(side='left', padx=10)
        self.changebt = tk.Button(self.frame3, text='修改',command=self.amend_book, font=('隶书', 20))
        self.changebt.pack(side='right', padx=100)
        # 返回按钮
        self.backbt = tk.Button(self.window, text="返回", command=self.back, font=('隶书', 20))
        self.backbt.pack(anchor='se', padx=50, pady=50, side="bottom")


    def read_books(self):
        f = open(r'lib.txt', "r+")
        lists = f.readlines()
        list1 = []
        for item in lists:
            if item != "\n":
                list1.append(eval(item))
        f.close()
        return list1

    list3 = []
    def find_book(self):  # 显示书籍信息
        list1 = self.read_books()
        print("你想通过什么方式修改书?\n0.名称\n1.作者\n2.出版社\n3. 出版日期, \n4.ISBN, \n5.价格")
        choice = 0
        # if choice == 0:
        #     print("请输入书本名称")
        # self.select["values"]=('书名','作者','出版社','出版时间（年、月）','ISBN','价格')
        print(self.select.get())
        if self.select.get() == '书名':
            choice = 0
        elif self.select.get() == '作者':
            choice = 1
        elif self.select.get() == '出版社':
            choice = 2
        elif self.select.get() == '出版时间（年、月）':
            choice = 3
        elif self.select.get() == 'ISBN':
            choice = 4
        elif self.select.get() == '价格':
            choice = 5
        self.n = 0
        for i in range(0, len(list1) - 1):
            if self.entry1.get() == list1[i][choice]:
                print(i)
                self.xswindow.insert("", index=self.n, values=list1[i])
                self.list3.append(i)
                self.n = self.n + 1
            elif i == len(list1):
                tk.messagebox.showinfo(title='完成提示框', message='查无此书')
                break
    def add_book(self, _book_info, mode='w+'):
        f = open(r'lib.txt', mode)
        print(_book_info, file=f)
        f.close()

    def writeFile(self,list1):
        objFile = open(r'lib.txt', "w")
        for item in list1:
            value = str(item) + "\n"
            objFile.write(value)
        objFile.close()

    def amend_book(self):
        list1 = self.read_books()
        choice = 0
        if self.changeselect.get() == '书名':
            choice = 0
        elif self.changeselect.get() == '作者':
            choice = 1
        elif self.changeselect.get() == '出版社':
            choice = 2
        elif self.changeselect.get() == '出版时间（年、月）':
            choice = 3
        elif self.changeselect.get() == 'ISBN':
            choice = 4
        elif self.changeselect.get() == '价格':
            choice = 5
        list1 = self.read_books()  # list1是接收文件所传入的所有书本的信息
        list2 = []  # list2对应的是接收转化后所对应的上面的n的值
        list0 = self.xswindow.selection()  # list0接收的是鼠标多对应的光标值即为i001  i002...i00A
        for i in list0:
            self.xswindow.delete(i)
            str_list = list(i)  # str_list是接收将光标信号i001转化为列表['0''0''1']已将i删去的列表
            del str_list[0]
            print(str_list)
            for p in range(0, len(str_list) - 1):
                if str_list[0] == '0':
                    del str_list[0]
                    print(p)
                else:
                    break
            for k in str_list:
                list2.append(int(ord(k) - 55))
                m = len(list2)
                if m == 1:
                    x = list2[0] - 1
                    print(x)
                    list1[self.list3[x]][choice] = self.entry2.get()
                elif m == 2:
                    x = list2[0] * 10 + list2[1] - 1
                    list1[self.list3[x]][choice] = self.entry2.get()
        tk.messagebox.showinfo(title='完成提示框', message='修改成功！')
        self.writeFile(list1)

    def back(self):
        mdfbook.withdraw()
        main_page(main_window)


class del_page:
    i = 0
    def __init__(self, window):
        self.window = window
        self.window.title("删除图书信息")
        self.window.geometry("1100x700")
        self.frame1 = tk.Frame(window, height=10)
        self.frame1.pack()
        self.selectw = tk.Label(self.frame1, text='查找方式:', font=('隶书', 15))
        self.selectw.pack(side='left')
        self.select = ttk.Combobox(self.frame1, width=12, textvariable=tkinter.StringVar(), state="readonly")
        self.select.pack(side='left', padx=50)
        self.select["values"] = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN', '价格')
        self.gjc = tk.Label(self.frame1, text="关键词：", font=('隶书', 15))
        self.gjc.pack(side='left')
        self.sch = tk.StringVar()
        self.entry1 = tk.Entry(self.frame1, textvariable=self.sch, width=20)
        self.entry1.pack(side='left', padx=10)
        self.schbt = tk.Button(self.frame1, text='搜索', command=self.del_book,font=('隶书', 20))
        self.schbt.pack(side='right', padx=100)

        self.frame2 = tk.Frame(window, height=10)
        self.frame2.pack()
        lists = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN号', '价格', "简介")
        xscroll = tk.Scrollbar(self.frame2, orient=tk.HORIZONTAL)
        yscroll = tk.Scrollbar(self.frame2, orient=tk.VERTICAL)
        self.xswindow = ttk.Treeview(self.frame2,
                                     height=15,  # 表格显示的行数,height行
                                     columns=lists,  # 显示的列
                                     show='headings',  # 隐藏首列
                                     xscrollcommand=xscroll.set,  # x轴滚动条
                                     yscrollcommand=yscroll.set, )  # y轴滚动条)
        self.xswindow["columns"] = lists

        self.xswindow.column("书名", width=150)  # #设置列
        self.xswindow.column("作者", width=150)
        self.xswindow.column("出版社", width=150)
        self.xswindow.column("出版时间（年、月）", width=150)
        self.xswindow.column("ISBN号", width=150)
        self.xswindow.column("价格", width=150)
        self.xswindow.column("简介", width=150)
        self.xswindow.heading("书名", text="书名")  # #设置显示的表头名
        self.xswindow.heading("作者", text="作者")
        self.xswindow.heading("出版社", text="出版社")
        self.xswindow.heading("出版时间（年、月）", text="出版时间（年、月）")
        self.xswindow.heading("ISBN号", text="ISBN号")
        self.xswindow.heading("价格", text="价格")
        self.xswindow.heading("简介", text="简介")
        self.xswindow.pack()
        # 删除
        self.changebt = tk.Button(window, text='删除图书', command=self.delect,font=('隶书', 20))
        self.changebt.pack(anchor='center', pady=75)
        self.backbt = tk.Button(self.window, text="返回", command=self.back, font=('隶书', 20))
        self.backbt.pack(anchor='se', padx=50, pady=50, side="bottom")

    def read_books(self):
        f = open(r'lib.txt', "r+")
        lists = f.readlines()
        list1 = []
        for item in lists:
            if item != "\n":
                list1.append(eval(item))
        f.close()
        return list1

    list3 = []
    def del_book(self):  # 显示书籍信息

        list1 = self.read_books()
        print("你想通过什么方式删除书?\n0.名称\n1.作者\n2.出版社\n3. 出版日期, \n4.ISBN, \n5.价格")
        choice = 0
        # if choice == 0:
        #     print("请输入书本名称")
        # self.select["values"]=('书名','作者','出版社','出版时间（年、月）','ISBN','价格')
        print(self.select.get())
        if self.select.get() == '书名':
            choice = 0
        elif self.select.get() == '作者':
            choice = 1
        elif self.select.get() == '出版社':
            choice = 2
        elif self.select.get() == '出版时间（年、月）':
            choice = 3
        elif self.select.get() == 'ISBN':
            choice = 4
        elif self.select.get() == '价格':
            choice = 5
        print(choice)
        print(list1[2][1])
        self.n = 0
        for i in range(0, len(list1) - 1):
            if self.entry1.get() == list1[i][choice]:
                print(i)
                self.xswindow.insert("", index=self.n, values=list1[i])
                self.list3.append(i)
                self.n = self.n + 1
            elif i == len(list1):
                tk.messagebox.showinfo(title='完成提示框', message='查无此书')
                break
    def add_book(self, _book_info, mode='w+'):
        f = open(r'lib.txt', mode)
        print(_book_info, file=f)
        f.close()

    def writeFile(self,list1):
        objFile = open(r'lib.txt', "w")
        for item in list1:
            value = str(item) + "\n"
            objFile.write(value)
        objFile.close()

    def delect(self):
        list1=self.read_books()#list1是接收文件所传入的所有书本的信息
        list2=[]#list2对应的是接收转化后所对应的上面的n的值
        list0=self.xswindow.selection()#list0接收的是鼠标多对应的光标值即为i001  i002...i00A
        for i in list0:
            self.xswindow.delete(i)
            str_list=list(i)#str_list是接收将光标信号i001转化为列表['0''0''1']已将i删去的列表
            del str_list[0]
            print(str_list)
            for p in range(0,len(str_list)-1):
                if str_list[0]=='0':
                    del str_list[0]
                    print(p)
                else:break
            for k in str_list:
                list2.append(int(ord(k)-55))
                print(list2)

            print(str_list)
            m =len(list2)
            if m==1:
               x = list2[0] - 1
               print(x)
               del list1[self.list3[x]]
            elif m==2:
                x= list2[0]*10+list2[1]-1
                del list1[self.list3[x]]
            elif m==3:
                x=list2[0]*100+list2[1]*10+list2[2]-1
                del list1[self.list3[x]]
        self.writeFile(list1)

    def back(self):
        delbook.withdraw()
        main_page(main_window)
#显示所有书籍

class show_page:
    _return_info = []

    def read_books(self):
        f = open(r'lib.txt', "r")  # r'lib.txt'中r的存在可以避免防止出现转义字符引起的问题
        _books_info = f.read()
        _books_info_str = _books_info.split("\n")[
                          :-1]  # 采用split函数读取出text文件中的内容，但读出后的值为字符串类型通过\n进行分割，Split函数可以对字符串按照指定规则分割，并将分割后的字段作为list返回的函数，print函数可以通过\n区别两个字符串，[:-1]是把最后多出来的一个\n给刨去，只取前面几个用的值

        for _book in _books_info_str:
            self._return_info.append(eval(_book))  # eval将字符串类型转化为列表类型
        # print(_books_info_str)
        # print(len(_books_info_str))
        f.close()
        self.n = len(self._return_info)
        print(self.n)

    def __init__(self, window):
        self.window = window
        self.window.title("显示图书信息")
        self.window.geometry("1100x700")

        self.frame1 = tk.Frame(window, height=10)
        self.frame1.pack(pady=50)
        lists = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN号', '价格', "简介")
        self.xswindow = ttk.Treeview(self.frame1,
                                     height=20,  # 表格显示的行数,height行
                                     columns=lists,  # 显示的列
                                     show='headings',  # 隐藏首列
                                     )

        self.xswindow.column("书名", width=150)  # #设置列
        self.xswindow.column("作者", width=150)
        self.xswindow.column("出版社", width=150)
        self.xswindow.column("出版时间（年、月）", width=150)
        self.xswindow.column("ISBN号", width=150)
        self.xswindow.column("价格", width=150)
        self.xswindow.column("简介", width=150)
        self.xswindow.heading("书名", text="书名")  # #设置显示的表头名
        self.xswindow.heading("作者", text="作者")
        self.xswindow.heading("出版社", text="出版社")
        self.xswindow.heading("出版时间（年、月）", text="出版时间（年、月）")
        self.xswindow.heading("ISBN号", text="ISBN号")
        self.xswindow.heading("价格", text="价格")
        self.xswindow.heading("简介", text="简介")
        self.xswindow.pack()
        self.read_books()

        for i in range(self.n):
            self.xswindow.insert("", i, values=self._return_info[i])

        self.selectw = tk.Label(self.frame1, text='排序方式:', font=('隶书', 15))
        self.selectw.pack(side='left')
        self.select = ttk.Combobox(self.frame1, width=12, textvariable=tkinter.StringVar(), state="readonly")
        self.select.pack(side='left', padx=50)
        self.select["values"] = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN', '价格')
        self.pxw = tk.Label(self.frame1, text='升/倒序:', font=('隶书', 15))
        self.pxw.pack(side='left')
        self.select = ttk.Combobox(self.frame1, width=12, textvariable=tkinter.StringVar(), state="readonly")
        self.select.pack(side='left', padx=50)
        self.select["values"] = ('升序', '倒序')
        self.paixu = tk.Button(self.frame1, text='排序', font=('隶书', 20))
        self.paixu.pack(side='right', padx=20)

        # 返回按钮
        self.backbt = tk.Button(self.window, text="返回", command=self.back, font=('隶书', 20))
        self.backbt.pack(anchor='se', padx=50, pady=50)

    def back(self):
        if 1:
            self.window.destroy()
        main_page(main_window)

mainpage = main_page(main_window)
main_window.mainloop()
addbook.mainloop()
schbook.mainloop()
mdfbook.mainloop()
delbook.mainloop()
showbook.mainloop()
