FROM python:3.10

ENV SLACK_BOT_TOKEN xoxb-
ENV SLACK_APP_TOKEN xapp-

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
EXPOSE 5000

CMD [ "python", "./main.py" ]
