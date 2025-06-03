import time

class GrowthMonitor:
    def __init__(self):
        self.progress = 0
        self.stage = "Inizio"

    def update(self):
        time.sleep(1)
        self.progress += 5
        if self.progress < 30:
            self.stage = "Espansione"
        elif self.progress < 60:
            self.stage = "Ottimizzazione"
        elif self.progress < 90:
            self.stage = "Consolidamento"
        else:
            self.stage = "Autonomia"

    def is_ready(self):
        return self.progress >= 100