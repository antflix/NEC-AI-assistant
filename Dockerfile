# Use the PyTorch image with CUDA and cuDNN support
FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 6000 for the Flask app
EXPOSE 6000

# Set environment variables (do not include actual values here)
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
# Add any other environment variables as needed

# Command to run the application
CMD ["python", "app.py"]