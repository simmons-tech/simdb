from django.db import models
from .utils import NullableTextField


class SDB_sds_users_all(models.Model):
    username = models.TextField(primary_key=True)
    # password = NullableTextField(null=True, blank=True)
    # salt = NullableTextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    # hosts_allow = models.TextField(default='%')
    # immortal = models.BooleanField(default=False)

    class Meta:
        db_table = 'sds_users_all'
        managed = False

    def __str__(self):
        return self.username


class SDB_rooms(models.Model):
    room = models.TextField(primary_key=True)
    floor = models.IntegerField(null=True)
    type = models.TextField()
    size = models.IntegerField(null=True)
    # phone1
    # phone2
    grt = models.TextField(null=True)
    frosh = models.NullBooleanField()
    handicapped = models.NullBooleanField()

    class Meta:
        db_table = 'rooms'
        managed = False

    def __str__(self):
        return self.room


class SDB_user_types(models.Model):
    type = models.TextField(primary_key=True)
    description = NullableTextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'user_types'
        managed = False

    def __str__(self):
        return self.type


class SDB_lounges(models.Model):
    lounge = models.TextField(primary_key=True)
    description = models.TextField()
    # url = NullableTextField(null=True, blank=True,
    # default='http://simmons.mit.edu/atria/')
    contact = models.ForeignKey(SDB_sds_users_all,
                                related_name='lounge_contact1')
    contact2 = models.ForeignKey(SDB_sds_users_all, null=True,
                                 related_name='lounge_contact2')
    active = models.BooleanField(default=True)
    # allocation = models.DecimalField(10, 2, null=True)
    # allocation2 = models.DecimalField(10, 2, null=True)

    class Meta:
        db_table = 'lounges'
        managed = False

    def __str__(self):
        return self.lounge


class SDB_public_active_directoryManager(models.Manager):
    def get_queryset(self):
        return super(SDB_public_active_directoryManager, self) \
            .get_query_set().filter(
                private=False,
                username__active=True)


class SDB_directory(models.Model):
    username = models.OneToOneField(SDB_sds_users_all, primary_key=True)
    firstname = models.TextField()
    lastname = models.TextField()
    room = models.ForeignKey(SDB_rooms, null=True)
    # phone = NullableTextField(null=True, blank=True)
    year = models.IntegerField(null=True)
    cellphone = NullableTextField(null=True, blank=True)
    homepage = NullableTextField(null=True, blank=True)
    home_city = NullableTextField(null=True, blank=True)
    home_state = NullableTextField(null=True, blank=True)
    home_country = NullableTextField(null=True, blank=True)
    quote = NullableTextField(null=True, blank=True)
    favorite_category = NullableTextField(null=True, blank=True)
    favorite_value = NullableTextField(null=True, blank=True)
    private = models.BooleanField(default=False)
    type = models.ForeignKey(SDB_user_types)
    email = models.TextField()
    lounge = models.ForeignKey(SDB_lounges, null=True, blank=True)
    title = NullableTextField(null=True, blank=True)
    loungevalue = models.IntegerField(null=True, blank=True)
    showreminders = models.BooleanField(default=True)
    guest_list_expiration = models.TextField(null=True, blank=True)

    objects_public_active_directory = SDB_public_active_directoryManager()

    def save(self, *args, **kwargs):
        raise Exception('Save called on directory')

    def delete(self, *args, **kwargs):
        raise Exception(
            'You should not be calling delete on this model (directory)')

    @staticmethod
    def random():
        import random as r
        count = SDB_directory.objects.count()
        random_index = r.randint(0, count - 1)
        return SDB_directory.objects.all()[random_index]

    class Meta:
        db_table = 'directory'  # 'public_active_directory'
        managed = False

    def __str__(self):
        return '%s %s (%s)' % (self.firstname, self.lastname, self.username)
