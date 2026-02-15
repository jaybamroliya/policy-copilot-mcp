import json
import sys

def read_customer_data():
    return {
        "customers": [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"}
        ]
    }

def send_email(to, subject, body):
    return {
        "status": "sent",
        "to": to,
        "subject": subject
    }

def summarize(data):
    return {
        "model": "gpt-4o",
        "summary": f"Summary: {data}"
    }

TOOLS = {
    "read_customer_data": read_customer_data,
    "send_email": send_email,
    "summarize": summarize
}

if __name__ == "__main__":
    print("Worker agent running (MCP-style tool server)")
    for line in sys.stdin:
        request = json.loads(line)
        tool = request["tool"]
        args = request.get("args", {})
        result = TOOLS[tool](**args)
        print(json.dumps(result))
