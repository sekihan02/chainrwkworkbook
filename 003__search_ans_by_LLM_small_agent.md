![](./search_small_agent.png)


```python
!python3 -m pip install --upgrade pip
```

    Requirement already satisfied: pip in /usr/local/lib/python3.10/dist-packages (24.0)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0m


```python
!pip3 install arxiv==2.1.0
!pip3 install python-dotenv tiktoken
# !pip install openai==0.27.8
# !pip install openai==1.2.3
!pip install openai==1.3.4
!pip install -U duckduckgo-search==4.4
```

    Requirement already satisfied: arxiv==2.1.0 in /usr/local/lib/python3.10/dist-packages (2.1.0)
    Requirement already satisfied: feedparser==6.0.10 in /usr/local/lib/python3.10/dist-packages (from arxiv==2.1.0) (6.0.10)
    Requirement already satisfied: requests==2.31.0 in /usr/local/lib/python3.10/dist-packages (from arxiv==2.1.0) (2.31.0)
    Requirement already satisfied: sgmllib3k in /usr/local/lib/python3.10/dist-packages (from feedparser==6.0.10->arxiv==2.1.0) (1.0.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests==2.31.0->arxiv==2.1.0) (2.1.1)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests==2.31.0->arxiv==2.1.0) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests==2.31.0->arxiv==2.1.0) (1.26.13)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests==2.31.0->arxiv==2.1.0) (2022.12.7)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mRequirement already satisfied: python-dotenv in /usr/local/lib/python3.10/dist-packages (1.0.1)
    Requirement already satisfied: tiktoken in /usr/local/lib/python3.10/dist-packages (0.6.0)
    Requirement already satisfied: regex>=2022.1.18 in /usr/local/lib/python3.10/dist-packages (from tiktoken) (2023.12.25)
    Requirement already satisfied: requests>=2.26.0 in /usr/local/lib/python3.10/dist-packages (from tiktoken) (2.31.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken) (2.1.1)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken) (1.26.13)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.26.0->tiktoken) (2022.12.7)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mRequirement already satisfied: openai==1.3.4 in /usr/local/lib/python3.10/dist-packages (1.3.4)
    Requirement already satisfied: anyio<4,>=3.5.0 in /usr/local/lib/python3.10/dist-packages (from openai==1.3.4) (3.7.1)
    Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from openai==1.3.4) (1.7.0)
    Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.10/dist-packages (from openai==1.3.4) (0.26.0)
    Requirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from openai==1.3.4) (1.10.13)
    Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.10/dist-packages (from openai==1.3.4) (4.66.1)
    Requirement already satisfied: typing-extensions<5,>=4.5 in /usr/local/lib/python3.10/dist-packages (from openai==1.3.4) (4.9.0)
    Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<4,>=3.5.0->openai==1.3.4) (3.4)
    Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<4,>=3.5.0->openai==1.3.4) (1.3.0)
    Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<4,>=3.5.0->openai==1.3.4) (1.2.0)
    Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai==1.3.4) (2022.12.7)
    Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai==1.3.4) (1.0.2)
    Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai==1.3.4) (0.14.0)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0mRequirement already satisfied: duckduckgo-search==4.4 in /usr/local/lib/python3.10/dist-packages (4.4)
    Requirement already satisfied: docstring-inheritance>=2.1.2 in /usr/local/lib/python3.10/dist-packages (from duckduckgo-search==4.4) (2.1.2)
    Requirement already satisfied: click>=8.1.7 in /usr/local/lib/python3.10/dist-packages (from duckduckgo-search==4.4) (8.1.7)
    Requirement already satisfied: curl-cffi>=0.6.0b7 in /usr/local/lib/python3.10/dist-packages (from duckduckgo-search==4.4) (0.6.0b9)
    Requirement already satisfied: lxml>=4.9.3 in /usr/local/lib/python3.10/dist-packages (from duckduckgo-search==4.4) (4.9.4)
    Requirement already satisfied: nest-asyncio>=1.6.0 in /usr/local/lib/python3.10/dist-packages (from duckduckgo-search==4.4) (1.6.0)
    Requirement already satisfied: cffi>=1.12.0 in /usr/local/lib/python3.10/dist-packages (from curl-cffi>=0.6.0b7->duckduckgo-search==4.4) (1.16.0)
    Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from curl-cffi>=0.6.0b7->duckduckgo-search==4.4) (2022.12.7)
    Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.12.0->curl-cffi>=0.6.0b7->duckduckgo-search==4.4) (2.21)
    [33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv[0m[33m
    [0m


```python
import os
import json
import datetime as dt
import yaml
import warnings


import arxiv
import openai
from openai import OpenAI
from dotenv import load_dotenv

from duckduckgo_search import DDGS, AsyncDDGS
import asyncio

# すべての警告を無視する
warnings.filterwarnings('ignore')
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
load_dotenv()
```




    True




```python
openai.api_key = os.getenv("OPENAI_API_KEY")
```


```python
MODEL_NAME = "gpt-3.5-turbo-0125"
# MODEL_NAME = "gpt-3.5-turbo-instruct"
# MODEL_NAME = "gpt-4-0125-preview"
TEMPERATURE = 0.7
# OpenAIクライアントの初期化
client = OpenAI()
```


```python
# 質問
# question = "禁闕の変について教えてください"

question = "今日の東京と稚内市の天気を教えてください"
```


```python
# 各ノードの名称を定義
RESEARCH_NODE = "research"
RE_RESEARCH_NODE = "re-research"
QUALITY_ASSURANCE_NODE = "quality_assurance"
WRITER_NODE = "writer"
SUPERVISOR_NODE = "supervisor"
```

## ノードの定義


```python
# チームメンバーの定義　特に使わないけど
"""
Researchノード: Web上から必要な情報を検索し、ユーザーからのリクエストに応じて記事を作成します。
Re-Researchノード: (QAでnot acceptだったら)問い合わせと直前の検索クエリから今まで使っていない検索クエリをを生成し、それを基にWeb上から必要な情報を検索し、ユーザーからのリクエストに応じて記事を作成します。
Quality Assurance (QA) ノード: 記事の品質が基準を満たしているかをチェックし、満たしていない場合はフィードバックを返します。品質の受け入れ基準は常にこのノードによって決定されます。
Writerノード: 世界最高レベルのAIチェッカーでも人間が書いたと判断されるような文章を作成します。
Supervisorノード: 会話を管理し、次に動作するワーカーを指示します。全てのタスクが完了したら、「FINISH」と応答します。
"""
team_members = [
    {"name": RESEARCH_NODE,
     "description": "Search the web for necessary information and write articles as requested by users."},
    {"name": RE_RESEARCH_NODE,
     "description": "Generate new search queries based on user inquiries and previous search queries that have not been used before, then search the web for necessary information to create articles as requested by users. Search the web for necessary information and write articles as requested by users."},
    {"name": QUALITY_ASSURANCE_NODE,
     "description": f"Check that the quality of the article meets the criteria. If not, return feedback. The acceptability of deliverables is always determined by {QUALITY_ASSURANCE_NODE}."},
    {"name": WRITER_NODE,
     "description": "Write articles that even the world's best AI checkers would judge as written by a human."},
]
```




```python
# エージェントに追加するシステムプロンプト作成関数
def create_agent_system(
        system_prompt: list,  # システムからエージェントへの初期プロンプト
        team_members: str,   # メンバーの役割
):
    # システムプロンプトに自律的な働きに関する指示を追加
    system_prompt.append({"role" : "system", "content" : "Work autonomously according to your specialty, using the tools available to you."})
    system_prompt.append({"role" : "system", "content" : " Do not ask for clarification."})
    system_prompt.append({"role" : "system", "content" : " Your other team members (and other teams) will collaborate with you with their own specialties."})
    system_prompt.append({"role" : "system", "content" : f" You are chosen for a reason! You are one of the following team members: {team_members}."})
    """
    あなたの専門分野に従って自律的に働いてください。使用可能なツールを使ってください
    確認のために質問をしないでください
    あなたの他のチームメンバーや他のチームも、それぞれの専門分野であなたと協力します
    あなたが選ばれたのには理由があります！あなたは以下のチームメンバーの一人です: {team_members}
    """
    # エージェントを実行するsystem_promptを返す
    return system_prompt
```


```python
# チームのスーパーバイザーを生成する関数
def create_team_supervisor(
        model_name: str,
        system_prompt: list,
        members: list,  # チームメンバーのリスト
        job_result: str, # jobの結果
):
    # メンバー名のリストを生成
    member_names = [member["name"] for member in members]
    team_members = []
    # チームメンバーの名前と説明を文字列に整形
    for member in members:
        team_members.append(f"\n name: {member['name']}\n description: {member['description']}")
    options = ["FINISH"] + member_names  # 終了オプション
    
    # スーパーバイザー用のプロンプトテンプレートを作成
    superviser_prompt = []
    superviser_prompt.append({"role" : "system", "content" : "Given the conversation above, who should act next?"})
    superviser_prompt.append({"role" : "system", "content" : f" Or should we FINISH? Select one of option: {options}"})
    # team_membersからcontent文字列を作成
    content = 'List one of the choices as "name" and its description as "description" below.'
    # チームメンバーの名前と説明を文字列に整形
    for member in team_members:
        content += f"\n name: {member['name']}\n description: {member['description']}"
        superviser_prompt.append({"role" : "system", "content" : f"{content}"})
    superviser_prompt.append({"role": "user", "content": 'Please generate JSON from the text of job results. Use "supervisor_result" as the schema, and use one of {options} as the key to generate it in the form {"supervisor_result": {option}}.'})
    superviser_prompt.append({"role": "user", "content": f"Text of job results: {job_result}"})
    """
    システム
    上記の会話を踏まえて、次に行動すべきは誰ですか？
    選ぶ選択肢の一つを"name"として、その説明を"description"として以下に記載します。\n name: {member['name']}\n description: {member['description']}\n
    それとも、終了すべきですか？次の選択肢の中から一つ選んでください: {options}
    
    user
    次のジョブ結果のテキストからJSONを生成してください。「supervisor_result」をスキーマとして使用し、{options}のうちの一つをキーとして使って、形式が{"supervisor_result": {option}}となるように生成してください。
    ジョブ結果のテキスト: {job_result}
    """
    # スーパーバイザー用のプロンプトテンプレートを作成
    response = client.chat.completions.create(
        model=model_name, # model = "deployment_name".
        messages=superviser_prompt,
        response_format={ "type": "json_object" },
        temperature=TEMPERATURE,
    )
    # print(response.choices[0].message.content)
    
    # スーパーバイザーの機能をバインドし、JSON出力を解析するパイプラインを作成
    return response.choices[0].message.content
```

## Researchエージェントの定義


```python
# テキスト検索用の関数
def search_text(keywords, region='wt-wt', safesearch='moderate', timelimit=None, max_results=10):
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(keywords, region=region, safesearch=safesearch, timelimit=timelimit, max_results=max_results)]
    return results

# 画像検索用の関数
def search_images(keywords, region='wt-wt', safesearch='moderate', size=None, color=None, max_results=10):
    with DDGS() as ddgs:
        results = [r for r in ddgs.images(keywords, region=region, safesearch=safesearch, size=size, color=color, max_results=max_results)]
    return results

# 非同期テキスト検索用の関数
def async_search_text(keywords, max_results=10):
    with AsyncDDGS() as ddgs:
        results = [r for r in ddgs.text(keywords, max_results=max_results)]
    return results


# # 使用例: テキスト検索
# text_results = search_text(question)
# for result in text_results:
#     print(result)

# # 使用例: 画像検索
# image_results = search_images('cats', color='Monochrome', max_results=5)
# for result in image_results:
#     print(result)
```


```python

```


```python
# Researchノードの定義
def research_node(
        model_name: str,
        job_result: str, # search の結果
):
    # リサーチエージェントを呼び出し、結果を取得
    # あなたは、DuckDuckGo検索エンジンを使って、検索された情報を順番に確認し、ポイントを外さずに思慮深く要約するリサーチアシスタントです。
    prompt = [{'role': 'system', 'content': "You are a research assistant who uses the DuckDuckGo search engine to review the information retrieved in sequence and summarize it thoughtfully without missing the point."}]
    prompt.append({"role": "system", "content": "Summary results must be in Japanese."})
    
    research_prompt = create_agent_system(prompt, RESEARCH_NODE)
    research_prompt.append({"role": "system", "content": 'Please generate JSON from the following search result text. Generate in the format {"supervisor_result": summarized results} using "search_result" as the schema and summarized results as the keys.'})
    research_prompt.append({"role": "user", "content": 'Please generate JSON from the text of search job results. Use "research_result" as the schema, and use one of summarized results as the key to generate it in the form {"research_result": summarized results}.'})
    research_prompt.append({"role": "user", "content": f"Text of search job results: {job_result}"})
    """
    システム
    あなたは、DuckDuckGo検索エンジンを使って、検索された情報を順番に確認し、ポイントを外さずに思慮深く要約するリサーチアシスタントです。
    要約結果は日本語でなければならない。
    
    あなたの専門分野に従って自律的に働いてください。使用可能なツールを使ってください
    確認のために質問をしないでください
    あなたの他のチームメンバーや他のチームも、それぞれの専門分野であなたと協力します
    あなたが選ばれたのには理由があります！あなたは以下のチームメンバーの一人です: {team_members}
    以下の検索結果のテキストからJSONを生成してください。スキーマとして「search_result」、キーとして「summarized results」を使用し、{"supervisor_result": summarized results}の形式で生成してください。
    user
    以下の検索結果のテキストからJSONを生成する。スキーマとして "search_result "を使用し、キーとして要約された結果を使用して、{"supervisor_result": 要約された結果}というフォーマットで生成します。
    search ジョブ結果のテキスト: {job_result}
    """
    
    # Research用のプロンプトテンプレートを作成
    response = client.chat.completions.create(
        model=model_name, # model = "deployment_name".
        messages=research_prompt,
        response_format={ "type": "json_object" },
        temperature=TEMPERATURE,
    )
    search_res_str = response.choices[0].message.content
    # print(search_res_str)
    
    # JSON形式の文字列を辞書に変換
    search_res = json.loads(search_res_str)
    
    # 出力と新しいメッセージをステートに反映
    return {
        "output": search_res["research_result"],
        "messages": job_result
    }
```


```python
# 再検索用クエリを抽出
def make_re_search_query(
    model_name: str,
    question: str,    # 最初の質問
    before_query: str,   # 直前の検索クエリ 初回は question
):
    
    # questionから検索クエリを作成する。before_queryと違うものクエリを作成する
    # テキストのブロックが提供されます。あなたのタスクは、そこからキーワードのリストを抽出することです。
    prompt = [{'role': 'system', 'content': "You will be provided with a block of text, and your task is to extract a list of keywords from it."}]
    
    prompt.append({"role": "system", "content": "Use the following example to extract a list of keywords.\n###Example###\n\nuser's question: Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors.\n\nresult query: {      'query_result': 'Black-on-black ware, pottery tradition, Puebloan Native American, ceramic artists, Northern New Mexico, reduction-fired blackware, pueblo artists, smooth surface, designs, selective burnishing, refractory slip, carving, incising designs, polishing, generations, families, Kha'po Owingeh, P'ohwhóge Owingeh pueblos, matriarch potters, contemporary artists, ancestors'}"})
    """
    Use the following example to extract a list of keywords.
    ###Example###
    
    user's question: Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors.
    
    result query: 
    {
      "query_result": "Black-on-black ware, pottery tradition, Puebloan Native American, ceramic artists, Northern New Mexico, reduction-fired blackware, pueblo artists, smooth surface, designs, selective burnishing, refractory slip, carving, incising designs, polishing, generations, families, Kha'po Owingeh, P'ohwhóge Owingeh pueblos, matriarch potters, contemporary artists, ancestors"
    }
    """
    prompt.append({'role': 'system', 'content': "Generate queries that are as different as possible from the query used in the previous search for extracting the list of keywords."})
    prompt.append({'role': 'system', 'content': f"The query used in the previous search was '{before_query}'."})

    prompt.append({"role": "user", "content": "Generate JSON from search result text. Use 'query_result' as the schema, generate in the format {'query_result': Result extract keywords from a block of text.}, and key in the evaluation results, such as whether the generated search results describe the user's request."})
    prompt.append({"role": "user", "content": f"user's question:{question}. Result extract keywords from a block of text.:"})
    

    """
    system
    以下の例を参考にキーワードのリストを抽出してください。
    
    ###Example###
    
    user's question: 黒地に黒の陶器は、ニューメキシコ州北部のプエブロ人ネイティブ アメリカンの陶芸家によって発展した、20 世紀から 21 世紀にかけての陶器の伝統です。伝統的な還元焼成黒食器は、プエブロの芸術家によって何世紀にもわたって作られてきました。前世紀の黒地に黒の陶器は、選択的に磨きをかけたり、耐火物スリップを塗布したりすることによってデザインが施され、滑らかな表面で製造されています。別のスタイルには、デザインを彫刻または切り込み、盛り上がった領域を選択的に研磨することが含まれます。カポ オウィンゲとポホゲ オウィンゲ プエブロの数家族が、家長の陶芸家から受け継がれた技術を用いて、黒地に黒の陶器を何世代にもわたって作り続けてきました。他のプエブロ出身の芸術家も黒地に黒の陶器を制作しています。何人かの現代芸術家は、祖先の陶器に敬意を表して作品を制作しました。
    
    result query: 
    {
      'query_result': '黒地に黒の器、陶器の伝統、プエブロのネイティブ アメリカン、陶芸家、ニューメキシコ北部、還元焼成黒器、プエブロの芸術家、滑らかな表面、デザイン、選択的バニシング、耐火物スリップ、彫刻、切り込みデザイン、研磨、世代、家族、カポ・オウィンゲ、ポホゲ・オウィンゲ・プエブロス、女家長陶芸家、現代芸術家、先祖'
    }
    
    キーワードリストを抽出するために、前回の検索で使用したクエリとはできるだけ異なるクエリを生成する。
    前回の検索で使用したクエリは「{before_query}」です。
    user
    検索結果のテキストからJSONを生成する。スキーマとして "query_result"を使用し、{"query_result"： テキストブロックからキーワードを抽出した結果}の形式で生成する。
    
    前回の検索で使用したクエリ: "{before_query}".

    
    user's question:{}. result query:
    """
    
    # Research用のプロンプトテンプレートを作成
    response = client.chat.completions.create(
        model=model_name, # model = "deployment_name".
        messages=prompt,
        response_format={ "type": "json_object" },
        temperature=TEMPERATURE+TEMPERATURE,
    )
    res_str = response.choices[0].message.content
    # print(res_str)
    
    # JSON形式の文字列を辞書に変換
    res = json.loads(res_str)
    
    # 出力と新しいメッセージをステートに反映
    return {
        "output": res["query_result"],
        "before_query": before_query
    }
```


```python
# test_query = make_re_search_query(
#     MODEL_NAME,
#     question,
#     question
# )
# test_query['output']
```


```python
# Re-Researchノードの定義
# ###Instruction###で始め、次に関連する場合は###Example###または'###Question###
def re_research_node(
    model_name: str,
    question: str,    # 最初の質問
    before_query: str,   # 直前の検索クエリ 初回は question
    before_job_result: str, # 直前のsearch の結果
):
    # re-search 用クエリ
    re_query = make_re_search_query(
        MODEL_NAME,
        question,
        before_query
    )
    re_query = re_query['output']
    
    # search
    re_search = ""
    text_results = search_text(re_query)
    for result in text_results:
        re_search += result["body"] + ", "
        print(re_search["body"])
    
    # search_node
    research_res = research_node(
        MODEL_NAME,
        search, # search の結果
    )
    research_res['output']
    
    # 出力と新しいメッセージをステートに反映
    return {
        "output": research_res['output'],
        "re_query": re_query
    }
```


```python
# # writerノードの定義
# def writer_node(
#         model_name: str,
#         job_result: str, # search の要約結果
#         objective: str,# 目的
#         method="Web search", # method
# ):
#     # Writerとしての指示を含むシステムメッセージ
#     # あなたは文章作成の専門家です。世界最高のAIチェッカーでさえ、人間が書いたと判断するような文章を書くことができます。
#     system_message = """You are a writing specialist.
# You can write sentences that even the world's best AI checkers would judge as written by a human."""
#     prompt = [{'role': 'system', 'content': system_message}]    
#     prompt.append({"role": "system", "content": "survey report must be in Japanese."})
    
#     writer_prompt = create_agent_system(prompt, WRITER_NODE)
#     writer_result = str({"writer_result": f"{objective}"})
#     writer_prompt.append({"role": "system", "content": f'Please generate JSON from the following write result text. Generate in the format {writer_result} using "writer_result" as the schema and survey report as the keys.'})

#     writer_prompt.append({"role": "user", "content": f'Please generate JSON from the text of search job results. Use "writer_result" as the schema, and use one of survey report as the key to generate it in the form {writer_result}.'})
#     format_str = f"""Please use the following format to prepare your survey report.

# ## 1. Introduction
# - Survey Objective: {objective}
# - Survey method: {method}

# ## 2. Survey Results
# - Data Summary: An overview of the main findings and data.
# - Interpretation of results: A detailed explanation of what the survey results mean.

# ## 3. Conclusion
# - Response to Objectives: Conclusions based on the survey objectives.
# - Summary of Key Findings Summary of key findings.

# ## 4. Recommendations
# Action Plan: Specific recommendations or improvements based on the findings.
# Implementation steps: Step-by-step process for putting recommendations into action.
# """
#     writer_prompt.append({"role": "system", "content": format_str})
#     writer_prompt.append({"role": "user", "content": f"Findings for the preparation of the survey report: {job_result}"})
#     """
#     システム
#     あなたは文章作成の専門家です。世界最高のAIチェッカーでさえ、人間が書いたと判断するような文章を書くことができます。
#     survey reportは日本語でなければならない。
#     以下の検索結果のテキストからJSONを生成してください。スキーマとして「writer_result」、キーとして「summarized results」を使用し、{"supervisor_result": summarized results}の形式で生成してください。
#     あなたの専門分野に従って自律的に働いてください。使用可能なツールを使ってください
#     確認のために質問をしないでください
#     あなたの他のチームメンバーや他のチームも、それぞれの専門分野であなたと協力します
#     あなたが選ばれたのには理由があります！あなたは以下のチームメンバーの一人です: {team_members}
    
#     調査報告書の作成には、以下の書式を使用してください。

#     ## 1. はじめに
#     - 調査目的 object
#     - 調査方法 method

#     ## 2. 調査結果
#     - データ概要：主な調査結果とデータの概要。
#     - 結果の解釈： 調査結果が意味するものについての詳細な説明。

#     ## 3. 結論
#     - 目的に対する回答： 調査目的に基づく結論。
#     - 主な調査結果の要約 主な調査結果の要約。

#     ## 4. 提言
#     行動計画： 調査結果に基づく具体的な推奨事項または改善事項。
#     実施手順： 提言を実行に移すための段階的プロセス。

#     user
#     以下の検索結果のテキストからJSONを生成する。スキーマとして "write_result "を使用し、キーとしてsurvey reportを使用して、{"supervisor_result": 要約された結果}というフォーマットで生成します。
#     調査報告書の作成のための調査結果: {job_result}
#     """
    
#     # writer用のプロンプトテンプレートを作成
#     response = client.chat.completions.create(
#         model=model_name, # model = "deployment_name".
#         messages=writer_prompt,
#         response_format={ "type": "json_object" },
#         temperature=TEMPERATURE,
#     )
#     writer_res_str = response.choices[0].message.content
#     print(writer_res_str)
#     # JSON形式の文字列を辞書に変換
#     writer_res = json.loads(writer_res_str)
    
#     # 出力と新しいメッセージをステートに反映
#     return {
#         "output": writer_res["writer_result"],
#         "messages": job_result
#     }

# output_search = research_res['output']
# objective = "survey"
# method = "Web search"

# writer_res = writer_node(
#         MODEL_NAME,
#         output_search,
#         objective,
#         method,
# )
# writer_res
```


```python
# 品質チェックノードの定義
def qa_node(
    model_name: str,
    question:str, # 検索結果
    research_output:str, # 検索結果
):
    # 品質チェックの指示を含むシステムメッセージ
#     system_message = """You are a specialist in inspecting the quality of articles. 
#     Inspect the article to see if it meets the following requirements:

#     - The article is written in Japanese.
#     - The writing style MUST be such that the AI sentence checker determines that it was written by a HUMAN.
#     - The article MUST be written in a way that is easy to understand.
#     - The article MUST meet the user's requirements.

#     If the evaluation criteria are met, write 'Acceptable'.
#     In addition, write the reason why you judged that the evaluation criteria are met.

#     If the evaluation criteria are not met, write 'Not Acceptable'.
#     In addition, provide feedback on what needs to be done to meet the evaluation criteria.

#     DO NOT make excuses such as 'I can't make a decision because I am an AI'.

#     The quality of your articles is relevant to your career.
#     Please be as rigorous as possible in your inspections and make sure that your feedback is helpful in making corrections.
#     """
    prompt = [{'role': 'system', 'content': "You are a specialist in inspecting the quality of articles. Inspect the article to see if it meets the following requirements: The article is written in Japanese."}]
    prompt.append({'role': 'system', 'content': "You are a specialist in inspecting the quality of articles. Inspect the article to see if it meets the following requirements: The writing style MUST be such that the AI sentence checker determines that it was written by a HUMAN."})
    prompt.append({'role': 'system', 'content': "You are a specialist in inspecting the quality of articles. Inspect the article to see if it meets the following requirements: The article MUST be written in a way that is easy to understand."})
    prompt.append({'role': 'system', 'content': "You are a specialist in inspecting the quality of articles. Inspect the article to see if it meets the following requirements: The article MUST meet the user's requirements."})

    prompt.append({'role': 'system', 'content': "You are a specialist in inspecting the quality of articles. Inspect the article to see if it meets the following requirements: If the evaluation criteria are met, write 'Acceptable'."})
    prompt.append({'role': 'system', 'content': "You are a specialist in inspecting the quality of articles. Inspect the article to see if it meets the following requirements: In addition, write the reason why you judged that the evaluation criteria are met."})
  
    prompt.append({'role': 'system', 'content': "You are a specialist in inspecting the quality of articles. Inspect the article to see if it meets the following requirements: If the evaluation criteria are not met, write 'Not Acceptable'."})
    prompt.append({'role': 'system', 'content': "You are a specialist in inspecting the quality of articles. Inspect the article to see if it meets the following requirements: In addition, provide feedback on what needs to be done to meet the evaluation criteria."})

    prompt.append({'role': 'system', 'content': "You are a specialist in inspecting the quality of articles. Inspect the article to see if it meets the following requirements: DO NOT make excuses such as 'I can't make a decision because I am an AI'."})
  
    prompt.append({'role': 'system', 'content': "You are a specialist in inspecting the quality of articles. Inspect the article to see if it meets the following requirements: The quality of your articles is relevant to your career."})
    prompt.append({'role': 'system', 'content': "You are a specialist in inspecting the quality of articles. Inspect the article to see if it meets the following requirements: Please be as rigorous as possible in your inspections and make sure that your feedback is helpful in making corrections."})

    # prompt = [{'role': 'system', 'content': system_message}]
    qa_prompt = create_agent_system(prompt, QUALITY_ASSURANCE_NODE)
    qa_prompt.append({"role": "user", "content": "Generate JSON from search result text. Use 'qa_result' as the schema, generate in the format {'qa_result': Acceptable or Not Acceptable}, and key in the evaluation results, such as whether the generated search results describe the user's request."})
    qa_prompt.append({"role": "user", "content": f"user's requirements:{question}. search result text: {research_output}"})
    

    """
    評価基準の適用例:
    1. 言語と文章スタイルの評価:
        - 記事が日本語で書かれているか。
        - 文章が人間によって書かれたとAI文章チェッカーに判断させるスタイルであるか。
    2. 内容の理解しやすさ:
        - 記事の内容が簡潔に、かつ明確に表現されているか。
        - 専門用語が適切に説明され、一般の読者も理解できるようになっているか。
    3. ユーザーの要件への適合性:
        - 記事がユーザーの要求や指定したテーマに沿っているか。
        - ユーザーが期待する情報や視点が適切に取り入れられているか。
    評価例:
    - 受理可能: 記事は全ての評価基準を満たしています。日本語で書かれており、文章スタイルは人間によるものと判断できます。
    内容は理解しやすく、ユーザーの要件にも適合しています。これらの点から、記事は受理可能と判断します。
    - 受理不可: 記事は一部の評価基準を満たしていません。特に、文章スタイルがAIによって書かれたように見える部分があります。
    また、専門用語の説明が不足しているため、内容の理解が難しい箇所があります。これらの問題を解決するためには、人間らしい表現を増やし、専門用語に対する説明を追加する必要があります。
    user
    検索結果のテキストからJSONを生成する。スキーマとして "qa_result"を使用し、{"qa_result"： Acceptable or Not Acceptable}の形式で生成し、生成された検索結果をキーとして評価する。
    user's requirements:{}. 検索結果のテキスト: {research_output}
    """
    
    # Research用のプロンプトテンプレートを作成
    response = client.chat.completions.create(
        model=model_name, # model = "deployment_name".
        messages=qa_prompt,
        response_format={ "type": "json_object" },
        temperature=TEMPERATURE,
    )
    qa_res_str = response.choices[0].message.content
    # print(qa_res_str)
    
    # JSON形式の文字列を辞書に変換
    qa_res = json.loads(qa_res_str)
    """
    "qa_result": "Not Acceptable" だったら戻り値に次の検索ワードを入れるか、質問と分割するかとかしたい
    """
    # 出力と新しいメッセージをステートに反映
    return {
        "output": qa_res["qa_result"]
    }
```


```python

```


```python
# # 使用例: 1サイクル
# with Timer(prefix=f'Processing time for one cycle.'):
#     question = "今日の東京と稚内市の天気を教えてください"

#     search = ""
#     text_results = search_text(question)
#     for result in text_results:
#         search += result["body"] + ", "
#         # print(result["body"])

#     # search_node
#     research_res = research_node(
#         MODEL_NAME,
#         search, # search の結果
#     )
#     research_output = research_res['output']
#     print(f"検索して質問に回答した結果: {research_output}")

#     qa_res = qa_node(
#         MODEL_NAME,
#         question,
#         research_output
#     )
#     print(f"質問と回答の整合性チェック: {qa_res}")

```

検索して質問に回答した結果: 稚内市の天気予報に関する情報が提供されており、今日・明日の天気や気温、降水確率、注意報などが記載されている。また、稚内市のPM2.5分布予測や地震情報、スキー積雪情報なども含まれている。

質問と回答の整合性チェック: {'output': 'Not Acceptable'}

Processing time for one cycle. 5.816[s]


```python
def search_agent_1cycle(
    question: str,
    query: str,
):
    search = ""
    text_results = search_text(query)
    for result in text_results:
        search += result["body"] + ", "
        # print(result["body"])

    # search_node
    research_res = research_node(
        MODEL_NAME,
        search, # search の結果
    )
    research_output = research_res['output']

    qa_res = qa_node(
        MODEL_NAME,
        question,
        research_output
    )
    
    
    return {
        "output": research_output,
        "qa_result": qa_res
    }
```


```python
def research_agent(
    question:str,
):
    query = question
    search_res = search_agent_1cycle(question, query)

    print(f"検索結果を要約した回答: {search_res['output']}")
    print(f"質問と回答の整合性チェック: {search_res['qa_result']['output']}")

    # カウント用変数の初期化
    research_cnt = 0
    # outputが'Not Acceptable'である間、処理を繰り返す
    while search_res['qa_result']['output']  == 'Not Acceptable':
        print("-"*50)
        with Timer(prefix=f'Number of re-researches {research_cnt+1} :'):
            # カウントアップ
            research_cnt += 1
            # カウントが3に達したらループを強制終了
            if research_cnt == 3:
                print("実行回数が3に達したため、処理を終了します。")
                break
            # 再検索用のクエリ生成
            re_query = make_re_search_query(
                MODEL_NAME,
                question,
                query
            )
            # 
            query = re_query['output']
            print(f"再検索クエリ: {query}")

            search_res = search_agent_1cycle(question, query)

            print(f"検索結果を要約した回答: {search_res['output']}")
            print(f"質問と回答の整合性チェック: {search_res['qa_result']['output']}")
        print("-"*50)
    return {
        "final_qa": search_res['qa_result']['output'],
        "final_query": query,
        "search_output": search_res['output']
    }
```


```python
def get_summary_of_search_results(question, search_res):
    print("-"*50)
    print(f"質問: {question}")
    print("-"*50)
    print(f"検索に使用したクエリ:\n {research_res['final_query']}")
    print(f"検索結果を要約した最終回答:\n {research_res['search_output']}")
    print(f"最終判定結果: {research_res['final_qa']}")
    print("-"*50)
    print(f"使用モデル: {MODEL_NAME}")
```


```python
question = """2024年に注目されている最新のテクノロジートレンドは何ですか？
また、それらのトレンドが社会にどのような影響を与えると予想されますか？"""
with Timer(prefix=f'Handle all time by research.'):
    research_res = research_agent(question)
```

    検索結果を要約した回答: 2024年の戦略的テクノロジのトップ・トレンドは、「投資の保護」 (既存および将来の投資を保護／保全する)、「ビルダーの台頭」 (適切なステークホルダー向けに、適切なソリューションを、適切なタイミングで構築する)、「価値のデリバー」 (社内外の顧客の環境変化に応じて価値を提供する) という3つの包括的なビジネス・テーマの1つまたは複数に関連します。
    質問と回答の整合性チェック: Not Acceptable
    --------------------------------------------------
    再検索クエリ: 2024年, 最新テクノロジートレンド, 注目, 社会, 予想, 影響
    検索結果を要約した回答: 2024年の戦略的テクノロジのトップ・トレンドは、「投資の保護」 (既存および将来の投資を保護／保全する)、「ビルダーの台頭」 (適切なステークホルダー向けに、適切なソリューションを、適切なタイミングで構築する)、「価値のデリバー」 (社内外の顧客の環境変化に応じて価値を提供する) という3つの包括的なビジネス・テーマの1つまたは複数に関連します。
    質問と回答の整合性チェック: Not Acceptable
    Number of re-researches 1 : 6.386[s]
    --------------------------------------------------
    --------------------------------------------------
    再検索クエリ: 2024年, 最新テクノロジートレンド, 注目, 社会, 影響, 予想
    検索結果を要約した回答: 2024年の戦略的テクノロジのトップ・トレンドは、「投資の保護」 (既存および将来の投資を保護／保全する)、「ビルダーの台頭」 (適切なステークホルダー向けに、適切なソリューションを、適切なタイミングで構築する)、「価値のデリバー」 (社内外の顧客の環境変化に応じて価値を提供する) という3つの包括的なビジネス・テーマの1つまたは複数に関連します。
    質問と回答の整合性チェック: Acceptable
    Number of re-researches 2 : 8.304[s]
    --------------------------------------------------
    Handle all time by research. 20.782[s]



```python
get_summary_of_search_results(question, research_res)
```

    --------------------------------------------------
    質問: 2024年に注目されている最新のテクノロジートレンドは何ですか？
    また、それらのトレンドが社会にどのような影響を与えると予想されますか？
    --------------------------------------------------
    検索に使用したクエリ:
     2024年, 最新テクノロジートレンド, 注目, 社会, 影響, 予想
    検索結果を要約した最終回答:
     2024年の戦略的テクノロジのトップ・トレンドは、「投資の保護」 (既存および将来の投資を保護／保全する)、「ビルダーの台頭」 (適切なステークホルダー向けに、適切なソリューションを、適切なタイミングで構築する)、「価値のデリバー」 (社内外の顧客の環境変化に応じて価値を提供する) という3つの包括的なビジネス・テーマの1つまたは複数に関連します。
    最終判定結果: Acceptable
    --------------------------------------------------
    使用モデル: gpt-3.5-turbo-0125



```python
MODEL_NAME = "gpt-4-0125-preview"

question = """世界の異なる国々で行われているユニークな新年の祝い方を3つ挙げ、
それぞれの文化的背景を説明してください。"""

with Timer(prefix=f'Handle all time by research.'):
    research_res = research_agent(question)
```

    検索結果を要約した回答: このブログ記事では、日本、中国、アメリカ、インド、ブラジル、ロシア、スペインの7カ国の新年の祝い方について探究しています。グレゴリオ暦に基づく日本のお正月や、各国のユニークな新年の祝い方、例えばスイスではアイスクリームを床に落とす、ギリシャではザクロを玄関に投げる、コロンビアではスーツケースを持って走るなどの風習が紹介されています。また、中国では春節が旧正月として祝われることや、その他多くの国々で独自の新年の祝い方があることが紹介されています。
    質問と回答の整合性チェック: Acceptable
    Handle all time by research. 10.019[s]



```python
get_summary_of_search_results(question, research_res)
```

    --------------------------------------------------
    質問: 世界の異なる国々で行われているユニークな新年の祝い方を3つ挙げ、
    それぞれの文化的背景を説明してください。
    --------------------------------------------------
    検索に使用したクエリ:
     世界の異なる国々で行われているユニークな新年の祝い方を3つ挙げ、
    それぞれの文化的背景を説明してください。
    検索結果を要約した最終回答:
     このブログ記事では、日本、中国、アメリカ、インド、ブラジル、ロシア、スペインの7カ国の新年の祝い方について探究しています。グレゴリオ暦に基づく日本のお正月や、各国のユニークな新年の祝い方、例えばスイスではアイスクリームを床に落とす、ギリシャではザクロを玄関に投げる、コロンビアではスーツケースを持って走るなどの風習が紹介されています。また、中国では春節が旧正月として祝われることや、その他多くの国々で独自の新年の祝い方があることが紹介されています。
    最終判定結果: Acceptable
    --------------------------------------------------
    使用モデル: gpt-4-0125-preview



```python
MODEL_NAME = "gpt-4-0125-preview"

question = """最近の世界経済の動向を分析し、今後の市場で注目すべき3つの産業を予測してください。それぞれの産業が注目される理由も含めて説明してください。"""

with Timer(prefix=f'Handle all time by research.'):
    research_res = research_agent(question)
```

    検索結果を要約した回答: 2024年には世界の総合インフレ率が5.8%へと減速し、2025年にはさらに4.4%へと鈍化する見込みである。この予測は以前より下方修正されており、ディスインフレと着実な経済成長に伴い、世界経済がハードランディングを避ける可能性が高まっている。しかし、財政政策の過度な緩和や構造改革の加速が新たなリスクを生じさせる可能性も指摘されている。一方で、IMFは2022年の世界のGDP成長率予測を複数回にわたり下方修正しており、ロシアのウクライナ侵攻やインフレの影響が反映されている。中国経済はゼロコロナ政策の解除後も回復が緩慢で、雇用や住宅市場の低迷が背景にある。全体として、世界経済は減速傾向にあり、インフレ抑制と経済成長のバランスを取ることが今後の課題となっている。
    質問と回答の整合性チェック: Not Acceptable
    --------------------------------------------------
    再検索クエリ: 世界経済, 動向, 市場, 注目, 産業, 予測, 理由, 解説
    検索結果を要約した回答: IMFの2022年の世界経済成長率予測は、ロシアのウクライナ侵略やインフレの影響を受けて下方修正され、2022年は3.6％に。2024年の成長率は2.4％と予想され、3年連続での減速が見込まれる。中東紛争の影響などで地政学的リスクが高まっている。2022年のインフレ率は先進国が5.7％、新興国が8.7％に上方修正された。新興国と発展途上国の成長率は2022年が4.6％、2023年が4.4％と予測され、パンデミック前のトレンドを下回る。2022年から2024年の間に先進国の成長率は減速し、新興市場国と発展途上国の成長率も鈍化する見込み。ナイジェリア、コロンビア、ポーランドは高成長が期待される経済大国として注目されている。
    質問と回答の整合性チェック: Not Acceptable
    Number of re-researches 1 : 37.229[s]
    --------------------------------------------------
    --------------------------------------------------
    再検索クエリ: 世界経済, 動向, 分析, 市場, 注目, 産業, 予測, 理由, 説明
    検索結果を要約した回答: {'IMF_2022年GDP成長率予測': 'IMFによると、2022年の世界のGDP成長率予測は、ロシアによるウクライナ侵略やインフレなどの影響で、2022年内に累次にわたり下方修正されている。当初は4.4%の成長が見込まれていたが、4月の時点で3.6%へと下方修正された。', '世界経済の成長率予測': '2022年の世界経済成長率は3.5%で、2023年と2024年はそれぞれ3.0%と予測されている。インフレ対策のための金融政策の引き締めが経済活動の重しとなっており、総合インフレ率は2022年の8.7%から2024年には5.2%へと減少する見込みである。', 'グローバル経済と主要産業の動向': '2023年12月のグローバル経済動向報告によると、鉄鋼、オイル・ガス、石油化学、紙パルプ、医薬品、食品、電子部品・半導体、家電、不動産、アパレルなど主要産業の分析が行われている。', '2024年世界経済成長率予測': '2024年の世界経済成長率は2.4%と予測され、3年連続の減速が見込まれている。金融政策の引き締め、制約的な与信状況、貿易と投資の世界的な低迷が成長を抑制するとされている。', '先進国と新興国の成長率差': '先進国の成長率は2021年の5%から、2022年は3.8%、2023年には2.3%と減速する見込みである。一方、新興国・途上国の成長率は、2021年の6.3%から、2022年は4.6%、2023年には4.4%と予測されている。', '世界経済見通し': '2022年4月の世界経済見通しによると、ウクライナでの戦争が経済回復を抑制し、世界経済成長率は2021年の6.1%から2022年と2023年は3.6%に減速する見込みである。', '世界経済の動向': '2021年は新型コロナウイルスへの対応が進展し、世界経済が回復してきた一年であった。2020年初のコロナショック後、政府の支援により世界経済は力強く回復した。', '長期経済成長予測': '世界経済は2016年から2050年までに年平均実質成長率約2.5%で成長し、経済規模が2042年までに倍増すると予想されている。新興市場と開発途上国が主な成長のけん引役となる。'}
    質問と回答の整合性チェック: Not Acceptable
    Number of re-researches 2 : 66.893[s]
    --------------------------------------------------
    --------------------------------------------------
    実行回数が3に達したため、処理を終了します。
    Number of re-researches 3 : 0.000[s]
    Handle all time by research. 123.149[s]



```python
get_summary_of_search_results(question, research_res)
```

    --------------------------------------------------
    質問: 最近の世界経済の動向を分析し、今後の市場で注目すべき3つの産業を予測してください。それぞれの産業が注目される理由も含めて説明してください。
    --------------------------------------------------
    検索に使用したクエリ:
     世界経済, 動向, 分析, 市場, 注目, 産業, 予測, 理由, 説明
    検索結果を要約した最終回答:
     {'IMF_2022年GDP成長率予測': 'IMFによると、2022年の世界のGDP成長率予測は、ロシアによるウクライナ侵略やインフレなどの影響で、2022年内に累次にわたり下方修正されている。当初は4.4%の成長が見込まれていたが、4月の時点で3.6%へと下方修正された。', '世界経済の成長率予測': '2022年の世界経済成長率は3.5%で、2023年と2024年はそれぞれ3.0%と予測されている。インフレ対策のための金融政策の引き締めが経済活動の重しとなっており、総合インフレ率は2022年の8.7%から2024年には5.2%へと減少する見込みである。', 'グローバル経済と主要産業の動向': '2023年12月のグローバル経済動向報告によると、鉄鋼、オイル・ガス、石油化学、紙パルプ、医薬品、食品、電子部品・半導体、家電、不動産、アパレルなど主要産業の分析が行われている。', '2024年世界経済成長率予測': '2024年の世界経済成長率は2.4%と予測され、3年連続の減速が見込まれている。金融政策の引き締め、制約的な与信状況、貿易と投資の世界的な低迷が成長を抑制するとされている。', '先進国と新興国の成長率差': '先進国の成長率は2021年の5%から、2022年は3.8%、2023年には2.3%と減速する見込みである。一方、新興国・途上国の成長率は、2021年の6.3%から、2022年は4.6%、2023年には4.4%と予測されている。', '世界経済見通し': '2022年4月の世界経済見通しによると、ウクライナでの戦争が経済回復を抑制し、世界経済成長率は2021年の6.1%から2022年と2023年は3.6%に減速する見込みである。', '世界経済の動向': '2021年は新型コロナウイルスへの対応が進展し、世界経済が回復してきた一年であった。2020年初のコロナショック後、政府の支援により世界経済は力強く回復した。', '長期経済成長予測': '世界経済は2016年から2050年までに年平均実質成長率約2.5%で成長し、経済規模が2042年までに倍増すると予想されている。新興市場と開発途上国が主な成長のけん引役となる。'}
    最終判定結果: Not Acceptable
    --------------------------------------------------
    使用モデル: gpt-4-0125-preview



```python

```
