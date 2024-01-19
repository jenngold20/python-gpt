import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages =[
        {
            "role": "user",
            "content": "dame una lista de proyectos en Python"
        }
    ],
    #maxTokens=100,
)

print(response)