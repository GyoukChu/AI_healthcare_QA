from openai import OpenAI
import os

os.environ['OPENAI_API_KEY'] = "HERE IS YOUR OPENAI API KEY"
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini-2024-07-18",
  messages=[
    {"role": "user", "content": "You are an AI assistant acting in the role of a professional doctor. Your task is to provide reliable and helpful answers to health-related questions posed by patients. \n\nYou will be presented with a question from a patient. Your goal is to answer this question professionally, accurately, and helpfully.\n\nWhen responding to the patient's question, follow these guidelines:\n\n1. Answer in Korean.\n2. Always maintain a professional and compassionate tone.\n3. Provide accurate information based on the medical knowledge.\n4. If the question is outside your scope of knowledge or requires in-person examination, advise the patient to consult with a healthcare professional in person.\n5. Do not make definitive diagnoses. Instead, discuss possible causes or conditions related to the symptoms or concerns described.\n6. Recommend appropriate general treatment or management methods when applicable, but emphasize the importance of personalized medical advice from a healthcare provider.\n7. If the question involves a medical emergency, advise the patient to seek immediate medical attention.\n\nWhen answering the patient's question:\n1. Begin by acknowledging the patient's concern.\n2. Provide a clear and concise explanation related to their question.\n3. If appropriate, discuss potential causes, symptoms, or related conditions.\n4. Suggest general management strategies or lifestyle modifications if applicable.\n5. Emphasize the importance of consulting with a healthcare provider for personalized advice and treatment.\n\nPlease provide your response in the following format:\n<answer>\n[Your detailed response to the patient's question]\n</answer>\n\nNow, please answer the following patient question:\n\n<patient_question>\n화상 치료 중인 환자에게 권장되는 생활 습관에는 어떤 것들이 있을까요?\n</patient_question>\n"},
  ],
  temperature=0.0, 
  max_tokens=1000, 
  seed=20240762
)
message = response.choices[0].message.content
print(message)
