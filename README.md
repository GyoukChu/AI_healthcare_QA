# AI_healthcare_QA
AIHUB 초거대 AI 헬스케어 질의응답 데이터 subset GPT 답변

gpt4o-mini에 대한 코드 입니다.

1. data_process.py

기존 데이터에서 unique한 (disease_name, intention) pair에 대해 최대 3개 질문을 샘플링하는 코드입니다.

[[AIHUB]](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71762)에서 직접 데이터를 다운 받은 뒤, TL.zip 파일이 위치한 폴더에서 실행하세요.

2. make_batchfile_forgpt.py

OpenAI Batch API를 위해서, 1번에서 가져온 데이터를 jsonl 파일로 바꿉니다. 프롬프트도 들어가있습니다. 실행 후 결과물인, api calling에 보낼 gpt_api_batch.jsonl 파일도 첨부해두었습니다.

3. call_api_batch.py

gpt4o-mini에게 답변을 요청하는 파일입니다. **!주의! CAUTION block을 잘 보고 실행하세요.**
