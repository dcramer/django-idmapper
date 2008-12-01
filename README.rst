A brief overview of the design implementation (see http://code.djangoproject.com/ticket/17 for more information).

    from singletons import SingletonModel

    class MyModel(SingletonModel):
        ....

This will enable all queries (and relational queries) to this model to use the singleton cache.