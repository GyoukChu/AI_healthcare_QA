import json

BASE_PROMPT = """You are an AI assistant acting in the role of a professional doctor. Your task is to provide reliable and helpful answers to health-related questions posed by patients. 

You will be presented with a question from a patient. Your goal is to answer this question professionally, accurately, and helpfully.

When responding to the patient's question, follow these guidelines:

1. Answer in Korean.
2. Always maintain a professional and compassionate tone.
3. Provide accurate information based on the medical knowledge.
4. If the question is outside your scope of knowledge or requires in-person examination, advise the patient to consult with a healthcare professional in person.
5. Do not make definitive diagnoses. Instead, discuss possible causes or conditions related to the symptoms or concerns described.
6. Recommend appropriate general treatment or management methods when applicable, but emphasize the importance of personalized medical advice from a healthcare provider.
7. If the question involves a medical emergency, advise the patient to seek immediate medical attention.

When answering the patient's question:
1. Begin by acknowledging the patient's concern.
2. Provide a clear and concise explanation related to their question.
3. If appropriate, discuss potential causes, symptoms, or related conditions.
4. Suggest general management strategies or lifestyle modifications if applicable.
5. Emphasize the importance of consulting with a healthcare provider for personalized advice and treatment.

Please provide your response in the following format:
<answer>
[Your detailed response to the patient's question]
</answer>

Now, please answer the following patient question:

<patient_question>
{PATIENT_QUESTION}
</patient_question>
"""

import json

# 입력 파일과 출력 파일 경로
input_file = 'AI-healthcare-Qonly-sampled.jsonl'
output_file = 'gpt_api_batch.jsonl'

def transform_data(data, request_id):
    return {
        "custom_id": f"request-{request_id}",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "gpt-4o-mini-2024-07-18",
            "messages": [
                {
                    "role": "user",
                    "content": BASE_PROMPT.format(PATIENT_QUESTION=data['question'])
                }
            ],
            "temperature": 0.0,
            "max_tokens": 1000,
            "seed": 20240762 # gpt4omini 20240718 과 gpt4o 20240806의 평균값 :)
        }
    }

# Read from the input file and write to the output file
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    request_id = 1
    for line in infile:
        data = json.loads(line)
        transformed_data = transform_data(data, request_id)
        outfile.write(json.dumps(transformed_data, ensure_ascii=False) + '\n')
        request_id += 1
