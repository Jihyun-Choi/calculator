FROM python:3.9.6

RUN git clone https://github.com/Jihyun-Choi/calculator.git\
&& pip3 install django

WORKDIR ./calculator

RUN pip3 install -r requirements.txt

CMD ["0.0.0.0:8000"]
ENTRYPOINT ["python3","manage.py","runserver"]
