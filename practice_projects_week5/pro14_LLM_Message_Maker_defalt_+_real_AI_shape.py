# que 14:

"""
### Project 14 — LLM Message Maker (default + real AI shape)
- **EN:** Write `make_message(text, role="user")` that **returns** a dict `{"role": role, "content": text}`. Make a normal user message and a `role="system"` message. (This is exactly how AI chat messages look!)
- **हिंदी:** `make_message(text, role="user")` बनाओ जो dict `{"role": role, "content": text}` **return** करे। एक normal user message और एक `role="system"` message बनाओ। (AI chat messages बिल्कुल ऐसे ही दिखते हैं!)
- **Concepts:** default value, returning a dict, agentic link
- **Hint:** `return {"role": role, "content": text}`.

"""

# step 1:
## "make_message(text, role="user")" banao jo dict "{"role": role, "content": text}" **return** kare. ek normal or ek role="system" message banao (AI chat messages bilkul ise he dikhate hai.)

# step 2:  ex. (text, role="user") = role="system" >>> ('role': 'system', 'content': 'Hello, How are you')

# step 3:

# 1: def mai fun lo or us mai parater do or defalt pameter do.
# 2: return mai {"role": role, "content": text} do.
# 3: print mai function or uske value do.

# step 4:

def make_message(text, role="user"):
    return {"role": role, "content": text}

print(make_message("Hello, How are you", role="System"))    

# step 5:

"""
{'role': 'system', 'content': 'Hello, How are you'}

"""