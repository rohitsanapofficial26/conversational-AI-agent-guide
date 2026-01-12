from agent.intents import detect_intent
from agent.rag import get_pricing_info
from agent.tools import mock_lead_capture

def handle_message(user_input, state):

    intent = detect_intent(user_input)

    if intent == "greeting":
        return "Hi! How can I help you today?"

    if intent == "pricing":
        return get_pricing_info()

    if intent == "high_intent":
        state.high_intent = True
        return "Great! May I know your name?"

    if state.high_intent:
        if not state.name:
            state.name = user_input
            return "Thanks! What's your email?"

        if not state.email:
            state.email = user_input
            return "Which platform do you create content on?"

        if not state.platform:
            state.platform = user_input
            mock_lead_capture(state.name, state.email, state.platform)
            return "Lead captured successfully!"

    return "Can you please clarify?"

