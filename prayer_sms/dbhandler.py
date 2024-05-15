
import boto3

INTENTION_TABLE_NAME = 'PrayerIntentionTable'
DYNAMO_DB_CLIENT = boto3.client('dynamodb')

def get_random_prayer():
    response = DYNAMO_DB_CLIENT.scan(
        TableName = INTENTION_TABLE_NAME
    )

    return response
