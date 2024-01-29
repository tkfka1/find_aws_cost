import boto3

# AWS Pricing Client 생성
pricing_client = boto3.client('pricing', region_name='us-east-1')
# pricing_client = boto3.client('pricing', region_name='ap-northeast-2')


# 특정 서비스의 가격 정보 가져오기
response = pricing_client.get_products(
    ServiceCode='AmazonEC2', # 예를 들어 Amazon EC2 서비스의 가격 정보를 조회
    Filters=[
        {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': 'm5.large'} # 필터 조건
    ],
    MaxResults=1
)

# 응답 출력
print(response)
