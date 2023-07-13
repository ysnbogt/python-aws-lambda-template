from __future__ import annotations

import json
from logging import getLogger
from typing import Any

import boto3

from utils.log_method import log_method
from utils.set_handlers import set_handlers


class AWS:
    logger = None

    def __init__(self) -> None:
        if self.logger is None:
            self.logger = getLogger(self.__class__.__name__)
            self.logger.disabled = True

    @classmethod
    def init_logger(cls, log_file_path: str = None) -> None:
        if cls.logger is None:
            cls.logger = getLogger(cls.__name__)
        cls.logger = set_handlers(cls.logger, log_file_path)
        cls.logger.disabled = False

    def check_response(
        self, response: Any, error_message: str, success_message: str
    ) -> None:
        if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
            self.logger.error(error_message)
            return
        self.logger.info(success_message)


class S3(AWS):
    def __init__(self, bucket_name: str) -> None:
        super().__init__()
        self.bucket_name = bucket_name
        self.client = boto3.client("s3")

    @log_method()
    def save(self, key: str, value: Any) -> None:
        json_data = json.dumps(value)
        response = self.client.put_object(
            Bucket=self.bucket_name, Key=key, Body=json_data
        )
        self.check_response(
            response,
            "Failed to save data to S3",
            "Saved data to S3",
        )

    @log_method()
    def get(self, key: str) -> Any:
        response = self.client.get_object(Bucket=self.bucket_name, Key=key)
        self.check_response(
            response,
            "Failed to get data from S3",
            "Got data from S3",
        )
        body = response["Body"].read()
        return json.loads(body.decode("utf-8"))


class SNS(AWS):
    def __init__(self, topic_arn: str) -> None:
        super().__init__()
        self.topic_arn = topic_arn
        self.client = boto3.client("sns")

    @log_method()
    def publish(self, subject: str, message: str) -> None:
        response = self.client.publish(
            TopicArn=self.topic_arn, Message=message, Subject=subject
        )
        self.check_response(
            response,
            "Failed to publish message to SNS",
            "Published message to SNS",
        )
