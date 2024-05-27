import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정
font_path = ''
if plt.get_backend() == 'TkAgg':
    import platform
    if platform.system() == 'Windows':
        font_path = 'C:/Windows/Fonts/malgun.ttf'  # Windows
    elif platform.system() == 'Darwin':
        font_path = '/System/Library/Fonts/AppleGothic.ttf'  # MacOS
    else:
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  # Linux
    font_prop = fm.FontProperties(fname=font_path)
    plt.rc('font', family=font_prop.get_name())

# 데이터를 DataFrame으로 생성

df = pd.read_csv('C:/Users/net/Desktop/data.csv')

# 기업 유형별로 데이터 나누기
overall = df[df['컨설팅수진여부'] == '수진기업(전체)']
manufacturing = df[df['컨설팅수진여부'] == '수진기업(제조업)']
small_manufacturing = df[df['컨설팅수진여부'] == '비수진기업(중소제조업)']

# 그래프 그리기
fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True)

# 수진기업(전체)
for i, row in overall.iterrows():
    axes[0].plot(['2017년', '2018년', '2019년'], row[['2017년', '2018년', '2019년']], marker='o', label=row['구분'])
axes[0].set_title('수진기업(전체)')
axes[0].legend()
axes[0].set_ylabel('증가율 (%)')

# 수진기업(제조업)
for i, row in manufacturing.iterrows():
    axes[1].plot(['2017년', '2018년', '2019년'], row[['2017년', '2018년', '2019년']], marker='o', label=row['구분'])
axes[1].set_title('수진기업(제조업)')
axes[1].legend()
axes[1].set_ylabel('증가율 (%)')

# 비수진기업(중소제조업)
for i, row in small_manufacturing.iterrows():
    axes[2].plot(['2017년', '2018년', '2019년'], row[['2017년', '2018년', '2019년']], marker='o', label=row['구분'])
axes[2].set_title('비수진기업(중소제조업)')
axes[2].legend()
axes[2].set_ylabel('증가율 (%)')
axes[2].set_xlabel('연도')

# 그래프 간격 조정
plt.tight_layout()
plt.show()
