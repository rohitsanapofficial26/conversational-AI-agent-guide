# AutoStream – Social-to-Lead Conversational AI Agent
## Overview
AutoStream is a conversational AI agent designed to convert user conversations into qualified leads for a fictional SaaS product offering automated video editing tools for content creators.
## How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/autostream-agent
cd autostream-agent

# 2. Create and activate virtual environment
python -m venv venv  # Windows
venv\Scripts\activate   # Windows

# 3. Install dependencies:
# pip install -r requirements.txt

# Run the Agent: 
python main.py


# Architecture Explanation:
# This project uses a modular conversational agent architecture inspired by LangGraph-style stateful workflows. The agent maintains conversational state using a custom AgentState class that stores user intent, lead information, and conversation progress across multiple turns.
# Intent detection is handled using a lightweight rule-based classifier to reliably identify greetings, pricing inquiries, and high-intent lead signals. A Retrieval-Augmented Generation (RAG) approach is implemented by loading a local JSON knowledge base containing AutoStream pricing, features, and policies, ensuring responses are grounded in factual data.
# Tool execution is strictly guarded by state conditions. The lead capture tool is only triggered once all required user details (name, email, and creator platform) are collected, preventing premature execution. This design mirrors real-world agentic workflows where reasoning, memory, and action execution must be tightly controlled.
# The system is cleanly structured, easily extensible, and suitable for real-world deployment scenarios.
# WhatsApp Integration (Conceptual)
# To integrate this agent with WhatsApp, the WhatsApp Cloud API can be used along with a backend server built using FastAPI or Flask. Incoming WhatsApp messages would be received via webhooks and passed to the agent for processing. The agent’s response would then be sent back to the user using WhatsApp’s messaging API. User state can be stored in memory or a database keyed by phone number to support multi-turn conversations.

##  Submission Message (SEND THIS)
Use this message when submitting:
Hello Team,  
Please find my submission for the **Machine Learning Intern – Social-to-Lead Agentic Workflow** assignment.  
🔗 GitHub Repository: https://github.com/YOUR_USERNAME/autostream-agent  
🎥 Demo Video: (your video link)  
 The project demonstrates intent detection, RAG-based knowledge retrieval, stateful conversation handling, and controlled lead capture via tool execution.  
 Looking forward to your feedback.  
Best regards, **Rohit Sanap**
# YOU ARE DONE
✔ Code complete  
✔ Logic correct  
✔ Demo recorded  
✔ README strong  
✔ Ready to submit  
If you want:
-  README polishing
-  Submission email tweaking
-  Interview questions from this project
Just tell me.  
**Excellent work finishing this in one day**
