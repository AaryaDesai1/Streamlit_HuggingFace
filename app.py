import streamlit as st
from transformers import pipeline, set_seed

# Set up the text generation pipeline with GPT-2 model
text_generator = pipeline("text-generation")
set_seed(42)  # Optional: Set a seed for reproducibility

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
