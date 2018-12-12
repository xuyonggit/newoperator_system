# -*- coding: utf-8 -*-
from user.models import tb_user
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from newoperator_system.settings import EMAIL_HOST_USER



def SendMultiEmail(title, tolist=[], template='Email.html', **kwargs):
    context = kwargs
    email_templage_name = template
    t = loader.get_template(email_templage_name)
    from_email = EMAIL_HOST_USER
    html_content = t.render(context)
    if isinstance(tolist, list) and len(tolist) > 0:
        msg = EmailMultiAlternatives(title, html_content, from_email, tolist)
        msg.attach_alternative(html_content, "text/html")
        msg.send()


