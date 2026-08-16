# c50:  que 3:
## Agent project mein ReverseTool add karke use_tool("reverse", "hello") test karo.
 
# step 1:
## Agent project mein ReverseTool add karke use_tool("reverse", "hello") test karo.

# step 2:

# step 3:

# 1: from ami fol.file do import mai * lo.
# 2: ReverseTool(Tool) ka class banao.
# 3: def mai __init__ ki method lo. usme common word do. super().__init("usme text likho.").
# 4: def mai run method mai common word or *args do. text = args[0] lo. return mai ::-1 do.
# 5: agent mai tool add karo. object mai agent.use_tool("Reverse", "ek word lo")
# 6: print mai text : object do.

# step 4:

from code.agent_tools import *

class ReverseTool(Tool):
    def __init__(self):
        super().__init__("Reverse", "Reverse the given text")
        
    def run(self, *args):
        text = args[0]
        return text[::-1]

agent.add_tool(ReverseTool())

reverse_result = agent.use_tool("Reverse", "hello")

print("================================================")
print("Reverse Result : ", reverse_result)
print("================================================")


# step :

"""
==============================
Reverse Result : olleh
==============================

"""