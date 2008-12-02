from django.test import TestCase

from base import SingletonModel
from django.db import models

class Category(SingletonModel):
    name = models.CharField(max_length=32)

class Article(SingletonModel):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category)

class RegularCategory(models.Model):
    name = models.CharField(max_length=32)

class RegularArticle(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(RegularCategory)

class SingletonsTest(TestCase):
    # TODO: test for cross model relation (singleton to regular)
    
    def setUp(self):
        for n in xrange(0, 2):
            category = Category.objects.create(name="Category %d" % (n,))
            regcategory = RegularCategory.objects.create(name="Category %d" % (n,))
        
        for n in xrange(0, 10):
            Article.objects.create(name="Article %d" % (n,), category=category)
            RegularArticle.objects.create(name="Article %d" % (n,), category=regcategory)
    
    def test_basic(self):
        article_list = Article.objects.all().select_related('category')
        last_article = article_list[0]
        for article in article_list[1:]:
            self.assertEquals(article.category is last_article.category, True)
            last_article = article

    def test_regular(self):
        article_list = RegularArticle.objects.all().select_related('category')
        last_article = article_list[0]
        for article in article_list[1:]:
            self.assertEquals(article.category is last_article.category, False)
            last_article = article