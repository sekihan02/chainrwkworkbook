# # Socket Modeから、Enable Socket ModeをONにする
# # https://qiita.com/hayahaya2/items/0787225d9fa66dbcdf4f
# # https://slack.dev/bolt-python/ja-jp/tutorial/getting-started
# import os
# from slack_bolt import App
# from slack_bolt.adapter.socket_mode import SocketModeHandler

# # ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
# app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# # 'hello' を含むメッセージをリッスンします
# # 指定可能なリスナーのメソッド引数の一覧は以下のモジュールドキュメントを参考にしてください：
# # https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
# @app.message("hello")
# def message_hello(message, say):
#     # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
#     say(f"Hey there <@{message['user']}>!")

# # アプリを起動します
# if __name__ == "__main__":
#     SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

# Socket ModeからEnable Socket ModeをOFFに変更
# Event SubscriptionsのEnable EventsをONにし Request URLに作成したコンテナアプリの概要から見れるアプリケーション URL(https://***.io)/slack/eventsを設定する Verified になります
# Interactivity & ShortcutsをONにし、 Request URLに作成したコンテナアプリの概要から見れるアプリケーション URL(https://***.io)/slack/eventsを設定する 
import os
from slack_bolt import App

# ボットトークンと署名シークレットを使ってアプリを初期化します
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# 'hello' を含むメッセージをリッスンします
@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text":"Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )

# アプリを起動します
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5000)))