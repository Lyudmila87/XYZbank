FROM python:3.11
ENV TZ="Europe/Moscow"

COPY . ./app

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "pytest", "--alluredir=allure_report" ]
