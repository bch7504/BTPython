import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('result.csv')

# In ra danh sách các cột để kiểm tra
print("Columns in the DataFrame:", df.columns.tolist())

# Các chỉ số cần phân tích
columns_to_analyze = [
    'goals', 'assists', 'xG', 'npxG', 'xAG', 'PrgC', 'PrgP', 'PrgR',
    'GA', 'GA90', 'SoTA', 'Saves', 'Save%', 'W', 'D', 'L', 'CS', 'CS%',
    'PKatt', 'PKA', 'PKsv', 'PKm', 'Save%',
    'Sh', 'SoT', 'SoT%', 'Sh/90', 'SoT/90', 'G/Sh', 'G/SoT', 'Dist', 'FK', 'PK', 'PKatt',
    'Cmp', 'Att', 'Cmp%', 'TotDist', 'PrgDist', 'Ast', 'xA', 'A-xAG', 'KP', '1/3', 'PPA', 'CrsPA', 'PrgP',
    'Live', 'Dead', 'FK', 'TB', 'Sw', 'Crs', 'TI', 'CK',
    'In', 'Out', 'Str', 'Cmp', 'Off', 'Blocks',
    'SCA', 'SCA90', 'PassLive', 'PassDead', 'TO', 'Sh', 'Fld', 'Def',
    'GCA', 'GCA90', 'PassLive', 'PassDead', 'TO', 'Sh', 'Fld', 'Def',
    'Tkl', 'TklW', 'Def 3rd', 'Mid 3rd', 'Att 3rd', 'Tkl', 'Att', 'Tkl%', 'Lost',
    'Blocks', 'Sh', 'Pass', 'Int', 'Tkl + Int', 'Clr', 'Err',
    'Touches', 'Def Pen', 'Def 3rd', 'Mid 3rd', 'Att 3rd', 'Att Pen', 'Live',
    'Att', 'Succ', 'Succ%', 'Tkld', 'Tkld%',
    'Carries', 'TotDist', 'ProDist', 'ProgC', '1/3', 'CPA', 'Mis', 'Dis',
    'Rec', 'PrgR', 'Starts', 'Mn/Start', 'Compl', 'Subs', 'Mn/Sub', 'unSub', 'PPM', 'onG', 'onGA',
    'onxG', 'onxGA', 'Fls', 'Fld', 'Off', 'Crs', 'OG', 'Recov',
    'Won', 'Lost', 'Won%'
]

# Tính toán trung vị, trung bình và độ lệch chuẩn cho toàn giải
overall_stats = []
for column in columns_to_analyze:
    if column in df.columns:
        median_value = df[column].median()
        mean_value = df[column].mean()
        std_value = df[column].std()

        overall_stats.append({
            'Attribute': column,
            'Median': median_value,
            'Mean': mean_value,
            'Std': std_value
        })

# Tính toán cho từng đội bóng
team_stats = []
for team in df['team'].unique():
    team_data = df[df['team'] == team]

    for column in columns_to_analyze:
        if column in team_data.columns:
            median_value = team_data[column].median()
            mean_value = team_data[column].mean()
            std_value = team_data[column].std()

            team_stats.append({
                'Attribute': column,
                'Team': team,
                'Median': median_value,
                'Mean': mean_value,
                'Std': std_value
            })

# Chuyển đổi kết quả thành DataFrame
overall_stats_df = pd.DataFrame(overall_stats)
team_stats_df = pd.DataFrame(team_stats)

# Ghi kết quả ra file CSV
overall_stats_df.to_csv('results2.csv', mode='w', index=False)
team_stats_df.to_csv('results2.csv', mode='a', header=False, index=False)

print("Results written to 'results2.csv'.")