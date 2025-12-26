from fastapi import FastAPI
from openai import OpenAI
import uvicorn


# Models.Base.metadata.create_all(bind=engine)
app = FastAPI()




def service_deepseek(otazka: str):
    client = OpenAI(api_key="sk-64b3912c13324e439241138f10489762", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "меня зовут герман"},
            {"role": "user", "content": otazka},
        ],
        max_tokens=1024,
        temperature=0.7,
        stream=False
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

@app.get("/otazka")
async def promt(otazka: str):

    return service_deepseek(otazka)

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.77.23", port=8001)