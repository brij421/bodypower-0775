# from django.test import TestCase
# from .models import Member
# import datetime

# # Create your tests here.
# class MemberTestCase(TestCase):
#     def setUp(self):
#         Member.objects.create(
#                                 first_name='Brijesh',
#                                 last_name='Makwana',
#                                 mobile_number='0899568334',
#                                 email='brijeshmk07@gmail.com',
#                                 registration_date=datetime.datetime.now(),
#                                 subscription_type='gym',
#                                 subscription_period='1',
#                                 amount='500',
#                                 fee_status='paid',
#                                 batch='morning',
#                             )

#     def test_member(self):
#         check = Member.objects.get(first_name='Brijesh')
#         print(check)
