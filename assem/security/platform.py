import random
import string

def generate_id():
    segments = []
    for _ in range(3):  # Генерация 3 сегментов
        segment_length = random.randint(5, 10)  # Длина каждого сегмента от 5 до 10 символов
        segment = ''.join(random.choices(string.ascii_letters + string.digits, k=segment_length))
        segments.append(segment)
    return '-'.join(segments)


