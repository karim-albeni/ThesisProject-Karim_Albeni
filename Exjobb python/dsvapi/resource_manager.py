import psutil, time

print("Logging CPU och RAM varje sekund i 2 minuter...\n")
for _ in range(120):
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    print(f"CPU: {cpu}%   RAM: {ram}%")
    time.sleep(1)
