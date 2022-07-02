from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import home.views
import timesheet.views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", include('account.urls', namespace="account")),
                  path("", include('user_profile.urls', namespace="user_profile")),
                  path("", include('appointment.urls', namespace="appointment")),
                  path('drugs/', include('drugs.urls', namespace='drugs')),
                  path('timesheet/', timesheet.views.timesheet, name='timesheet'),
                  path('month/', timesheet.views.MonthView.as_view(), name='month'),
                  path('year/', timesheet.views.YearView.as_view(), name='year'),
                  path('timesheetday/edit/<int:timesheetday_id>/', timesheet.views.timesheetday,
                       name='timesheetday_edit'),
                  path('workingday/edit/<int:workingday_id>/', timesheet.views.workingday, name='workingday_edit'),
                  path('paycheck/edit/<int:paycheck_id>/', timesheet.views.paycheck, name='paycheck_edit'),
                  path('massive_edit/', timesheet.views.massive_edit, name='massive_edit'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
