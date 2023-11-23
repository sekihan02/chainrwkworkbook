# Audacityを使用して録音した音声ファイルmp3をWhisper + GPTで議事録書き出しとサマリ生成の実施

実験に使用している動画:

[【神々に愛された英雄】アルジュナの生い立ちとその時代／FGO×ゲームさんぽ#03](https://www.youtube.com/watch?v=VCbPdoaKTRo&t=1215s)(27:53)


```python
!python3 -m pip install --upgrade pip
```

    Requirement already satisfied: pip in /usr/local/lib/python3.10/dist-packages (23.3.1)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0m


```python
# !pip install openai==0.27.8
!pip install openai==1.2.3
```

    Collecting openai==1.2.3
      Downloading openai-1.2.3-py3-none-any.whl.metadata (16 kB)
    Collecting anyio<4,>=3.5.0 (from openai==1.2.3)
      Downloading anyio-3.7.1-py3-none-any.whl.metadata (4.7 kB)
    Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from openai==1.2.3) (1.7.0)
    Collecting httpx<1,>=0.23.0 (from openai==1.2.3)
      Downloading httpx-0.25.1-py3-none-any.whl.metadata (7.1 kB)
    Requirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from openai==1.2.3) (1.10.13)
    Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.10/dist-packages (from openai==1.2.3) (4.66.1)
    Requirement already satisfied: typing-extensions<5,>=4.5 in /usr/local/lib/python3.10/dist-packages (from openai==1.2.3) (4.8.0)
    Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<4,>=3.5.0->openai==1.2.3) (3.4)
    Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<4,>=3.5.0->openai==1.2.3) (1.3.0)
    Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<4,>=3.5.0->openai==1.2.3) (1.1.3)
    Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai==1.2.3) (2022.12.7)
    Collecting httpcore (from httpx<1,>=0.23.0->openai==1.2.3)
      Downloading httpcore-1.0.2-py3-none-any.whl.metadata (20 kB)
    Collecting h11<0.15,>=0.13 (from httpcore->httpx<1,>=0.23.0->openai==1.2.3)
      Downloading h11-0.14.0-py3-none-any.whl (58 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m58.3/58.3 kB[0m [31m1.4 MB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hDownloading openai-1.2.3-py3-none-any.whl (220 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m220.3/220.3 kB[0m [31m2.5 MB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hDownloading anyio-3.7.1-py3-none-any.whl (80 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m80.9/80.9 kB[0m [31m3.0 MB/s[0m eta [36m0:00:00[0m
    [?25hDownloading httpx-0.25.1-py3-none-any.whl (75 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m75.0/75.0 kB[0m [31m3.0 MB/s[0m eta [36m0:00:00[0m
    [?25hDownloading httpcore-1.0.2-py3-none-any.whl (76 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m76.9/76.9 kB[0m [31m3.9 MB/s[0m eta [36m0:00:00[0m
    [?25hInstalling collected packages: h11, anyio, httpcore, httpx, openai
      Attempting uninstall: anyio
        Found existing installation: anyio 4.0.0
        Uninstalling anyio-4.0.0:
          Successfully uninstalled anyio-4.0.0
    Successfully installed anyio-3.7.1 h11-0.14.0 httpcore-1.0.2 httpx-0.25.1 openai-1.2.3
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0m


```python
!pip install python-dotenv tiktoken
```

    Collecting python-dotenv
      Downloading python_dotenv-1.0.0-py3-none-any.whl (19 kB)
    Collecting tiktoken
      Downloading tiktoken-0.5.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
    Requirement already satisfied: regex>=2022.1.18 in /usr/local/lib/python3.10/dist-packages (from tiktoken) (2023.10.3)
    Requirement already satisfied: requests>=2.26.0 in /usr/local/lib/python3.10/dist-packages (from tiktoken) (2.31.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken) (2.1.1)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken) (1.26.13)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken) (2022.12.7)
    Downloading tiktoken-0.5.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.0 MB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m2.0/2.0 MB[0m [31m2.9 MB/s[0m eta [36m0:00:00[0m00:01[0m00:01[0m
    [?25hInstalling collected packages: python-dotenv, tiktoken
    Successfully installed python-dotenv-1.0.0 tiktoken-0.5.1
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0m


```python
# Release 20231117
!pip install git+https://github.com/openai/whisper.git@v20231117
# !pip install git+https://github.com/openai/whisper.git
#  (from sympy->torch->openai-whisper==20231117) (1.3.0)
```

    Collecting git+https://github.com/openai/whisper.git@v20231117
      Cloning https://github.com/openai/whisper.git (to revision v20231117) to /tmp/pip-req-build-zupnis8i
      Running command git clone --filter=blob:none --quiet https://github.com/openai/whisper.git /tmp/pip-req-build-zupnis8i
      Resolved https://github.com/openai/whisper.git to commit e58f28804528831904c3b6f2c0e473f346223433
      Installing build dependencies ... [?25ldone
    [?25h  Getting requirements to build wheel ... [?25ldone
    [?25h  Preparing metadata (pyproject.toml) ... [?25ldone
    [?25hRequirement already satisfied: triton<3,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (2.1.0)
    Requirement already satisfied: numba in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (0.58.1)
    Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (1.24.1)
    Requirement already satisfied: torch in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (2.1.0+cu118)
    Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (4.66.1)
    Requirement already satisfied: more-itertools in /usr/lib/python3/dist-packages (from openai-whisper==20231117) (8.10.0)
    Requirement already satisfied: tiktoken in /usr/local/lib/python3.10/dist-packages (from openai-whisper==20231117) (0.5.1)
    Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from triton<3,>=2.0.0->openai-whisper==20231117) (3.9.0)
    Requirement already satisfied: llvmlite<0.42,>=0.41.0dev0 in /usr/local/lib/python3.10/dist-packages (from numba->openai-whisper==20231117) (0.41.1)
    Requirement already satisfied: regex>=2022.1.18 in /usr/local/lib/python3.10/dist-packages (from tiktoken->openai-whisper==20231117) (2023.10.3)
    Requirement already satisfied: requests>=2.26.0 in /usr/local/lib/python3.10/dist-packages (from tiktoken->openai-whisper==20231117) (2.31.0)
    Requirement already satisfied: typing-extensions in /usr/local/lib/python3.10/dist-packages (from torch->openai-whisper==20231117) (4.8.0)
    Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from torch->openai-whisper==20231117) (1.12)
    Requirement already satisfied: networkx in /usr/local/lib/python3.10/dist-packages (from torch->openai-whisper==20231117) (3.0)
    Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from torch->openai-whisper==20231117) (3.1.2)
    Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from torch->openai-whisper==20231117) (2023.4.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken->openai-whisper==20231117) (2.1.1)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken->openai-whisper==20231117) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken->openai-whisper==20231117) (1.26.13)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken->openai-whisper==20231117) (2022.12.7)
    Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->torch->openai-whisper==20231117) (2.1.3)
    Requirement already satisfied: mpmath>=0.19 in /usr/local/lib/python3.10/dist-packages (from sympy->torch->openai-whisper==20231117) (1.3.0)
    Building wheels for collected packages: openai-whisper
      Building wheel for openai-whisper (pyproject.toml) ... [?25ldone
    [?25h  Created wheel for openai-whisper: filename=openai_whisper-20231117-py3-none-any.whl size=801358 sha256=bd88758e6f65fc841c40b679d8746aef42d1615922ab54516cdf0ca8079473ae
      Stored in directory: /tmp/pip-ephem-wheel-cache-xrybzu06/wheels/82/ef/3d/4c2e010696be8ff45a064a7629234956fc2c50b05bb9299d53
    Successfully built openai-whisper
    Installing collected packages: openai-whisper
    Successfully installed openai-whisper-20231117
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0m


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
from tqdm import tqdm
from pathlib import Path
```


```python
audio_file_path = Path('./data/fgo.mp3')
```


```python
# 入力音声の変換
import soundfile as sf
import librosa

y, sr = librosa.load(audio_file_path)
# リサンプリング
y_16k = librosa.resample(y, sr, 16000)
n_samples = int(15 * 60 * 16000)

# 音声ファイルを15分ごとに分割する
segments = [y_16k[i:i+n_samples] for i in range(0, len(y_16k), n_samples)]

# 分割した音声ファイルを保存する
with Timer(prefix=f'audio segmentation'):
    for i, segment in tqdm(enumerate(segments)):
        sf.write(f"./data/meeting_{i}.wav", segment, 16000, format="WAV")
```

    /tmp/ipykernel_43/3366858311.py:7: FutureWarning: Pass orig_sr=22050, target_sr=16000 as keyword args. From version 0.10 passing these as positional arguments will result in an error
      y_16k = librosa.resample(y, sr, 16000)
    2it [00:00,  3.02it/s]

    audio segmentation 0.666[s]


    



```python
# 音声処理: whisper
import whisper
import torch
import os

# 指定されたファイルの音声を文字起こしする関数
def generate_transcribe(file_path):
    # モデルの保存先を指定
    model_dir = Path('./model')
    # モデルの保存先指定
    os.environ['WHISPER_CACHE_DIR'] = str(model_dir)

    # モデル保存先のディレクトリが存在しない場合は作成
    model_dir.mkdir(parents=True, exist_ok=True)
    
    # GPUが利用可能か確認
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    
    # Whisper高速化テクニック
    # https://qiita.com/halhorn/items/d2672eee452ba5eb6241
    model = whisper.load_model('large', device=device)
    # モデルの処理を半精度浮動小数点数に設定して高速化
    _ = model.half()
    # モデルをCUDA（GPU）に移動
    # _ = model.cuda()

    # exception without following code
    # reason : model.py -> line 31 -> super().forward(x.float()).type(x.dtype)
    # Whisperモデル内のLayerNorm層を単精度浮動小数点数に設定
    # これを行わないと、型の不一致によりエラーが発生する
    for m in model.modules():
        if isinstance(m, whisper.model.LayerNorm):
            m.float()
    # 音声ファイルを文字起こし
    result = model.transcribe(file_path)
    return result
```


```python
# トランスクリプト（文字起こしテキスト）を初期化
transcript = ""
# 各セグメントを文字起こしする
with Timer(prefix=f'generate transcription'):
    for i in range(len(segments)):
        # 各セグメントのファイルパスを生成
        file_path = f'./data/meeting_{i}.wav'
        # 文字起こしを実行
        transcribe = generate_transcribe(file_path)
        # 文字起こし結果の各セグメントからテキストを抽出し、トランスクリプトに追加
        for seg in transcribe['segments']:
            transcript += seg['text'] + "\n"
```

    100%|█████████████████████████████████████| 2.88G/2.88G [47:58<00:00, 1.07MiB/s]
    /usr/local/lib/python3.10/dist-packages/torch/nn/modules/conv.py:306: UserWarning: Applied workaround for CuDNN issue, install nvrtc.so (Triggered internally at ../aten/src/ATen/native/cudnn/Conv_v8.cpp:80.)
      return F.conv1d(input, weight, bias, self.stride,


    generate transcription 3159.078[s]



```python
import openai
from openai import OpenAI
import tiktoken
from dotenv import load_dotenv
load_dotenv()


def completion(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",  # モデルの指定
        messages=[
            {"role": "system", "content": "You summarize the transcript of the meeting."},
            {"role": "system", "content": "Outputs should be generated in step by step."},
            {"role": "user", "content": f"{text}"}
        ],
        temperature=0.8,
    )
    return response.choices[0].message.content
```


```python
import json
def create_prompt(transcript):
    return f"""以下は、ある会議の書き起こしです。

{transcript}

この会議のサマリーを作成してください。サマリーは、以下のような形式で書いてください。

- 会議の目的
- 会議の内容
- 会議の結果

サマリー:
"""
```


```python
import json
def create_prompt_act(transcript):
    return f"""以下は、ある会議の書き起こしです。

{transcript}

この会議の次にするアクションを作成してください。アクションの記述は以下のルールに従ってください。

・リスト形式で出力する (先頭は - を使う)
・簡潔に表現する

アクション:
"""
```


```python
with Timer(prefix=f'create_summary'):
    prompt = create_prompt(transcript)
    summary = completion(prompt)
```

    create_summary 31.651[s]



```python
with Timer(prefix=f'create_action'):
    act_prompt = create_prompt_act(transcript)
    action = completion(act_prompt)
```

    create_action 31.507[s]



```python
print(transcript)
```

    じゃあ彼らに続きまして
    アルジナの方も見ていきたいと思います
    お願いします
    はい
    召喚の方から一旦流させていただきます
    はい
    サーバント
    アーチャー
    アルジナと申します
    マスター
    私を存分にお使いください
    はい
    という感じで
    こちらもちょっと言葉は少ないですけども
    だいぶなんかいい人感というか
    精錬な感じはやっぱりします
    真面目そうなね
    はい
    マテリアルの方でも
    至って勤勉
    精錬
    光明
    盛大
    火の打ち所のない完璧な人格
    みたいな風な説明がされてますね
    沖田さんとかアルジナとか
    今回FGOで見て
    どういうところとか注目しますか
    肌の色が
    黒いのが
    アルジナは色黒だっていう接点
    原点ではなんでいるので
    そこを多く見とって
    描かれているのかなっていうのと
    黒っていうのは
    マハーバーラタの中で
    すごく重要な意味を持っていて
    クリシュナで黒っていう意味なんですけど
    マハーバーラタにクリシュナが3人出てきて
    一人がいわゆるクリシュナ神のクリシュナですけど
    もう一人がマハーバーラタの作者とされる
    ビアサセンがクリシュナっていう名前もあるんですね
    もう一人がドラウパディの別名が
    クリシュナーって言うんですけど
    最後の語尾を伸ばして女性系にするんですが
    3人クリシュナがいるって言うんで
    黒の女子子って言ってもいいようなところがあって
    アルジナもクリシュナと二人で
    クリシュナウって呼ばれて
    二人のクリシュナって呼ばれるぐらいだから
    黒っていうのがやっぱり重要なところかなって
    思いました
    そういう意味でやっぱり
    全体的に黒い感じがあると
    天竺さんとかどうですか
    もうねやっぱりね
    顔がいいっていう
    2回目
    こういう言い方あんまりしたくないんですけど
    でも本当に顔がいい
    スタイリングで着込んでいくじゃないですか
    これが今第一なんですが
    第二とかだと
    そう服が増えるのがね最高ですね
    増えるのが最高
    ね最高です
    第三とかになると
    うんそう何度ついちゃうんですよ
    かっこいいみたいな
    頭像的な話で気になるところとかありますか
    やっぱり持ってる弓と矢ですよね
    それはさすがアルジナだな
    弓といえばやっぱりアルジナ
    アルジナですよね
    ガンディーバですよね
    そうそう
    あれ又貸しなんですよ
    また貸し
    あのねアグニシンがアルジナに与えるんだけど
    本来の持ち主はバルナシンって言うんで
    そう海の神様
    海の神様
    神様又貸ししてる
    バルナシンが海底の宮殿に宝物庫を持ってて
    そこにガンディーバが納められているんですけれども
    それをアグニシンが借りて
    それをアルジナに与えたってことになってるので
    実はバルナの持ち物なんですよ
    なるほど
    ちなみにこの宝具の名前がアグニガンディーバっていう
    弓の名前ですね
    アルジナが持ってるやつが
    なのでなんか名前的に明らかにアグニのものかと思ってたんですけど
    違うという
    本来はバルナシン
    私とのはアグニだけど本来はバルナシン
    筆記の絵で見るとまたちょっとなんか細かい装飾とかが増えてきてる感じですね
    アルジナ
    これ第3でこれ第2第1
    なんか後ろにまた
    蓮っぽいものがやっぱりありますね
    仏教とかもそうですけど
    蓮ってさっき太陽や未明みたいなのがあると思うんですけど
    それ以外に池とかにも植え付けたりするじゃないですか
    蓮って世界そのものの例えでもありますね
    眠ってるヴィシュヌ神のへそから蓮の花が生えて
    そこにブラフマン神が乗っかってるっていう図像があると思うんですけど
    それってブラフマンが創造神だから
    蓮の上にこれから世界を創造する
    っていうところなんですね
    蓮は世界の例えだと思います
    泥の中からあんなに綺麗な花を咲かせるから
    それだけで聖なるものであるっていうね
    そういう意味合いももちろん蓮の花自体にあるんですけれども
    蓮の花ってそもそもそういうなんていうんですか
    ルマチ
    ルマチそうそうそう
    そういうところから美しい花が咲くっていうのもあるし
    花が開いた状態ってやっぱり
    その太陽の光そのものでもあるので
    聖なるものとして
    今でも神様にお供えしたりとかもね
    普通に蓮の花とかもしますけど
    多分泥っていうのが世界の始まりの時の混沌を表してるんですね
    なるほど汚いとかじゃなくて
    混沌ですね
    そこから蓮が生えてそれが世界になっているね
    ちなみにカルナとの対比で
    結構青色と白のイメージがあるというのは強いなと思うんですけど
    そういうところって何か
    インド神話的な意味合いとかってあったりするんですか
    色で言うとさっき
    太陽神はルビーだって話をしたじゃないですか
    インドラはサファイアなんですよ
    そういうことなんですね
    インドラの青サファイアの色
    そういう風に言われることはありますね
    あとは青っていうのは
    クリシュナって黒って言ったんですけど
    その青はカルナっていうのかな
    黒と青っていうのがすごく近いところにある
    紺色っていうのはね
    そのサファイアの青っていうのはすごい聖なる色ではあるので
    カルナさんのルビーの赤とサファイアが
    元々けどコランダムだから一緒の鉱石ですよね
    色は違うだけなので
    なんかすごく色合い的に
    本当に兄弟って感じでいいなっていうのは
    なんとなく思いました
    確かアルジナって白っていう意味じゃなかったっけ
    アルジナ自身は白です
    言葉がね
    そうそうそう
    白を意味してるんですよ
    そうそうでも肌は黒いんですよ
    そうそうそう
    そう聞くと黒の序詞っていう意味合いも含まれつつ
    アルジナ本来の意味合いも含まれつつ
    インドラの色の様子が入ってるんですよね
    入ってるっていう
    そういうカラーリングなんですよ
    じゃあちょっと早速プロフィールの方も見ていきたいと思います
    インド古代ジョジシーマハーバーラタの大英雄
    マハーバーラタはインドのあらゆる英雄が集結する
    絢爛なる物語であるが
    アルジナはその中心に位置する存在と言っても過言ではない
    という感じですね
    はいその通りですね
    なんか聞こうかなと思ったら
    主人公っていうのはやっぱ存在するんですか
    一応やっぱりねアルジナでいいんだと思うんですよ
    そこのアルジナね
    そうアルジナですね
    それは一番出演多いってことですかマハーバーラタ
    そういう意味合いではないかと
    ほんとねちょっとニュアンスが違うかもしれないですけど
    出演回数ね
    さっきカルナの話聞いても
    カルナはもう主人公レベルのストーリーを持ってるじゃないですか
    ただストーリーの多さっていうのでは
    あのもう全然桁違いですね
    桁違いに多い
    出演回数っていう風に言うと
    マハーバーラタの中で
    アルジナの方が圧倒的です
    圧倒的に描写が多い
    それはもうアルジナとカルナっていうその比較だけじゃなく
    他の英雄たちも含めて圧倒的ってことですか
    そうですね
    じゃあやっぱ人気はあるってことですね
    うんむちゃくちゃ人気はありますねやっぱり
    さっきすいません
    カルナを経たせいで
    だいぶその株が
    カルナの株が上がりすぎてる結果
    カルナが上がってきた
    いい話とか聞けたらなっていうところなんですけど
    ちょっとプロフィール読みながらまた進められたらと思います
    でちょっとパラメータ的な話で言うと
    さっきあの
    カルナの方がだいぶ候補が低かったのに対して
    アルジナはだいぶ高いという感じで
    差別化されてる感じはしますね
    何気に運はいいですよね
    カルナはね
    てかクリシュナがついてるから
    ああ神がついてるから
    神がねついてるから
    前世で二人はね仲良しなんですよ
    ナラとナラヤナですね
    うん二人は
    前世から繋がりはあるので
    このマハーバーラタの子の時には
    そのそれぞれ別の存在ですけど
    前世からの繋がりはあるので
    一緒に仲良く
    森を燃やしてみたりとか
    それは大丈夫なんですか
    アグリに言われてね
    森燃やしちゃうんだよね
    これ何の意味があるんだろうって
    ずっと思ってて起きた説なんですけど
    その森焼きを生き残った動物たちが
    7名なんですね
    そしたらマハーバーラタの大戦争で
    パンダ場側で生き残ったのが
    7名なんですよ
    ご兄弟とクリシュナと
    あとクリシュナの親友のサーティアキっていう
    英雄なんですけど
    だから森焼きが大戦争の予兆になってるのかな
    と思って
    だからその戦争の残酷さとか
    そういったものをちょっと示しているのかな
    って思ったりしています
    確かに数字的には一致してますし
    ゲーム内のスキルとかで
    授かりの英雄って言われ方を
    アルジナはされてるんですが
    やっぱり生まれ持って
    そういう神との繋がりとか
    味方してくれてるって意味では
    やっぱりカルナとの差を感じるところがありますね
    そうですねもう生まれながらの英雄のようなものがあるんですけど
    そうですねもう生まれながらの英雄のようなものがあるんですけど
    生まれながらの王子様で
    インドラって言ったら
    古代インドの時代ではトップなんですよね
    神々の王っていうのはインドラなので
    めちゃくちゃ強いパワーを持っていた存在なんです
    ヒンドゥイ教の時代になると
    その役割をビシュヌとかシワとかが受け継いでいくので
    インドラの地位自体は若干下がってるんですけど
    古代でいくと
    マハバラというよりもっと昔の段階の聖典なんかだと
    インドラが一番っていう
    そういう神様の息子ではあるので
    そういう意味で
    神の中の神というか
    そうですね神々の王の子供っていう意味では
    かなりの力を持ってても当たり前かなみたいな
    で先ほども出てきたアイヨンの意味は
    ガーン・ディーバ・エンジン・アクニから授けられた神宮であると
    これはもらった時のエピソードとかはあるんですか?
    森明のさっきの
    さっきの時にこれを使ったってことですか?
    アグニ神が森明をクリシュナとアルジュナに依頼した時に
    じゃあ武器くれって言うんですね二人が
    なるほど
    じゃああげましょうっていうんで
    ガーン・ディーバをアルジュナに与えて
    クリシュナには武器のエンバ・チャクラを与えるっていう場面ですね
    またがせる意味はここで
    ここで使われたってこと?
    なるほど
    森焼くのにだいぶいいのもらってますね
    ただ森を焼くっていうよりも
    アグニっていうのはモノの神様なんですけど
    古代インドなんかではアグニが食べたものが浄化されるんですね
    で浄化されてその天に昇っていくっていう
    要は清めのアイヨコミが食べることがあるんですよ
    要は清めのアイヨコミが食べることがあるんですよ
    だからそのアグニが食べたいって言ってるから
    じゃあアグニにあげましょうっていう
    穀物をあげましょうみたいな感じなので
    食べてるってことなんですね燃やしてるって
    そうですね
    日本だとゴマ仏教だから
    ゴマで火炊いていっていろいろ投げてる
    あれも元々はインドのバラモン教の儀式のホーマっていうのから
    ゴマっていうのも来てたりして
    燃やしながらそこにその穀物を与える
    インドの人はそのゴマを使って
    ゴマの花を作って
    その花を作って
    その花を作って
    その花を作って
    その花を作って
    その花を作って
    インドのなんかだと火の中に投じることで
    それが燃やされて天に行くので
    それが儀式の一つになってるみたいな
    アグニ神は自然の火の神というよりは
    祭歌なんですよね
    祭式の火なんですよね
    穀物を与えて神々にそれを届けて
    神々にお話を聞いてもらうとか
    そういう意味ではその森ごとアグニに捧げられたみたいなね
    ただ山火事とは全然違うわけですよね
    火の意味が
    だからアグニに頼まれて
    だからアグニに頼まれて
    だからアグニに頼まれて
    火が焼かれたら燃やすしかないよねみたいな
    でも確かインドラが
    インドラがやってきて
    タクシャカ竜王が逃げてきて
    インドラに頼んで
    アルジュナとインドラと戦うけど
    インドラがアルジュナ息子の武勇に満足して
    じゃあもう好きにせよみたいな感じで
    天下に帰っていくっていう
    アルジュナとインドラ戦うんですね
    親子同士の戦いが
    アルジュナの一つの試練だと思うんですけど
    アルジュナは父神インドラとも戦ってるし
    あとシバシンとも
    シバシンが山岳民のキラータっていうのに変身した時に
    それと戦って負けるんですけど
    とにかく戦ったっていうんで
    シバシンから祝福を受けて武器を授かる
    資格を得るっていう場面もあります
    なんか試練を確かに受けつつも
    なんかエリート教育されてる感はありますね
    神との繋がりがすごい密接な感じがするね
    そうですね
    ちょっとプロフィール2の方も
    カルナが施しの英雄であるならば
    アルデナこそは授かりの英雄である
    クル王の息子
    ファーン・ダマ五兄弟の三男として生まれた彼は
    同時に雷神インドラの息子でもあった
    あのカルナが太陽の子で
    インドラは神々の王だけど
    自然現象としては雷雨なので
    アルジュナとカルナの対立っていうのが
    自然現象としては太陽とそれを覆い隠す雷雨っていうイメージなんですね
    そこでも因縁があるって感じですね
    そうですね
    二人の因縁というよりは神々のところの因縁
    そうですね
    太陽とね雨だからねっていう
    両立はしない二つです
    そういうことになります
    だからカルナの時にも申し上げたように
    カルナかアルジュナかどちらか一人が残るっていうのは
    そういう太陽と雷の対立をも表すかもしれない
    確かに確かに
    授かりの英雄っていう感じで書かれてますが
    何かといいことが多い感じなんですかアルジュナさん
    カルナに比べたらそりゃあぜぇー
    いやーもう
    いやーもう
    いやーもう
    じゃあちょっと次もいければと思うんですが
    その器量性格あらゆる面でまさに火の落ちる所ない英雄であった彼は
    兄が賭け事に敗北したことによって国を覆われることになる
    この時すでに彼の中でカルナとの対決が不可避であるといい予感があった
    何しろカルナはパンダ場ご兄弟を知的と睨む
    ドゥルヨーナラを父と仰いでいたからだ
    という感じで
    兄が賭け事に敗北したことによって国を覆われることになるんですよ
    という風にも書かれてるんです
    これもエピソードがまたあるんで
    ユディンシュテラの唯一の欠点が
    賭け事に
    賭け事好きだからもう
    お兄ちゃんやっちゃったみたいなもん
    イカサマ賭博でやられちゃって
    亡国も弟たちも取られて
    妻のドラウパディも最後に取られてしまう
    だいぶ大きなもの賭けだった
    もうね賭け事はねダメ
    賭け事はしちゃいけないっていう教訓だと思うこれは
    シンプルに
    でもね
    神話的には意味があって
    ゲームね
    それ自体が世界の運行を表しているんですね
    ユディンシュテラは王なので
    王の宿命として賭け事を行わなければならなかった
    それはその世界を動かすっていう意味があって
    これから破滅に向かっていく世界なので
    破滅に向かっていく世界っていうのは
    インドに宇宙的な4つの時代区分があって
    クリタユガ
    トレーターユガ
    ドゥバーバラユガ
    最後にカリユガってあるんですけど
    ちなみに現代はカリユガです
    最悪の時代です
    悪くなっていきます
    3つ目のドゥガパラユガからカリウガに移る
    その時にクルクシェイトラの戦争が行われます
    実際にはクリシュナが死んで
    その時にカリウガが始まるってされてるんですね
    時代の推移をこの神話全体が表しているわけなんですよ
    そこでユディシュトラが行う
    宇宙の運行を示す掛け事っていうのは
    そういう神話的な意味合いがあるんですね
    この時すでに彼の中でカルナとの対決が不可避であるという予感があったみたいな
    ちょっとこれは運命的な話ではあると思うんですけど
    こちらはゲームのオリジナルの優れた部分だと思いますね
    掛け事でカルナは別に参加してなかったってことですか
    その場所にはいて
    ドラバリーが服を剥ぎ取られようとされて
    領収されるという場面があるんですけど
    そこにカルナも居合わせていたので
    同罪ですよね
    同罪です確かに
    ドラバリーは
    その事件以来ずっと夫たちに戦争を起こして
    すぐにでも王位を奪還しなさいって言うんだけど
    ユディシュトラが法にかなった行動をするべきだって言って
    戦争を避けようとするっていうのがベースにあります
    パンダバ五兄弟たちは別にそんな戦争は望んでないって感じなんですね
    放浪して13年間約束通り過ごして戻ってきて
    王国の半分を受け取るっていうことで
    納得していたっていうことになっています
    追い出されて国からね
    追い出されていろんなところ行って
    あれやこれやしてるんですけど
    でもね戻してくれなかったんですね
    結局そこで
    トリオダナはね
    嫌だって言ったんですよ
    僕たち13年放浪して
    約束通り色々やったのに
    今返さないって何事っていうのがあって
    それでじゃあお前たちパンダバ五兄弟に就く
    それともクル族に就く
    どっちに就くよみたいなので
    いろんな国がこう色々
    言い出してクル族対パンダバ大戦争みたいな
    なるほどそこで戦争が
    そうする始まるという感じですよね
    プロフィール5なんですが
    カルナを殺さなければならないと決意したのは
    いつからだったか
    多分最初に顔を合わせた時からだろう
    それは神々によって定められた運命ではない
    アルジナが順善たる敵意と共に選んだ業である
    たとえ正しくなかったとしても
    アルジナはそれをやり遂げなければならなかったのだ
    という風に書かれていますね
    うん
    すごいよねこのね
    二人の因縁みたいなものね
    物語作ってるのすごいね
    そうですね
    原点どうのっていうよりも
    そのゲームの中で
    こういう魅力的な設定にできてるっていうのが
    私すごく好きだなって思います
    ちょっとここでそのゲーム内のアルジナと
    カルナの描かれ方みたいな話で言うと
    アルジナが最後のカルナを殺す時の
    考察に近いって
    多分カルナの文面では分かると思うんですけど
    それに対しての後悔を
    なんかすごい
    ちょっと抱いてるっていう感じで
    ゲーム内では出てくるって感じですね
    ルール的には多分
    あまりよろしくないことをやってしまったっていう
    ところですごい後悔してるって描写が多いですね
    なのでカルナとの正式な戦いはやっぱり望んでるという
    一応そのゲーム内でもそういうの望んで召喚されてるっていう
    多分だからこのゲームの中では
    アルジナの心残りっていうところになってるんですよね
    あのカルナの倒し方っていうのがね
    うん
    確かに今の価値観で言うと
    若干確かに引き押しで引き押しで言うと
    じゃないですか
    最後のやり方っていうのは
    それってなんかその当時の人たちというか
    読んでた人たちはなんかどういう受け止め方をする?
    いや当時も卑怯ですよ
    ちょっと言い方によるかもしれないけど
    基本的に戦ってる時に
    待ってくれって言われてるところに
    その矢を追いかけたりするのは
    あれあんまりよろしくないことではあって
    結局その戦争の話なので
    ハーバーアラタは
    色々やっちゃいかんことをしていくわけですよね
    あの最後のその戦争のところではね
    今まで正義だってずっと言ってた
    そのユディシティは
    もうしんどいことになっていくわけじゃないですか
    なんかねあのユディシティの戦車が
    ずっと地上から少し浮いてたんですよ
    それはユディシティが真実の人だから
    地面に触れなかった
    嘘つかない
    彼は嘘つかないってね
    嘘をついてしまったんですね
    あのドローナっていう将軍を殺す時に
    ドローナの息子のアシュバッターマン
    アシュバッターマンが死んだっていう嘘をついたんですよ
    それはビーマが
    アシュバッターマンっていう名前の象を殺して
    ああ
    それについて言及するのに
    小さく象のアシュバッターマンが死んだ
    それめっちゃ面白いですよね
    言ったんですよ
    それでその時ユディシティラは
    生まれて初めて嘘をついた
    で戦車が地面についた
    小さくは言ってますけど
    小さくは言ってるけど
    やっぱりそこね
    やっぱり意図がね明らかだから
    騙そうっていうことですね
    騙そうとして
    ドローナがもう全てを諦めて
    ヨーガに入って死んだっていう話になるので
    うん
    だからもうすごい殺されちゃったって
    そう思い込んじゃって
    うん
    もうあの戦争不義
    抗議しちゃうんですよねもう
    うん
    もう何もしないみたいな感じで
    そこでね彼は終わりでみたいな感じで
    はい
    正義サイドで描かれがついたこのパンダバー側も
    やっぱりそういうこと
    最後その戦争のシーンだと
    そのやっちゃいけないって言われてるところを
    あえてやってしまうような
    ビーマなんかもそうですよね
    うん
    ダラマっていうのがすごく重視されるんですけど
    こうですね
    はい
    法律の方っていうよりは
    もっと広い概念なんですけれども
    結構そのダルマの乱れ
    うん
    時代の推移の話をしましたけれども
    時代が悪くなっていくので
    なるほど
    ダルマが乱れていく
    はい
    それをパンダバーの正義の揺らぎみたいな形で
    現れているのかなって思ってます
    この英雄たちも抗えない部分というか
    そうですね
    乱れてたりする
    大きな時代の流れの中で生きている
    半身の英雄たちですから
    うん
    最後ちょっと宝具だけ見れればと思ってます
    パーシュパタっていうのは
    パシュパティに属するっていう意味なんですね
    パシュパティっていうのがシバです
    家畜の主っていう意味で
    シバのことですね
    シバの武器っていう意味になります
    こうやってね
    マハバラタナイとかで
    なんかもらうみたいな話が多分ありました
    確かね
    調べましたね
    ありました
    ありましたね
    ありました
    戦争中にね
    シバのとこ行っていいんですよね
    シバと戦争前に戦ってもらったやつは
    プラフマシラスですよね
    そうだね
    そうだね
    プラフマシラスですよね
    本当にいろいろもらってますね
    いろいろもらってますね
    強い武器
    その後
    戦争中にね
    クリシュナと一緒に
    シバのとこ行ったんじゃないかな
    違ったかな
    うん
    ちゃんと自分で書いてある
    戦争のね
    14日目
    18日間戦争があるんですけど
    その14日目に
    アルジュナはシバ神の必殺の武器を授かるため
    クリシュナとともに
    シバ神の神的な住処へ行き
    そこで武器
    パーシュパタを習得した
    はい
    ちゃんと自分で書いてました
    習得したってニュアンスは
    技みたい
    道具というか技
    そうなんですよ
    ちょっとね
    イメージしづらいんですけど
    プラフマシラスっていうのも
    多分そうなんですけど
    弓に継がれる神的な何かなんですよ
    何か
    飛び道具というか
    なんというか
    魔術的なものなんですけど
    矢なのか何なのかみたいな
    そうですね
    でもとにかく強い
    めちゃ強武器です
    そうですね
    まあ
    シバ様
    自体が一応
    世界破壊しちゃう神様なので
    まあその神様の武器だったら
    世界ぐらい滅ぼしちゃうかもみたいな
    そう
    そういう
    じゃあちょっと映像の方も
    すっかくなんで
    見れればなと思います
    神聖領域かけ
    空間固定
    神話執行機器
    ついてる
    全承認
    シバの怒りをもったり
    なんじらの命をここで断つ
    パーシュパタ
    スゴイ
    あはっ
    スゴイ
    スゴイスゴイ
    はい
    という感じで
    多分ゲーム中でもそのなんか強力な描写みたいなのが
    まあストーリーとかも出てきて
    みんな退避しないと巻き込まれるとか
    あとだから使ったらもうやけの腹になって
    完全に何もなくなっちゃってるみたいな話もあるので
    まあそれほどやっぱり強力な武器として
    まあゲームでも描かれてるって感じですね
    結構夢もあってもね
    ここはパシパタなんだよ
    あみたいだね
    確かに
    そうなんだみたいなね
    さっきの話で使えるのが
    使える何かっていうと
    弓で発出してもいい感じもちょっとありますよね
    多分だから
    パーシュパタ多分そのまま使ったら
    世界滅びると思う
    物理的に多分世界が滅びるので
    一部だけ凝縮してんのかなみたいな
    確かに本気出したらもう
    本気出して使ったら多分ヤバいことになるんで
    ゲームが終わっちゃう
    ゲーム終わる
    そのまま
    世界が終わるぐらいでね
    このパーシュパタとかそのマハバラじゃないでは使われたりはするんですか
    ブラゴマシラスは最後のシーン
    アシュバッターマンと
    アシュバッターマンとの戦いのところでは使うんですけど
    ブラゴマシラスってのはどういうものなんですか
    ブラゴマシの頭っていう意味で
    詳細がよくわかってないんですよ
    インド神話研究してる河村祐人先生って方が
    最近ブラゴマシラスで神話学研究会ってとこで発表してくださったんですけど
    ちょっと詳細不明なんですよ
    謎なんですねそれは
    でどこがどういう風に不明なのかっていうのを
    先生が明らかにしてくれたんだけど
    アルジュナーとアシュバッターマンが
    それを
    お互いに持ってるんです
    お互いに出すんですけど
    アルジュナーはその先生たちの声を聞いて
    引っ込めることができたんですよ
    一旦出したブラゴマシラスを回収することができた
    フェイントみたいな感じですね
    フェイントっていうちょっとニュアンスが違うかもしれないけど
    アシュバッターマンにはその力がなかった
    つまり武器を出すことよりも回収することの方が大変なんですね
    ということになっていて
    でアシュバッターマンは消せないので
    パンダバの妻たちの腹にそれを放った
    でどういうことになるかっていうと
    その胎児がみんな死んで
    パンダバの家系が絶えることになる
    っていうことなんですけど
    結局クリシュナの助力で一人だけ蘇生して
    それが応答に繋がっていくっていう話ですね
    ちょっとパーシュバッターがどこで使われているのかは
    ごめんなさい今わからないです
    ただ強力であるのは間違いないですね
    そうですね
    ブラゴマシラス
    アルジュナー結局使ったんですか?引っ込めて?
    引っ込めました
    引っ込めただけで使わない
    結構そのなんだろう
    マハバラタの中にいろんな武器が出てくるんですけど
    ブラゴマシラスが最強って言われて
    最強っていうのから
    多分どれも強いんですけど
    ヤバさ的にものすごいヤバいみたいな
    でそれをアシュバッターマンとアルジュナーが
    両方めっちゃヤバ武器ぶつけたら
    それこそ本当世界は滅びちゃうんで
    ちょっとやめてみたいな話になった時に
    アルジュナーは分かりましたってできたけど
    アシュバッターマンはそれを引っ込めることができなかった
    意味合いで引っ込めたんですねアルジュナーは
    止められてますもんね
    ちょっとそれさすがにヤバいからやめとこうみたいな
    すごい衝撃が全部無くなっちゃう
    すごいことになっちゃうので
    でもアシュバッターマンは止められなかったからって話ですね
    結局武器を放ったっていう
    あごめんなさい
    いいですよね
    ザルさん
    なんかアルジュナーの別例として
    ちょっとこの物したやつがあったり
    旗印がサルさん
    そうそうこのサルさんはそれですよね
    アルジュナーの
    旗の
    そうなんですね
    戦争の時に旗をみんな掲げるんですけど
    それぞれ旗の模様が
    それこそサルの神ってインドにいます
    ハヌマンですね
    ハヌマンとかそうですよね
    別にマハーバラタニアが出てこないんですか
    ハヌマン出てきます
    出てきます
    ハヌマンは出てきますね
    ビーマの試練の時に
    ビーマがドラウパディにねだられて
    神の花を取りに
    クベラ神の庭園ってとこに行くんですけど
    そこでハヌマンに出会って
    最初はサルだったんですけど
    そこでハヌマンがドラッガーってバカにするんだけど
    実は兄であって
    兄なんです
    同じ梅雨神を父としているので
    それでハヌマンに併伏して
    あなたの真の姿を見たいって言ったら
    ハヌマンすごい大きな姿になって
    神としての姿を現したっていう
    ような場面があります
    なるほど
    ビーマ編でちょっと出てくる
    そうですね
    せっかくビーマの話ができたので
    ビーマ軽く見てコメントいただきます
    それではまた
    



```python
from IPython.display import display, Markdown, Latex

display(Markdown("## Summary\n\n" + summary + "\n\n## Action\n\n" + action))
```


## Summary

会議の目的:
この会議は、FGO（Fate/Grand Order）というゲームに登場するキャラクター「アルジュナ」についての深い理解と、その背景にあるインド神話の知識を共有することを目的としています。

会議の内容:
- アルジュナのキャラクター紹介と彼のサーヴァントとしての役割の説明。
- アルジュナの人物像とマテリアル（ゲーム内の設定資料）に記述されている性格、外見、武器に関する情報の共有。
- アルジュナの肌の色の意味と、インド神話「マハーバーラタ」における黒い肌の重要性についての論議。
- インド神話におけるアルジュナのエピソードや、彼の神々との関係、特にクリシュナとの関係についての議論。
- アルジュナと対照的なキャラクターであるカルナについての比較と、両者の関係性の検討。
- アルジュナの武器である「パーシュパタ」などの神話上の武器の説明とゲーム内での表現についての考察。
- ゲーム内でのアルジュナのプロフィールや彼のストーリー上の役割に関する詳細な読み解き。

会議の結果:
- アルジュナに関する詳細な情報が共有され、参加者間での理解が深まった。
- ゲームとインド神話との関連性が議論され、キャラクターの背景が明らかになった。
- アルジュナが「授かりの英雄」として、彼の神々との結びつきが非常に強いことが強調された。
- アルジュナとカルナの対立は、ゲーム内外で重要なテーマであり、その対比が詳細に分析された。

## Action

- 神話学の専門家にアルジュナの背景やエピソードに関する詳細な分析や解説を求める。
- ゲームのシナリオライターと協力して、アルジュナとカルナの関係性をより深く探るストーリー展開を考案する。
- アルジュナが使う武器やその背景に関する追加リサーチを行い、正確な情報を得る。
- マハーバーラタにおける他のキャラクター、例えばハヌマンやビーマについても研究し、関連するエピソードを紹介する。
- ゲーム内でアルジュナの旗印やモチーフとなるサル（ハヌマン）についての説明やエピソードを追加する。
- アルジュナのプロフィール、特に『授かりの英雄』としての部分をさらに詳細に展開する。
- アルジュナの道徳的ジレンマや彼が直面した試練について、より深く掘り下げる。
- ゲームのビジュアルデザインチームと連携し、武器や衣装の細部にまで神話の要素を反映させる。
- プレイヤーがアルジュナのバックストーリーや神話への理解を深められるような追加コンテンツを作成する。



```python

```
