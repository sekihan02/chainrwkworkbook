FROM python:3.9

ENV SLACK_BOT_TOKEN xoxb-
ENV SLACK_APP_TOKEN xapp-
ENV SLACK_SIGNING_SECRET 184952


WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
EXPOSE 5000

CMD [ "python", "./app.py" ]
