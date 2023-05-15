@REM ローカルで試す場合、Dockerfileをaci_flask_movetestとしてbuild
@REM docker build -t slack_bot:0.1 .
@REM build後動作するかを確認 Slackの設定で、Slash Commandsを作成して、リクエストをこのアプリケーションのURLに転送するように設定してください。 http://<your_server_ip>:5000/weather
@REM docker run -p 5000:5000 --rm slack_bot:0.1

@REM Dockerイメージのビルドとプッシュを--registryで指定したコンテナレジストリに--imageで指定した名前とタグで登録
az acr build --registry CResistry --image socket_bot:0.2 .
@REM 実行するとビルドに必要なファイルをACRに転送してACR上でイメージのビルドが開始されます
@REM 最後のログにRun ID: xxx was successfulと表示されていれば成功です
