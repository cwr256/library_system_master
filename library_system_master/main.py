import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import datetime
from pypinyin import lazy_pinyin, Style
main_window = tk.Tk()

dlkey = 0

def addchange():
    if dlkey==1:
        addbook = tk.Toplevel(main_window)
        add_page(addbook)


def schchange():
    if dlkey == 1:
        schbook = tk.Toplevel(main_window)
        sch_page(schbook)


def mdfchange():
    if dlkey == 1:
        mdfbook = tk.Toplevel(main_window)
        mdf_page(mdfbook)


def delchange():
    if dlkey == 1:
        delbook = tk.Toplevel(main_window)
        del_page(delbook)


def showchange():
    if dlkey == 1:
        showbook = tk.Toplevel(main_window)
        show_page(showbook)


def exit():
    main_window.destroy()

def dlpage():
    dlbook = tk.Toplevel(main_window)
    dl_page(dlbook)
    dlbook.transient(main_window)
    dlbook.grab_set()
    main_window.wait_window(dlbook)


# 主界面
class main_page():

    # 主界面
    def __init__(self, window):
        self.window = window
        self.window.title("图书管理系统")
        self.window.geometry('750x660')
        self.hello_label = tk.Label(self.window, text='简易的图书管理系统', width=20, height=2, font=("隶书", 30))
        self.hello_label.pack(pady=10)
        # 按钮
        self.addbt = tk.Button(self.window, text='增加图书信息', command=addchange, width=15, height=1, font=('黑体', 20),relief='raised',bd=5)
        self.addbt.pack(pady=10)
        self.schbt = tk.Button(self.window, text='查找图书信息', command=schchange, width=15, height=1, font=('黑体', 20),relief='raised',bd=5)
        self.schbt.pack(pady=10)
        self.mdbt = tk.Button(self.window, text='修改图书信息', command=mdfchange, width=15, height=1, font=('黑体', 20),relief='raised',bd=5)
        self.mdbt.pack(pady=10)
        self.delbt = tk.Button(self.window, text='删除图书信息', command=delchange, width=15, height=1, font=('黑体', 20),relief='raised',bd=5)
        self.delbt.pack(pady=10)
        self.showbt = tk.Button(self.window, text='显示图书信息', command=showchange, width=15, height=1,
                                font=('黑体', 20),relief='raised',bd=5)
        self.showbt.pack(pady=10)

        self.frameend0 = tk.Frame(window)
        self.frameend0.pack(side='left')
        self.zzr = tk.Label(self.frameend0, text='小组成员：\n蒋经翼\n裘与创\n蔡王榕',font=('隶书', 25))
        self.zzr.pack(side='left',ipadx=30,pady=20)


        # 信息
        self.frameend=tk.Frame(window)
        self.frameend.pack(side='right',ipadx=600)
        self.exitbt = tk.Button(self.frameend, text='退出', command=exit, width=15, font=('黑体', 20),relief='raised',bd=5)
        self.exitbt.pack(anchor='se')
        self.image_file = tk.PhotoImage(file='2.gif')
        self.image = tk.Label(self.frameend, image=self.image_file, anchor="se")
        self.image.pack(side='right', ipadx=170, padx=10)


        if dlkey==0:
            dlpage()

#登录页面
class dl_page():

    def __init__(self,window):
        self.window=window
        self.window.title('登陆界面')
        self.window.geometry('369x200+500+500')
        # 用户登陆
        self.w1=tk.Label(window, text='用户登陆', font=('隶书', 15)).pack()
        # 登陆账号
        self.frame1 = tk.Frame(window)
        self.frame1.pack()
        self.l1=tk.Label(self.frame1, text='登陆账号:', font=('微软雅黑', 15)).pack(side='left')
        # 账号输入框
        self.account_entryw = tk.StringVar()
        self.account=tk.Entry(self.frame1, textvariable=self.account_entryw)
        self.account.pack(padx=5,side='right')
        # 登陆密码
        self.frame2 = tk.Frame(window)
        self.frame2.pack()
        self.l2=tk.Label(self.frame2, text='登陆密码:', font=('微软雅黑', 15)).pack(side='left')
        # 密码输入框
        self.passwordw = tk.StringVar()
        self.passwd=tk.Entry(self.frame2, textvariable=self.passwordw, show='*')
        self.passwd.pack(padx=5,side='right')

        # 登陆按钮
        tk.Button(window, text='登陆', font='微软雅黑', bg='red', fg='white', width=10, command=self.land).pack()
        tk.Label(window, text='公共用户名:admin 登陆密码:123456', fg='gray').pack()
    def land(self):
        global dlkey
        account=self.account.get()
        passwd=self.passwd.get()
        if account == 'admin' and passwd== '123456':
            tkinter.messagebox.showinfo(title='温馨提示', message='登录成功')
            self.window.destroy()
            dlkey=1
            main_page(main_window)
        else:
            tkinter.messagebox.showerror(title='警告', message='账号或密码错误')

        if self.window.destroy():
            main_window.destroy()

# 子页面
class add_page():
    def __init__(self, window):
        self.window = window
        self.window.title("增加图书信息")
        self.window.geometry("550x500")
        # 书名
        self.frame1 = tk.Frame(window, height=10)
        self.frame1.pack()
        self.label1 = tk.Label(self.frame1, text='书名: \t')
        self.label1.pack(pady=10, side='left')
        self.bookname = tk.StringVar()
        self.entry1 = tk.Entry(self.frame1, textvariable=self.bookname)
        self.entry1.pack(side='right')
        # 作者
        self.frame2 = tk.Frame(window, height=10)
        self.frame2.pack()
        self.label2 = tk.Label(self.frame2, text='作者: \t')
        self.label2.pack(pady=10, side='left')
        self.author = tk.StringVar()
        self.entry2 = tk.Entry(self.frame2, textvariable=self.author)
        self.entry2.pack(side='right')
        # 出版社
        self.frame3 = tk.Frame(window, height=10)
        self.frame3.pack()
        self.label3 = tk.Label(self.frame3, text='出版社: \t')
        self.label3.pack(pady=10, side='left')
        self.press = tk.StringVar()
        self.entry3 = tk.Entry(self.frame3, textvariable=self.press)
        self.entry3.pack(side='right')
        # 出版时间
        self.frame4 = tk.Frame(window, height=10)
        self.frame4.pack()
        self.label4 = tk.Label(self.frame4, text='出版时间: \n(年.月)')
        self.label4.pack(pady=10, side='left')
        self.date = tk.StringVar()
        self.entry4 = tk.Entry(self.frame4, textvariable=self.date)
        self.entry4.pack(side='right')
        # ISBN号
        self.frame5 = tk.Frame(window, height=10)
        self.frame5.pack()
        self.label5 = tk.Label(self.frame5, text='ISBN号: \t')
        self.label5.pack(pady=10, side='left')
        self.isbn = tk.StringVar()
        self.entry5 = tk.Entry(self.frame5, textvariable=self.isbn)
        self.entry5.pack(side='right')
        # 价格
        self.frame6 = tk.Frame(window, height=10)
        self.frame6.pack()
        self.label6 = tk.Label(self.frame6, text='价格： \t')
        self.label6.pack(pady=10, side='left')
        self.price = tk.StringVar()
        self.entry6 = tk.Entry(self.frame6, textvariable=self.price)
        self.entry6.pack(side='right')
        # 内容简介
        self.frame7 = tk.Frame(window, height=10)
        self.frame7.pack()
        self.label7 = tk.Label(self.frame7, text='内容简介: \t')
        self.label7.pack(pady=10, side='left')
        self.book = tk.StringVar()
        self.entry7 = tk.Entry(self.frame7, textvariable=self.book)
        self.entry7.pack(side='right')
        # 增加按钮
        self.adbt = tk.Button(self.window, text="添加", command=self.add, font=('隶书', 20))
        self.adbt.pack()
        # 返回按钮
        self.backbt = tk.Button(self.window, text="返回", command=self.back, font=('隶书', 20))
        self.backbt.pack(anchor='ne', padx=50, pady=50)

    def read_books(self):
        self._return_info = []
        f = open(r'lib.txt', "r")  # r'lib.txt'中r的存在可以避免防止出现转义字符引起的问题
        _books_info = f.read()
        _books_info_str = _books_info.split("\n")[
                          :-1]  # 采用split函数读取出text文件中的内容，但读出后的值为字符串类型通过\n进行分割，Split函数可以对字符串按照指定规则分割，并将分割后的字段作为list返回的函数，print函数可以通过\n区别两个字符串，[:-1]是把最后多出来的一个\n给刨去，只取前面几个用的值

        for _book in _books_info_str:
            self._return_info.append(eval(_book))  # eval将字符串类型转化为列表类型
        f.close()
        self.n = len(self._return_info)

    # 检验ISBN号合法性
    def ISBN_assist(self, number_str):
        number_list = []
        for i in range(0, len(number_str) - 1):
            str2int = eval(number_str[i])
            number_list.append(str2int)
        return number_list

    def ISBN_legal_check(self, single_book):
        number_bar = single_book[4].split('-')
        numbers = ''.join(number_bar)
        final = ''
        number_int = self.ISBN_assist(numbers)
        if len(numbers) == 10:
            S = 0
            for i in range(0, 9):
                S = S + number_int[i] * (10 - i)
            last_number = 11 - (S % 11)
            if last_number == 10:
                final = 'X'
            elif last_number == 1:
                final = '0'
            else:
                final = str(last_number)
        elif len(numbers) == 13:
            S = 0
            for i in range(0, 6):
                S = S + number_int[2 * i] + 3 * number_int[2 * i + 1]
            last_number = 10 - (S % 10)
            if last_number == 10:
                final = '0'
            else:
                final = str(last_number)
        if final == numbers[-1]:
            check = 1
        else:
            check = 0
        return check

    # 检测ISBN号的唯一性
    def ISBN_repeat_check(self, single_book):
        self.read_books()
        book_list = self._return_info
        ISBN_list = []
        same_list = []
        for book in book_list:
            ISBN_list.append(book[4])
        ISBN_copy = ISBN_list.copy()
        if single_book is None:
            for single_ISBN in ISBN_copy:
                if ISBN_copy.count(single_ISBN) > 1:
                    while True:
                        if single_ISBN in ISBN_copy:
                            num = ISBN_copy.index(single_ISBN)
                            same_list.append(num)
                            ISBN_copy[num] = None
                        else:
                            break
                    break
            return same_list
        else:
            if single_book[4] in ISBN_list:
                return ISBN_list.index(single_book[4])
            else:
                return -1

    # 向文件中输入单个书本信息
    def add_book(self, _book_info, mode='a+'):
        f = open(r'lib.txt', mode)
        print(_book_info, file=f)
        f.close()

    def add(self):
        self.the_add_book = []  # 先设定一个空列表
        bookname = self.entry1.get()
        bookauthor = self.entry2.get()
        bookpress = self.entry3.get()
        date = self.entry4.get()
        isbn = self.entry5.get()
        price = self.entry6.get()
        book = self.entry7.get()
        listall = [bookname, bookauthor, bookpress, date, isbn, price, book]
        key = 1
        for i in listall:
            if i == '':
                tk.messagebox.showinfo(title='警告', message="请输入完整信息")
                key = 0
                break
        k = self.ISBN_repeat_check(listall)
        if self.ISBN_legal_check(listall) == 0 or k != -1:
            tk.messagebox.showinfo(title='警告', message='ISBN号错误，请查询正确后重新输入！')
        if key == 1 and self.ISBN_legal_check(listall) == 1 and k == -1:
            self.the_add_book.append(bookname)
            self.the_add_book.append(bookauthor)
            self.the_add_book.append(bookpress)
            self.the_add_book.append(date)
            self.the_add_book.append(isbn)
            self.the_add_book.append(price)
            self.the_add_book.append(book)
            self.add_book(str(self.the_add_book))
            tk.messagebox.showinfo(title='完成提示框', message='添加成功！')
            self.window.destroy()

    def back(self):
        self.window.destroy()
        main_page(main_window)


class sch_page:

    def __init__(self, window):
        # 窗口
        self.window = window
        self.window.title("搜索图书信息")
        self.window.geometry("1400x700")

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
        self.xswindow = ttk.Treeview(self.frame2,
                                     height=20,  # 表格显示的行数,height行
                                     columns=lists,  # 显示的列
                                     show='headings', )  # 隐藏首列
        self.xswindow["columns"] = lists
        self.xswindow.column("书名", width=150)  # #设置列
        self.xswindow.column("作者", width=150)
        self.xswindow.column("出版社", width=150)
        self.xswindow.column("出版时间（年、月）", width=150)
        self.xswindow.column("ISBN号", width=150)
        self.xswindow.column("价格", width=150)
        self.xswindow.column("简介", width=300)
        self.xswindow.heading("书名", text="书名")  # #设置显示的表头名
        self.xswindow.heading("作者", text="作者")
        self.xswindow.heading("出版社", text="出版社")
        self.xswindow.heading("出版时间（年、月）", text="出版时间（年、月）")
        self.xswindow.heading("ISBN号", text="ISBN号")
        self.xswindow.heading("价格", text="价格")
        self.xswindow.heading("简介", text="简介")
        self.xswindow.pack()
        # 返回按钮
        self.backbt = tk.Button(self.window, text="返回", command=self.back, font=('隶书', 20))
        self.backbt.pack(anchor='se', padx=50, pady=50, side="bottom")

    def read_books(self):
        self._return_info = []
        f = open(r'lib.txt', "r")  # r'lib.txt'中r的存在可以避免防止出现转义字符引起的问题
        _books_info = f.read()
        _books_info_str = _books_info.split("\n")[
                          :-1]  # 采用split函数读取出text文件中的内容，但读出后的值为字符串类型通过\n进行分割，Split函数可以对字符串按照指定规则分割，并将分割后的字段作为list返回的函数，print函数可以通过\n区别两个字符串，[:-1]是把最后多出来的一个\n给刨去，只取前面几个用的值

        for _book in _books_info_str:
            self._return_info.append(eval(_book))  # eval将字符串类型转化为列表类型

        f.close()
        self.n = len(self._return_info)

    def find_book(self):  # 显示书籍信息

        self.read_books()
        choice = 0

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
        self.m = 0
        k=0
        for i in range(0, len(self._return_info)):
            if self.entry1.get() == self._return_info[i][choice]:
                # print(i)
                self.xswindow.insert("", index=self.m, values=self._return_info[i])
                self.m = self.m + 1
                k=1
        if k==0:
            tk.messagebox.showinfo(title='完成提示框', message='查无此书')


    def back(self):
        self.window.destroy()
        main_page(main_window)


class mdf_page:
    def __init__(self, window):
        self.window = window
        self.window.title("修改图书信息")
        self.window.geometry("1400x700")
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
        self.xswindow = ttk.Treeview(self.frame2,
                                     height=15,  # 表格显示的行数,height行
                                     columns=lists,  # 显示的列
                                     show='headings',) # 隐藏首列

        self.xswindow["columns"] = lists

        self.xswindow.column("书名", width=150)  # #设置列
        self.xswindow.column("作者", width=150)
        self.xswindow.column("出版社", width=150)
        self.xswindow.column("出版时间（年、月）", width=150)
        self.xswindow.column("ISBN号", width=150)
        self.xswindow.column("价格", width=150)
        self.xswindow.column("简介", width=300)
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
        self.changebt = tk.Button(self.frame3, text='修改', command=self.amend_book, font=('隶书', 20))
        self.changebt.pack(side='right', padx=100)
        # 返回按钮
        self.backbt = tk.Button(self.window, text="返回", command=self.back, font=('隶书', 20))
        self.backbt.pack(anchor='se', padx=50, pady=50, side="bottom")


    def read_books(self):
        self._return_info = []
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

    list3 = []

    def find_book(self):  # 显示书籍信息
        self.read_books()

        choice = 0

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
        self.m = 0
        k=0
        for i in range(0, self.n):
            if self.entry1.get() == self._return_info[i][choice]:
                self.xswindow.insert("", index=self.m, values=self._return_info[i])
                self.list3.append(i)
                self.m = self.m + 1
                k=1
        if k==0:
            tk.messagebox.showinfo(title='完成提示框', message='查无此书')

    def add_book(self, _book_info, mode='w+'):
        f = open(r'lib.txt', mode)
        print(_book_info, file=f)
        f.close()

    def writeFile(self, list1):
        objFile = open(r'lib.txt', "w")
        for item in list1:
            value = str(item) + "\n"
            objFile.write(value)
        objFile.close()

    def amend_book(self):
        self.read_books()
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
        q=0
        for i in list0:
            self.xswindow.delete(i)
            str_list = list(i)  # str_list是接收将光标信号i001转化为列表['0''0''1']已将i删去的列表
            del str_list[0]
            for p in range(0, len(str_list)):
                if str_list[0] == '0':
                    del str_list[0]
                else:
                    break
            for k in str_list:
                if str_list[0] >= 'A':
                    list2.append(int(ord(k) - 55))
                elif str_list[0] <= '9':
                    list2.append(int(k))
            m = len(list2)
            if m == 1:
                x = list2[0] - 1
                self._return_info[self.list3[x]][choice] = self.entry2.get()
                q=x
            elif m == 2:
                x = list2[0] * 10 + list2[1] - 1
                self._return_info[self.list3[x]][choice] = self.entry2.get()
                q=x
        tk.messagebox.showinfo(title='完成提示框', message='修改成功！')
        self.writeFile(self._return_info)
        self.xswindow.insert("", index=q, values=self._return_info[self.list3[q]])

    def back(self):
        self.window.destroy()
        main_page(main_window)


class del_page:

    def __init__(self, window):
        self.window = window
        self.window.title("删除图书信息")
        self.window.geometry("1400x700")

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
        self.schbt = tk.Button(self.frame1, text='搜索', command=self.del_book, font=('隶书', 20))
        self.schbt.pack(side='right', padx=100)

        self.frame2 = tk.Frame(window, height=10)
        self.frame2.pack()
        lists = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN号', '价格', "简介")

        self.xswindow = ttk.Treeview(self.frame2,
                                     height=15,  # 表格显示的行数,height行
                                     columns=lists,  # 显示的列
                                     show='headings')  # 隐藏首列

        self.xswindow["columns"] = lists

        self.xswindow.column("书名", width=150)  # #设置列
        self.xswindow.column("作者", width=150)
        self.xswindow.column("出版社", width=150)
        self.xswindow.column("出版时间（年、月）", width=150)
        self.xswindow.column("ISBN号", width=150)
        self.xswindow.column("价格", width=150)
        self.xswindow.column("简介", width=300)
        self.xswindow.heading("书名", text="书名")  # #设置显示的表头名
        self.xswindow.heading("作者", text="作者")
        self.xswindow.heading("出版社", text="出版社")
        self.xswindow.heading("出版时间（年、月）", text="出版时间（年、月）")
        self.xswindow.heading("ISBN号", text="ISBN号")
        self.xswindow.heading("价格", text="价格")
        self.xswindow.heading("简介", text="简介")
        self.xswindow.pack()
        # 删除
        self.changebt = tk.Button(window, text='删除图书', command=self.delect, font=('隶书', 20))
        self.changebt.pack(anchor='center', pady=75)

        # 返回按钮
        self.frameend = tk.Frame(window, height=50, )
        self.frameend.pack(padx=10, pady=10, side="bottom", )
        self.backbt = tk.Button(self.frameend, text="返回", command=self.back, font=('隶书', 20))
        self.backbt.pack(anchor='se')

    def read_books(self):
        f = open(r'lib.txt', "r+")
        lists = f.readlines()
        list1 = []
        for item in lists:
            if item != "\n":
                list1.append(eval(item))
        f.close()
        return list1

    def writeFile(self, list1):
        objFile = open(r'lib.txt', "w")
        for item in list1:
            value = str(item) + "\n"
            objFile.write(value)
        objFile.close()

    list3 = []

    def del_book(self):  # 显示书籍信息

        list1 = self.read_books()

        choice = 0

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
        self.m = 0
        k=0
        for i in range(0, len(list1)):
            if self.entry1.get() == list1[i][choice]:
                print(i)
                self.xswindow.insert("", index=self.m, values=list1[i])
                self.list3.append(i)
                self.m = self.m + 1
                k=1
        if k==0:
            tk.messagebox.showinfo(title='完成提示框', message='查无此书')

    def add_book(self, _book_info, mode='w+'):
        f = open(r'lib.txt', mode)
        print(_book_info, file=f)
        f.close()

    def delect(self):
        list1 = self.read_books()
        list2 = []
        list0 = self.xswindow.selection()
        for i in list0:
            self.xswindow.delete(i)
            str_list = list(i)
            del str_list[0]
            for p in range(0, len(str_list) - 1):
                if str_list[0] == '0':
                    del str_list[0]
                else:
                    break
            for k in str_list:
                list2.append(int(k))

            x = list2[0] - 1
            del list1[self.list3[x]]
        self.writeFile(list1)
        tk.messagebox.showinfo(title='完成提示框', message='删除成功')
        self.window.destroy()

    def back(self):
        self.window.destroy()
        main_page(main_window)


class show_page:
    def chi2num1(self, chi_input):
        chi_list = ['书名', '作者', '出版社', '出版时间（年、月）', 'ISBN', '价格']
        num = chi_list.index(chi_input)
        return num

    def chi2num2(self, chi_input):
        chi_list = ['降序', '升序']
        num = chi_list.index(chi_input)
        return num

        # 数字转化函数：将含有日期和价格的字符串转化为日期形式和数形式，为汉字转化函数的辅助函数
        # 输入single_str为字符串，kind为排序类型，date_sep为待转化日期的分隔符，默认为逗号
        # 输出为名称对应的字符串、数字对应的数形、日期对应的日期形式，用于后续转化

    def judge_number(self, single_str, kind, date_sep='.'):
        if kind == 5:  # kind为5时表示价格
            single_str = eval(single_str)
            return single_str
        elif kind == 3:  # kind为3时表示日期
            year_month = single_str.split(date_sep)
            year_number = eval(year_month[0])
            if year_month[1][0] == '0':  # 排除月份的第一位数字为0的情况，防止eval()函数出错
                year_month[1] = year_month[1][-1]
            month_number = eval(year_month[1])
            day = datetime.date(year=year_number, month=month_number, day=1)
            return day
        else:  # kind为其他时都为名称，直接返回
            return single_str

        # 汉字转化函数：将汉字转化为拼音，为排序函数的辅助函数。
        # 输入的chinese为字符串，kind为排序类型，输出为中文拼音相连的字符串
        # 需要辅助函数judge_number()

    def Chinese_to_Pinyin(self, chinese, kind):
        chinese = self.judge_number(chinese, kind)  # 辅助函数judge_number()将含有数字的字符串转化为数型或日期形式
        if isinstance(chinese, str):  # 判断输入的是否为字符串类型
            pinyin = lazy_pinyin(chinese, style=Style.NORMAL)  # 将字符串内的中文转成含拼音的字符串组成的列表
            pinyins = ''.join(pinyin)  # 将列表内的字符串串联成一个字符串
            return pinyins.lower()  # 将大写的字母小写化，避免排序出错
        else:  # 输入的为其他类型时直接返回
            return chinese

    def paixu_movement(self, all_list):
        for i in self.xswindow.get_children():
            self.xswindow.delete(i)
        for i in range(self.n):
            self.xswindow.insert("", i, values=all_list[i])

    def sort(self, kind, up_or_down):
        name_list = []
        for book in self._return_info:
            information = self.Chinese_to_Pinyin(book[kind], kind)  # 辅助函数Chinese_to_Pinyin()将中文转化成拼音
            name_list.append(information)
        book_list = []
        if up_or_down == 1:  # 此选择结构确定顺序或倒序
            name_sort = sorted(name_list)
        else:
            name_sort = sorted(name_list, reverse=True)
        for name in name_sort:
            name_number = name_list.index(name)
            book_list.append(self._return_info[name_number])
            name_list[name_number] = None
        return book_list

    def read_books(self):
        self._return_info = []
        f = open(r'lib.txt', "r")  # r'lib.txt'中r的存在可以避免防止出现转义字符引起的问题
        _books_info = f.read()
        _books_info_str = _books_info.split("\n")[
                          :-1]  # 采用split函数读取出text文件中的内容，但读出后的值为字符串类型通过\n进行分割，Split函数可以对字符串按照指定规则分割，并将分割后的字段作为list返回的函数，print函数可以通过\n区别两个字符串，[:-1]是把最后多出来的一个\n给刨去，只取前面几个用的值

        for _book in _books_info_str:
            self._return_info.append(eval(_book))  # eval将字符串类型转化为列表类型
        f.close()
        self.n = len(self._return_info)

    def __init__(self, window):
        self.window = window
        self.window.title("显示图书信息")
        self.window.geometry("1400x700")

        self.frame1 = tk.Frame(window, height=10)
        self.frame1.pack(pady=50)
        lists = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN号', '价格', "简介")
        self.xswindow = ttk.Treeview(self.frame1,
                                     height=20,  # 表格显示的行数,height行
                                     columns=lists,  # 显示的列
                                     show='headings',)  # 隐藏首列


        self.xswindow.column("书名", width=150)  # #设置列
        self.xswindow.column("作者", width=150)
        self.xswindow.column("出版社", width=150)
        self.xswindow.column("出版时间（年、月）", width=150)
        self.xswindow.column("ISBN号", width=150)
        self.xswindow.column("价格", width=150)
        self.xswindow.column("简介", width=300)
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
        self.select1 = ttk.Combobox(self.frame1, width=12, textvariable=tkinter.StringVar(), state="readonly")
        self.select1.pack(side='left', padx=50)
        self.select1["values"] = ('书名', '作者', '出版社', '出版时间（年、月）', 'ISBN', '价格')
        self.pxw = tk.Label(self.frame1, text='升/降序:', font=('隶书', 15))
        self.pxw.pack(side='left')
        self.select2 = ttk.Combobox(self.frame1, width=12, textvariable=tkinter.StringVar(), state="readonly")
        self.select2.pack(side='left', padx=50)
        self.select2["values"] = ('升序', '降序')
        self.paixu = tk.Button(self.frame1, text='排序', font=('隶书', 20), command=lambda: self.paixu_movement(
            self.sort(self.chi2num1(self.select1.get()), self.chi2num2(self.select2.get()))))
        self.paixu.pack(side='right', padx=20)

        # 返回按钮
        self.backbt = tk.Button(self.window, text="返回", command=self.back, font=('隶书', 20))
        self.backbt.pack(anchor='se', padx=50, pady=50)

    def back(self):
        self.window.destroy()
        main_page(main_window)


mainpage = main_page(main_window)
main_window.mainloop()
