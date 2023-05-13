# Socket ModeからEnable Socket ModeをOFFに変更
# Event SubscriptionsのEnable EventsをONにし Request URLに作成したコンテナアプリの概要から見れるアプリケーション URL(https://***.io)/slack/eventsを設定する Verified になります
# アプリの権限を設定します。以下のスコープをアプリに追加してください：
# chat:write：メッセージを送信するために必要
# files:write：ファイルをアップロードするために必要
# channels:history：チャンネルの履歴を読み取るために必要（メッセージイベントを受信するため）

# Interactivity & ShortcutsをONにし、 Request URLに作成したコンテナアプリの概要から見れるアプリケーション URL(https://***.io)/slack/eventsを設定する 
import os
import tempfile
from slack_bolt import App
import matplotlib.pyplot as plt
import numpy as np
import threading
import uuid

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


# 疑似データを可視化する関数
def visualize_data(channel):
    # データの生成
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # プロット作成
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Sin Wave')

    # ユニークな一時ファイル名を生成
    unique_filename = str(uuid.uuid4())
    image_dir = "/path/to/save/"
    os.makedirs(image_dir, exist_ok=True)
    image_path = os.path.join(image_dir, f"{unique_filename}.png")

    # 画像を保存
    plt.savefig(image_path)

    # 画像をSlackにアップロードしてメッセージとして返す
    client = app.client
    
    try:
        response = client.files_upload(
            channels=channel,
            file=image_path,
            initial_comment="Here is the plot!"
        )
        file_url = response["file"]["url_private"]
        image_link = f"<{file_url}|Click here to view the image>"
        return image_link
    except Exception as e:
        print(f"Error uploading image: {e}")

# 'image' を含むメッセージをリッスンします
# def message_image(message, say):
@app.message("image")
def message_image(ack, message, say):
    channel = message["channel"]
    ack()  # 即座に応答を返す

    def upload_and_send_image():
        image_link = visualize_data(channel)
        # if image_link:
        #     say(f"Image uploaded: {image_link}")
        # else:
        #     say("Failed to upload image.")

    # 非同期に画像をアップロードしてメッセージを送信するために、別のスレッドで画像をアップロードしてメッセージを送信
    threading.Thread(target=upload_and_send_image).start()

# アプリを起動します
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5000)))