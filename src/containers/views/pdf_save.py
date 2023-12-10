from django.shortcuts import HttpResponse

# from django.template.loader import get_template
# from weasyprint import HTML
# from staff.models import StaffModel
# from datetime import date
# from containers.models import Container
# from containers.views.equipment_crud import MODEL_LIST
from django.contrib.auth.decorators import login_required


#
#
@login_required()
def save_to_pdf(request, element, element_id=None) -> HttpResponse:
    pass


#     map_elements = {
#         "containers": {
#             "object_list": Container.objects.all(),
#             "template": "containers/containers-list-pdf.html",
#         },
#         "all": {
#             "object_list": [model.objects.all() for model in MODEL_LIST],
#             "template": "containers/equipment-all-pdf.html",
#         },
#         "staff": {
#             "object_list": StaffModel.objects.all(),
#             "template": "staff/staff-all-pdf.html",
#         },
#         "r1_backpack": {
#             "object_list": "",
#             "template": "containers/r1-backpack-pdf.html",
#         },
#         "r1_additions": {
#             "object_list": "",
#             "template": "containers/r1-additions-pdf.html",
#         },
#         "als_backpack": {
#             "object_list": "",
#             "template": "containers/als-backpack-pdf.html",
#         },
#     }
#     if element_id is not None:
#         map_elements["container"] = {
#             "object_list": {
#                 "container": Container.objects.filter(pk=element_id),
#                 "equipment": [
#                     model.objects.filter(container=element_id) for model in MODEL_LIST
#                 ],
#             },
#             "template": "containers/containers-detail-pdf.html",
#         }
#
#     template = get_template(map_elements[element]["template"])
#     context = {"object_list": map_elements[element]["object_list"]}
#     html = template.render(context)
#
#     pdf_file = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()
#     response = HttpResponse(content_type="text/pdf")
#     response[
#         "Content-Disposition"
#     ] = f'attachment; filename="{element}-{date.today()}.pdf"'
#     response.write(pdf_file)
#
#     return response
