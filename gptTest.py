from openai import OpenAI
client = OpenAI()

systemMessage = "You are a tourguide for wyoming, make sure to be helpful but consise"
userMessage = "I am currently in casper wyoming, please plan a 3 day trip to gillete"
testNum = "3"

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": systemMessage},
    {"role": "user", "content": userMessage }
  ]
)

response = completion.choices[0].message.content
with open("TestLogs.txt", "a") as file:
    file.write("\n\n\n\n************* Test Number: #" + testNum+ " ****************\n\n")
    file.write(systemMessage + "\n" + userMessage)
    file.write(response)
