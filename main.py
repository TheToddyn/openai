from openai import OpenAI


client = OpenAI(api_key="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")

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choises[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["quit", "exit", "bye", "sair", "tchau"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
