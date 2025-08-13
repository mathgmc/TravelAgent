import json
from settings.sqs import get_agent_question_queue, get_agent_answer_queue


def send_to_queue(question: str, user_id: str):
    """
    Send a question message to the agent question queue.
    """
    question_queue = get_agent_question_queue()
    message_body = json.dumps({
        "question": question,
        "user_id": user_id
    })
    question_queue.send_message(MessageBody=message_body)
    print(f"Sent question to queue: {question} for user ID: {user_id}")


def receive_from_queue():
    """
    Receive messages from the agent answer queue.
    """
    answer_queue = get_agent_answer_queue()
    
    while True:
        messages = answer_queue.receive_messages(MaxNumberOfMessages=10, WaitTimeSeconds=20)
        if not messages:
            print("No messages received.")
            continue
        else:
            for message in messages:
                print(f"Received message from queue: {message.body}")
                message.delete()

                body = json.loads(message.body)
                print(f"Answer: {body}")
                
                # Delete the message after processing
                print("Message deleted from queue.")
            break

if __name__ == "__main__":
    while True:
        question = input()
        send_to_queue(question, user_id="12345")
        receive_from_queue()
        # This loop will continuously send questions and receive answers