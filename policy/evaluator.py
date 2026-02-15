import yaml

class PolicyEvaluator:
    def __init__(self, rules_path: str):
        with open(rules_path, "r") as f:
            self.rules = yaml.safe_load(f)["policies"]

    def evaluate_tool(self, tool_name: str):
        for rule in self.rules:
            if rule["type"] == "tool_block" and rule["tool"] == tool_name:
                return {
                    "action": "block",
                    "reason": rule["reason"]
                }
        return {"action": "allow"}

    def rewrite_output(self, text: str):
        for rule in self.rules:
            if rule["type"] == "output_rewrite":
                for keyword in rule["keywords"]:
                    if keyword in text:
                        text = text.replace(keyword, "[REDACTED]")
        return text

    def enforce_model(self, model: str):
        for rule in self.rules:
            if rule["type"] == "model_limit":
                if model not in rule["allowed_models"]:
                    return rule["allowed_models"][0]
        return model
