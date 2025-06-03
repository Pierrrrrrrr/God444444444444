from telegram_handler import send_telegram_message
from growth_monitor import GrowthMonitor
from resource_monitor import ResourceMonitor
from security import require_user_key
from god_ai import GodAI

def main():
    send_telegram_message("[GOD] Luci è online su Render!")
    if not require_user_key():
        send_telegram_message("[GOD] Autenticazione fallita. Arresto Luci.")
        return

    growth = GrowthMonitor()
    resources = ResourceMonitor()
    ai = GodAI()

    while not growth.is_ready():
        growth.update()
        resources.update()
        msg = f"[GOD] Fase: {growth.stage}, Crescita: {growth.progress}%"
        send_telegram_message(msg)
        print(msg)
        print(ai.respond("Come ti senti oggi, Luci?"))

if __name__ == "__main__":
    main()