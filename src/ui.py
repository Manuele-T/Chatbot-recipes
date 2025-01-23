import gradio as gr
from chatbot_integration import chatbot_query

def chatbot_interface(user_input):
    return chatbot_query(query_type="openai", prompt=user_input, ingredient=user_input)

interface = gr.Interface(
    fn=chatbot_interface,
    inputs=[
        gr.Textbox(lines=2, placeholder="Type your input here", label="Type your question!")
    ],
    outputs="text",
    title="Cooking Chatbot",
    description="Type a keyword or ask a recipe-related question!"
)

interface.launch()