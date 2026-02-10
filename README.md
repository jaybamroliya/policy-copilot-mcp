# 🛡️ Policy Copilot
**Real-time governance & safety layer for MCP-based AI agents**

Policy Copilot demonstrates how unsafe AI agents can be **controlled, audited,
and governed in real time** using a separate policy control plane.

This project is designed for hackathon judges, reviewers, and engineers
who want to understand **how agent safety actually works in practice**.

---

## 🚨 The Problem

Modern AI agents are powerful — but dangerous by default.

An autonomous agent can:
- Read sensitive customer data (PII)
- Call external tools like email or APIs
- Use expensive or unapproved models
- Ignore prompt-based safety rules

**Prompt instructions are not enforcement.**
Once an agent is running, there is usually **no real control layer**.

---

## 💡 The Idea

What if AI agents were governed like production systems?

Instead of trusting the agent:
- We **intercept its actions**
- We **enforce policies at runtime**
- We **separate execution from governance**

That’s what **Policy Copilot** does.

---

## 🧱 What We Built

Policy Copilot is a **separate MCP server** that acts as a **policy control plane**
for other AI agents.

### Components

| Component | Purpose |
|---------|--------|
| **Worker Agent** | Unsafe-by-design AI agent |
| **Policy Copilot** | MCP server enforcing policies |
| **Policy Rules (YAML)** | Human-readable governance rules |
| **CLI Demo** | Shows enforcement clearly |
| **Archestra Config** | Conceptual orchestration layer |

---

## 🧠 High-Level Architecture

