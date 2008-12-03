from django.db.models.manager import Manager

class SharedMemoryManager(Manager):
    # TODO: improve on this implementation
    # We need a way to handle reverse lookups so that this model can
    # still use the singleton cache, but the active model isn't required
    # to be a SharedMemoryModel.
    def get(self, **kwargs):
        items = kwargs.keys()
        if len(items) == 1 and items[0] in ('pk', self.model.pk.attname):
            return self.get_cached_instance(kwargs[item[0]])
        super(SharedMemoryManager, self).get(**kwargs)