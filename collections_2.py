from datetime import datetime, timedelta


def parse_date(date_str: str) -> datetime:
    """Prima datum u formatu 'YYYY-MM-DD' i vraća datetime."""
    return datetime.strptime(date_str, "%Y-%m-%d")


def format_date(dt: datetime) -> str:
    """Pretvara datetime u string 'YYYY-MM-DD'."""
    return dt.strftime("%Y-%m-%d")


def add_days(date_str: str, days: int) -> str:
    """Dodaje broj dana na datum (YYYY-MM-DD) i vraća novi datum (YYYY-MM-DD)."""
    dt = parse_date(date_str) + timedelta(days=days)
    return format_date(dt)


def add_hours_to_date(date_str: str, hours: int, hours_per_day: int = 8) -> str:
    """
    Dodaje sate na datum tako da sate pretvori u dane (ceil), pa doda dane na datum.
    Npr. 9 sati uz 8 sati/dan => 2 dana.
    """
    if hours <= 0:
        return date_str
    days = (hours + hours_per_day - 1) // hours_per_day  # ceil
    return add_days(date_str, days)


def is_weekend(date_str: str) -> bool:
    """Vraća True ako je datum subota ili nedjelja."""
    dt = parse_date(date_str)
    return dt.weekday() >= 5  # 5=Sat, 6=Sun


def zad02_najduzi_zastoj(zastoj_min: tuple) -> int:
    """
    Tema: proizvodnja
    U tuple-u su trajanja zastoja u minutama.
    Vrati najveći zastoj (max).
    """
    # STUDENT CODE START
    return max(zastoj_min)
    # STUDENT CODE END


assert zad02_najduzi_zastoj((5, 12, 3, 12, 1)) == 12
assert zad02_najduzi_zastoj((0,)) == 0