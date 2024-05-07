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
            winlose = int(input("请输入球队胜负："))
            score = int(input("请输入球队积分："))
        except:
            print("输入无效，请重新输入")
        team = {'name': name, 'trun': trun, 'winlose': winlose, 'score': score}
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
        name = ''
        if os.path.exists(filename):
            name = input("请输入球队名字：")
            with open(filename, 'r', encoding='utf-8') as file:
                team = file.readlines()
                for item in team:
                    d = dict(eval(item))
                    if name != '':
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
            print("无球队信息")
            return


def show_query(lst):
    if len(lst) == 0:
        print("无相关信息")
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('姓名', '球队轮次', '球队胜负', '球队积分'))
    # 定义内容显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('name'),
                                 item.get('trun'),
                                 item.get('winlose'),
                                 item.get('score')))
def delete():
    while True:
        team_name = input("请输入删除球队的name：")
        if team_name != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    team_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:  # 空列表等于 False，非空列表等于True
                with open(filename, 'w', encoding='utf-8') as wfile:
                    # 只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转换为字典
                        if d['name'] != team_name:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{team_name}的学生信息已被删除')
                    else:
                        print(f'没有找到学生ID为{team_name}的学生')
            else:
                print("无球队信息")
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
            team_old = file.readlines()
    else:
        return
    team_name = input("请输入修改球队的name：")
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in team_name:
            d = {}
            d = dict(eval(item))
            if d['id'] == team_name:
                print("已经找到球队信息，请修改相关信息")
                while True:
                    try:
                        d['name'] = input("请输入姓名")
                        d['trun'] = input("请输入球队轮次")
                        d['winlose'] = input("请输入球队胜负")
                        d['score'] = input("请输入球队积分")
                    except:
                        print("输入有误，请重新输入")
                    else:
                        break
                    wfile.write(str(d) + '\n')
                    print("修改成功")
            else:
                wfile.write(str(d) + '\n')
            answer = input("是否继续修改其他球队信息？y/n")
            if answer == 'y':
                modify()
            else:
                return

def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            teams = file.readlines()
            if teams:
                print(f"总共有{len(teams)}个球队")
            else:
                print("无球队信息")
    else:
        print("无球队信息")


def show():
    team_query = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            team = file.readlines()
            for item in team:
                d = dict(eval(item))
                team_query.append(d)
        show_query(team_query)
        # 清空列表
        team_query.clear()
    else:
        print("无球队信息")
        return


if __name__ == '__main__':
    main()