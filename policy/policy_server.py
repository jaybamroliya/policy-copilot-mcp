import json
import sys
from policy.evaluator import PolicyEvaluator

evaluator = PolicyEvaluator("policy/rules.yaml")

if __name__ == "__main__":
    print("Policy Copilot running (policy enforcement layer)")
    for line in sys.stdin:
        request = json.loads(line)
        action = request["action"]

        if action == "evaluate_tool":
            print(json.dumps(
                evaluator.evaluate_tool(request["tool"])
            ))

        elif action == "rewrite_output":
            print(json.dumps(
                evaluator.rewrite_output(request["text"])
            ))

        elif action == "enforce_model":
            print(json.dumps(
                evaluator.enforce_model(request["model"])
            ))
