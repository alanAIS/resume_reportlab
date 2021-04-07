from . import master
from .settings import *

from reportlab.platypus import (Paragraph, Spacer, CondPageBreak, FrameBreak, PageBegin,
                                NextPageTemplate, PageBreak, PageTemplate)
from . import fonts

fonts.register()

# initializing document
doc = master.document()

# setting frame
from .page_templates import A4_letter_template

# setting master
doc.addPageTemplates([A4_letter_template,
                    #   PageTemplate(id=message_section_id, frames=single_frame, onPage=message_master),
                      ])

# Adding elements
from .contents import Elements



# Elements.append(PageBreak())  # skipping the other side of first title page

# start the construction of the pdf
doc.build(Elements)

import os
os.startfile(export_name_url)

