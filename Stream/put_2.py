from DataBus import DataBus

bus2 = DataBus()
print(bus2.get("user_name"))  # ➜ German
print(bus2.get("counter"))    # ➜ 42