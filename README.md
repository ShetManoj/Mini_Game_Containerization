# Rock Paper Scissors Game (Flask)

This is a simple web-based implementation of the classic **Rock, Paper, Scissors** game using **Flask**. The game allows the user to select one of the three choices and pits them against a random choice made by the computer.

## Features
- Play against the computer in a fun, interactive way.
- Random computer choice on each game round.
- Clear results indicating a win, loss, or tie.
- Clean user interface built with HTML.

## Prerequisites
Before running this application, ensure you have the following installed on your system:
- [Python 3.9+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)

## Docker Setup

### 1. Build the Docker Image
To containerize the application, build the Docker image using the provided **Dockerfile**.
```bash
docker build -t rock-paper-scissors-app .

### 2. Run the Docker Container
Once the image is built, you can run the application inside a container:
```bash
docker run -p 5000:5000 rock-paper-scissors-app

