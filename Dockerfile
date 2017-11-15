FROM python:3

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

# コンテナ起動時に app.py を実行
CMD [ "python", "app.py" ]