import boto3
from settings.envs import (
    SQS_ENDPOINT,
    SQS_REGION,
    SQS_ACCESS_KEY,
    SQS_SECRET_KEY,
    AGENT_QUESTION_QUEUE,
    AGENT_ANSWER_QUEUE,
)


sqs = boto3.resource(
    "sqs",
    endpoint_url=SQS_ENDPOINT,
    region_name=SQS_REGION,
    aws_access_key_id=SQS_ACCESS_KEY,
    aws_secret_access_key=SQS_SECRET_KEY,
)

def get_queue(queue_name: str):
    """
    Get an SQS queue by name if it exists, otherwise create it.
    """
    try:
        queue = sqs.get_queue_by_name(QueueName=queue_name)
    except sqs.meta.client.exceptions.QueueDoesNotExist:
        queue = sqs.create_queue(QueueName=queue_name)
    return queue

def get_agent_question_queue():
    """
    Get the agent question queue.
    """
    return get_queue(AGENT_QUESTION_QUEUE)

def get_agent_answer_queue():
    """
    Get the agent answer queue.
    """
    return get_queue(AGENT_ANSWER_QUEUE)
