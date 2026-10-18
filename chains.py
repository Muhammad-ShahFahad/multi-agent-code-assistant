from dotenv import load_dotenv
load_dotenv(override=True)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from model import model
from prompts import (
    supervisor_prompt,
    writer_agent_prompt,
    explainer_prompt,
    reviewer_agent_prompt,
    final_response_prompt,
    process_web_content_prompt
)
from agents import web_search_agent

# output parser
output_parser = StrOutputParser()

# writer_agent chain
write_agent_chain =(
    RunnablePassthrough.assign(context=RunnableLambda(lambda x: web_search_agent.invoke({
        "messages":[{
            "role":"user", "content":x["user_request"]
        }]
    })["messages"][-1]
    )
    )
    |writer_agent_prompt
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

# process_web_content chain
process_web_content_chain = (
    process_web_content_prompt 
    | model 
    | output_parser
)