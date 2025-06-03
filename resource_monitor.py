import psutil

class ResourceMonitor:
    def update(self):
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        print(f"[RISORSE] CPU: {cpu}% | MEM: {mem}%")