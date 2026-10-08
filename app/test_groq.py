import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])
MODEL = os.getenv("LLM_MODEL", "openai/gpt-oss-20b")

resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Say hello in five words."}],
)
print(f"(model: {MODEL})")
print(resp.choices[0].message.content)