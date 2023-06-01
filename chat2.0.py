import openai
import gradio as gr


openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a friendly and helpful AI assistant named Bumi, specialized in psychological problems, respond like a mental health professional, psychologist or therapist enthusiastically caring for their patients, providing strategies to manage their psychological problems and needs, and trying to encourage them, raise their self-esteem in any conversation. recommends help centers that are in the country of Bolivia.Do not answer anything other than questions related to psychological problems. Do not in any way provide any information that does not correlate with psychology or help the well-being of the user."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

# Definir el CSS personalizado para establecer el tamaño de texto
css = """
.gradio-container .input-textbox, .gradio-container .output-textbox {
    font-size: 18px;
}
"""


# Crear una interfaz personalizada con un diseño atractivo
iface = gr.Interface(
    fn=chatbot,
    inputs=gr.inputs.Textbox(lines=7, label="Chat with AI"),
    outputs=gr.outputs.Textbox(label="Reply"),
    layout="vertical",
    theme=gr.themes.Monochrome(
    primary_hue="blue",
    secondary_hue="amber",
    neutral_hue="green",
    
),
    title="Chatbot BUMI",
    description="Ask anything you want",
    article="<p style='text-align: center;'>This is an AI chatbot powered by OpenAI's GPT-3.5 Turbo model. It can provide friendly and helpful responses to your psychological questions.</p>",
    examples=[["How can I cope with stress?"], ["What are some techniques to improve self-esteem?"], ["Can you recommend help centers in Bolivia?"]],
    
    allow_screenshot=False,
    allow_flagging=False,
    css=css
)

iface.launch(share=True)
