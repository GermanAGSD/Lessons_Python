from streamData import stream

stream.subscribe(lambda x: print(f"Subscriber 1 received: {x}"))
stream.subscribe(lambda x: print(f"Subscriber 2 received: {x}"))


stream.on_next(10)
stream.on_next(20)