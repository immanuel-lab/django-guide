from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import generic
from django.contrib.auth import REDIRECT_FIELD_NAME
from admin_honeypot.forms import HoneypotLoginForm
from admin_honeypot.models import LoginAttempt
from admin_honeypot.signals import honeypot


class AdminHoneypot(generic.FormView):
    """
    Fake Django admin login view that captures login attempts
    but never authenticates anyone.
    """
    template_name = 'admin_honeypot/login.html'
    form_class = HoneypotLoginForm

    def dispatch(self, request, *args, **kwargs):
        # Always keep a trailing slash
        if not request.path.endswith('/'):
            return redirect(request.path + '/', permanent=True)
        # Never call Django's real login redirection
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return self.form_class(self.request, **self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'app_path': self.request.get_full_path(),
            REDIRECT_FIELD_NAME: reverse('admin_honeypot:index'),
            'title': _('Log in'),
        })
        return context

    def form_valid(self, form):
        # Always pretend login failed
        return self.form_invalid(form)

    def form_invalid(self, form):
        # Record the attempt
        instance = LoginAttempt.objects.create(
            username=self.request.POST.get('username'),
            session_key=self.request.session.session_key,
            ip_address=self.request.META.get('REMOTE_ADDR'),
            user_agent=self.request.META.get('HTTP_USER_AGENT'),
            path=self.request.get_full_path(),
        )
        honeypot.send(sender=LoginAttempt, instance=instance, request=self.request)

        # Add a fake “invalid credentials” message
        form.add_error(None, _("Please enter the correct username and password for a staff account."))
        return super().form_invalid(form)
