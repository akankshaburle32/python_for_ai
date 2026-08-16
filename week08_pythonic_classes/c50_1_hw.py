# c50:  que 1:
## Upar wale Agent project mein ek teesra tool add karo: `ReverseTool` jo string ulta kare.

# step 1:
## Upar wale Agent project mein ek teesra tool add karo: `ReverseTool` jo string ulta kare.

# step 2:

# step 3:

# 1: from ami fol.file do import mai * lo.
# 2: ReverseTool(Tool) ka class banao.
# 3: def mai __init__ ki method lo. usme common word do. super().__init("usme text likho.").
# 4: def mai run method mai common word or *args do. text = args[0] lo. return mai ::-1 do.
# 5: agent mai tool add karo.

# step 4:

from code.agent_tools import *

class ReverseTool(Tool):
    def __init__(self):
        super().__init__("Reverse", "Reverse the given text")
        
    def run(self, *args):
        text = args[0]
        return text[::-1]

agent.add_tool(ReverseTool())

# step 5: