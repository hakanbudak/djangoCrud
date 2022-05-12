import logging

from django.db import models

logger = logging.getLogger(__name__)


class Library(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=30)
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.name, self.stock)

    @classmethod
    def get_all_books(cls):
        """ Function return all books """
        return cls.objects.all()

    @classmethod
    def get_book_with_id(cls, book_id: int):
        """ Function return book with id """
        try:
            book = cls.objects.get(id=book_id)
            return {
                'name': book.name,
                'stock': book.stock
            }
        except Exception as e:
            logger.info(e)

            return {}

    @classmethod
    def update_book_details(cls, book_id: int, details: dict):
        """ Function Update book datas """
        try:
            book = cls.objects.get(id=book_id)
            book.name = details.get('name')
            book.stock = details.get('stock')
            book.save()

            return True
        except Exception as e:
            logger.error(e)

        return False

    @classmethod
    def delete_book_with_id(cls, book_id: int):
        """ Function delete book and return boolean """
        try:
            book = cls.objects.get(id=book_id)
            book.delete()

            return True
        except Exception as e:
            logger.error(e)

        return False

    class Meta:
        db_table = 'Library_cursor'
        managed = False
