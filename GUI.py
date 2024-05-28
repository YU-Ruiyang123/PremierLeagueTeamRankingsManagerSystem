import tkinter as tk
from tkinter import ttk


class TeamManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("球队管理")
        self.geometry("1000x500")

        # 创建球队列表
        self.teams = [("球队A", 0, 0, 0), ("球队B", 0, 0, 0), ("球队C", 0, 0, 0)]

        # 创建树形视图展示球队信息
        self.tree = ttk.Treeview(self, columns=( "名称", "轮次", "胜", "负", "积分"), show="headings")
        self.tree.heading("名称", text="球队名称")
        self.tree.heading("轮次", text="轮次")
        self.tree.heading("胜", text="胜")
        self.tree.heading("负", text="负")
        self.tree.heading("积分", text="积分")

        # 填充树形视图
        for i, (name, round_, wins, losses) in enumerate(self.teams):
            self.tree.insert("", "end", iid=str(i), values=(name, round_, wins, losses, (wins * 3) + (losses * 0)))

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)



if __name__ == "__main__":
    app = TeamManagerApp()
    app.mainloop()