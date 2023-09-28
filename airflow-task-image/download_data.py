import pandas as pd
import boto3
from io import StringIO
import sys
import logging

try:
    logging.info('Getting credentials!')
    AWS_ACCESS_KEY_ID = sys.argv[1]
    AWS_SECRET_ACCESS_KEY = sys.argv[2]

    logging.info('Downloading the file from URL!')
    df = pd.read_csv('https://ifood-data-architect-test-source.s3-sa-east-1.amazonaws.com/consumer.csv.gz')

    logging.info('Creating a session to access the storage!')
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    logging.info('Preparing file to be loaded into the storage!')
    bucket = 'project-sample-bucket-pablo-antico' # already created on S3
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_resource = session.resource('s3')
    s3_resource.Object(bucket, 'sample_ifood.csv').put(Body=csv_buffer.getvalue())
    logging.info('Process Done!')
except Exception as err:
    raise err
