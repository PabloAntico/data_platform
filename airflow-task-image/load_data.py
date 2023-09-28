import pandas as pd
import boto3
import sys
import logging

try:
    logging.info('Getting credentials!')
    AWS_ACCESS_KEY_ID = sys.argv[1]
    AWS_SECRET_ACCESS_KEY = sys.argv[2]

    logging.info('Creating a session to access the storage!')
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    logging.info('Reading the file in the storage!')
    s3 = session.client('s3')
    response = s3.get_object(
        Bucket='project-sample-bucket-pablo-antico',
        Key='sample_ifood.csv'
    )

    file = pd.read_csv(response.get("Body"))
    head = file.head()

    print(head)
    logging.info('Process Done!')
except Exception as err:
    raise err
