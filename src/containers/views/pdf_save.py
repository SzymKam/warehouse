from django.shortcuts import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa
from staff.models import StaffModel
from datetime import date
from containers.models import Container
from containers.views.equipment_crud import MODEL_LIST
from django.contrib.auth.decorators import login_required


@login_required()
def save_to_pdf(request, element, element_id=None) -> HttpResponse:
    map_elements = {
        "containers": {
            "object_list": Container.objects.all(),
            "template": "containers/containers-list-pdf.html",
            "title": "List of medical equipment containers",
        },
        "all": {
            "object_list": [model.objects.all() for model in MODEL_LIST],
            "template": "containers/equipment-all-pdf.html",
            "title": "List of all medical equipment of GRM PCK",
        },
        "staff": {
            "object_list": StaffModel.objects.all(),
            "template": "staff/staff-all-pdf.html",
            "title": "List of staff",
        },
        "r1_backpack": {
            "object_list": "",
            "template": "containers/r1-backpack-pdf.html",
            "title": "R1 backpack - standard equipment",
        },
        "r1_additions": {
            "object_list": "",
            "template": "containers/r1-additions-pdf.html",
            "title": "R1 bag - additional equipment",
        },
        "als_backpack": {
            "object_list": "",
            "template": "containers/als-backpack-pdf.html",
            "title": "ALS backpack - standard equipment",
        },
    }
    if element_id is not None:
        map_elements["container"] = {
            "object_list": {
                "container": Container.objects.filter(pk=element_id),
                "equipment": [
                    model.objects.filter(container=element_id) for model in MODEL_LIST
                ],
            },
            "template": "containers/containers-detail-pdf.html",
            "title": f"Equipment list of: {Container.objects.filter(pk=element_id)[0].name}",
        }

    template = get_template(map_elements[element]["template"])
    context = {
        "object_list": map_elements[element]["object_list"],
        "title": map_elements[element]["title"],
    }

    html = template.render(context)

    pdf_file = HttpResponse(content_type="application/pdf")
    pdf_file[
        "Content-Disposition"
    ] = f'attachment; filename="{element}-{date.today()}.pdf'

    pisa_status = pisa.CreatePDF(html, dest=pdf_file)

    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)

    return pdf_file
