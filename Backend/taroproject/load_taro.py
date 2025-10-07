import os
import django
import uuid
from django.utils.text import slugify
from django.core.files import File
from storages.backends.s3boto3 import S3Boto3Storage

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taroproject.settings")
django.setup()

from taroapp.models import TaroCard

BASE_DIR = r"taro"
storage = S3Boto3Storage()  # используем явный storage

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
        unique_suffix = uuid.uuid4().hex[:6]
        file_name = f"{safe_name}_{unique_suffix}{ext}"

        # загружаем в R2 через storage
        with open(img_path, "rb") as f:
            saved_name = storage.save(file_name, f)
            card.img.name = file_name  # сохраняем путь в модель
            card.filename = file_name

    card.save()
    print("✅", "создано" if created else "обновлено", card_name)
