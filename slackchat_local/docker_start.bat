@REM 2回目以降の起動時
@REM docker run -p 5000:5000 --rm -v C:\Users\akaha\Documents\docker\workspace\chat\work:/work -w /work --name chat chat-app
docker run -p 5000:5000 --name chat slack-chat
