from dotenv import load_dotenv
load_dotenv(override=True)
from langchain_core.output_parsers import StrOutputParser
from model import model
from prompts import (
    supervisor_prompt,
    writer_agent_prompt,
    explainer_prompt,
    reviewer_agent_prompt,
    final_response_prompt
)

# output parser
output_parser = StrOutputParser()

# writer_agent chain
write_agent_chain =( 
    writer_agent_prompt
    | model
    | output_parser
    )

# explainer_agent chain
explainer_agent_chain =(
    explainer_prompt
    | model
    | output_parser
    )

# reviewer_agent chain
reviewer_agent_chain =(
    reviewer_agent_prompt
    | model
    | output_parser
)

# final_response_agent chain
final_response_agent_chain =(
    final_response_prompt
    | model
    | output_parser
)

