AI Ops Assistant

AI Ops Assistant is a Python-based tool that automates tasks using multiple tools and APIs. It converts user requests into structured steps using a Planner LLM and executes them via specialized agents.

Table of Contents

Setup Instructions

Environment Variables

Architecture

Integrated APIs & Tools

Example Prompts

Known Limitations / Tradeoffs

Setup Instructions

Follow these steps to run the AI Ops Assistant locally:

Clone the repository:

git clone https://github.com/yourusername/ai_ops_assistant.git
cd ai_ops_assistant


Create and activate a Python virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Create a .env file (or use .env.example) with your API keys:

GEMINI_API_KEY=your_gemini_api_key_here
OPENWEATHER_API_KEY=your_openweather_api_key_here


Run the assistant locally:

python main.py


The system will execute tasks and print results to the console.

Environment Variables

Create a .env file in the project root or set system environment variables:

# Gemini API Key (for Planner LLM)
GEMINI_API_KEY=your_gemini_api_key_here

# OpenWeather API Key (for weather queries)
OPENWEATHER_API_KEY=your_openweather_api_key_here


Optional: Copy the .env.example file and fill in the keys.

Architecture

AI Ops Assistant has a modular agent-based architecture:

Agents:

Planner: Converts natural language tasks into structured steps (tool, action, params) using Gemini LLM.

Executor: Runs the planned steps via the appropriate tool/API.

Verifier: Checks and corrects outputs returned by agents.

Tools: Each tool handles specific actions:

Weather — fetches real-time weather data from OpenWeather API.

Wiki / Place Info — retrieves summaries of cities or locations (Wikipedia or local file).

GitHub — queries repositories (planned for future integration).

News — fetches latest news (planned for future integration).

Flow:

User Task → Planner Agent → Steps → Executor → Results → Verifier → Final Output

Integrated APIs & Tools

Gemini LLM API: For planning tasks into structured steps.

OpenWeather API: For real-time weather queries.

Wikipedia / Local City Info File: For city/place data retrieval.

GitHub API (future): Repository information.

News API (future): Latest news on topics of interest.

Example Prompts

Here are 3–5 example prompts you can use to test the system:

City Info

Give me interesting facts about the city 'Delhi' from the city info file.


Weather

What is the current weather in New York?


GitHub Repos

List the top 5 repositories for 'pandas' on GitHub.


News

Give me the latest news about artificial intelligence.


Multi-step Task

Find the weather in Paris and give a short summary about Paris from the city info file.

Known Limitations / Tradeoffs

Quota Limits: Free Gemini LLM models have daily and per-minute limits; exceeding them results in RESOURCE_EXHAUSTED errors.

Weather API Key: Required for weather queries; otherwise the executor will fail.

City Info Coverage: Wikipedia or local JSON may not contain all cities.

LLM JSON Parsing: Planner responses must be valid JSON; otherwise, parsing errors occur.

API Response Time: Some APIs may have latency affecting execution speed.

No Web Interface Yet: Outputs are printed in the console; future versions may include a web UI.