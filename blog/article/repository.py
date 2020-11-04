from blog.article.models import Article
from blog import db


class ArticleRepority:

    @classmethod
    def article_add(cls, title: str, describe: str, content: str, tags: list, category: int):
        article_ins = Article(
            title=title,
            describe=describe,
            content=content,
            category_id=category,
            tags=tags
        )
        db.session.add(article_ins)
        db.session.commit()


