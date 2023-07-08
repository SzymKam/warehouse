from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
)


class MyPasswordResetView(PasswordResetView):
    template_name = "staff/password-reset.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM Password reset"
        context["subtitle"] = "Reset Password"
        return context


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "staff/password-reset-sent.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM Password reset sent"
        context["subtitle"] = "Password reset sent"
        return context


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "staff/password-reset-done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM Password reset done"
        context["subtitle"] = "Password reset done"
        return context


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "staff/password-reset-form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM Password reset confirm"
        context["subtitle"] = "Password reset confirm"
        return context
