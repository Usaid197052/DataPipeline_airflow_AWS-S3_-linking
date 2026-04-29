import boto3

s3 = boto3.client(
    's3',
    access_key_id='key_id',
    secret-access_key='Secret_key_id',
    region_name='your_region'
)

file_name = "/opt/airflow/data/processed/cleaned_api_data.csv"
bucket_name = "usaid-data-pipeline-bucket"
object_name = "cleaned_api_data.csv"

s3.upload_file(file_name, bucket_name, object_name)

print("File uploaded successfully!")