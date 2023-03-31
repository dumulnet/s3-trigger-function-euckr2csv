import boto3
import urllib


INPUT_FILE_ENCODING='EUC-KR'

OUTPUT_BUCKET_NAME='replica-output-data'
OUTPUT_FILE_PATH='utf8'

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print(event)

    # Get object from S3
    bucket = event['Records'][0]['s3']['bucket']['name']
    objkey = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    # if not objkey.endswith('.csv') and not objkey.endswith('.CSV'):
    #     print("File type is missing.")
    #     return {'status_code': 200}
    # else:
    
    print("Previous training data loading...")
    response = s3.get_object(Bucket=bucket, Key=objkey)
    body = response['Body'].read().decode(INPUT_FILE_ENCODING)
    
    s3obj = boto3.resource('s3')
    output_object = s3obj.Object(OUTPUT_BUCKET_NAME, OUTPUT_FILE_PATH + '/' + objkey)
    output_object.put(Body = body)
            

    return {'status_code': 200}
    

