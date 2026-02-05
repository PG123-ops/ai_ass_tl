import json
from llm.client import call_llm

def plan_task(user_task: str):
    """
    Convert a user task into structured steps with proper parameters.
    Ensures each step has:
    - tool
    - action
    - params (with all required keys)
    """

    prompt = f"""
You are a Planner Agent.

Convert the user task into an ordered list of steps.
Each step must include:
- tool (weather, github, news, wiki)
- action (what to do with the tool)
- params (all necessary parameters)

If the tool is 'wiki', 'params' must include 'place'.
Do NOT leave any required fields empty.

User task: {user_task}

Respond ONLY in strict JSON like this:
{{
  "steps": [
    {{
      "tool": "string",
      "action": "string",
      "params": {{
        "place": "string"
      }}
    }}
  ]
}}
"""

    # Call the LLM
    response = call_llm([{"role": "user", "content": prompt}])

    # Parse the JSON safely
    try:
        data = json.loads(response)
        steps = data.get("steps", [])
    except (json.JSONDecodeError, AttributeError):
        # LLM failed to produce valid JSON
        raise ValueError("LLM returned invalid JSON for plan_task")

    # Validate every step
    for step in steps:
        if "tool" not in step or "action" not in step or "params" not in step:
            raise ValueError(f"Step missing required fields: {step}")
        if step["tool"] == "wiki" and "place" not in step["params"]:
            raise ValueError(f"'wiki' tool step missing 'place' param: {step}")

    return steps
