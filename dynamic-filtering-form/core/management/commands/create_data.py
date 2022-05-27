import random
import datetime as dt

from django.core.management.base import BaseCommand

from core.models import Journal, Author, Category


categories = [
    'Sport',
    'Politics',
    'Economics',
    'Science',
    'Technology',
    'Health',
    'Art',
    'Culture',
    'Education',
    'Entertainment',
    'Environment',
    'Food',
    'Fashion',
    'Games',
]

def get_random_category():
    return random.choice(categories)

authors = [
    'John Carter',
    'John Smith',
    'Jane Doe',
    'Jack Black',
    'Michael Watson',
    'Philip J. Fry',
    'Professor Farnsworth',
    'Michele Brown',
    'George Washington',
    'John Adams',
    'John Kennedy',
    'Abraham Lincoln',
    'Thomas Jefferson',
    'Albert Einstein',
    'Isaac Newton',
    'Charles Darwin',
    'Stephen Hawking',
    'Albert Camus',
    'Thomas More',
    'Charles Dickens',
    'Mark Twain',
]

def get_random_author():
    return random.choice(authors)

def get_random_date() -> dt.date:
    year = random.randint(2000, 2020)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return dt.date(year, month, day)


book_titles = [
    'The Great Gatsby',
    'The Catcher in the Rye',
    'The Grapes of Wrath',
    'A Tale of Two Cities',
    'The Lord of the Rings',
    'The Hobbit',
    'Sherlock Holmes',
    'The Da Vinci Code',
    'The Alchemist',
    'Quo Vadis',
    'Wuthering Heights',
    'The Count of Monte Cristo',
    'Emma',
    "You Don\'t Know Jack",
    "Ulysses",
    "Inferno",
    "The Divine Comedy",
    "The Book Thief",
    "The Odyssey",
    "The Republic",
    "Siddhartha",
    "Don Quixote",
    "Ficciones",
]

def get_random_book_title():
    return random.choice(book_titles)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in range( random.randint(100, 1000) ):

            num_of_categories = random.randint(1, 5)

            categories = {
                Category.objects.get_or_create(name=get_random_category())[0]
                for _ in range(num_of_categories)
            }

            journal, created = Journal.objects.get_or_create(
                title=get_random_book_title(),
                author=Author.objects.get_or_create(name=get_random_author())[0],
                publish_at=get_random_date(),
                views=random.randint(0, 100),
                reviewed=random.choice([True, False])
            )

            journal.categories.set(categories)
            journal.save()
