# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name=u"Новая группа", header=u"хедер", footer=u"футер"))
    app.session.logout()