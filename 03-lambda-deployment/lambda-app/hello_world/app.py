import json

# import requests


def lambda_handler(event, context):


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "juneed baba v2",
            # "location": ip.text.replace("\n", "")
        }),
    }
