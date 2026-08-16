from abc import ABC, abstractmethod

class Tool(ABC):

    def __init__(self, name, description):
        self.name = name
        self.description = description

        @abstractmethod
        def run(self, *args):
            ...



class CalculaterTool(Tool):
    def __init__(self):
        super().__init__("Calculater", "Add Tool for adding and multiplication no. ")

    def add(self, a, b):
        return a + b

    def multiplication(self, a, b):
        return a * b

    def run(self, *args):

        a, b, name = args # 1, 2, "add"

        if name == name:
            return self.add(a, b)

        elif name == "mul":
            return self.multiplication(a, b)

        else:
            raise ValueError(f"Invalied operation : {name}")

class GreeterTool(Tool):
    def __init__(self):
        super().__init__("Greeter", "Add Tool for greeting people")
    
    def run(self, *args):
        name = args[0]
        return f"Hello, {name}!"


class Agent:
    def __init__(self, name):
        self.name = name    # My first agent
        self.tools = [] # [CalculaterTool. GreeterTool]

    def add_tool(self, tool: Tool):
        self.tools.append(tool)

    def list_tool(self):    
        for tool in self.tools:
            print(f"{tool.name}, {tool.description}")   # CalculaterTool().name, CalculaterTool()description

    def use_tool(self, tool_name:str, *args):        
        for tool in self.tools:
            if tool.name == tool_name:
                return tool.run(*args)

        return f"Tool {tool_name} not found"

agent = Agent("My first agent")                

print("=============================================================")

agent.add_tool(CalculaterTool())
agent.add_tool(GreeterTool())

agent.list_tool()

print("=============================================================")

add_result = agent.use_tool("Calculater", 5, 7, "add")
multi_result = agent.use_tool("Calculater", 5, 7, "mul")

greet_result = agent.use_tool("Greeter", "Chakuli")

print("Addition Result : ", add_result)
print("Mutiplication Result : ", multi_result)

print("==============================================================")

print("Greeter Result : ", greet_result)

print("==============================================================")