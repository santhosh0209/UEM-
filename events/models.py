from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from phone_field import PhoneField


EVENT_STATUSES = (
    (0, 'Closed'),
    (1, 'Open'),
)

PARTICIPATION_STATUSES = (
    (0, 'No, thanks'),
    (1, 'I may attend'),
    (2, 'I\'ll be there'),
)


class Event(models.Model):
    title = models.CharField(max_length=200, default=None)
    venue = models.CharField(max_length=200, default=None)
    department = models.CharField(max_length=100,default=None)
    event_category = models.CharField(max_length=200,default=None)
    description = models.TextField(default=None)
    # date = models.DateTimeField()
    date_added = models.DateField()
    event_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)

    event_status = models.PositiveIntegerField(
        choices=EVENT_STATUSES,
        default='1',
    )
    techinical_event = models.TextField(default=None)
    non_techinical_event = models.TextField(default=None)
    reg_fee_in_rupees = models.PositiveIntegerField(default=0)

    event_organizer_name = models.CharField(max_length=50, default=None)
    event_organizer_contact = models.CharField(max_length=10, default=None)
    student_coordinator_name = models.CharField(max_length=100,default=None)
    student_coordinator_mobile = models.CharField(max_length=10,default=None)

    event_booking_email = models.EmailField()
    event_image = models.ImageField(upload_to='image', blank=True,help_text="only upload an 750*500 photo")





    class Meta:
        ordering = ['-date_added']
        app_label = 'events'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" %(self.id)


class Participation(models.Model):
    event = models.ForeignKey(
        Event,
        related_name='event_participations',
        on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        User, related_name='person_partications',
        on_delete=models.CASCADE
    )
    participation_status = models.PositiveIntegerField(
        choices=PARTICIPATION_STATUSES,
        default='0',
    )
    date_registered = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #    return '{} - {} ({})'.format(self.person, self.event, self.get_status_display())


# in events
 # participants = models.ManyToManyField(
    #     User,
    #     related_name='in_events'
    # )
# organizers = models.ManyToManyField(
    #     User,
    #     related_name='organized_events')
