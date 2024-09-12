from openpyxl import Workbook
from django.http import HttpResponse

class ExportExcelMixin:
    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'
        wb = Workbook()
        ws = wb.active
        ws.append(field_names)
        for obj in queryset:
            data = []
            for field in field_names:
                value = getattr(obj, field)
                if isinstance(value, (str, int, float)):
                    data.append(value)
                else:
                    data.append(str(value))  # 转换为字符串
            ws.append(data)
        wb.save(response)
        return response
    export_as_excel.short_description = '导出Excel'
