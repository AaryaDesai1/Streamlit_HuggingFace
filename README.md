# Streamlit_HuggingFace

[![CI/CD Pipeline](https://github.com/AaryaDesai1/Streamlit_HuggingFace/actions/workflows/actions.yml/badge.svg)](https://github.com/AaryaDesai1/Streamlit_HuggingFace/actions/workflows/actions.yml)

## Objective
This week's mini project was aimed at creating a Streamlit app that uses a Hugging Face model to generate text. The app was containerized and deployed using Docker.

## Steps

### 1. Create a Streamlit App
The Streamlit app was extremely easy to create and I did so by converting my previous flask app into a Streamlit app. The app was created in a file called [`app.py`](https://github.com/AaryaDesai1/Streamlit_HuggingFace/blob/main/app.py).

**Contents of the app.py file:**
The app.py file comprises of 3 main sections:
**i. Importing the necessary libraries and setting up Hugging Face model:** The first section of the app.py file imports the necessary libraries, including Streamlit, Transformers, and TensorFlow. It also loads the Hugging Face model (GPT-2) using the TFAutoModelForCausalLM class from the Transformers library.
```python
import streamlit as st
from transformers import pipeline, set_seed

# Set up the text generation pipeline with GPT-2 model
text_generator = pipeline("text-generation")
set_seed(42)
```

**ii. Function for generating text:** For my app, I wanted users to be able to input their personal traits and have the model generate potential career choices for them as a response based on those traits. I created a function called generate_professions that takes the user input as an argument and generates text using the Hugging Face model.
```python
def generate_professions(input_traits):
    # Construct the prompt sentence
    prompt = f"The best professions for someone with the following traits and/or skills {input_traits} are:"

    # Generate text using GPT-2 based on the constructed prompt
    generated_texts = text_generator(
        prompt,
        max_length=50,
        num_return_sequences=3,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
    )

    # Extract the generated texts excluding the original prompt
    generated_professions = [
        generated_text["generated_text"].replace(prompt, "")
        for generated_text in generated_texts
    ]

    return generated_professions
```
As you can see I have set certain parameters for the model to generate the text. The max_length is set to 50, which means the maximum number of tokens in the generated text is 50. The num_return_sequences is set to 3, which means the model will generate 3 different sequences of text. The temperature is set to 0.7, which controls the randomness of the generated text. The top_k and top_p parameters are used to filter the tokens during text generation.

**iii. Main function for Streamlit app:** The main function of the Streamlit app is where the user interface is defined. The user interface includes a text input field for users to enter their personal traits, a button to generate career choices based on the input traits, and a section to display the generated career choices. The main function also calls the generate_professions function to generate career choices based on the user input.
```python
def main():
    st.title("Professions Generator")

    input_traits = st.text_input("Enter traits and/or skills:")
    if st.button("Generate"):
        generated_professions = generate_professions(input_traits)
        st.markdown("### Generated Professions:")
        for profession in generated_professions:
            st.write(profession)

if __name__ == "__main__":
    main()
```

### 2. Create a Dockerfile
The Dockerfile was created to containerize the Streamlit app. The Dockerfile was created in a file called [`Dockerfile`](https://github.com/AaryaDesai1/Streamlit_HuggingFace/blob/main/Dockerfile).
**Contents of the Dockerfile:**
The Dockerfile comprises of 8 steps:
i. FROM python:3.10: Specifies the base image to use for the Docker container, which is an official Python 3.10 image.

ii. `RUN pip install tf-keras`: Installs the tf-keras package using pip, providing compatibility with Keras 2.x for Transformers library.

iii. `WORKDIR /app`: Sets the working directory inside the Docker container to /app, where the application code will be located.

iv. `COPY requirements.txt .`: Copies the requirements.txt file from the host machine to the /app directory inside the Docker container.

v. `RUN pip install -r requirements.txt`: Installs the Python dependencies specified in the requirements.txt file using pip.

vi. `COPY . .`: Copies all files from the current directory (including the application code) on the host machine to the /app directory inside the Docker container.

vii. `EXPOSE 8501`: Exposes port 8501 in the Docker container, which is the default port used by Streamlit applications.

viii. `CMD ["streamlit", "run", "--server.port=8501", "app.py"]`: Specifies the command to run when the Docker container starts, which is to run the Streamlit application (app.py) using the streamlit run command and specify the port as 8501.

### 3. Build the Docker Image
The Docker image was built using the following commands:
```bash
docker build -t my_streamlit_app .
```

### 4. Run the Docker Container
The Docker container was run using the following command:
```bash
docker run -p 8501:8501 my_streamlit_app

```

### 5. Access the Streamlit App
The Streamlit app was accessed by navigating to http://localhost:8501 in a web browser. If you see the screenshot below, I could access the Streamlit app from my Docker application directly. 
<img width="1255" alt="Screenshot 2024-04-06 at 3 26 53 PM" src="https://github.com/AaryaDesai1/Streamlit_HuggingFace/assets/143753050/e9eb54fc-6b15-4ee9-9d2e-5215b6245a91">

The following screenshots show the succesfull deployment of the Streamlit app using Docker:
<img width="1708" alt="Screenshot 2024-04-06 at 3 26 12 PM" src="https://github.com/AaryaDesai1/Streamlit_HuggingFace/assets/143753050/81ba6c02-f20c-4400-b662-85780eb23c52">

This is what is looks like when it's loading the answers using the Hugging Face model:
<img width="328" alt="Screenshot 2024-04-06 at 3 26 19 PM" src="https://github.com/AaryaDesai1/Streamlit_HuggingFace/assets/143753050/fb436bf9-7432-49c5-b8d4-0d029ed050e3">

And finally, this is what the output looks like. Not too comprehensive but it's a start!
<img width="1700" alt="Screenshot 2024-04-06 at 3 26 30 PM" src="https://github.com/AaryaDesai1/Streamlit_HuggingFace/assets/143753050/cbc1af16-8874-4654-bcd7-b56d6d7ae444">


## Conclusion, 

Overall, I think my experience using Streamlit was better than using Flask. It was much easier to create a web app using Streamlit and the deployment process was also quite straightforward. I was able to containerize the Streamlit app using Docker and deploy it successfully. Also, the user interface of the Streamlit app was more interactive and visually appealing compared to the Flask app. I look forward to exploring more features of Streamlit in the future and creating more interactive web applications.




