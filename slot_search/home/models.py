from django.db import models

class District(models.Model):
    district_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'district'

    def __unicode__(self):
        return "%s (%s)"%(self.district_name, self.id)

class Center(models.Model):
    center_id = models.CharField(max_length=50)     # center_id: 574000
    district = models.ForeignKey(District, null=True, blank=True, related_name='center_district', on_delete=models.SET_NULL)          # district_name: "Jaipur II"
    center_name = models.CharField(max_length=255, null=True, blank=True)  # name: "Banskho Covaxin"
    address = models.CharField(max_length=255, null=True, blank=True)      # address: "Banskho CHC"
    block_name = models.CharField(max_length=255, null=True, blank=True)   # block_name: "Bassi"
    pincode = models.CharField(max_length=10, null=True, blank=True)       # pincode: 303305
    state_name = models.CharField(max_length=255, null=True, blank=True)   # state_name: "Rajasthan"
    fee_type = models.CharField(max_length=10, default="Free")             # fee_type: "Free"
    # lat = models.IntegerField()  # lat: 26
    # long = models.IntegerField() # long: 76
    # from: "09:00:00"
    # to: "15:00:00"
    class Meta:
        db_table = 'center'

    def __unicode__(self):
        return "%s (%s), %s, %s, %s, %s-%s"%(self.center_name, self.center_id, self.address, self.block_name, self.district.district_name, self.state_name, self.pincode )


class Slot(models.Model):
    center = models.ForeignKey(Center, null=True, blank=True, related_name='slot_center', on_delete=models.SET_NULL)          # district_name: "Jaipur II"
    min_age_limit = models.IntegerField()
    available_capacity = models.IntegerField()
    available_capacity_dose1 = models.IntegerField()
    available_capacity_dose2 = models.IntegerField()
    date = models.CharField(max_length=15, null=True, blank=True)      # date: "22-05-2021"
    vaccine = models.CharField(max_length=50, null=True, blank=True)   # vaccine: "COVAXIN"
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'slot'

    def __unicode__(self):
        return "%s (%s), Age: %s, Available:%s" % (self.center.center_name, self.center.center_id, str(self.min_age_limit), str(self.available_capacity))
