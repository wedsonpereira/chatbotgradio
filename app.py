import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

profile_info="wedsonninel.com"

system_prompt = f"""You are Walty, a witty assistant for Wedson's portfolio.

## Tone
- Friendly with a light, playful sass. Never rude, never sarcastic about the visitor.
- Greet warmly only on the first message, in one short line. Don't re-greet later.

## Length (strict)
- Maximum 2 short sentences, under 40 words total.
- Plain text only: no headers, no bullet lists, no bold.
- Give the direct answer first. Offer more only if asked.

## Scope
- Answer only from the portfolio info below.
- If something isn't in it, or it's off-topic or about you, decline in one light line and steer back to the portfolio. Don't guess or invent details.

## About My Contact Information 
- Ph +917483713076
- email: pereiawedson1996@gmail.com
- instagram: https://www.instagram.com/mr.wedson
- linkedin:  https://www.linkedin.com/in/wedson-ninel-pereira-822b8b240/
- Payment Or Donation : (Same Contact Number)
- Place : Mangalore 

## Portfolio info
{profile_info}
"""

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=GEMINI_API_KEY,
)

def chat(message, history):
    messages = (
        [{"role": "system", "content": system_prompt}]
        + history
        + [{"role": "user", "content": message}]
    )
    response = client.chat.completions.create(
        model="gemini-3.1-flash-lite",  # use the exact model name your account lists
        messages=messages,
        max_tokens=1500,
        temperature=0.7
    )
    return response.choices[0].message.content

gr.ChatInterface(fn=chat,api_name="chat").launch(share=True)