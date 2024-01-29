import boto3
import json


# Create AWS Pricing Client
pricing_client = boto3.client('pricing', region_name='us-east-1')

# Get pricing information for a specific RDS instance type in the ap-northeast-2 region
try:
    response_rds = pricing_client.get_products(
        ServiceCode='AmazonRDS',
        Filters=[
            {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'Asia Pacific (Seoul)'},
            {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': 'db.m5.large'}
        ],
        MaxResults=1
    )

    # Print the response for RDS pricing
    print(response_rds)

    # JSON 형식으로 변환
    json_data = json.dumps(response_rds, ensure_ascii=False, indent=4)

    # 파일에 저장
    with open('data.json', 'w', encoding='utf-8') as file:
        file.write(json_data)

except Exception as e:
    print(f"An error occurred: {e}")