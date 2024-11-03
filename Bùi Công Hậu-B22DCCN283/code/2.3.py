import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Đọc dữ liệu từ file result.csv
df = pd.read_csv('result.csv')

# Các cột chỉ số cần phân tích
columns_to_analyze = [
    'goals', 'assists', 'xG', 'npxG', 'xAG', 'PrgC', 'PrgP', 'PrgR', 'GA', 'GA90',
    'SoTA', 'Saves', 'Save%', 'W', 'D', 'L', 'CS', 'CS%', 'PKatt', 'PKA', 'PKsv',
    'PKm', 'Sh', 'SoT', 'SoT%', 'Sh/90', 'SoT/90', 'G/Sh', 'G/SoT', 'Dist', 'FK',
    'PK', 'Cmp', 'Att', 'Cmp%', 'TotDist', 'PrgDist', 'Ast', 'xA', 'KP', '1/3',
    'PPA', 'CrsPA', 'PrgP'
]

# Tạo thư mục lưu biểu đồ
if not os.path.exists('histograms'):
    os.makedirs('histograms')

# Vẽ histogram cho mỗi chỉ số cho toàn giải
for column in columns_to_analyze:
    if column in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], kde=True, bins=30)
        plt.title(f'Histogram of {column} for All Players')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.savefig(f'histograms/{column}_all_players.png')
        plt.close()

# Vẽ histogram cho mỗi chỉ số cho từng đội
teams = df['team'].unique()
for team in teams:
    team_data = df[df['team'] == team]
    for column in columns_to_analyze:
        if column in team_data.columns:
            plt.figure(figsize=(10, 6))
            sns.histplot(team_data[column], kde=True, bins=30)
            plt.title(f'Histogram of {column} for {team}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.savefig(f'histograms/{column}_{team}.png')
            plt.close()

print("Histograms have been saved in the 'histograms' directory.")