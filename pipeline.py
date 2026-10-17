from chains import (
    write_agent_chain,
    explainer_agent_chain,
    reviewer_agent_chain,
    final_response_agent_chain,
)
from supervisor import supervisor_agent_chain


def code_assistance_pipeline(topic: str) -> dict:
    state = {}
    chain_names = {
        "writer":write_agent_chain,
        "explainer":explainer_agent_chain,
        "reviewer":reviewer_agent_chain
    }

    supervisor_agent_response = supervisor_agent_chain.invoke({
        "user_request":topic
    })
    state["supervisor_agent_response"]= supervisor_agent_response
    print(state)

    for agent_call in state["supervisor_agent_response"].agents:
        if agent_call == "writer":
            state["writer_agent_response"] = chain_names[agent_call].invoke({
                "user_request": topic
            })
        else:
            state[f"{agent_call}_agent_response"] = chain_names[agent_call].invoke({
                "user_request": topic,
                "code": state["writer_agent_response"]
            })


    print("\n" + "=" * 50)
    print("Final response agent is preparing the response")
    print("=" * 50 + "\n")

    final_response_agent_response = final_response_agent_chain.invoke({
        "user_request": topic,
        "writer_output": state.get("writer_agent_response",""),
        "explainer_output": state.get("explainer_agent_response",""),
        "reviewer_output": state.get("reviewer_agent_response",""),
    })

    state["final_response_agent_response"] = final_response_agent_response
    print(f"Final response:\n{state['final_response_agent_response']}")

    return state


if __name__ == "__main__":
    topic = input("Enter a topic you want to write code about: ")
    code_assistance_pipeline(topic)
