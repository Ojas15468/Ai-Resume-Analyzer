from groq import Groq 
import os 
from dotenv import load_dotenv
load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))

import fitz

# PDF se text nikalo
base_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(base_dir, "resume.pdf")
doc = fitz.open(pdf_path)
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


table_data = []
for issue in data['issues']:
    table_data.append([issue['problem'], issue['solution']])



print(f"Score: {data['overall_score']}")
print(f"\nIssues found: {len(data['issues'])}")
print(tabulate(table_data, headers=["Problem", "Solution"], tablefmt="grid"))

print(f"\nImprovements:")
for i, imp in enumerate(data['improvements'], 1):
    print(f"{i}. {imp}")
