import zipfile
import json
from tqdm import tqdm 
import pandas as pd
import random

def read_json_from_zip(zip_ref, json_filename):
    with zip_ref.open(json_filename) as json_file:
        data = json.load(json_file)
        return data

def extract_all_json(zip_path, base_folder, output_path):
    selected_data = []

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # zip 파일 내 모든 JSON 파일 경로를 리스트로 생성
        all_files = [file_info for file_info in zip_ref.infolist() 
                     if file_info.filename.startswith(base_folder) and file_info.filename.endswith('.json')]
        
        # 진행 상황 표시를 위한 tqdm 설정
        for file_info in tqdm(all_files, desc="Processing JSON files"):
            # JSON 파일 읽기
            data = read_json_from_zip(zip_ref, file_info.filename)
            # 'fileName','question','disease_name_kor','intention' 필드만 추출
            selected_data.append({
                'fileName': data['fileName'],
                'disease_name': data['disease_name']['kor'],
                'intention': data['intention'],
                'question': data['question']
            })

    # 모든 데이터를 하나의 JSON 파일로 저장
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(selected_data, outfile, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    zip_file_path = "TL.zip"  # zip 파일 경로
    base_folder = "1.질문/"  # 찾고자 하는 하위 폴더의 루트 경로
    output_json_path = "AI-healthcare-Qonly.json"  # 저장할 새로운 JSON 파일 경로

    # 지정된 폴더 내 모든 JSON 파일에서 필요한 데이터 추출 후 저장
    extract_all_json(zip_file_path, base_folder, output_json_path)
    
    print(f"Selected data from all JSON files saved to {output_json_path}")

    # JSONL 파일 경로
    file_path = "AI-healthcare-Qonly.jsonl"
    output_file_path = "AI-healthcare-Qonly-sampled.jsonl"

    # 데이터 저장용 리스트
    data_list = []

    # JSONL 파일을 한 줄씩 읽어 DataFrame으로 변환
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        data_list = [json.loads(line) for line in lines]

    # DataFrame으로 변환
    df = pd.DataFrame(data_list)

    # (disease_name, intention) 쌍의 고유한 조합
    distinct_pairs = df[['disease_name', 'intention']].drop_duplicates()

    # 샘플 데이터 저장용 리스트
    samples = []

    # 각 distinct pair에 대해 3개의 랜덤 샘플 추출
    for _, pair in tqdm(distinct_pairs.iterrows(), total=distinct_pairs.shape[0], desc="Sampling"):
        pair_data = df[(df['disease_name'] == pair['disease_name']) & (df['intention'] == pair['intention'])]
        if len(pair_data) >= 3:
            sampled_data = pair_data.sample(n=3, random_state=42).to_dict(orient='records')
            samples.extend(sampled_data)
        elif len(pair_data) > 0:
            sampled_data = pair_data.to_dict(orient='records')
            samples.extend(sampled_data)

    # 샘플 데이터를 JSONL 형식으로 저장
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for sample in samples:
            file.write(json.dumps(sample, ensure_ascii=False) + '\n')

    print(f"Random samples saved to {output_file_path}. Total samples: {len(samples)}") # 12130