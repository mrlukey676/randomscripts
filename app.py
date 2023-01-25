import openai
openai.api_key = "apikey"
end = False
inputPrompt = input("Enter a question: ")
response = openai.Completion.create(engine="text-davinci-002", prompt=inputPrompt)
print(response["choices"][0]["text"])
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while end == False:
    inputPrompt = input("Enter a question: ")
    if inputPrompt[0].lower() in alphabet:
        response = openai.Completion.create(engine="text-davinci-002", prompt=inputPrompt)
    elif inputPrompt[0] == "#":
        response = openai.Completion.create(engine="text-coding-001", prompt=inputPrompt[1:])
    response = openai.Completion.create(engine="text-davinci-002", prompt=inputPrompt)
    print(response["choices"][0]["text"])
