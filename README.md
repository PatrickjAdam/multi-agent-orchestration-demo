# Multi-Agent Orchestration Demo

This project demonstrates a simple **multi-agent orchestration system** inspired by the paper:  
**Orchestral AI: A Framework for Agent Orchestration**.

The system is implemented in Python and simulates multiple collaborating agents without requiring any external AI API keys.  

---

## Project Overview

The system consists of three types of agents:

1. **Planner Agent** – Breaks a user-provided task into smaller steps.  
2. **Worker Agent** – Executes each step of the task.  
3. **Verifier Agent** – Checks the results produced by the Worker agent.  

This architecture demonstrates key ideas from the paper, including:

- **Agent architecture**: Each agent has a distinct responsibility.  
- **Task decomposition**: Complex tasks are broken into manageable subtasks.  
- **Verification and orchestration**: Outputs are validated and combined to produce a final result.


