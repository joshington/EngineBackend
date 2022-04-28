#custom renderer which exports data in EXcel or PDF format.
from email import charset
import os,openpyxl,pdfkit,random

from django.template.loader import render_to_string

from rest_framework.renderers import BaseRenderer 
from rest_framework.response import Response 


#for newwer python do the configuration for pdfkit
config=pdfkit.configuration(wkhtmltopdf=r'path_to_bin/wkhtmltopdf')

class XLSXRenderer(BaseRenderer):
    pass 

class PDFRenderer(BaseRenderer):
    media_type = 'application/pdf'
    format='pdf'
    charset='utf-8'

    def render(self,data,accepted_media_type=None,renderer_context=None):
        if hasattr(data, 'items'):
            for key,value in data.items():
                if key == 'results':
                    html_string = render_to_string(
                        'user_mbe/EmployeeList.html',
                        {'header':('first_name','last_name','id_number','phone_number','email',
                            'job_title'
                        ),'data':[tuple(x.values()) for x in value]})
                    result = pdfkit.from_string(html_string,output_path=False, configuration=config)
                    return result 
        return None