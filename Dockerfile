FROM python:3.10

# Install tf-keras
RUN pip install tf-keras

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application files
COPY . .

# Expose the port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "--server.port=8501", "app.py"]
