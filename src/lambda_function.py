from datetime import datetime
from logging import INFO, getLogger

import pytz

from libs.aws import S3, SNS
from settings import AWS_BUCKET_NAME, AWS_TOPIC_ARN, TIMEZONE
from utils.timer import timer

root_logger = getLogger()
root_logger.setLevel(INFO)
root_logger.handlers = []


def lambda_handler(event: dict, context: dict) -> dict:
    process_event(event)
    return {"statusCode": 200, "body": "ok"}


@timer
def process_event(event: dict) -> None:
    jst = pytz.timezone(TIMEZONE)
    now = datetime.now(jst)
    today = now.strftime("%Y-%m-%d")
    hour = now.hour

    S3.init_logger()
    s3 = S3(bucket_name=AWS_BUCKET_NAME)

    SNS.init_logger()
    sns = SNS(topic_arn=AWS_TOPIC_ARN)

    # Save data to S3
    key = f"{today}/{hour}.json"
    s3.save(key, [])

    # Publish SNS
    sns.publish(
        message="Message",
        subject="Lambda function completed",
    )


if __name__ == "__main__":
    lambda_handler(None, None)
