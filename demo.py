from langchain.agents import create_agent
def get_weather(city : str)-> str:
    """Generate code taks"""
    return f"The weather in {city} is sunny."
agent=create_agent(
    model="google_genai:gemini-3.5-flash-lite",
    tools=[get_weather],
    system_prompt="your a useful assitant"
)

res=agent.invoke({"messages":[{"role":"user","content":"Whats the weather in hyderabad"}]})
# print(res["messages"][-1].content)
# print(type(res["messages"][-1]))
# print(repr(res["messages"][-1].content))
print(res["messages"][-1].content_blocks[0]["text"])


