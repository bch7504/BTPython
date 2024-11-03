import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('result.csv')

# In ra danh sách các cột để kiểm tra
print("Columns in the DataFrame:", df.columns.tolist())


# Hàm để tìm top 3 cầu thủ có điểm cao nhất và thấp nhất cho mỗi chỉ số
def find_top_bottom_players(df, column):
    # Chuyển các giá trị không thể chuyển đổi sang số thành NaN
    df[column] = pd.to_numeric(df[column], errors='coerce')

    # Loại bỏ các hàng với giá trị NaN
    df_cleaned = df.dropna(subset=[column])

    # Tìm top 3 cầu thủ có điểm cao nhất
    top_players = df_cleaned.nlargest(3, column)[['player', 'team', 'nationality', 'position', 'age', column]]

    # Tìm top 3 cầu thủ có điểm thấp nhất
    bottom_players = df_cleaned.nsmallest(3, column)[['player', 'team', 'nationality', 'position', 'age', column]]

    return top_players, bottom_players


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

# Tạo từ điển để lưu kết quả
results = {}

# Tìm top 3 cầu thủ có điểm cao nhất và thấp nhất cho mỗi chỉ số
for column in columns_to_analyze:
    if column in df.columns:
        top_players, bottom_players = find_top_bottom_players(df, column)
        results[column] = {
            'top': top_players,
            'bottom': bottom_players
        }
    else:
        print(f"Column '{column}' does not exist in DataFrame.")

# Hiển thị kết quả
for stat, players in results.items():
    print(f"Top 3 players for {stat}:")
    print(players['top'].to_string(index=False))
    print(f"Bottom 3 players for {stat}:")
    print(players['bottom'].to_string(index=False))
    print("\n")