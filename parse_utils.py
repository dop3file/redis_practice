from dataclasses import dataclass


@dataclass
class ParsedResult:
    title: str


TITLE_SELECTOR = "#book-card__wrapper > div.BookCard_book__1IAPE > div:nth-child(3) > div > div:nth-child(1) > h1"