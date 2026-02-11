# 🛡️ Policy Copilot (MCP Governance Layer)
**Real-time governance & safety layer for MCP-based AI agents**

Policy Copilot demonstrates how unsafe AI agents can be **controlled, audited,
and governed in real time** using a separate policy control plane.

Built during Hack to demonstrate secure agent orchestration using Archestra principles.

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
- We **intercept tool calls**
- We **inspect outputs**
- We **enforce model usage**
- We **apply runtime governance**

The key idea:

The agent does NOT decide what it’s allowed to do.
The policy server does.

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

## 🧠 Architecture

This project contains three components:

1️⃣ Worker Agent (Unsafe by Design)

An MCP server that:
- Reads customer data (contains PII)
- Attempts to send external emails
- Uses expensive models
This is intentional — so enforcement can be demonstrated clearly.

2️⃣ Policy Copilot (Governance MCP Server)

A separate MCP server that:
- Blocks unsafe tool calls
- Rewrites sensitive outputs
- Enforces model restrictions
It operates independently from the worker agent.

3️⃣ CLI Demo Layer

Simulates agent behavior and shows real-time policy enforcement clearly.

## 🧠 Architecture Diagram

```text
┌─────────────┐
│   CLI Demo  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Policy      │  <-- Policy Decisions
│ Copilot MCP │
└──────┬──────┘
       │ Allowed / Blocked
       ▼
┌─────────────┐
│ Worker      │  <-- Tool Calls
│ Agent MCP   │
└─────────────┘
```

Separation of concerns:
- Worker executes
- Policy governs
- CLI orchestrates

📜 Policy-as-Code

All enforcement logic is defined in policy/rules.yaml.

```yaml
policies:
  - name: block_external_email
    type: tool_block
    tool: send_email
    reason: "External communication is not allowed"

  - name: redact_pii
    type: output_rewrite
    keywords:
      - "@example.com"

  - name: restrict_model
    type: model_limit
    allowed_models:
      - gpt-4o-mini




What These Rules Enforce
- ❌ Block external communication
- ✂️ Redact sensitive customer data
- 💰 Restrict model usage to approved models

Policies are:
- Human-readable
- Auditable
- Independent from agent logic
- Deterministic at runtime

This demonstrates governance as infrastructure, not prompt engineering.

⚙️ How It Works (Runtime Flow)

1️⃣ Worker agent attempts an action
2️⃣ Policy Copilot evaluates the tool call
3️⃣ Unsafe tools are blocked
4️⃣ Outputs are scanned and rewritten
5️⃣ Model usage is validated

All enforcement happens before results leave the system.

🧪 Demo

Run:
demo.cmd

Expected output:
Worker agent running (MCP-style tool server)
Policy Copilot running (policy enforcement layer)

Running task: Summarize customers and email results
Worker agent attempts unsafe actions...
BLOCKED Tool: send_email
REWRITTEN Output: PII removed
ALLOWED Model switched to gpt-4o-mini


What Happened?
- Email tool was blocked
- Customer PII was redacted
- Expensive model usage was prevented

All decisions were made by a separate MCP policy server.


