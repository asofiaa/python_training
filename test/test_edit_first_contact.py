# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname=u"Anastasia", middlename="Vera", lastname="Aleksandrova", nickname="aleksandria", title="title", company="company", address="address", home="123", mobile="123", work="123", fax="123", email="aaa@aaa.ru", email2="aaa@aaa.ru", email3="aaa@aaa.ru", homepage="google.com", bday="29", bmonth="December", byear="1986", aday="13", amonth="January", ayear="1995", address2="address2", phone2="123", notes="notes"))
    app.session.logout()