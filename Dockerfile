# Uses the official Python 3.9 image as the base for the container
FROM python:3.9
# Sets the working directory inside the container
WORKDIR /app
# Copies all files from the current directory on the host to /app in the containe
COPY . /app
# Installs Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt
# Documents that the container listens on port 5000 at runtime
EXPOSE 5000
# Specifies the command to run the application using Python when the container starts 
CMD ["python", "app.py"]
                             