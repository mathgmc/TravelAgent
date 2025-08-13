import json
from settings.sqs import get_agent_question_queue, get_agent_answer_queue
from schemas.queue_types import QuestionMessage
from travel_agent import agent_run


def run_worker():
    """
    Run the worker to process messages from the agent question queue and send answers to the agent answer queue.
    """
    question_queue = get_agent_question_queue()
    answer_queue = get_agent_answer_queue()

    while True:
        # Receive messages from the question queue
        messages = question_queue.receive_messages(MaxNumberOfMessages=10, WaitTimeSeconds=20)
        
        for message in messages:
            try:
                data = json.loads(message.body)

                question_message = QuestionMessage(**data)

                # Run the agent with the received question and user ID
                response = agent_run(
                    question=question_message.question,
                    user_id=question_message.user_id
                )
                
                # Send the response to the answer queue
                answer_queue.send_message(MessageBody=json.dumps(response))
                
                # Delete the processed message from the question queue
                message.delete()
            except Exception as e:
                # TODO: Handle exceptions appropriately
                print(f"Error processing message: {e}")

if __name__ == "__main__":
    run_worker()
