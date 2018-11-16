from tkinter import *
from tkinter import ttk
from git import GetI
import webbrowser


class Hupugui(object):
        
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = Tk()
        # 给主窗口设置标题内容
        self.root.title("虎扑NBA论坛精华 ver 0.1")
        # 创建一个输入框,并设置尺寸
        self.key_word = Label(self.root, width=20, text='虎扑热帖亮帖爬取')
        self.teamSelect = ''
        self.url_list = []
        # self.ip_input = tkinter.Entry(self.root, width=30)

        # 创建一个回显列表
        self.swipe = Label(self.root, width=20, text='新闻')
        self.sb1 = Scrollbar(self.root)
        # self.sb2 = Scrollbar(self.root)
        self.display_info = Listbox(self.root, width=80, height=10,
                                    yscrollcommand=self.sb1.set)

        self.display_info.bind('<Double-Button-1>', self.v2url)

        self.news = Label(self.root, width=20, text='比分')
        self.display_info_1 = Listbox(self.root, width=80, height=5)

        self.game = Label(self.root, width=20, text='球队分区')
        self.display_info_2 = Listbox(self.root, width=80, height=5)
        self.team = Label(self.root, width=20, text="请选择球队分区:")

        # Adding a Combobox
        team = StringVar()
        self.teamChosen = ttk.Combobox(self.root, width=12, textvariable=team)
        self.teamChosen['values'] = ('火箭', '勇士', '湖人', '其他')
        # 设置初始显示值，值为元组['values']的下标
        self.teamChosen.current(0)
        self.teamChosen.config(state='readonly')  # 设为只读模式

        self.teamChosen.bind('<<ComboboxSelected>>', self.goo)

        # 创建一个查询结果的按钮
        self.result_button = Button(self.root, command=self.get_inf, text="获取")

    # 获取ComboBox的选择结果
    def goo(self, args):
        self.teamSelect = self.teamChosen.get()

    # 触发listBox的双击事件
    def v2url(self, event):
        v2url = self.url_list[self.display_info.curselection()[0]]
        webbrowser.open('https:' + v2url, new=0, autoraise=True)


    # 完成布局
    def gui_arrang(self):
        self.key_word.pack()
        # self.ip_input.pack()

        self.swipe.pack()
        self.sb1.pack(side=RIGHT, fill=Y)
        # self.sb2.pack(side=BOTTOM, fill=X)
        self.display_info.pack()
        self.sb1.config(command=self.display_info.yview)
        # self.sb2.config(command=self.display_info.xview)

        self.news.pack()
        self.display_info_1.pack()

        self.game.pack()
        self.teamChosen.pack()

        self.display_info_2.pack()
        self.result_button.pack()

    def get_inf(self):
        # 获取输入信息
        # self.key_word = self.ip_input.get()
        # target = self.search_by_name(self.key_word)
        # 为了避免非法值,导致程序崩溃,有兴趣可以用正则写一下具体的规则,我为了便于新手理解,减少代码量,就直接粗放的过滤了
        try:
            get_inf = GetI()
            g_r = get_inf.get_game_result()
            h_l, h_c, href = get_inf.get_hot_lines()
            self.url_list = href
            s_l, s_c, s_href = get_inf.get_selected_lines(self.teamSelect + '专区')
        except:
            pass

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

        # 清空回显列表可见部分,类似clear命令
        for item in range(10):
            self.display_info.insert(0, "")
            self.display_info_1.insert(0, "")
            self.display_info_2.insert(0, "")

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
    HG.gui_arrang()
    # HG.get_inf()
    # 主程序执行
    mainloop()
    pass


if __name__ == "__main__":
    main()