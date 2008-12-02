Django Singletons
=================

Please note, the code is a proof of concept, and should be considered as only lightly tested.

A brief overview of the design implementation can be found on the Django project Trac: http://code.djangoproject.com/ticket/17


Usage
-----
To use the singleton model you simply need to inherit from it (instead of models.Model). This enable all queries (and relational queries) to this model to use the singleton instance cache, effectively creating a single instance for each unique row (based on primary key) in the queryset.

For example, if you want to simply mark all of your models as a SingletonModel, you might as well just import it as models.
::

	import singletons as models

	class MyModel(models.SingletonModel):
	    name = models.CharField(...)

Because the system is isolated, you may mix and match SingletonModel's with regular Model's.
::

	import singletons as models

	class MyModel(models.SingletonModel):
    	name = models.CharField(...)
		fkey = models.ForeignKey('Other')

	class Other(models.Model):
		name = models.CharField(...)