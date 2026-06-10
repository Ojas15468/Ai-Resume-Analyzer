from groq import Groq 
import os 
from dotenv import load_dotenv
load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))

import fitz

# PDF se text nikalo
doc = fitz.open(r"C:\Users\Naman\OneDrive\Desktop\LLM\MODULE 3\resume.pdf")
text = ""
for page in doc:
    text += page.get_text()

# Yeh text ab resume variable ki jagah use karo!


response=client.chat.completions.create(
          model="llama-3.3-70b-versatile",
          
          messages=[{"role": "system", "content": """
You are an expert resume analyzer.
analyze the resume step by step and provide the best solution
Reply in JSON format only:
{
    "overall_score": "",
    "issues": [
        {
            "problem": "",
            "solution": ""
        }
    ],
    "improvements": []
}
"""},
{"role": "user", "content": f"Analyze this resume:\n{text}"}
]
)
# print(response.choices[0].message.content)

import json

content = response.choices[0].message.content
content = content.replace("```json", "").replace("```", "").strip()
data = json.loads(content)
from tabulate import tabulate

# Table banane ke liye data chahiye — list of lists
table_data = []
for issue in data['issues']:
    table_data.append([issue['problem'], issue['solution']])



print(f"Score: {data['overall_score']}/10")
print(f"\nIssues found: {len(data['issues'])}")
print(tabulate(table_data, headers=["Problem", "Solution"], tablefmt="grid"))

print(f"\nImprovements:")
for i, imp in enumerate(data['improvements'], 1):
    print(f"{i}. {imp}")
