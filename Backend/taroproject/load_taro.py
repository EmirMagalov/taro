import os
import django
import uuid
from django.utils.text import slugify
from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taroproject.settings")
django.setup()

from taroapp.models import TaroCard

BASE_DIR = r"C:/PYTHON/parser/taro"

def read_file(path):
    return open(path, "r", encoding="utf-8").read() if os.path.exists(path) else ""

for card_name in os.listdir(BASE_DIR):
    card_dir = os.path.join(BASE_DIR, card_name)
    if not os.path.isdir(card_dir):
        continue

    print(f"Загружаю {card_name}...")

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

    img_path = os.path.join(card_dir, f"{card_name}.jpg")
    if os.path.exists(img_path):
        safe_name = slugify(card_name) or "card"
        ext = os.path.splitext(img_path)[1]
        unique_suffix = uuid.uuid4().hex[:6]  # короткий уникальный суффикс
        new_file_name = f"{safe_name}_{unique_suffix}{ext}"

        with open(img_path, "rb") as img_file:
            card.img.save(new_file_name, File(img_file), save=True)
    else:
        card.save()

    print("✅", "создано" if created else "обновлено", card_name)
