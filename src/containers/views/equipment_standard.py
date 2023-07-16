from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class StandardEquipment:
    @staticmethod
    @login_required
    def r1_backpack_standard(request):
        return render(
            request, "containers/r1-backpack.html", {"title": "R1 Backpack standard"}
        )

    @staticmethod
    @login_required
    def r1_additions_standard(request):
        return render(
            request, "containers/r1-additions.html", {"title": "R1 Additions standard"}
        )

    @staticmethod
    @login_required
    def als_backpack_standard(request):
        return render(
            request, "containers/als-backpack.html", {"title": "ALS Backpack standard"}
        )
