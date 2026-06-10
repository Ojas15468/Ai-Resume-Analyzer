from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))
# response=client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[{"role": "user" , "content": " Tell me about cat"}]
    
# )
# print(response.choices[0].message.content)

# response=client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[{"role" : "user", "content" : "tell me 3 fun facts about the dog in simple English. Each line should be contains only one line. "}]
# )
# print(response.choices[0].message.content)



# response=client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[{"role": "user", "content": """reply with only sad or happy. :
# 'i got my salary : happy'
# 'i lost my money in game : sad'
# 'i meet my cousin after a long time : happy'

# now classify this:
# 'i meet my friend' ->"""}]
# )
# print(response.choices[0].message.content)


# response=client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[{"role": "user" , "content": "What is recursion?"}]
# )
# print(response.choices[0].message.content)

# response=client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[{"role": "system", "content": " you are a teacher who explains everthing using funny real life examples. keep answers under 3 lines."},
#     {"role": "user", "content": "What is recursion?"}
#     ]
# )
# print(response.choices[0].message.content)

# # System prompt Examples
# response=client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[{"role": "system", "content": " you are a strict teacher who explains everything in strict terms. keep answers under 3 lines."},
#     {"role": "user", "content": "What is a function?"}
#     ]
# )
# print(response.choices[0].message.content)


#Cot = Chain of Thought in this concept we ask the model to verify the step by step solution to the problem. This is very useful for complex problems 
    #   where the model can make mistakes in the final answer but can get the steps right. By asking the model to think step by step, we can increase the chances of getting the correct answer.

# #without CoT
# response=client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     # Bina CoT
#     messages=[
#     {"role": "system", "content": "Answer directly, no explanation."},
#     {"role": "user", "content": """A store has a 20% discount on a shirt worth 500 rupees. 
# There is also 18% GST applied AFTER the discount. 
# If you buy 3 shirts, and you have a coupon for 50 rupees off the total,
# what is the final amount you pay?"""}
# ]
# )
# print(response.choices[0].message.content)


# #Cot concept ke saath 
# response=client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
    
#     # CoT ke saath
# messages=[
#     {"role": "user", "content": """A store has a 20% discount on a shirt worth 500 rupees. 
# There is also 18% GST applied AFTER the discount. 
# If you buy 3 shirts, and you have a coupon for 50 rupees off the total,
# what is the final amount you pay?

# Think step by step."""}
# ]
# )
# print(response.choices[0].message.content)



# Structured Output (JSON) 

# response=client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
    
#     messages=[
#     {"role": "user", "content": "Tell me about Virat Kohli"}
# ]
# )
# print(response.choices[0].message.content)


# Structured Output (JSON) with system prompt to enforce JSON format

response=client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    
    messages=[
    {"role": "system", "content": """You are a data extractor. 
Always respond in JSON format only. 
No extra text, no explanation."""},
    {"role": "user", "content": """Tell me about Virat Kohli in this exact JSON format:
{
    "name": "",
    "age": "",
    "country": "",
    "role": "",
    "top_3_records": []
}"""}
]
)
print(response.choices[0].message.content)



import json

# JSON string ko Python dict mein convert karo
data = json.loads(response.choices[0].message.content)

# Ab seedha values nikalo!
print(data["name"])          # Virat Kohli
print(data["country"])       # India
print(data["top_3_records"]) # list of records