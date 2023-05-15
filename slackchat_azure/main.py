# https://slack.dev/bolt-python/ja-jp/tutorial/getting-started
# 1.https://api.slack.com/apps にアクセスし、Create Appからfrom scratch を押し、App Name をWorkspaceに設定する
# 2. 左サイドバーの「OAuth & Permissions」をクリックし、「Bot Token Scopes」セクションまで下にスクロールします。「Add an OAuth Scope」をクリックします。
# ここでは chat:write というスコープのみを追加します。このスコープは、アプリが参加しているチャンネルにメッセージを投稿することを許可します。files:write, channels:history
# 3. OAuth & Permissions ページの一番上までスクロールし、「Install App to Workspace」をクリックします。Slack の OAuth 確認画面 が表示されます。この画面で開発用ワークスペースへのアプリのインストールを承認します。
# 4. インストールを承認すると OAuth & Permissions ページが表示され、Bot User OAuth Access Token を確認できるでしょう。
# 5. 次に「Basic Informationのページ」まで戻り、アプリトークンのセクションまで下にスクロールし「Generate Token and Scopes」をクリックしてアプリレベルトークンを作成します。このトークンに connections:write のスコープを付与し、作成された xapp トークンを保存します。これらのトークンは後ほど利用します
# 6. 左サイドメニューの「Socket Mode」のEnable Socket Modeを有効にします。
# 7. Event Subscriptions にアクセスして、機能を有効にしてください。 Subscribe to Bot Events 配下で、ボットが受け取れる　イベントを追加することができます。4つのメッセージに関するイベントがあります。
# message.channels アプリが参加しているパブリックチャンネルのメッセージをリッスン
# message.groups アプリが参加しているプライベートチャンネルのメッセージをリッスン
# message.im あなたのアプリとユーザーのダイレクトメッセージをリッスン
# message.mpim あなたのアプリが追加されているグループ DM をリッスン
# 8. 左サイドバーの「OAuth & Permissions」をクリックし、「Bot Token Scopes」セクションまで下にスクロールします。files:writeを追加しreinstall workspace

# Azureの設定は、ContainerAppを作成し、アプリ設定でAzure Container Resistryにプッシュしたイメージを指定するだけ
import os
import re
import io
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


# 疑似データを可視化し、Slackに送信する関数
def visualize_data(channel):
    # データの生成
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # データを可視化
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Sin Wave')

    # グラフを画像として取得
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Slackに画像を送信
    app.client.files_upload(
        channels=channel,
        file=buf,
        filename='visualization.png',
        initial_comment='Data Visualization'
    )

    # メモリ上の画像をクローズ
    plt.close()


# メンションが含まれるメッセージに反応する
@app.message(re.compile(r"<@[\w\d]+>"))  # 正規表現パターンでメッセージをフィルタリング
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"Hey there <@{message['user']}>!")


@app.message("image")
def visual_image(message, say):
    # visualize_data()関数を呼び出して可視化結果をSlackに送信
    visualize_data(message['channel'])

# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()