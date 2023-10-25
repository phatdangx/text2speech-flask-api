# Text-To-Speech API

A Text-To-Speech (TTS) API implemented using Flask. This repository provides a Docker setup to easily get up and running.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [API Documentation](#api-documentation)

## Prerequisites
- Docker and Docker Compose installed on your machine.
    - [Install Docker](https://docs.docker.com/get-docker/)
    - [Install Docker Compose](https://docs.docker.com/compose/install/)
- Production only:
    - [Install Nginx](https://nginx.org/en/docs/install.html)

## Setup
1. Clone this repository:
    ```sh
    git clone <repository-url>
    cd <repository-dir>
2. **IMPORTANT** - Set the API_KEY enviroment variable, this helps  to prevent your API from unauthorized ussage. You can use any UUID online generator for this, like this [UUID Generator](https://www.uuidgenerator.net/version1):
    ```
    export API_KEY=value
    ```
3. Build and start the Docker containers
    ```
    docker-compose up --build -d
    ```
    If you are running with `sudo`. You should run the below, otherwise it can not load the env variable:
    ```
    sudo -E docker-compose up --build -d
    ```

Note: If you want to change the API_KEY for any reason:
```
1. SSH to your server
2. sudo docker-compose stop
3. export API_KEY=new_value
4. sudo -E docker-compose up --build -d
```

## Ussage
To use the TTS API, make a POST request to the API endpoint with the text you want to convert:
```
curl --location 'https://yourdomain.com/tts' \
--header 'x-api-key: sample_api_key' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Hello world, this is a test",
    "voice": "en-US-ChristopherNeural",   
    "rate": 20,
    "volume": -50
}'
```