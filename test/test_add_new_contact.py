# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname=u"Sofia", middlename="Sofia", lastname="Alekseeva", nickname="asofiaa", title="title", company="company", address="address", home="123", mobile="123", work="123", fax="123", email="aaa@aaa.ru", email2="aaa@aaa.ru", email3="aaa@aaa.ru", homepage="google.com", bday="15", bmonth="December", byear="1995", aday="10", amonth="January", ayear="1996", address2="address2", phone2="123", notes="notes"))
    app.contact.return_to_the_home_page()
    app.session.logout()
