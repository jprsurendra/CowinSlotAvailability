from django.views.generic import TemplateView
from django.http import HttpResponse
from home.models import Slot


class MainPage(TemplateView):
    template_name = 'home/ index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MainPage, self).get_context_data(*args, **kwargs)
        slots = []

        slot_queryset = Slot.objects.all().order_by('-date', 'min_age_limit', '-available_capacity_dose1', '-available_capacity')
        for slot in slot_queryset:
            try:
                created_on = slot.created_on.strftime("%b %d, %Y %H:%M:%S") # "%b %d, %Y")
            except:
                created_on = '--'
            slots.append({
                'date': slot.date,
                'fee_type': slot.center.fee_type,
                'min_age_limit': str(slot.min_age_limit) ,
                'available_capacity': str(slot.available_capacity) + '  (Dose1: ' + str(slot.available_capacity_dose1) + ', Dose2: ' + str(slot.available_capacity_dose2) + ')',
                'vaccine': slot.vaccine,
                'center_name': slot.center.center_name + ' (' + slot.center.center_id + ')',
                'center_address': slot.center.address + ', ' + slot.center.block_name + ', ' + slot.center.district.district_name + ', ' + slot.center.state_name + ', ' + slot.center.pincode,
                'created_on': created_on,
            })

        context['slots'] = slots
        return context


def do_empty(request):
    try:
        deleted, _rows_count = Slot.objects.all().delete()

        html = "<html><body>%s row(s) deleted.</body></html>" % _rows_count.get('home.Slot', 0)
        return HttpResponse(html)
    except Exception as e:
        html = "<html><body>Exception:.</body></html>" % str(e)
        return HttpResponse(html)

def do_start(request):
    try:
        from slot_search.CowinSlotAvailability import  CowinSlotAvailability
        slot_finder = CowinSlotAvailability(chk_date="22-05-2021")  # chk_district=571
        slot_finder.do_start()

        html = "<html><body>work started ....</body></html>"
        return HttpResponse(html)
    except Exception as e:
        html = "<html><body>Exception:.</body></html>" % str(e)
        return HttpResponse(html)
