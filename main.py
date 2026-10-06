import json
import os
import random
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from telegram_bot import send_message
from shopee_adapter import get_eligible_products

load_dotenv()

INTERVAL_MINUTES = int(os.getenv("INTERVAL_MINUTES", "30"))
MAX_HISTORY = int(os.getenv("MAX_HISTORY", "100"))
HISTORY_FILE = Path("data/history.json")


def load_history():
    if not HISTORY_FILE.exists():
        return []
    try:
        return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []


def save_history(history):
    HISTORY_FILE.write_text(
        json.dumps(history[-MAX_HISTORY:], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def choose_random(products, history):
    available = [p for p in products if p.get("id") not in history]
    if not available:
        history.clear()
        available = products
    return random.choice(available) if available else None


def format_alert(product):
    return (
        "🤖 *Robô Shopee 24h*\n\n"
        f"🎲 Produto escolhido: *{product['title']}*\n"
        f"💰 Preço: {product.get('price', 'N/D')}\n"
        f"🏷️ Categoria: {product.get('category', 'N/D')}\n"
        f"🔗 Link: {product.get('affiliate_link', 'N/D')}\n\n"
        "ℹ️ Seleção aleatória entre produtos elegíveis."
    )


def run_once():
    products = get_eligible_products()
    history = load_history()

    product = choose_random(products, history)
    if not product:
        send_message("⚠️ Não encontrei produtos elegíveis para esta execução.")
        return

    history.append(product["id"])
    save_history(history)

    send_message(format_alert(product))
    print(datetime.now(timezone.utc).isoformat(), product["title"])


if __name__ == "__main__":
    print("Robô iniciado. Ctrl+C para parar.")
    while True:
        try:
            run_once()
        except Exception as exc:
            print("Erro:", repr(exc))
            try:
                send_message(f"🚨 Erro no robô: `{exc}`")
            except Exception:
                pass
        time.sleep(INTERVAL_MINUTES * 60)
