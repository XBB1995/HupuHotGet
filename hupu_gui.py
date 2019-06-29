from tkinter import *
from tkinter import ttk
from git import GetI
import webbrowser
import tkinter.filedialog as dir


# 手机版网页转换成普通网页
def url_exchange(url):
    return 'https://bbs.hupu.com/' + url[-13:]


class Hupugui(object):
        
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = Tk()
        # 给主窗口设置标题内容
        self.root.title("虎扑NBA论坛精华 ver 0.1")
        # 禁止窗体大小变化
        self.root.resizable(False, False)
        self.path = "E:"
        # 创建一个输入框,并设置尺寸
        self.key_word = Label(self.root, width=20, text='虎扑热帖亮帖爬取')
        self.teamSelect = ''
        self.url_list = []
        self.s_url_list = []
        # self.ip_input = tkinter.Entry(self.root, width=30)

        self.fm1 = ttk.LabelFrame(self.root, text="热点")
        # 创建一个回显列表
        # self.swipe = Label(self.fm1, width=20, text='新闻')
        self.sb1 = ttk.Scrollbar(self.fm1)
        # self.sb2 = Scrollbar(self.root)
        self.display_info = Listbox(self.fm1, bg="silver", width=80, height=10,
                                    yscrollcommand=self.sb1.set)

        self.display_info.bind('<Double-Button-1>', self.v2url)

        self.fm2 = ttk.Frame(self.root)
        self.fm21 = ttk.LabelFrame(self.fm2, text="今日赛况")
        # self.news = Label(self.fm21, width=20, text='今日比分')
        self.display_info_1 = Listbox(self.fm21, width=35, height=5, bg="silver")

        self.fm22 = ttk.LabelFrame(self.fm2, text="分区")
        self.fm221 = ttk.Frame(self.fm22)
        self.game = Label(self.fm221, width=20, text='球队分区')
        self.fm222 = ttk.Frame(self.fm22)
        self.display_info_2 = Listbox(self.fm222, width=45, height=5, bg="silver")
        self.display_info_2.bind('<Double-Button-1>', self.v2url2)
        # self.team = Label(self.fm22, width=20, text="请选择球队分区:")

        # Adding a Combobox
        team = StringVar()
        self.teamChosen = ttk.Combobox(self.fm221, width=12, textvariable=team)
        self.teamChosen['values'] = ('火箭', '勇士', '湖人', '其他')
        # 设置初始显示值，值为元组['values']的下标
        # self.teamChosen.current(0)
        self.teamChosen.config(state='readonly')  # 设为只读模式

        self.teamChosen.bind('<<ComboboxSelected>>', self.goo)

        # 创建一个查询结果的按钮
        self.result_button = ttk.Button(self.root, command=self.get_inf, text="获取")

    # 获取ComboBox的选择结果
    def goo(self, args):
        self.teamSelect = self.teamChosen.get()
        self.get_inf()

    # 触发listBox的双击事件
    def v2url(self, event):
        v2url = self.url_list[self.display_info.curselection()[0]]
        webbrowser.open(url_exchange('https:' + v2url), new=0, autoraise=True)

    # 触发listBox的双击事件
    def v2url2(self, event):
        v2url2 = self.s_url_list[self.display_info_2.curselection()[0]]
        webbrowser.open(url_exchange('https:' + v2url2), new=0, autoraise=True)

    def open_dir(self):
        d = dir.Directory()
        self.path = d.show(initialdir=self.path)

    # 创建菜单
    def create_menu(self):
        menu = Menu(self.root)

        # 创建二级菜单
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="球队排名", command=self.open_dir)
        file_menu.add_separator()

        scan_menu = Menu(menu)
        file_menu.add_command(label="球员数据查询")

        about_menu = Menu(menu, tearoff=0)
        about_menu.add_command(label="Version:0.1 By XBB")

        # 在菜单栏中添加以下一级菜单
        menu.add_cascade(label="扩展功能", menu=file_menu)
        menu.add_cascade(label="关于", menu=about_menu)
        self.root['menu'] = menu

    # 完成布局
    def gui_arrang(self):
        self.key_word.pack()
        # self.ip_input.pack()

        # self.swipe.pack()
        self.sb1.pack(side=RIGHT, fill=Y)
        # self.sb2.pack(side=BOTTOM, fill=X)
        self.display_info.pack()
        self.sb1.config(command=self.display_info.yview)
        # self.sb2.config(command=self.display_info.xview)
        self.fm1.pack(side=TOP, fill=BOTH, expand=YES)

        # self.news.pack()
        self.display_info_1.pack()
        self.fm21.pack(side=LEFT, padx=10)

        self.game.pack(side=LEFT)
        self.teamChosen.pack(side=LEFT)
        self.fm221.pack()

        self.display_info_2.pack()
        self.fm222.pack()
        self.fm22.pack(side=LEFT)
        self.fm2.pack()

        self.result_button.pack()

    def get_inf(self):
        # 获取输入信息
        # self.key_word = self.ip_input.get()
        # target = self.search_by_name(self.key_word)
        # 为了避免非法值,导致程序崩溃,有兴趣可以用正则写一下具体的规则,我为了便于新手理解,减少代码量,就直接粗放的过滤了
        get_inf = GetI()
        g_r = get_inf.get_game_result()
        h_l, h_c, href = get_inf.get_hot_lines()
        self.url_list = href
        s_l, s_c, s_href = get_inf.get_selected_lines(self.teamSelect + '专区')
        self.s_url_list = s_href

        # 创建临时列表
        swipe_info = []
        news_info = []
        game_info = []

        for i in range(len(h_l)):
            # swipe_info.append('%s    %s    %s' % (h_l[len(h_l) - 1 - i],
            #                                       h_c[len(h_l) - 1 - i],
            #                                       'https:'+href[len(h_l) - 1 - i]))
            swipe_info.append('%s    %s' % (h_l[len(h_l) - 1 - i],
                                            h_c[len(h_l) - 1 - i]))
        for i in range(len(s_l)):
            # news_info.append('%s    %s    %s' % (s_l[len(s_l) - 1 - i],
            #                                      s_c[len(s_l) - 1 - i],
            #                                      'https:'+s_href[len(s_l) - 1 - i]))
            news_info.append('%s    %s' % (s_l[len(s_l) - 1 - i],
                                           s_c[len(s_l) - 1 - i]))
        for i in range(len(g_r)):
            key = list(g_r.keys())
            value = list(g_r.values())
            game_info.append('%s : %s' % (key[i], value[i]))

        # 清空Listbox中的内容
        self.display_info.delete(0, END)
        self.display_info_1.delete(0, END)
        self.display_info_2.delete(0, END)

        # 为回显列表赋值
        for item in swipe_info:
            self.display_info.insert(0, item)
        for item in news_info:
            self.display_info_2.insert(0, item)
        for item in game_info:
            self.display_info_1.insert(0, item)
        # 这里的返回值,没啥用,就是为了好看

        return swipe_info


def main():
    # 初始化对象
    HG = Hupugui()
    # 进行布局
    HG.create_menu()
    HG.gui_arrang()
    # HG.get_inf()
    # 主程序执行
    print("This is a new version control system.")
    mainloop()


if __name__ == "__main__":
    main()
