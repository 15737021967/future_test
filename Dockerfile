FROM python:3.7

ENV FLASK_APP ezreal

WORKDIR /opt/code
COPY requirements.txt /opt/code

RUN echo "Asia/Shanghai" > /etc/timezone

RUN mkdir -p ~/.pip && echo "[global]" > ~/.pip/pip.conf \
 && echo "index-url = https://mirrors.aliyun.com/pypi/simple/" >> ~/.pip/pip.conf \
 && pip install --upgrade pip \
 && pip install -r requirements.txt

COPY . /opt/code

CMD ["gunicorn", "-b", "0.0.0.0:8081", "-w", "2", "ezreal:app"]
