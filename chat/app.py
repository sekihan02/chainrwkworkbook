import os
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
plt.style.use('fivethirtyeight')
from flask import Flask, request, jsonify, render_template
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
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import torch
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig, pipeline
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MaxNLocator
from scipy import stats
from scipy.stats import norm

# from langchain.llms import OpenAI

# # LLMの準備
# llm = OpenAI(temperature=0.9)

device_num = -1 # CPU
if torch.cuda.is_available():
    device_num = 0 # cuda:0

with Timer(prefix=f'set model'):
    tokenizer = AutoTokenizer.from_pretrained(
        # "mosaicml/mpt-7b-chat"
        "./models/mpt-7b-chat"
    )
    
    config = AutoConfig.from_pretrained(
        # "mosaicml/mpt-7b-chat",
        "./models/mpt-7b-chat", 
        trust_remote_code=True
    )
    config.update({"max_seq_len": 4096})
    model = AutoModelForCausalLM.from_pretrained(
        # "mosaicml/mpt-7b-chat",
        "./models/mpt-7b-chat", 
        config=config,
        torch_dtype=torch.float16,
        trust_remote_code=True
    ).to("cuda:0")

    pipe = pipeline(
        "text-generation", model=model, tokenizer=tokenizer,
      max_new_tokens=256, device=device_num, torch_dtype=torch.float16
    )
    # LLMの準備
    llm = HuggingFacePipeline(pipeline=pipe)
# 疑似データ
def meke_df():
    # データ件数と異常値の数を設定
    data_size = 1000
    num_anomalies = 10

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
    return df
df = meke_df()


app = Flask(__name__, template_folder=".", static_folder="static")

messages = []

def create_image():
    sns.set(style="whitegrid")
    tips = sns.load_dataset("tips")
    ax = sns.boxplot(x=tips["total_bill"])
    img = BytesIO()
    ax.figure.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

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
    g.set_title("Number and percentage of {}".format(title))
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
    
    img = BytesIO()
    ax.figure.savefig(img, format='png')
    img.seek(0)
    # plt.show()
    return base64.b64encode(img.getvalue()).decode()


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
    
    img = BytesIO()
    ax.figure.savefig(img, format='png')
    img.seek(0)
    # plt.show()
    return base64.b64encode(img.getvalue()).decode()

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
    
    img = BytesIO()
    ax.figure.savefig(img, format='png')
    img.seek(0)
    # plt.show()
    return base64.b64encode(img.getvalue()).decode()

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
    
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    # plt.show()
    return base64.b64encode(img.getvalue()).decode()

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


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form["message"]
        if message == "画像":
            messages.append((message, "画像を出力します。", False, False))
            response = create_image()
            messages.append(("", response, True, True))
        elif message == "クリア":
            messages.clear()
        elif message == "plot":
            messages.append((message, "plotを出力します。", False, False))
            response = plot_dist3(df, 'response_time', '目的変数のデータ分布')
            messages.append(("", response, True, True))
        else:
            response = "Hello World!"
            messages.append((message, response, False, False))
    return render_template("template.html", messages=messages)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.get_json()["user_input"]
    
    response = "Hello World!"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0")
