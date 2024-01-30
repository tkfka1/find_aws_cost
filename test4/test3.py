import boto3
import json

# AWS Price List Service client 생성
client = boto3.client('pricing', region_name='us-east-1')


# 필터 설정 예시 (온디맨드)
filters = [
    {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': 't4g.nano'},
    {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'Asia Pacific (Seoul)'},
    {'Type': 'TERM_MATCH', 'Field': 'termType', 'Value': 'SavingsPlan'},
    # 추가 필터가 필요할 수 있음 (예: 운영 체제, 예약 옵션 등)
]

# API 호출
response = client.get_products(ServiceCode='AmazonEC2', Filters=filters)


# # 결과 처리
# print(json.dumps(json.loads(response['PriceList']), indent=4))
#     # print(json.loads(price))




ri_filters = [
    {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': 't4g.nano'},
    {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'Asia Pacific (Seoul)'},
    {'Type': 'TERM_MATCH', 'Field': 'termType', 'Value': 'Reserved'},
    {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
    {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'}        
    # 추가 필터를 적용할 수 있음 (예: 예약 기간, 결제 옵션 등)
]

# 필터 설정 예시 (세이빙 플랜)
sp_filters = [
    {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': 't4g.nano'},
    {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': 'Asia Pacific (Seoul)'},
    {'Type': 'TERM_MATCH', 'Field': 'termType', 'Value': 'OnDemand'},
    {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
    {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'}
    # 추가 필터를 적용할 수 있음 (예: 세이빙 플랜 유형, 기간 등)
]

# 예약 인스턴스 API 호출
ri_response = client.get_products(ServiceCode='AmazonEC2', Filters=ri_filters)

# 세이빙 플랜 API 호출
sp_response = client.get_products(ServiceCode='AmazonEC2', Filters=sp_filters)

# # 예약 인스턴스 결과 처리
# for price in ri_response['PriceList']:
#     temp =json.loads(price)
#     temp2 = json.dumps(temp,indent=4)
#     print(temp2)


# 세이빙 플랜 결과 처리
for k,price in enumerate(sp_response['PriceList']):
    temp =json.loads(price)
    temp2 = json.dumps(temp,indent=4)
    print(temp2)
    info_name = f"sp_price_info_name{k}.json"
    with open(info_name, 'w') as file:
        json.dump(temp, file, indent=4)