import os
import re

TIMEZONE = "Asia/Tokyo"

# Logging
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(name)s : %(message)s"
ANSI_ESCAPE_PATTERN = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")

# AWS
AWS_TOPIC_ARN = os.environ["AWS_TOPIC_ARN"]
AWS_BUCKET_NAME = os.environ["AWS_BUCKET_NAME"]
