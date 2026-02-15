# 🛡️ Policy Copilot (MCP Governance Layer)
**Governance Layer for Archestra Agent Orchestration**

Policy Copilot is a runtime governance extension for Archestra, adding deterministic enforcement to AI agent orchestration built on MCP.

Policy Copilot is a runtime governance extension for Archestra, adding deterministic enforcement to AI agent orchestration built on MCP.

---

## 🚨 The Problem

It transforms Archestra from a coordination system into a governed agent infrastructure platform.

An autonomous agent can:
- AI agents orchestrated by platforms like Archestra can:
- Trigger external APIs
- Send emails
- Use expensive models
- Bypass prompt-based safety

**Prompt instructions are not enforcement.**
Modern AI systems lack deterministic runtime governance.

---

## 💡 The Idea

We extended Archestra with a Governance Middleware Layer called Policy Copilot.

Instead of trusting the agent:
Archestra routes every action through a policy enforcement layer.
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
User Request
     ↓
┌─────────────────────┐
│ Archestra           │
│ Orchestrator        │  ← Routing, planning, context mgmt
└─────────┬───────────┘
          ↓
┌─────────────────────┐
│ Policy Copilot      │  ← Governance middleware
│ (Compliance Layer)  │     - RBAC
│                     │     - Cost control
│                     │     - Tool allow/block
│                     │     - Safety
└─────────┬───────────┘
          ↓ Approved Plan
┌─────────────────────┐
│ Worker Agent (MCP)  │  ← Executes plan
│                     │     - Tool calls
│                     │     - Model calls
│                     │     - External APIs
└─────────┬───────────┘
          ↓
┌─────────────────────┐
│ Tools / Models      │  ← Databases, APIs, LLMs, Files
└─────────────────────┘

```

Separation of concerns:
- Archestra → Orchestration
- Policy Copilot → Enforcement
- Worker Agent → Execution

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
```



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

All enforcement happens before results leave the system.

🧪 Demo Scenario

Task:
- Summarize customer data and email results

Enforcement Results:

- ❌ External email blocked
- ✂️ PII redacted
- 💰 Expensive model prevented
- ✅ Allowed model automatically applied


🎯 Why This Matters
Policy Copilot demonstrates:
- Governance as Infrastructure
- Runtime AI Safety
- Enterprise Compliance Control
- Deterministic Agent Enforcement
- Deterministic Agent Enforcemen

This turns Archestra into a production-grade AI control plane.






