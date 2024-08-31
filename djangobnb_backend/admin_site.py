from django.contrib import admin

class MyAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return True  # Bypasses the login requirement

admin_site = MyAdminSite(name='myadmin')
