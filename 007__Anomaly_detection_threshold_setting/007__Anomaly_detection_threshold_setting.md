# シナリオ案

- 問題：分析実装後のアラームの再設定検討や仕組みを理解するための時間が増え作業負荷が増大したように感じる
- 課題：アラームに対して次のアプローチを考えることが(時間がかかったり技術が無く)難しい

※ 事前に入力として現在設定している閾値を持っていることとする。

- アラーム発生からそれ以前のデータを収集し、データ分布や時系列での状況を可視化+GPTでデータの概要を生成する。(○○に発生したアラームではHTTPステータス○○のエラーが発生し、処理が正常終了しなかったためアラームが発生しました。このアラームの直前には○○が起きており、このアラームより前のデータ○○個のデータをみると...)
- アラーム発生からそれ以前のデータを使い簡易的な分析を実施、新しい閾値の提案とその場合データはどのように読み取ることができるようになるのかを現状と比較しての概要説明をGPTモデルで生成する
    - 閾値設定用の分析は、取得データの分布95%のデータを正常とし、5%を異常とする形でHold Out法で教師なしで分析を実施する。時系列を考慮したARIMAでの分析もしたいな

あたかもGPTモデルがデータの説明・可視化、閾値の再設定案の提示まで自動でやってくれる感じにしたい<br>
入出力のあいまいさを許しつつ出力の曖昧さはルールで補う形でプロンプトを作成する

- アラームに対して次のアプローチを提示するためアラーム発報時のデータの重要度の高いトークンをいくつか抽出(HTTPステータスが抽出されるイメージ)し、ReActでDBまたはネットからトークンに関連する情報をもとに次のアプローチを生成する


```python
!pip install japanize-matplotlib
```

    Requirement already satisfied: japanize-matplotlib in /usr/local/lib/python3.10/dist-packages (1.1.3)
    Requirement already satisfied: matplotlib in /usr/local/lib/python3.10/dist-packages (from japanize-matplotlib) (3.7.1)
    Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib->japanize-matplotlib) (1.0.7)
    Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib->japanize-matplotlib) (0.11.0)
    Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib->japanize-matplotlib) (4.39.3)
    Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib->japanize-matplotlib) (1.4.4)
    Requirement already satisfied: numpy>=1.20 in /usr/local/lib/python3.10/dist-packages (from matplotlib->japanize-matplotlib) (1.23.5)
    Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib->japanize-matplotlib) (23.1)
    Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib->japanize-matplotlib) (9.5.0)
    Requirement already satisfied: pyparsing>=2.3.1 in /usr/lib/python3/dist-packages (from matplotlib->japanize-matplotlib) (2.4.7)
    Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib->japanize-matplotlib) (2.8.2)
    Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.7->matplotlib->japanize-matplotlib) (1.16.0)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0m


```python
# アラーム前まで仮定で設定している閾値(現在設定中の閾値)
threshold = 1000
```


```python
from contextlib import contextmanager
from time import time

class Timer:
    """処理時間を表示するクラス
    with Timer(prefix=f'pred cv={i}'):
        y_pred_i = predict(model, loader=test_loader)
    
    with Timer(prefix='fit fold={} '.format(i)):
        clf.fit(x_train, y_train, 
                eval_set=[(x_valid, y_valid)],  
                early_stopping_rounds=100,
                verbose=verbose)

    with Timer(prefix='fit fold={} '.format(i), verbose=500):
        clf.fit(x_train, y_train, 
                eval_set=[(x_valid, y_valid)],  
                early_stopping_rounds=100,
                verbose=verbose)
    """
    def __init__(self, logger=None, format_str='{:.3f}[s]', prefix=None, suffix=None, sep=' ', verbose=0):

        if prefix: format_str = str(prefix) + sep + format_str
        if suffix: format_str = format_str + sep + str(suffix)
        self.format_str = format_str
        self.logger = logger
        self.start = None
        self.end = None
        self.verbose = verbose

    @property
    def duration(self):
        if self.end is None:
            return 0
        return self.end - self.start

    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        out_str = self.format_str.format(self.duration)
        if self.logger:
            self.logger.info(out_str)
        else:
            print(out_str)
```


```python
import warnings
warnings.filterwarnings('ignore')

import gc
gc.collect()
```




    257



## 疑似データの作成


```python
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def seed(seed=42):
    np.random.seed(seed)
    random.seed(seed)
seed(42)

# データ件数と異常値の数を10:1になるように設定
data_size = 1000
num_anomalies = 100

# 日付インデックスを生成
date_rng = pd.date_range(start='2021-01-01', end='2021-12-31', freq='S')
date_rng = np.random.choice(date_rng, data_size, replace=False)
date_rng.sort()

# レスポンスタイムの正規分布に従ったランダムデータを生成
response_time_data = np.random.normal(loc=200, scale=20, size=data_size)

# ステータスコードのリストを作成
status_codes = ['200', '201', '204', '400', '401', '403', '404', '500', '502', '503']
status_code_probs = [0.6, 0.1, 0.05, 0.1, 0.02, 0.02, 0.08, 0.01, 0.01, 0.01]
status_code_data = np.random.choice(status_codes, size=data_size, p=status_code_probs)

# 異常値をランダムに挿入
anomaly_indices = random.sample(range(data_size), num_anomalies)
for idx in anomaly_indices:
    response_time_data[idx] = np.random.normal(loc=1000, scale=100)
    status_code_data[idx] = random.choice(['404', '500', '502', '503'])

# データフレームを作成
# df = pd.DataFrame(data={'response_time': response_time_data, 'status_code': status_code_data}, index=date_rng)
df = pd.DataFrame(data={'date_time': date_rng, 'response_time': response_time_data, 'status_code': status_code_data})

```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date_time</th>
      <th>response_time</th>
      <th>status_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-01-01 01:13:30</td>
      <td>235.196490</td>
      <td>201</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2021-01-01 14:29:43</td>
      <td>216.519988</td>
      <td>200</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2021-01-02 03:15:21</td>
      <td>188.627762</td>
      <td>200</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2021-01-02 10:17:39</td>
      <td>181.143408</td>
      <td>200</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021-01-02 16:28:55</td>
      <td>189.266348</td>
      <td>400</td>
    </tr>
  </tbody>
</table>
</div>



## データ概要可視化


```python
start_time = time()
```


```python
import matplotlib.pyplot as plt
import japanize_matplotlib

import seaborn as sns
plt.style.use('fivethirtyeight')

def plot_count(feature, title, df, size=1):
    """クラス/特徴量をプロットする
    Pram:
        feature : 分析するカラム
        title : グラフタイトル
        df : プロットするデータフレーム
        size : デフォルト 1.
    """
    f, ax = plt.subplots(1,1, figsize=(4*size,4))
    total = float(len(df))
    # 最大20カラムをヒストグラムで表示
#     g = sns.countplot(data=df, x = feature, order = df[feature].value_counts().index[:20], palette='Set3')
    g = sns.countplot(data=df, y = feature, order = df[feature].value_counts().index[:10], palette='Set3')
    # g.set_title("Number and percentage of {}".format(title))
    g.set_title("{}の割合".format(title))
    
#     if(size > 2):
        # サイズ2以上の時、行名を90°回転し、表示
#         plt.xticks(rotation=90, size=8)
    # データ比率の表示
    for p in ax.patches:
        height = p.get_height()
        width = p.get_width()
#         ax.text(p.get_x()+p.get_width()/2.,
#                 height + 3,
#                 '{:1.2f}%'.format(100*height/total),
#                 ha="center")
        ax.text(width + 40,
                p.get_y()+p.get_height()+.025/2.,
                '{:1.2f}%'.format(100*width/total),
                ha="right") 
    plt.tight_layout()
    plt.show()
```


```python
# 全データのstatus_codeの比率を確認する
plot_count(feature='status_code', title='status_code', df=df, size=3.5)
```


    
![png](output_11_0.png)
    



```python
df['status_code'].value_counts()
```




    status_code
    200    544
    404     96
    201     86
    400     84
    204     52
    500     39
    503     36
    502     33
    403     20
    401     10
    Name: count, dtype: int64




```python
print(f'Number of all data: {df.shape[0]}')
```

    Number of all data: 1000



```python
import matplotlib.dates as mdates

# 時系列可視化
def time_prot(df, threshold=0, lebel_name='threshold', color='darkblue', title='response_time の時系列推移'):
    fig, ax = plt.subplots(1,1, figsize=(4*3.2,4))
    ax.plot(df['date_time'], df['response_time'], marker='o', color='lightskyblue')

    # response_timeが800以上のデータのstatus_codeを表示
    for index, row in df.iterrows():
        if threshold != 0:
            if row['response_time'] >= threshold:
                # ax.text(row['date_time'], row['response_time'], str(row['status_code']), backgroundcolor="lightyellow")
                ax.text(row['date_time'], row['response_time'], str(row['status_code']), size=8)

    # x軸の設定
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # plt.xticks(rotation=45)
    plt.xticks(rotation=25)

    # 閾値の表示
    if threshold != 0:
        ax.axhline(y=threshold, c=color, linewidth = 1.6, alpha=0.64, label=lebel_name)
        # 凡例の設定
        # ax.legend(loc='upper left')
        ax.legend()

    # タイトルとラベルの設定
    plt.title(title)
    plt.xlabel('Date Time')
    plt.ylabel('Response Time')
    plt.tight_layout()
    plt.show()
```


```python
time_prot(df, threshold)
```


    
![png](output_15_0.png)
    



```python
df[df['response_time'] >= threshold]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date_time</th>
      <th>response_time</th>
      <th>status_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>25</th>
      <td>2021-01-13 05:21:11</td>
      <td>1124.366513</td>
      <td>500</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2021-01-13 15:37:20</td>
      <td>1045.896602</td>
      <td>502</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2021-01-14 04:53:20</td>
      <td>1049.931362</td>
      <td>502</td>
    </tr>
    <tr>
      <th>44</th>
      <td>2021-01-17 09:57:30</td>
      <td>1011.391710</td>
      <td>500</td>
    </tr>
    <tr>
      <th>80</th>
      <td>2021-01-30 08:08:47</td>
      <td>1016.802237</td>
      <td>404</td>
    </tr>
    <tr>
      <th>89</th>
      <td>2021-02-04 21:53:57</td>
      <td>1104.939942</td>
      <td>503</td>
    </tr>
    <tr>
      <th>95</th>
      <td>2021-02-06 18:43:58</td>
      <td>1003.455028</td>
      <td>500</td>
    </tr>
    <tr>
      <th>99</th>
      <td>2021-02-07 16:04:52</td>
      <td>1068.312356</td>
      <td>503</td>
    </tr>
    <tr>
      <th>104</th>
      <td>2021-02-09 01:14:46</td>
      <td>1107.179114</td>
      <td>502</td>
    </tr>
    <tr>
      <th>114</th>
      <td>2021-02-15 05:49:43</td>
      <td>1048.247816</td>
      <td>404</td>
    </tr>
    <tr>
      <th>127</th>
      <td>2021-02-20 03:53:35</td>
      <td>1079.416588</td>
      <td>502</td>
    </tr>
    <tr>
      <th>142</th>
      <td>2021-02-25 19:08:39</td>
      <td>1110.090483</td>
      <td>502</td>
    </tr>
    <tr>
      <th>163</th>
      <td>2021-03-05 21:08:30</td>
      <td>1040.464885</td>
      <td>503</td>
    </tr>
    <tr>
      <th>166</th>
      <td>2021-03-07 12:10:02</td>
      <td>1034.677382</td>
      <td>404</td>
    </tr>
    <tr>
      <th>196</th>
      <td>2021-03-17 13:34:40</td>
      <td>1004.078148</td>
      <td>404</td>
    </tr>
    <tr>
      <th>203</th>
      <td>2021-03-19 21:00:56</td>
      <td>1015.805468</td>
      <td>500</td>
    </tr>
    <tr>
      <th>214</th>
      <td>2021-03-23 10:01:46</td>
      <td>1094.918171</td>
      <td>404</td>
    </tr>
    <tr>
      <th>220</th>
      <td>2021-03-25 19:57:01</td>
      <td>1061.683363</td>
      <td>502</td>
    </tr>
    <tr>
      <th>223</th>
      <td>2021-03-26 08:06:39</td>
      <td>1057.038911</td>
      <td>503</td>
    </tr>
    <tr>
      <th>233</th>
      <td>2021-03-29 12:20:14</td>
      <td>1040.659326</td>
      <td>502</td>
    </tr>
    <tr>
      <th>250</th>
      <td>2021-04-03 09:20:39</td>
      <td>1012.544021</td>
      <td>503</td>
    </tr>
    <tr>
      <th>281</th>
      <td>2021-04-15 22:55:53</td>
      <td>1064.824344</td>
      <td>500</td>
    </tr>
    <tr>
      <th>296</th>
      <td>2021-04-23 01:10:46</td>
      <td>1050.135021</td>
      <td>500</td>
    </tr>
    <tr>
      <th>300</th>
      <td>2021-04-23 23:41:40</td>
      <td>1246.258677</td>
      <td>502</td>
    </tr>
    <tr>
      <th>429</th>
      <td>2021-06-06 01:38:11</td>
      <td>1125.659602</td>
      <td>500</td>
    </tr>
    <tr>
      <th>432</th>
      <td>2021-06-06 11:54:03</td>
      <td>1053.749146</td>
      <td>404</td>
    </tr>
    <tr>
      <th>459</th>
      <td>2021-06-19 14:20:14</td>
      <td>1000.740886</td>
      <td>503</td>
    </tr>
    <tr>
      <th>470</th>
      <td>2021-06-24 18:21:28</td>
      <td>1076.874877</td>
      <td>500</td>
    </tr>
    <tr>
      <th>549</th>
      <td>2021-07-24 08:44:28</td>
      <td>1090.182137</td>
      <td>404</td>
    </tr>
    <tr>
      <th>558</th>
      <td>2021-07-27 07:48:37</td>
      <td>1184.970069</td>
      <td>502</td>
    </tr>
    <tr>
      <th>591</th>
      <td>2021-08-10 11:30:35</td>
      <td>1013.334766</td>
      <td>503</td>
    </tr>
    <tr>
      <th>604</th>
      <td>2021-08-13 21:18:14</td>
      <td>1173.805152</td>
      <td>502</td>
    </tr>
    <tr>
      <th>616</th>
      <td>2021-08-18 01:01:21</td>
      <td>1228.750114</td>
      <td>500</td>
    </tr>
    <tr>
      <th>643</th>
      <td>2021-08-26 20:19:23</td>
      <td>1116.461138</td>
      <td>500</td>
    </tr>
    <tr>
      <th>650</th>
      <td>2021-08-29 03:20:05</td>
      <td>1047.428335</td>
      <td>500</td>
    </tr>
    <tr>
      <th>665</th>
      <td>2021-09-03 14:55:57</td>
      <td>1080.860239</td>
      <td>503</td>
    </tr>
    <tr>
      <th>714</th>
      <td>2021-09-19 19:59:01</td>
      <td>1061.391051</td>
      <td>503</td>
    </tr>
    <tr>
      <th>718</th>
      <td>2021-09-21 09:48:56</td>
      <td>1001.166794</td>
      <td>503</td>
    </tr>
    <tr>
      <th>721</th>
      <td>2021-09-22 13:27:14</td>
      <td>1127.094508</td>
      <td>500</td>
    </tr>
    <tr>
      <th>754</th>
      <td>2021-10-03 19:56:42</td>
      <td>1048.110733</td>
      <td>500</td>
    </tr>
    <tr>
      <th>758</th>
      <td>2021-10-04 15:54:42</td>
      <td>1019.475151</td>
      <td>500</td>
    </tr>
    <tr>
      <th>759</th>
      <td>2021-10-04 18:23:48</td>
      <td>1039.034874</td>
      <td>500</td>
    </tr>
    <tr>
      <th>777</th>
      <td>2021-10-09 21:12:59</td>
      <td>1066.065949</td>
      <td>503</td>
    </tr>
    <tr>
      <th>791</th>
      <td>2021-10-12 16:17:03</td>
      <td>1042.909050</td>
      <td>503</td>
    </tr>
    <tr>
      <th>825</th>
      <td>2021-10-23 14:51:17</td>
      <td>1041.578415</td>
      <td>404</td>
    </tr>
    <tr>
      <th>828</th>
      <td>2021-10-24 01:00:23</td>
      <td>1052.115665</td>
      <td>404</td>
    </tr>
    <tr>
      <th>854</th>
      <td>2021-11-03 06:21:13</td>
      <td>1008.916431</td>
      <td>404</td>
    </tr>
    <tr>
      <th>890</th>
      <td>2021-11-17 22:46:27</td>
      <td>1006.307230</td>
      <td>500</td>
    </tr>
    <tr>
      <th>906</th>
      <td>2021-11-23 11:08:10</td>
      <td>1049.682995</td>
      <td>500</td>
    </tr>
    <tr>
      <th>954</th>
      <td>2021-12-14 03:50:13</td>
      <td>1050.799370</td>
      <td>404</td>
    </tr>
    <tr>
      <th>964</th>
      <td>2021-12-17 18:15:30</td>
      <td>1169.843472</td>
      <td>404</td>
    </tr>
    <tr>
      <th>983</th>
      <td>2021-12-23 15:59:17</td>
      <td>1039.860099</td>
      <td>503</td>
    </tr>
    <tr>
      <th>986</th>
      <td>2021-12-24 09:14:18</td>
      <td>1081.662818</td>
      <td>502</td>
    </tr>
  </tbody>
</table>
</div>




```python
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

def res_plot_count(feature, title, df, size=1):
    """クラス/特徴量をプロットする
    Pram:
        feature : 分析するカラム
        title : グラフタイトル
        df : プロットするデータフレーム
        size : デフォルト 1.
    """
    f, ax = plt.subplots(1,1, figsize=(32*size,4))
    total = float(len(df))
    # 最大20カラムをヒストグラムで表示
#     g = sns.countplot(data=df, x = feature, order = df[feature].value_counts().index[:20], palette='Set3')
    g = sns.countplot(data=df, y = feature, order = df[feature].value_counts().index[:10], palette='Set3')
    # g.set_title("Setting Anomaly Data\nNumber and percentage of {}".format(title), size=16)
    g.set_title("異常として分類される {} の数と割合".format(title), size=16)
    
    
#     if(size > 2):
        # サイズ2以上の時、行名を90°回転し、表示
#         plt.xticks(rotation=90, size=8)
    # データ比率の表示
    for p in ax.patches:
        height = p.get_height()
        width = p.get_width()
#         ax.text(p.get_x()+p.get_width()/2.,
#                 height + 3,
#                 '{:1.2f}%'.format(100*height/total),
#                 ha="center")
        ax.text(width - 0.05,
                p.get_y()+p.get_height()-.05,
                f'Amount of data: {width}\nRatio: '+'{:1.2f}%'.format(100*width/total),
                ha="right") 
    plt.tight_layout()
    plt.show()
```


```python
# response_time=1000を異常と分類した時の異常データのstatus_codeの比率を確認する
res_plot_count(feature='status_code', title='status_code', df=df[df['response_time'] >= threshold], size=0.32)
```


    
![png](output_18_0.png)
    



```python
df[df['response_time'] >= threshold]['status_code'].value_counts()
```




    status_code
    500    17
    503    13
    404    12
    502    11
    Name: count, dtype: int64




```python
anomaly_num = df[df['response_time'] >= threshold].shape[0]
print(f'Number of Anomaly data: {anomaly_num}')
```

    Number of Anomaly data: 53



```python
# 概要可視化出力の処理時間
end_time = time()

elapsed_time = end_time - start_time
print(f"概要可視化出力の処理時間: {elapsed_time}秒")
```

    概要可視化出力の処理時間: 1.070552110671997秒


# 簡易分析の実施


```python
start_time = time()
```

## 分析の前に目的変数の正規性の確認


```python
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MaxNLocator
from scipy import stats
from scipy.stats import norm
```


```python
def plot_dist3(df, feature, title):
    """
    カラムが連続値用の可視化関数
    """
    fig = plt.figure(constrained_layout=True)
    fig.set_size_inches(16, 9)
    # 3列、3行のグリッドを作成します
    grid = gridspec.GridSpec(ncols=3, nrows=2, figure=fig)

    # ヒストグラムの図示    
    ax1 = fig.add_subplot(grid[0, :2])
    ax1.set_title('Histogram')
    
    # seaborn v0.14.0 removed
    # Please adapt your code to use either `displot` 
    # (a figure-level function with similar flexibility) or 
    # `histplot` (an axes-level function for histograms).
    # sns.distplot(df.loc[:, feature],
    #              hist=True,
    #              kde=True,
    #              fit=norm,
    #               hist_kws={
    #              'rwidth': 0.85,
    #              'edgecolor': 'black',
    #              'alpha': 0.8},
    #              ax=ax1,
    #              color='darkorange')

    sns.histplot(df.loc[:, feature],
                 kde=True,
                 hue_order =(0, 1),
                 bins=30,
                 color='darkorange',
                 ax=ax1,)

    ax1.axvline(df.loc[:, feature].mean(), color='darkblue', linestyle='dashed', linewidth=3)
    min_ylim, max_ylim = plt.ylim()
    # 平均値の表示
    ax1.text(df.loc[:, feature].mean()*1.05, max_ylim*0.85, 'Mean: {:.2f}'.format(df.loc[:, feature].mean()), color='Black', fontsize='12',
             bbox=dict(boxstyle='round',facecolor='darkorange', alpha=0.5))
    ax1.legend(labels=['Actual','Normal'])
    ax1.xaxis.set_major_locator(MaxNLocator(nbins=24))

    # QQプロット
    ax2 = fig.add_subplot(grid[1, :2])
    ax2.set_title('Probability Plot')
    stats.probplot(df.loc[:, feature].fillna(np.mean(df.loc[:, feature])),
                   plot=ax2)
    ax2.get_lines()[0].set_markerfacecolor('#e74c3c')
    ax2.get_lines()[0].set_markersize(12.0)
    ax2.xaxis.set_major_locator(MaxNLocator(nbins=24))

    # Box Plot
    ax3 = fig.add_subplot(grid[:, 2])
    ax3.set_title('Box Plot')
    sns.boxplot(y=feature, data=df, ax=ax3, palette='Set3')
    ax3.yaxis.set_major_locator(MaxNLocator(nbins=24))

    plt.suptitle(f'{title}', fontsize=24)
```


```python
# 全データでの正規性の確認
plot_dist3(df, 'response_time', 'Readability Score Distribution')
```


    
![png](output_27_0.png)
    



```python
# 仮定で設定している現閾値以下のデータで正規性を確認
plot_dist3(df[df['response_time'] < threshold], 'response_time', 'Below Threshold data Readability Score Distribution')
```


    
![png](output_28_0.png)
    



```python
# データ生成時に外れ値として設定した800以下のデータで正規性確認
plot_dist3(df[df['response_time'] < 800], 'response_time', 'Generation Threshold data Readability Score Distribution')
```


    
![png](output_29_0.png)
    




## 欠損値の確認


```python
# 欠損値計算関数
def missing_value_table(df):
    """欠損値の数とカラムごとの割合の取得
    Param : DataFrame
    確認を行うデータフレーム
    """
    # 欠損値の合計
    mis_val = df.isnull().sum()
    # カラムごとの欠損値の割合
    mis_val_percent = 100 * mis_val / len(df)
    # 欠損値の合計と割合をテーブルに結合
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    # カラム名の編集
    mis_val_table = mis_val_table.rename(
        columns={0:'Missing Values', 1:'% of Total Values'}
    )
    # データを欠損値のあるものだけにし。小数点以下1桁表示で降順ソートする
    mis_val_table = mis_val_table[mis_val_table.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False
    ).round(1)

    # 欠損値をもつカラム数の表示
    print('このデータフレームのカラム数は、', df.shape[1])
    print('このデータフレームの欠損値列数は、', mis_val_table.shape[0])
    # 欠損値データフレームを返す
    return mis_val_table
```


```python
missing_value_table(df)
```

    このデータフレームのカラム数は、 3
    このデータフレームの欠損値列数は、 0





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Missing Values</th>
      <th>% of Total Values</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
# 欠損値はないが一応除外処理
df.dropna(how='all', inplace=True)
```

## 学習用データを作成

四分位範囲外のデータを異常値と仮定して除外して、その半分を学習に使用する


```python
def remove_outlier(df_in, col_name):
    """
    カラムデータの四分位範囲外の除外
    Parametr:
        df_in:
            対象のデータフレーム
        col_name:
            対象のデータフレームカラム名
    Return:
        四分位範囲外を除外したカラムデータ
    """
    # 四分位範囲の算出
    q1 = df_in[col_name].quantile(0.25)     # 第一四分位数 25%パーセンタイル
    q3 = df_in[col_name].quantile(0.75)     # 第三四分位数 75%パーセンタイル
    iqr = q3-q1                             # 四分位範囲
    # 外れ値に当たる範囲を算出
    fence_low  = q1 - 1.5*iqr               # 第一四分位数-第四四分位数
    fence_high = q3 + 1.5*iqr               # 第三四分位数-第四四分位数
    
    # return fence_low, fence_high
    # 範囲外の除外
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
    
    df_in = df_in.loc[(df_in[col_name] <= fence_low) | (df_in[col_name] >= fence_high)]
    return df_out, df_in
```


```python
# 四分位範囲外のデータの除外
df_out, df_in = remove_outlier(df, 'response_time')
df_out.reset_index(inplace=True, drop=True)

# 除外結果
df.shape, df_out.shape, df_in.shape
```




    ((1000, 3), (897, 3), (103, 3))




```python
plot_dist3(df_out, 'response_time', '目的変数のデータ分布')
```


    
![png](output_38_0.png)
    



```python
time_prot(df_out, title='学習に使用する response_time の時系列データの推移')
```


    
![png](output_39_0.png)
    



```python
# dfの行数を取得し、半分を計算する
half_len = len(df_out) // 2

# 最初の半分の行を抽出する
train_df = df_out.iloc[:half_len]
train_df.reset_index(inplace=True, drop=True)
```


```python
valid_df = pd.concat([df_out.iloc[half_len:], df_in])
valid_df = valid_df.sort_values('date_time')

valid_df.reset_index(inplace=True, drop=True)
```


```python
train_df.shape, valid_df.shape
```




    ((448, 3), (552, 3))



## LOFによる簡易分析の実行


```python
start_time = time()
```


```python
from sklearn.neighbors import LocalOutlierFactor
```


```python
# LOFの近傍数kを変化させて検証用データに対する予測結果を取得(
preds = []
for k in range(1,11):
    with Timer(prefix=f'n_neighbors k={k}'):
        # 近傍数を設定してLOFをインスタンス化
        lof = LocalOutlierFactor(n_neighbors=k, novelty=True, contamination='auto')
        lof.fit(train_df.drop(['date_time', 'status_code'], axis=1))
        pred = lof._predict(valid_df.drop(['date_time', 'status_code'], axis=1))
        
        preds.append(pred)
```

    n_neighbors k=1 0.004[s]
    n_neighbors k=2 0.004[s]
    n_neighbors k=3 0.003[s]
    n_neighbors k=4 0.005[s]
    n_neighbors k=5 0.004[s]
    n_neighbors k=6 0.003[s]
    n_neighbors k=7 0.003[s]
    n_neighbors k=8 0.003[s]
    n_neighbors k=9 0.004[s]
    n_neighbors k=10 0.003[s]



```python
# 予測結果の平均をとり、0以上なら1(正常)、以下なら-1(異常)に設定
pred = np.mean(preds, axis=0)
pred[pred >= 0] = 1
pred[pred < 0] = -1
```


```python
valid_df['judgment'] = pred
```


```python
time_prot(valid_df, title='検証に使用する response_time の時系列データの推移')
```


    
![png](output_49_0.png)
    



```python
valid_df['judgment'].value_counts()
```




    judgment
     1.0    408
    -1.0    144
    Name: count, dtype: int64



## 新しい閾値の設定と可視化


```python
# 異常と予測したデータを閾値設定用データとして取得
pred_anomaly_df = valid_df[valid_df['judgment']==-1].copy()
pred_anomaly_df.reset_index(inplace=True, drop=True)
```


```python
pred_anomaly_df['judgment'].value_counts()
```




    judgment
    -1.0    144
    Name: count, dtype: int64




```python
# 500と503に対して重みを設定した加重平均を算出し新しい閾値とする
w_500 = 1.5
w_503 = 1.2

pred_anomaly_df['weights'] = 1.0
pred_anomaly_df.loc[pred_anomaly_df['status_code'] == '500', 'weights'] = w_500
pred_anomaly_df.loc[pred_anomaly_df['status_code'] == '503', 'weights'] = w_503

weighted_mean = (pred_anomaly_df['response_time'] * pred_anomaly_df['weights']).sum() / pred_anomaly_df['weights'].sum()
simple_mean = pred_anomaly_df['response_time'].mean()

# 異常と分類したデータ数が少ないのもあるが結果はほぼ同じになった
print('Weighted Mean:', weighted_mean)
print('Simple Mean:  ', simple_mean)

# 新しい閾値をセット
new_threshold = weighted_mean
print('New Threshold:', new_threshold)
```

    Weighted Mean: 781.3846612433357
    Simple Mean:   753.3878771255627
    New Threshold: 781.3846612433357


## 簡易分析の結果


```python
# GPTが生成した文章の前に付ける文章例
print(f'簡易的に分析を行い、再設定する場合の閾値を考えました。\n以下のアラーム発報時のデータから四分位範囲外を除外した結果を正常であると仮定し、そのデータの半分である{half_len}行を学習データとして使用しています。')
```

    簡易的に分析を行い、再設定する場合の閾値を考えました。
    以下のアラーム発報時のデータから四分位範囲外を除外した結果を正常であると仮定し、そのデータの半分である448行を学習データとして使用しています。



```python
# 全データでの正規性の確認
plot_dist3(df, 'response_time', '目的変数のデータ分布')
```


    
![png](output_57_0.png)
    



```python
time_prot(train_df, title='学習に使用した response_time の時系列推移')
```


    
![png](output_58_0.png)
    



```python
time_prot(valid_df, new_threshold, lebel_name='new_threshold', color='darkred', title='学習には使用せず閾値設定時にのみ使用した response_time の時系列推移')
```


    
![png](output_59_0.png)
    



```python
# GPTが生成した文章の前に付ける文章例
print(f'閾値の作成にはLOFを使用し、推論では近傍数kを1～10までそれぞれ変えたときの結果の平均を設定しています。\n提案したい閾値は、異常と分類されたデータの中でHTTPステータスが500または503である場合に重みを付与し、加重平均を算出した結果です。\n・新しい閾値:{new_threshold}\n新しい閾値を設定した場合の可視化結果は以下となります。')
```

    閾値の作成にはLOFを使用し、推論では近傍数kを1～10までそれぞれ変えたときの結果の平均を設定しています。
    提案したい閾値は、異常と分類されたデータの中でHTTPステータスが500または503である場合に重みを付与し、加重平均を算出した結果です。
    ・新しい閾値:781.3846612433357
    新しい閾値を設定した場合の可視化結果は以下となります。



```python
time_prot(df, new_threshold, lebel_name='new_threshold', color='darkred', title='新しい閾値を設定した場合の response_time の時系列推移')
```


    
![png](output_61_0.png)
    



```python
# 新しい閾値を異常と分類した時の異常と分類したデータのstatus_codeの比率を確認する
res_plot_count(feature='status_code', title='status_code', df=df[df['response_time'] >= new_threshold], size=0.32)
```


    
![png](output_62_0.png)
    



```python
# すべての処理時間
end_time = time()

elapsed_time = end_time - start_time
print(f"簡易分析の処理時間: {elapsed_time}秒")
```

    簡易分析の処理時間: 2.0428388118743896秒



```python

```
