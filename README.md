# YouTube Comment Responder AI Assistant

This repository contains a full pipeline to build an AI assistant that responds to YouTube comments in a natural and engaging style, combining fine-tuning and prompt engineering techniques.

## Contents

1. **`YT-response-assistant-api.ipynb`**  
   Uses **prompt engineering** to instruct a GPT assistant on how to reply to YouTube comments naturally and conversationally.  
   It provides detailed instructions along with a few examples.  
   Additionally, it integrates **Retrieval-Augmented Generation (RAG)** to help the assistant answer knowledge-based questions more accurately.

2. **`fine-tuning-Youtube-Responder.ipynb`**  
   Fine-tunes the GPT model using real YouTube comment and response data (`YT-comments.csv`).  
   This step adapts the assistant's style to match the YouTuber’s unique "vibe" and communication style.

3. **`response-app.py`**  
   Builds a **Gradio chatbot app** powered by the fine-tuned model.  
   This app provides a user-friendly interface where users can interact with the assistant and test its responses live.

## How to Use

- Set your OpenAI API key in sk.py
- Run `response-app.py` to launch the chatbot locally.
- (Optional) Deploy to platforms like Hugging Face Spaces for public access.

---

✅ This project demonstrates the powerful combination of fine-tuning, RAG, and Gradio to create highly customized AI assistants!
