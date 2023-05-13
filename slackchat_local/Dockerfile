FROM python:3.9

ENV SLACK_BOT_TOKEN xoxb-5088505216708-5282639600576-DAmWxvIvbG7lYsFwMJqjWv2o
ENV SLACK_APP_TOKEN xapp-1-A057PCGRJ20-5256169768565-db0383bd6487585b786ab871c5d977dd6e29ec83cf3e1bcf4f83058802f66135

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
EXPOSE 5000

CMD [ "python", "./app.py" ]
