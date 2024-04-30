import os.path

filename = 'teams.txt'

def main():
    while True:
        menu()
        choice = int(input('请选择功能'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print("欢迎您的使用！！")
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
        input()


def menu():
    print('==================学生信息管理系统==============')
    print('===============功能菜单==================')
    print('\t\t\t1. 录入球队信息')
    print('\t\t\t2. 查找学生信息')
    print('\t\t\t3. 删除学生信息')
    print('\t\t\t4. 修改学生信息')
    print('\t\t\t5. 对学生成绩进行排序')
    print('\t\t\t6. 统计学生总人数')
    print('\t\t\t7. 显示所有学生信息')
    print('\t\t\t0. 退出程序')
    print('======================================')


def insert():
    team_list = []
    while True:
        name = input("请输入姓名：")
        if not name:
            break
        try:
            trun = int(input("请输入球队轮次："))
            winlose = list(input("请输入球队胜负："))
            score = int(input("请输入球队积分："))
        except:
            print("输入无效，请重新输入")
        # 将录入的学生信息保存在字典中
        team = {'id': id, 'name': name, 'trun': trun, 'winlose': winlose, 'score': score}
        # 将学生信息添加到列表中
        team_list.append(team)
        answer = input("是否继续添加y/n?")
        if answer == 'y':
            continue
        else:
            break
    # 调用save函数保存信息
    save(team_list)
    print("球队信息保存成功")


def save(lst):
    try:
        tem_txt = open(filename, 'a', encoding='utf-8')
    except:
        tem_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        tem_txt.write(str(item) + '\n')
    tem_txt.close()


def search():
    team_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input("按ID查找请按1，按姓名查找请按2：")
            if mode == '1':
                id = input("请输入学生ID：")
            elif mode == '2':
                name = input("请输入学生新明：")
            else:
                print("输入有误，请重新输入")
                search()
            with open(filename, 'r', encoding='utf-8') as file:
                student = file.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            team_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            team_query.append(d)
            show_query(team_query)
            # 清空列表
            team_query.clear()
            answer = input("是否继续查询？y/n")
            if answer == 'y':
                continue
            else:
                break
        else:
            print("无学生信息")
            return


def show_query(lst):
    if len(lst) == 0:
        print("无相关信息")
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'Java成绩', '总成绩'))
    # 定义内容显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('english'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('english')) + int(item.get('java'))
                                 ))


def delete():
    while True:
        student_id = input("请输入删除学生的ID：")
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:  # 空列表等于 False，非空列表等于True
                with open(filename, 'w', encoding='utf-8') as wfile:
                    # 只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转换为字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到学生ID为{student_id}的学生')
            else:
                print("无学生信息")
                break
            show()
            answer = input("是否继续删除？y/n")
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_old = file.readlines()
    else:
        return
    student_id = input("请输入修改学生的ID：")
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = {}
            d = dict(eval(item))
            if d['id'] == student_id:
                print("已经找到学生信息，请修改相关信息")
                while True:
                    try:
                        d['name'] = input("请输入姓名")
                        d['english'] = input("请输入英语成绩")
                        d['python'] = input("请输入python成绩")
                        d['java'] = input("请输入Java成绩")
                    except:
                        print("输入有误，请重新输入")
                    else:
                        break
                    wfile.write(str(d) + '\n')
                    print("修改成功")
            else:
                wfile.write(str(d) + '\n')
            answer = input("是否继续修改其他学生信息？y/n")
            if answer == 'y':
                modify()
            else:
                return


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            students = file.readlines()
        students_new = []
        for item in students:
            d = dict(eval(item))
            students_new.append(d)
    else:
        return

    # 排序方式
    asc_or_desc = input("请选择升序 0 还是降序 1？")
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print("输入有误，请重新输入")
        sort()
    mode = input("请选择排序方式(1.英语 2.python 3.Java 4.总成绩)：")
    if mode == '1':
        students_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
        # x 代表列表students_new中的项
    elif mode == '2':
        students_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        students_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '4':
        students_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
    else:
        print("输入有误，请重新输入")
    show_query(students_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            students = file.readlines()
            if students:
                print(f"总共有{len(students)}名学生")
            else:
                print("无学生信息")
    else:
        print("无学生信息")


def show():
    student_query = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student = file.readlines()
            for item in student:
                d = dict(eval(item))
                student_query.append(d)
        show_query(student_query)
        # 清空列表
        student_query.clear()
    else:
        print("无学生信息")
        return


if __name__ == '__main__':
    main()