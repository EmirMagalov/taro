import os
from django.core.files import File
from taroapp.models import TaroCard

base_dir = r"C:/PYTHON/parser/taro"  # папка с картами

def read_file(path):
    return open(path, "r", encoding="utf-8").read() if os.path.exists(path) else ""

for card_name in os.listdir(base_dir):
    card_dir = os.path.join(base_dir, card_name)
    if not os.path.isdir(card_dir):
        continue

    print(f"Загружаю {card_name}...")

    img_path = os.path.join(card_dir, f"{card_name}.jpg")
    txt_files = {
        "descr_text": "descr.txt",
        "love_text": "love.txt",
        "work_text": "work.txt",
        "day_text": "day.txt",
        "advice_text": "advice.txt",
        "yesno_text": "yesno.txt",
    }

    card, created = TaroCard.objects.get_or_create(name=card_name)

    for field, fname in txt_files.items():
        setattr(card, field, read_file(os.path.join(card_dir, fname)))

    if os.path.exists(img_path):
        with open(img_path, "rb") as img_file:
            card.img.save(f"{card_name}.jpg", File(img_file), save=True)
    else:
        card.save()

    print("✅", "создано" if created else "обновлено", card_name)
