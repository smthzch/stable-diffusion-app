# Stable Diffusion App

This repository contains a FastApi and Streamlit app which you can use to run Stable Diffusion locally.

The stable diffusion model is pulled from huggingface [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)

![](fractal_goat.png)

## Setup

This was tested with python 3.9, Pytorch 1.12 on Cuda 11.6

```shell
pip install -r requirements.txt
python fetch_model.py
```

## Run

To run the graphical Streamlit app:

```shell
streamlit run app/stream_app.py
```

To run run a rest api service:

```shell
uvicorn app.main:app --reload
```

Prompts can be sent with a query parameter: `127.0.0.1:8000/?prompt=stable diffusion`

## Docker

A `Dockerfile` is included, see `docker_cmds.sh` for commands to build and run the docker container.
