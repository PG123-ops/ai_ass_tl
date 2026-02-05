import json

def verify_and_fix(task, results):
    # If results is a list, join or process them
    if isinstance(results, list):
        response = "\n".join(map(str, results))
    else:
        response = results.get("llm_response", "")
    # continue your verification logic...
