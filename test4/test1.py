import boto3
import json

# AWS Price List Service client 생성
pricing_client = boto3.client('pricing', region_name='us-east-1')

# EC2 Reserved Instances의 가격 정보 가져오기
def get_reserved_instances_price(instance_type, lease_contract_length, purchase_option, region):
    try:
        response = pricing_client.get_products(
            ServiceCode='AmazonEC2',
            Filters=[
                {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type},
                {'Type': 'TERM_MATCH', 'Field': 'leaseContractLength', 'Value': lease_contract_length},
                {'Type': 'TERM_MATCH', 'Field': 'purchaseOption', 'Value': purchase_option},
                {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': region},
                {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
                {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'}
            ],
            MaxResults=100
        )
        return json.loads(response['PriceList'][0])
    except Exception as e:
        print(f"Error fetching pricing info: {e}")
        return None

def get_aws_pricing_info(instance_type, lease_contract_length, purchase_option, region):
    try:
        # Reserved Instances 정보 가져오기
        ri_response = pricing_client.get_products(
            ServiceCode='AmazonEC2',
            Filters=[
                {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type},
                {'Type': 'TERM_MATCH', 'Field': 'leaseContractLength', 'Value': lease_contract_length},
                {'Type': 'TERM_MATCH', 'Field': 'purchaseOption', 'Value': purchase_option},
                {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': region},
                {'Type': 'TERM_MATCH', 'Field': 'preInstalledSw', 'Value': 'NA'},
                {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'}
            ],
            MaxResults=100
        )

        # Savings Plans 정보 가져오기
        sp_response = pricing_client.get_products(
            ServiceCode='AmazonEC2',
            Filters=[
                {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': region},
                {'Type': 'TERM_MATCH', 'Field': 'productFamily', 'Value': 'Compute Savings Plans'}
            ],
            MaxResults=100
        )

        return json.loads(ri_response['PriceList'][0]), json.loads(sp_response['PriceList'][0])
    except Exception as e:
        print(f"Error fetching pricing info: {e}")
        return None, None


# # ap-northeast-1 (도쿄) 리전 설정
# region = 'Asia Pacific (Tokyo)'
# ap-northeast-2 (서울) 리전 설정
region = 'Asia Pacific (Seoul)'


# # t4g.nano 인스턴스에 대한 1년 및 3년 컴퓨팅 절감형 플랜 가격 정보 가져오기
# instance_type = 't4g.nano'
# for lease_contract_length in ['1yr', '3yr']:
#     for purchase_option in ['No Upfront', 'Partial Upfront', 'All Upfront']:
#         price_info = get_reserved_instances_price(instance_type, lease_contract_length, purchase_option, region)
#         if price_info:
#             print(f"Region: {region}, Lease Contract Length: {lease_contract_length}, Purchase Option: {purchase_option}")
#             print(json.dumps(price_info, indent=4))


price_info = get_reserved_instances_price('t4g.nano', '1yr', 'No Upfront', region)
if price_info:
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(f"Region: {region}, Lease Contract Length: '1yr', Purchase Option: 'No Upfront'")
    print(json.dumps(price_info, indent=4))



# # t4g.nano 인스턴스에 대한 1년 및 3년 컴퓨팅 절감형 플랜 가격 정보 가져오기
# instance_type = 't4g.nano'
# for lease_contract_length in ['1yr', '3yr']:
#     for purchase_option in ['No Upfront', 'Partial Upfront', 'All Upfront']:
#         ri_price_info, sp_price_info = get_aws_pricing_info(instance_type, lease_contract_length, purchase_option, region)
#         if ri_price_info and sp_price_info:
#             print(f"Region: {region}, Lease Contract Length: {lease_contract_length}, Purchase Option: {purchase_option}")
            
#             print("Reserved Instances Pricing:")
#             ri_price_info_name = "price_info_ri.json"
#             with open(ri_price_info_name, 'w') as file:
#                 json.dump(ri_price_info, file, indent=4)

#             print("Savings Plans Pricing:")
#             sp_price_info_name = "price_info_sp.json"
#             with open(sp_price_info_name, 'w') as file:
#                 json.dump(sp_price_info, file, indent=4)