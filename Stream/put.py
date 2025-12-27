from DataBus import DataBus

while True:
    bus1 = DataBus()
    bus1.set("user_name", "German")
    bus1.set("counter", 42)

# from DataBus import DataBus
#
# bus2 = DataBus()
# print(bus2.get("user_name"))  # ➜ German
# print(bus2.get("counter"))    # ➜ 42
