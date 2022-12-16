FROM python:3.8-slim

EXPOSE 8501

WORKDIR /stable-diffusion
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY app/ app/
COPY fetch_model.py .
RUN python3 fetch_model.py

ENTRYPOINT python3 -m streamlit run app/stream_app.py
