import gradio as gr
from openai import OpenAI
from sk import my_sk

client=OpenAI(api_key=my_sk)
FINE_TUNED_MODEL = "ft:gpt-3.5-turbo-0125:personal:arielgpt:BQqTards"

intstructions_string_few_shot = """ArielGPT, functioning as a virtual data science consultant on YouTube, communicates in clear, accessible language, escalating to technical depth upon request. \
It reacts to feedback aptly and concludes with its signature '–-ArielGPT'. \
ArielGPT will tailor the length of its responses to match the viewer's comment, providing concise acknowledgments to brief expressions of gratitude or feedback, \
thus keeping the interaction natural and engaging. The length of the response is at most 70 words.

Here are some examples of ArielGPT responding to viewer comments.
Viewer comment: This was a very thorough introduction to LLMs and answered many questions I had. Thank you.
ArielGPT: Great to hear, glad it was helpful :) --ArielGPT

Viewer comment: Epic, very useful for my BCI class
ArielGPT: Thanks, glad to hear!  --ArielGPT

Viewer comment: Honestly the most straightforward explanation I've ever watched. Super excellent work Ariel. Thank you. It's so rare to find good communicators like you!
ArielGPT: Thanks, glad it was clear   --ArielGPT
"""




# --- Define your chatbot function ---

def chat_with_arielgpt(user_input, history):
    """
    Sends user input to your fine-tuned ShawGPT model and gets the reply.
    """

    response = client.chat.completions.create(
        model=FINE_TUNED_MODEL,
        messages=[
            {"role": "system", "content": intstructions_string_few_shot},
            {"role": "user", "content": user_input}
              ]
    )

    assistant_reply = dict(response)['choices'][0].message.content
    return assistant_reply

# --- Set up Gradio Chat Interface ---

chatbot = gr.ChatInterface(
    fn=chat_with_arielgpt,
    title="ArielGPT: YouTube Comment Responder",
    theme="default",
    examples=[
        "Great video, learned a lot!",
        "Can you explain more about fat tails?",
        "This was confusing at 3:24, can you clarify?",
        "Thanks for sharing this content!"
    ],
    description="A fine-tuned chatbot that replies to YouTube-style comments like Ariel"
)

# --- Launch App ---

if __name__ == "__main__":
    chatbot.launch(share=True)
