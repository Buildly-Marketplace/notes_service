from django.db import models
from django.utils import timezone


class NoteProvider(models.Model):
    provider_id = models.UUIDField('Note Provider UUID', null=True, blank=True)
    provider_name = models.CharField('Name of service connecting to for Notes', max_length=355, blank=True)
    provider_url = models.CharField('Main URL of Note Provider', max_length=355, blank=True)
    provider_api = models.CharField('Base API URL', max_length=355, blank=True)
    auth_type = models.CharField("Password or Token auth", max_length=355, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('note_provider_type', 'note_provider_username')

    def __unicode__(self):
        return '{}'.format(self.indicator_type) or ''

    def save(self, *args, **kwargs):
        # onsave add create date or update edit date
        if self.create_date == None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(NoteType, self).save(*args, **kwargs)


class UserRegistration(models.Model):
    core_userid = models.UUIDField('Buildly Core User ID UUID', null=True, blank=True)
    note_provider_type = models.ForeignKey("Note Provider", null=True, on_delete=models.SET_NULL)
    note_provider_username = models.CharField("Username on Provider Service", max_length=355, blank=True)
    note_provider_token = models.CharField("Token or Password on Provider service", max_length=355, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('note_provider_type','note_provider_username')

    def __unicode__(self):
        return '{}'.format(self.indicator_type) or ''

    def save(self, *args, **kwargs):
        # onsave add create date or update edit date
        if self.create_date == None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(UserRegistration, self).save(*args, **kwargs)