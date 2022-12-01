class Storage(object):  # storage = Storge()
    """
    Singleton storage.

    Read more about singleton design pattern:
    https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    https://en.wikipedia.org/wiki/Singleton_pattern

    It is used to emulate in-memory storage.
    It should be replaced with a database in a real application.
    """

    myobj = None
    myitems = None

    @classmethod
    def __new__(cls, *args):
        """Docstring."""
        if cls.myobj is None:
            cls.myobj = object.__new__(cls)  # noqa: WPS609
            cls.myitems = []
        return cls.myobj
