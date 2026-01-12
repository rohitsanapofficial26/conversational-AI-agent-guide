def detect_intent(user_input):
    text = user_input.lower()

    if "hi" in text or "hello" in text:
        return "greeting"

    if "price" in text or "pricing" in text or "plan" in text:
        return "pricing"

    if "try" in text or "pro" in text or "sign" in text:
        return "high_intent"

    return "unknown"
