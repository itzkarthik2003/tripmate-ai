from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

res = run_travel_agent("I want to travel to Paris next month and stay in a 4-star hotel.")
print(res)