# https://github.com/vigneshjm/Cowin-Slot-Availability

import requests
import json
from datetime import datetime
import datetime
import sched, time
from datetime import date

from home.models import  District,  Center, Slot


class CowinSlotAvailability:

    def __init__(self, chk_district=506, min_age_limit = 18, chk_date = None):
        self.chk_district = chk_district
        self.min_age_limit = min_age_limit if min_age_limit==18 or min_age_limit==45 else 18
        if chk_date:
            self.chk_date = chk_date
        else:
            today = date.today()
            self.chk_date = today.strftime("%d-%m-%Y") # DD-MM-YYYY

        self.task = sched.scheduler(time.time, time.sleep)

    def get_db_center(self, json_center):
        center_id = json_center.get('center_id', None)
        try:
            center = Center.objects.get(center_id=center_id)
            return center
        except Center.DoesNotExist:
            dict_center={
                'district_id': self.district.id,
                'center_id': json_center.get('center_id', None),
                'center_name': json_center.get('name', None),
                'address': json_center.get('address', None),
                'block_name': json_center.get('block_name', None),
                'pincode': json_center.get('pincode', None),
                'state_name': json_center.get('state_name', None),
                'fee_type': json_center.get('fee_type', None),
            }
            center= Center.objects.create(**dict_center)
            return center

    def check_availability(self, sc):
        # chk_date = "20-05-2021"
        # chk_district = 506  # "Jaipur II"
        # min_age_limit = 18
        browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={dist}&date={cdate}".format(dist = self.chk_district, cdate = self.chk_date)
        availabile_centers = []

        if(self.chk_date == '' or self.chk_district == ''):
          raise ValueError("Input Parameter missing")

        format = "%d-%m-%Y"
        try:
          datetime.datetime.strptime(self.chk_date, format)
        except:
          raise ValueError("Incorrect date format, should be DD-MM-YYYY")

        try:
            self.district = District.objects.get(id=self.chk_district)
        except District.DoesNotExist:
            raise ValueError("Incorrect district")

        print("===============================================================================")
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(" .... Search started ..... ", dt_string)
        response = requests.get(URL, headers=browser_header)
        if (response.ok) and ('centers' in json.loads(response.text)):
            resp_json = json.loads(response.text)['centers']
            for api_center in resp_json:
                db_center = self.get_db_center(json_center=api_center)
                for api_session in api_center['sessions']:
                    db_slot = {}
                    center = {}
                    if(api_session['available_capacity'] > 0 and api_session['min_age_limit'] == self.min_age_limit and api_session['date'] == self.chk_date):
                        db_slot = {
                            'center_id': db_center.id,
                            'min_age_limit': api_session.get('min_age_limit', None),
                            'available_capacity':api_session.get('available_capacity', None),
                            'available_capacity_dose1':api_session.get('available_capacity_dose1', None),
                            'available_capacity_dose2':api_session.get('available_capacity_dose2', None),
                            'date': api_session.get('date', None),
                            'vaccine': api_session.get('vaccine', None),
                            'created_on': now
                        }
                        Slot.objects.create(**db_slot)
                        center['slots'] = api_session['slots']
                        center['date'] = api_session['date']
                        center['capacity'] = api_session['available_capacity']
                        center['cid'] = api_center['center_id']
                        center['name'] = api_center['name']
                        center['address'] = api_center['address']
                    if bool(center):
                        availabile_centers.append(center)
                        print("---------------------------------------------------------------")
                        print("slots: ", str(','.join(center['slots'])))
                        print("date: ", str(center['date']))
                        print("capacity: ", str(center['capacity']))
                        print("cid: ", str(center['cid']))
                        print("name: ", str(center['name']))
                        print("address: ", str(center['address']))

        # return True if len(availabile_centers)>0 else False
        if availabile_centers and len(availabile_centers)>0:
            return True
        else:
            self.task.enter(120, 1, self.check_availability, (sc,))


    def do_start(self):
        self.task.enter(5, 1, self.check_availability, (self.task,))
        self.task.run()



# if __name__ == "__main__":
#     slot_finder = CowinSlotAvailability(chk_date = "22-05-2021") # chk_district=571
#     slot_finder.do_start()