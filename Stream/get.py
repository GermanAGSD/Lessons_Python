from DataBus import DataBus

bus2 = DataBus()
print(bus2.get("user_name"))  # ➜ German
print(bus2.get("counter"))    # ➜ 42

# bus1 и bus2 — это на самом деле один и тот же объект
# print(bus1 is bus2)  # ➜ True