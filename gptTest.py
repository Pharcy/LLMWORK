from openai import OpenAI
client = OpenAI()

systemMessage = "You are a tour guide, make sure to be helpful and throw in historical information along with answers"
userMessage = "I am touring laramie, what are some local favorite spots"
testNum = "5"

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
    file.write("system: " +systemMessage + "\nuser: " + userMessage + "\n\n")
    file.write(response)
