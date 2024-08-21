from openai import OpenAI
import os

os.environ['OPENAI_API_KEY'] = "HERE IS YOUR OPENAI API KEY"
client = OpenAI()
print(client.batches.list(limit=10)) # Completion 확인 용

######################## CAUTION!!!!! ########################
# CAUTION 주석 블록에 있는 아래 코드는 한번만 실행하고, 주석처리 하세요.
batch_input_file = client.files.create(
    file=open("./gpt_api_batch.jsonl", "rb"),
    purpose="batch"
)
batch_input_file_id = batch_input_file.id

batch_job = client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
)

print("**********BATCH JOB ID START**********")
print(batch_job.id)
print("**********BATCH JOB ID  END **********")
######################## CAUTION!!!!! ########################


# batch completion 확인한 뒤, (윗부분 주석 처리 후) 아래 코드 실행 
batch_job = client.batches.retrieve("HERE IS YOUR BATCH JOB ID")
result_file_id = batch_job.output_file_id
result = client.files.content(result_file_id).text
# print(result)
result_file_name = "AI-healthcare-sampled-gpt4o0806.jsonl"

with open(result_file_name, 'w', encoding='utf-8') as file:
    file.write(result)

import pandas as pd
temp = pd.read_json(result_file_name, lines=True)
temp.to_json("AI-healthcare-gpt4o0806-final.jsonl", index=False, lines=True, orient='records', force_ascii=False)
