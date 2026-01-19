# AutoStream – Soc## Overview
AutoStream is a conversational AI agent designed to convert user conversations into qualified leads for a fictional SaaS product offering automated video editing tools for content creators.
# Architecture Explanation:
# This project uses a modular conversational agent architecture inspired by LangGraph-style stateful workflows. The agent maintains conversational state using a custom AgentState class that stores user intent, lead information, and conversation progress across multiple turns.
# Intent detection is handled using a lightweight rule-based classifier to reliably identify greetings, pricing inquiries, and high-intent lead signals. A Retrieval-Augmented Generation (RAG) approach is implemented by loading a local JSON knowledge base containing AutoStream pricing, features, and policies, ensuring responses are grounded in factual data.
# Tool execution is strictly guarded by state conditions. The lead capture tool is only triggered once all required user details (name, email, and creator platform) are collected, preventing premature execution. This design mirrors real-world agentic workflows where reasoning, memory, and action execution must be tightly controlled.
# The system is cleanly structured, easily extensible, and suitable for real-world deployment scenarios.
# WhatsApp Integration (Conceptual)
# To integrate this agent with WhatsApp, the WhatsApp Cloud API can be used along with a backend server built using FastAPI or Flask. Incoming WhatsApp messages would be received via webhooks and passed to the agent for processing. The agent’s response would then be sent back to the user using WhatsApp’s messaging API. User state can be stored in memory or a database keyed by phone number to support multi-turn conversations. 
# conversational-AI-agent-guide
Auto-Stream AI Agent assignment
