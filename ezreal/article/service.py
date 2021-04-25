from ezreal.article.repository import ArticleRepority
from typing import Union


class ArticleService:

    @classmethod
    def article_add(cls, title: str, describe: str, category: int, content: str, tags: Union[str, list]):
        if isinstance(tags, str):
            tags = tags.split(",")
        ArticleRepority.article_add(
            title=title, tags=tags, describe=describe, category=category, content=content
        )
