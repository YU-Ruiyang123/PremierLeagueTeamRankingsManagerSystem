# gui.py

import tkinter as tk
from tkinter import messagebox, simpledialog
from main import League

class LeagueGUI:
    def __init__(self, master):
        self.master = master
        master.title("英超球队管理系统")
        self.league = League()

        # 创建UI元素
        self.create_widgets()

    def create_widgets(self):
        # 添加球队按钮
        self.add_team_button = tk.Button(self.master, text="添加球队", command=self.add_team)
        self.add_team_button.pack(pady=10)

        # 删除球队按钮（需要额外的输入来指定球队名称）
        self.remove_team_button = tk.Button(self.master, text="删除球队", command=self.remove_team)
        self.remove_team_button.pack(pady=10)

        # 更新比赛结果按钮（需要额外的输入来指定球队名称和结果）
        self.update_result_button = tk.Button(self.master, text="更新比赛结果", command=self.update_result)
        self.update_result_button.pack(pady=10)

        # 显示球队统计信息的标签（初始为空）
        self.stats_label = tk.Label(self.master, text="")
        self.stats_label.pack(pady=10)

    def add_team(self):
        team_name = simpledialog.askstring("添加球队", "请输入球队名称:")
        if team_name:
            if self.league.add_team(team_name):
                messagebox.showinfo("成功", f"球队 {team_name} 添加成功！")
                self.refresh_stats_label()
            else:
                messagebox.showerror("错误", f"添加球队 {team_name} 失败！")

    def remove_team(self):
        team_name = simpledialog.askstring("删除球队", "请输入要删除的球队名称:")
        if team_name:
            if self.league.remove_team(team_name):
                messagebox.showinfo("成功", f"球队 {team_name} 删除成功！")
                self.refresh_stats_label()
            else:
                messagebox.showerror("错误", f"删除球队 {team_name} 失败！")

    def update_result(self):
        team_name = simpledialog.askstring("更新比赛结果", "请输入球队名称:")
        if team_name:
            result = simpledialog.askstring("更新比赛结果", f"请输入球队 {team_name} 的比赛结果 (W/L/D):")
            if result and result.upper() in ['W', 'L', 'D']:
                self.league.update_result(team_name, result.upper())
                messagebox.showinfo("成功", f"球队 {team_name} 比赛结果更新成功！")
                self.refresh_stats_label()
            else:
                messagebox.showerror("错误", "请输入有效的比赛结果（W/L/D）！")

    def refresh_stats_label(self, team_name=None):
        stats = self.league.get_team_stats(team_name)
        if stats:
            stats_text = "\n".join([f"{team_name}: {team_stats}" for team_name, team_stats in stats.items()])
            self.stats_label.config(text=stats_text)
        else:
            self.stats_label.config(text="暂无球队信息。")

# 运行GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = LeagueGUI(root)
    root.mainloop()
