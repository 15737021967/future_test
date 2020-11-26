from feature.tests import BaseTestCase
from feature.article import models
from feature.article import repository
from feature import db
import unittest


class ArticleTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(ArticleTest, cls).setUpClass()
        category_ins = models.Category(
            name="test_category"
        )
        tag_ins_list = [
            models.Tag(
                name="123" + str(i)
            )
            for i in range(4)
        ]
        db.session.add(category_ins)
        db.session.add_all(tag_ins_list)
        db.session.commit()
        cls.tag_list = [
            tag.id
            for tag in tag_ins_list
        ]
        cls.category_id = category_ins.id

    def test_article_add(self):
        title = "123"
        describe = "123"
        content = "123"
        tags = models.Tag.query.filter(models.Tag.id.in_(self.tag_list))
        repository.ArticleRepority.article_add(
            title=title, describe=describe, content=content, tags=tags, category=self.category_id
        )
        article_ins: models.Article = models.Article.query.filter(models.Article.title == "123").first()
        self.assertEqual(article_ins.category_id, self.category_id)
        self.assertEqual(len(article_ins.tags.all()), len(self.tag_list))
