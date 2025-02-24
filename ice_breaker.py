import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
Elon Reeve Musk (/ˈiːlɒn mʌsk/; born June 28, 1971) is a businessman and U.S. special government employee, 
best known for his key roles in Tesla, Inc., SpaceX, and the Department of Government Efficiency (DOGE), 
and his ownership of Twitter. Musk is the wealthiest individual in the world; as of February 2025, 
Forbes estimates his net worth to be US$397 billion.
"""

if __name__ == "__main__":
    print("hello langchain!!")
    # load_dotenv()
    # print(os.environ.get("EXAMPLE_ENV_VARIABLE"))

    summary_template = """
    given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})

    print(res)
    """
    content="1. Elon Musk is a highly successful businessman and U.S. special government employee, known for his involvement in companies like Tesla, SpaceX, and Twitter. He is currently the wealthiest individual in the world, with a net worth estimated at US$397 billion as of February 2025.\n\n2. Two interesting facts about Elon Musk:\n   - He is the founder of SpaceX, a private aerospace manufacturer and space transportation company that aims to reduce space transportation costs and enable the colonization of Mars.\n   - Musk is also the owner of Tesla, Inc., a company that specializes in electric vehicles, energy storage, and solar panel manufacturing, with a mission to accelerate the world's transition to sustainable energy."
    additional_kwargs={'refusal': None}
    response_metadata={'token_usage': {'completion_tokens': 140, 'prompt_tokens': 144, 'total_tokens': 284, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}
    id='run-68a580ee-6dd7-4e1a-a8e2-33b378179f4f-0'
    usage_metadata={'input_tokens': 144, 'output_tokens': 140, 'total_tokens': 284, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
    """