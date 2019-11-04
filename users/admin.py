# Authors; Yaseen Hull, Laeeq Diedericks, Thobeka Gumede
# Project; Capstone SITPG
# Date; September 2019

from django.contrib import admin
from .models import Profile
import csv
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.site_header = 'UCTPGP admin'
admin.autodiscover()
admin.site.unregister(Group)
admin.site.unregister(User)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export selected as csv"


class ExportPdfMixin:
    def export_as_pdf(self, request, queryset):
        file_name = "Applicant details.pdf"
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(file_name)

        for d in queryset.all():
            item = [d.user, d.name, d.surname, d.title, d.student_number, d.email_address, d.citizenship, d.country_of_origin, d.race, d.city_of_residence, d.country_of_residence, d.country_of_previous_institute, d.previous_degree, d.nqf_equivalent, d.minimum_year_of_degree, d.previous_university, d.degree, d.years_of_IT_experience, d.math_level, d.math_average, d.thesis_completed_previously, d.thesis_description]
            data = [ ['Name:'],[d.name], ['Surname:'],[d.surname], ['Title:'],[d.title], ['Student number:'],[d.student_number], ['Email address:'],[d.email_address], ['Citizenship:'],[d.citizenship], ['Country of Origin:'],[d.country_of_origin], ['Race:'],[d.race], ['City of Residence:'], [d.city_of_residence],['Country of Residence:'],[d.country_of_residence], [
                       'Country of Previous Institute:'],[d.country_of_previous_institute], ['Previous degree:'],[d.previous_degree], ['NQF Equivalent:'], [d.nqf_equivalent], [
                       'Minimum Year of Degree:'], [d.minimum_year_of_degree], ['Previous University:'], [d.previous_university], ['Degree:'], [d.degree], ['Years of IT Experience:'],[d.years_of_IT_experience], [
                       'Math Level:'],[d.math_level], ['Math Average:'],[d.math_average], ['Thesis Completed Previously'],[d.thesis_completed_previously], ['Thesis Description:'],[d.thesis_description]]

            #data.append(item)

        doc = SimpleDocTemplate(response, pagesize=(9 * inch, 12 * inch))
        elements = []

        table_data = Table(data)
        table_data.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                        ("FONTSIZE", (0, 0), (-1, -1), 13)]))
        elements.append(table_data)
        doc.build(elements)

        return response

    export_as_pdf.short_description = "Export selected as pdf"


class ProfilesAdmin(admin.ModelAdmin, ExportCsvMixin, ExportPdfMixin):
    list_display = ('surname', 'name', 'title', 'student_number', 'status')
    list_filter = ('degree', 'status')
    actions = ['export_as_csv', 'export_as_pdf']


admin.site.register(Profile, ProfilesAdmin)
