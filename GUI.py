import tkinter as tk


def on_closing():
    root.destroy()  # 当点击关闭按钮时，调用这个函数来关闭窗口


root = tk.Tk()
root.title("Tkinter GUI 示例")  # 设置窗口标题
root.geometry("1000x800")  # 设置窗口大小

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)  # 使用pack布局，并添加一些垂直填充

button = tk.Button(root, text="退出", command=on_closing)  # 创建一个按钮，并绑定退出函数
button.pack(pady=10)  # 使用pack布局，并添加一些垂直填充

root.protocol("WM_DELETE_WINDOW", on_closing)  # 当点击窗口的关闭按钮时，调用on_closing函数

root.mainloop()