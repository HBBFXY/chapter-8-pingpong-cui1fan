import random
import matplotlib.pyplot as plt


plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

class PingPongMatch:
    """乒乓球比赛模拟类（11分制）"""
    def __init__(self, player1_name="选手A", player2_name="选手B"):
        self.player1_name = player1_name
        self.player2_name = player2_name

        self.score1 = 0
        self.score2 = 0
   
        self.serve_count = 0
     
        self.winner = None

    def serve(self):
        """模拟发球得分（随机生成，可调整胜率体现竞技差异）"""
        win_prob = 0.5  
        return 1 if random.random() < win_prob else 2

    def single_game(self):
        """模拟单局比赛（严格遵循11分制规则）"""
        self.score1, self.score2 = 0, 0
        self.serve_count = 0
        
        while True:
            self.serve_count += 1
            if (self.score1 + self.score2) < 20:
                serve_player = 1 if self.serve_count % 2 == 1 else 2
            else:
                serve_player = 1 if self.serve_count % 2 == 1 else 2

            score_winner = self.serve()
            if score_winner == 1:
                self.score1 += 1
            else:
                self.score2 += 1

            if (self.score1 >= 11 or self.score2 >= 11) and abs(self.score1 - self.score2) >= 2:
                self.winner = self.player1_name if self.score1 > self.score2 else self.player2_name
                break
            elif abs(self.score1 - self.score2) >= 2 and (self.score1 >= 11 and self.score2 >= 11):
                self.winner = self.player1_name if self.score1 > self.score2 else self.player2_name
                break

        return {
            "选手1得分": self.score1,
            "选手2得分": self.score2,
            "获胜方": self.winner
        }

    def multi_game_analysis(self, game_num=1000):
        """多局模拟分析竞技规律（默认1000局）"""
        player1_win = 0
        player2_win = 0
        score_diff_list = [] 
        
        for _ in range(game_num):
            result = self.single_game()
            score_diff = abs(result["选手1得分"] - result["选手2得分"])
            score_diff_list.append(score_diff)
            
            if result["获胜方"] == self.player1_name:
                player1_win += 1
            else:
                player2_win += 1


        avg_diff = sum(score_diff_list) / game_num  
        player1_win_rate = player1_win / game_num  
        player2_win_rate = player2_win / game_num  

       
        plt.figure(figsize=(12, 5))
       
        plt.subplot(1, 2, 1)
        plt.bar([self.player1_name, self.player2_name], [player1_win_rate, player2_win_rate], color=["red", "blue"])
        plt.title(f"{game_num}局模拟胜率")
        plt.ylabel("胜率")
        plt.ylim(0, 1)
        
  
        plt.subplot(1, 2, 2)
        plt.hist(score_diff_list, bins=10, color="green", alpha=0.7)
        plt.title(f"{game_num}局模拟分差分布")
        plt.xlabel("单局分差")
        plt.ylabel("局数")
        
        plt.tight_layout()
        plt.savefig("pingpong_analysis.png") 
        plt.show()

  
        return {
            f"{self.player1_name}胜率": round(player1_win_rate, 4),
            f"{self.player2_name}胜率": round(player2_win_rate, 4),
            "平均分差": round(avg_diff, 2),
            "最大分差": max(score_diff_list),
            "最小分差": min(score_diff_list)
        }

if __name__ == "__main__":
  
    match = PingPongMatch("马龙", "张继科")
    
 
    single_result = match.single_game()
    print("=== 单局比赛结果 ===")
    print(f"{match.player1_name}：{single_result['选手1得分']}分")
    print(f"{match.player2_name}：{single_result['选手2得分']}分")
    print(f"获胜方：{single_result['获胜方']}\n")

    print("=== 1000局竞技规律分析 ===")
    analysis_result = match.multi_game_analysis(game_num=1000)
    for key, value in analysis_result.items():
        print(f"{key}：{value}")# 在这个文件里编写代码
