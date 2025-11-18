import streamlit as st
import ollama

def generate_llm_response(prompt,model = "llama3.2"):

    messages = [
        {
            'role':'user',
            'content':prompt
        }
    ]
    response = ollama.chat(model=model,messages=messages)
    return response['message']['content']

st.title("LLM Text Generator")
st.write("intract with a Large Modl (LLM) and generate response.")

user_prompt = st.text_area("Enter your prompt")

if st.button("Generate Response"):
    if user_prompt.strip() != "":
        with st.spinner("Generating response..."):
            try:
                response = generate_llm_response(user_prompt)
                st.success("Response generated!")
                st.text_area("LLM Response:",value=response,height=200)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a prompt")
