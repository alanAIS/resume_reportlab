# external libraries import
from reportlab.platypus import PageTemplate, NextPageTemplate
# internal imports
from . import master
doc = master.document()



#==================================   Template 01  =========================================
frame = master.single_frame(doc, id='normal')
section_id = "LETTER"
A4_letter_template = PageTemplate(id=section_id, frames=frame, onPage=master.default_master)
next_page_template = NextPageTemplate(section_id)
#===========================================================================================
