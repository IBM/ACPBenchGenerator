import os
from dotenv import load_dotenv
from genai import Client, Credentials
from tqdm import tqdm 
from utils.logging_util import logger

from genai.schema import (
    DecodingMethod,
    LengthPenalty,
    TextGenerationParameters,
    TextGenerationReturnOptions,
)

load_dotenv()

# Set ENV variable names GENAI_KEY and GENAI_API in environment variables or .env file
credentials = Credentials.from_env()
client = Client(credentials=credentials)

# "parameters": {
#     "decoding_method": "sample",
#     "temperature": 0.7,
#     "top_p": 1,
#     "top_k": 50,
#     "typical_p": 1,
#     "repetition_penalty": 1.04,
#     "stop_sequences": [
#       "Input:"
#     ],
#     "include_stop_sequence": false,
#     "min_new_tokens": 1,
#     "max_new_tokens": 200
#   },
#   "moderations": {
#     "hap": {
#       "threshold": 0.75,
#       "input": true,
#       "output": true
#     },
#     "stigma": {
#       "threshold": 0.75,
#       "input": true,
#       "output": true
#     }
#   },
  
def generate_text(queries, model_id, instruction=None, max_token=200, stop_sequences=["Input:"]):
    results = []
    if instruction is not None: 
        prompts = [instruction+"\nInput: "+v+"\nOutput: " for _, _, v in queries]
    parameters = TextGenerationParameters(
                    max_new_tokens=max_token,
                    decoding_method=DecodingMethod.GREEDY,
                    stop_sequences=stop_sequences,
                    return_options=TextGenerationReturnOptions(input_text=True)
                )

    for i, response in enumerate(tqdm(
        total=len(queries),
        desc=f"Fetching text from {model_id}",
        unit=" prompts",
        iterable=client.text.generation.create(
            model_id=model_id,
            inputs=prompts,
            parameters=parameters
        ),
        file=logger
    )):
        logger.save_extra_data(response.results[0].model_dump(), file_name=f"{response.id}.json", mode="json",folder="bam_output")
        results.append(queries[i] + (response.results[0].generated_text.replace("Input:","").replace("\n",""),))
    assert len(results) == len(prompts)
    return results