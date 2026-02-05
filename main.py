from dotenv import load_dotenv
load_dotenv()

from agents.planner import plan_task
from agents.executor import execute_step
from agents.verifier import verify_and_fix

def run_agent(task):
    steps = plan_task(task)
    results = []

    for step in steps:
        output = execute_step(step)
        if output:
            results.append(output)

    final = verify_and_fix(task, results)

    return {
        "task": task,
        "steps": steps,
        "results": results,
        "final": final
    }

if __name__ == "__main__":
    task = "Get the latest news for the city 'Delhi' from the news API."

    #"Give me news about the city 'Kolkata' from the city info file. "
    
    
 #"Get the current weather information for the city 'Mumbai' from the city info file."
 
            
    print(run_agent(task))
