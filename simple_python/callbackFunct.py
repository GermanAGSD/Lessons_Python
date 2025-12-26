def my_callback(message):
    print(f"Callback executed with message: {message}")

def execute_callback(callback, arg):
    print("Executing callback...")
    callback(arg)

# Использование
execute_callback(my_callback, "Hello, world!")
