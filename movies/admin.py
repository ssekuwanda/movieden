from django.contrib import admin
from .models import Movie, Downloaded, QrCodePayment
from .models import SaleSummary
from django.contrib.admin.options import ModelAdmin
from django.db.models import Count, Sum

@admin.register(SaleSummary)
class SaleSummaryAdmin(ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'
    date_hierarchy = 'timestamp'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Count('id'),
            'total_sales': Sum('amount'),
        }

        response.context_data['summary'] = list(
            qs
            .values('creator')
            .annotate(**metrics)
            .order_by('-total_sales')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        return response

admin.site.register(Movie)
admin.site.register(Downloaded)
admin.site.register(QrCodePayment)