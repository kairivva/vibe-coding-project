import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Придумай 3 креативных названия для моего проекта: автоматический мониторинг сайтов конкурентов",
        }
    ],
)

print(response.choices[0].message.content)
