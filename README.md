# Stable Diffusion App

This repository contains a FastApi and Streamlit app which you can use to run Stable Diffusion locally.

The stable diffusion model is pulled from huggingface [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)

![](fractal_goat.png)

## Setup

This was tested with python 3.8, Pytorch 1.12 on Cuda 11.6

```shell
pip install -r requirements.txt
python fetch_model.py
```

## Run

To run the graphical Streamlit app:

```shell
streamlit run app/stream_app.py
```

Navigate to `127.0.0.1:8501` for a web UI to send prompts to stable-diffusion.

To run run a rest api service:

```shell
uvicorn app.main:app --reload
```

Prompts can be sent with a query parameter: `127.0.0.1:8000/?prompt=stable diffusion`

## Docker

A `Dockerfile` is included, to build and run the docker container:

```shell
docker build -t stable-diffusion .
docker run \
    -d \
    --name stable-diffusion \
    -p 8501:8501 \
    --gpus all \
    stable-diffusion
docker start stable-diffusion
```

The `--gpus all` flag can be omitted to run on cpu, though image generation takes multiple minutes on cpu.
