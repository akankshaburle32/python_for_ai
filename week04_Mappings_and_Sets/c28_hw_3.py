
# Ek config dict banao, use `MappingProxyType` se lock karo, padhne ki koshish (chalega) aur badalne ki koshish (error padho).


from types import MappingProxyType
config = MappingProxyType ({"Information Technology" : "IT", "Computer Science" : "CS"})
print(config["Information Technology"])