# que 16:

"""

### Project 16 — Chat History Appender (no data leak)
- **EN:** Write `add_message(text, history=None)` that appends `{"role": "user", "content": text}` to the history and returns it. Start two SEPARATE conversations and prove their histories do not mix.
- **हिंदी:** `add_message(text, history=None)` बनाओ जो `{"role": "user", "content": text}` को history में जोड़ कर उसे return करे। दो अलग बातचीत शुरू करके साबित करो कि उनकी history आपस में नहीं मिलती।
- **Concepts:** `None` default, list of dicts, `.append()`
- **Hint:** `if history is None: history = []` — otherwise both chats share one list (a privacy bug!).

"""

# step 1:
## "add_message(text, history=None)" banao jo "{"role": "user", "content": text}" ko history mai jod kar use return kare. do alag batchit shuru karke sabit karo ki unki history aaps mai nhi milti.

# step 2:  add_message(text, history=None) = .apped()  >> ['Tree']

# step 3:

# 1: def mai fun mai parameter or defalt parameter do.
# 2: if mai defalt parameter none: DP  = [].
# 3: DP .append lekar usme parameter do.
# 4: return mai DP.
# 5: print mai fun mai value do 2 baar print karo.

# step 4:

def add_message(text, history=None):
    if history is None:
        history = []
        history.append(text)
        return history

print(add_message("login"))
print(add_message("log out"))        

# step 5:

"""
['login']
['log out']

"""