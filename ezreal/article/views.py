from flask import request, jsonify
from ezreal.article import article_api
from ezreal.article.service import ArticleService
import json


@article_api.route("/add/")
def article_add():
    data = json.loads(request.get_data())
    title = data.get("title")
    describe = data.get("describe")
    content = data.get("content")
    tags = data.get("tags")
    category = data.get("category")
    ArticleService.article_add(
        title=title, describe=describe, content=content, tags=tags, category=category
    )


@article_api.route("/test/")
def test():

    print(request.headers)

    return jsonify({"status": True})
