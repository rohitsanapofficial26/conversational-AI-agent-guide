from agent.agent import handle_message
from agent.state import AgentState

state = AgentState()

print("AutoStream Agent Started (type 'exit' to quit)")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    response = handle_message(user, state)
    print("Agent:", response)
