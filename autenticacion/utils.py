from re import template
from unittest import result
# from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

def render_to_pdf(template_scr, context_dic={}):
    template = get_template(template_scr)
    html = template.render(context_dic)
    result = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    # if not pdf.err:
        # return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None