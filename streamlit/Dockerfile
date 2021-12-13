FROM python:3.8

# set environment
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
# install dependencies
RUN pip install -r requirements.txt
# copy project
COPY . /code/
EXPOSE 8501
CMD streamlit run app.py