# -*- coding: utf-8 -*- 
from unittest import TestCase
from django.test import TestCase as DjangoTestCase
from django_robokassa.forms import RobokassaForm, ResultURLForm
from django_robokassa.conf import LOGIN, PASSWORD1, PASSWORD2

class RobokassaFormTest(TestCase):
    def setUp(self):
        self.maxDiff = None
        self.form = RobokassaForm(initial = {
                       'OutSum': 100.00,
                       'InvId': 58,
                       'Desc' : u'Холодильник "Бирюса"',
                       'Email' : 'vasia@example.com'
                    })

    def testSignature(self):
        self.assertEqual(self.form._get_signature_string(),
                         '%s:100.0:58:%s:shpparam1=None:shpparam2=None' % (LOGIN, PASSWORD1))
        self.assertEqual(len(self.form.fields['SignatureValue'].initial), 32)

    def testSignatureMissingParams(self):
        form = RobokassaForm(initial = {'InvId': 5})
        self.assertEqual(form._get_signature_string(),
                         '%s::5:%s:shpparam1=None:shpparam2=None' % (LOGIN, PASSWORD1))

    def testRedirectUrl(self):
        url = "https://auth.robokassa.ru/Merchant/Index.aspx?MrchLogin=test_login&OutSum=100.0&InvId=58&Desc=%D0%A5%D0%BE%D0%BB%D0%BE%D0%B4%D0%B8%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA+%22%D0%91%D0%B8%D1%80%D1%8E%D1%81%D0%B0%22&SignatureValue=0EC23BE40003640B35EC07F6615FFB57&Email=vasia%40example.com&Encoding=utf-8&shpparam1=None&shpparam2=None"
        self.assertEqual(self.form.get_redirect_url(), url)


class RobokassaFormExtraTest(TestCase):
    def testExtra(self):
        form = RobokassaForm(initial={
                                'InvId': 58,
                                'OutSum': 100,
                                'param1': 'value1',
                                'param2': 'value2'
                            })
        self.assertEqual(form._get_signature_string(),
                         '%s:100:58:%s:shpparam1=value1:shpparam2=value2' % (LOGIN, PASSWORD1))


class ResultURLTest(DjangoTestCase):

    def testFormExtra(self):
        form = ResultURLForm({
                'OutSum': '100',
                'InvId': '58',
                'SignatureValue': 'B2111A06F6B7A1E090D38367BF7032D9',
                'shpparam1': 'Vasia',
                'shpparam2': 'None',
             })
        self.assertTrue(form.is_valid())
        self.assertEqual(form._get_signature_string(),
                         '100:58:%s:shpparam1=Vasia:shpparam2=None' % (PASSWORD2))
        self.assertEqual(form.extra_params(), {'param1': 'Vasia', 'param2': 'None'})


    def testFormValid(self):

        self.assertTrue(ResultURLForm({
                'OutSum': '100',
                'InvId': '58',
                'SignatureValue': '877D3BAF8381F70E56638C3BC82580C5',
                'shpparam1': 'None',
                'shpparam2': 'None',
             }).is_valid())

        self.assertFalse(ResultURLForm({
                'OutSum': '101',
                'InvId': '58',
                'SignatureValue': '877D3BAF8381F70E56638C3BC82580C5',
                'shpparam1': 'None',
                'shpparam2': 'None',
             }).is_valid())

        self.assertFalse(ResultURLForm({
                'OutSum': '100',
                'InvId': '58',
                'SignatureValue': '877D3BAF8381F70E56638C3BC82580C5',
                'shpparam1': 'Vasia',
                'shpparam2': 'None',
             }).is_valid())

    def testEmptyFormValid(self):
        self.assertFalse(ResultURLForm().is_valid())
