# main.py

class Team:
    def __init__(self, name):
        self.name = name
        self.rounds = 0
        self.wins = 0
        self.losses = 0
        self.points = 0

    def update_round(self, result):
        self.rounds += 1
        if result == 'win':
            self.wins += 1
            self.points += 3
        elif result == 'loss':
            self.losses += 1

    def get_stats(self):
        return {
            'rounds': self.rounds,
            'wins': self.wins,
            'losses': self.losses,
            'points': self.points
        }


class League:
    def __init__(self):
        self.teams = {}

    def add_team(self, team_name):
        if team_name not in self.teams:
            self.teams[team_name] = Team(team_name)
            print(f"球队 {team_name} 添加成功。")
        else:
            print(f"球队 {team_name} 已存在。")

    def remove_team(self, team_name):
        if team_name in self.teams:
            del self.teams[team_name]
            print(f"球队 {team_name} 删除成功。")
        else:
            print(f"球队 {team_name} 未找到。")

    def update_result(self, team_name, result):
        if team_name in self.teams:
            self.teams[team_name].update_round(result)
            print(f"球队 {team_name} 的比赛结果已更新。")
        else:
            print(f"球队 {team_name} 未找到。")

    def get_team_stats(self, team_name):
        if team_name in self.teams:
            return self.teams[team_name].get_stats()
        else:
            return None

