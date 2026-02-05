AI Ops Assistant
It is a Python-based tool that automates tasks using multiple tools and APIs. It converts user requests into structured steps using a Planner LLM and executes them via specialized agents.


### Setup Instructions (Run Locally)
Follow these steps to run AI Ops Assistant on your local machine (localhost):

1. Clone the repository

        git clone https://github.com/PG123-ops/ai_ass_tl.git
        cd ai_ass_tl

2. Create and activate a Python virtual environment

        python -m venv venv
        venv\Scripts\activate              # Windows
        source venv/bin/activate           # macOS/Linux

4. Install dependencies

        pip install -r requirements.txt

5. Set up environment variables

        GEMINI_API_KEY=your_gemini_api_key_here
        OPENWEATHER_API_KEY=your_openweather_api_key_here
        NEWS_API_KEY=your_news_api_key_here

6. Run the assistant

          python main.py

The system will execute tasks and print results to the console.




### Architecture
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


Example Prompts                      # Note:- you have to change the prompt in main.py under the name task

Give me interesting facts about the city 'Delhi' from the city info file.
What is the current weather in New York?
List the top 5 repositories for 'pandas' on GitHub.
Give me the latest news about artificial intelligence.





#### Known Limitations / Tradeoffs

Quota Limits: Free Gemini LLM models have daily and per-minute limits; exceeding them results in RESOURCE_EXHAUSTED errors.
Weather API Key: Required for weather queries; otherwise the executor will fail.
City Info Coverage: Wikipedia or local JSON may not contain all cities.
LLM JSON Parsing: Planner responses must be valid JSON; otherwise, parsing errors occur.
API Response Time: Some APIs may have latency affecting execution speed.
No Web Interface Yet: Outputs are printed in the console; future versions may include a web UI.
