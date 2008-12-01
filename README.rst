Django Singletons
=================

Please note, the code is not currently in a working state (even if it does somehow work for you). This is a proof of concept and should be considered as much.

A brief overview of the design implementation can be found on the Django project Trac: http://code.djangoproject.com/ticket/17


Usage
-----
The following marks a model as active within the Singleton cache. This enable all queries (and relational queries) to this model to use the singleton instance cache, effectively creating a single instance for each unique row (based on primary key) in the queryset.
::

	from singletons import SingletonModel

	class MyModel(SingletonModel):
	    ...

