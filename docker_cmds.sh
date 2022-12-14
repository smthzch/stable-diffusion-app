docker build -t stable-diffusion .
docker run -d --name stable-diffusion -p 80:80 --gpus all stable-diffusion
docker start stable-diffusion