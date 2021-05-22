from home.models import  District


def load_on_startup():
	pass
	from slot_search.CowinSlotAvailability import  CowinSlotAvailability
	slot_finder = CowinSlotAvailability(chk_date = "22-05-2021") # chk_district=571
	slot_finder.do_start()

	# districts=[
	# 	{
	# 		"id": 507,
	# 		"district_name": "Ajmer"},
	# 	{
	# 		"id": 512,
	# 		"district_name": "Alwar"},
	# 	{
	# 		"id": 519,
	# 		"district_name": "Banswara"},
	# 	{
	# 		"id": 516,
	# 		"district_name": "Baran"},
	# 	{
	# 		"id": 528,
	# 		"district_name": "Barmer"},
	# 	{
	# 		"id": 508,
	# 		"district_name": "Bharatpur"},
	# 	{
	# 		"id": 523,
	# 		"district_name": "Bhilwara"},
	# 	{
	# 		"id": 501,
	# 		"district_name": "Bikaner"},
	# 	{
	# 		"id": 514,
	# 		"district_name": "Bundi"},
	# 	{
	# 		"id": 521,
	# 		"district_name": "Chittorgarh"},
	# 	{
	# 		"id": 530,
	# 		"district_name": "Churu"},
	# 	{
	# 		"id": 511,
	# 		"district_name": "Dausa"},
	# 	{
	# 		"id": 524,
	# 		"district_name": "Dholpur"},
	# 	{
	# 		"id": 520,
	# 		"district_name": "Dungarpur"},
	# 	{
	# 		"id": 517,
	# 		"district_name": "Hanumangarh"},
	# 	{
	# 		"id": 505,
	# 		"district_name": "Jaipur I"},
	# 	{
	# 		"id": 506,
	# 		"district_name": "Jaipur II"},
	# 	{
	# 		"id": 527,
	# 		"district_name": "Jaisalmer"},
	# 	{
	# 		"id": 533,
	# 		"district_name": "Jalore"},
	# 	{
	# 		"id": 515,
	# 		"district_name": "Jhalawar"},
	# 	{
	# 		"id": 510,
	# 		"district_name": "Jhunjhunu"},
	# 	{
	# 		"id": 502,
	# 		"district_name": "Jodhpur"},
	# 	{
	# 		"id": 525,
	# 		"district_name": "Karauli"},
	# 	{
	# 		"id": 503,
	# 		"district_name": "Kota"},
	# 	{
	# 		"id": 532,
	# 		"district_name": "Nagaur"},
	# 	{
	# 		"id": 529,
	# 		"district_name": "Pali"},
	# 	{
	# 		"id": 522,
	# 		"district_name": "Pratapgarh"},
	# 	{
	# 		"id": 518,
	# 		"district_name": "Rajsamand"},
	# 	{
	# 		"id": 534,
	# 		"district_name": "Sawai Madhopur"},
	# 	{
	# 		"id": 513,
	# 		"district_name": "Sikar"},
	# 	{
	# 		"id": 531,
	# 		"district_name": "Sirohi"},
	# 	{
	# 		"id": 509,
	# 		"district_name": "Sri Ganganagar"},
	# 	{
	# 		"id": 526,
	# 		"district_name": "Tonk"},
	# 	{
	# 		"id": 504,
	# 		"district_name": "Udaipur"}]
	# save_district_list = []
	# for district in districts:
	# 	save_district_list.append(District(**district))
	# District.objects.bulk_create(save_district_list)