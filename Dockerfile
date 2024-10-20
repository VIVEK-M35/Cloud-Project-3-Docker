# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home/data

# Copy the Python script and text files to the container
COPY script.py .
COPY IF.txt .
COPY AlwaysRememberUsThisWay.txt .

# Create output directory
RUN mkdir -p /home/data/output

# Run the Python script
CMD ["python", "script.py"]
