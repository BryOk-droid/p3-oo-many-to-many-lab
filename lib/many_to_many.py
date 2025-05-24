class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Author name must be a string")
        self._name = value

    def contracts(self):
        """Return list of Contract instances for this author."""
        return [c for c in Contract.all if c.author is self]

    def books(self):
        """Return list of Book instances authored by this author via contracts."""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date_str, royalties):
        """
        Create and return a new Contract between this author and the given book.
        date_str should be a string; royalties should be an int or float.
        """
        return Contract(self, book, date_str, royalties)

    def total_royalties(self):
        """Return the sum of royalties across all this author's contracts."""
        return sum(c.royalties for c in self.contracts())

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Book title must be a string")
        self._title = value

    def contracts(self):
        """Return list of Contract instances for this book."""
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        """Return list of Author instances that have contracts for this book."""
        return [c.author for c in self.contracts()]

class Contract:
    all = []

    def __init__(self, author, book, date_str, royalties):
        # validate types
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date_str, str):
            raise Exception("date must be a string")
        if not (isinstance(royalties, int) or isinstance(royalties, float)):
            raise Exception("royalties must be a number")

       
        self.author = author
        self.book = book
        self.date = date_str
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date_str):
        """Return list of Contract instances with matching date."""
        if not isinstance(date_str, str):
            raise Exception("date must be a string")
        return [c for c in cls.all if c.date == date_str]
