from . import master
from .settings import *

from reportlab.platypus import (Paragraph, Spacer, CondPageBreak, FrameBreak, PageBegin,
                                NextPageTemplate, PageBreak, PageTemplate)
from . import fonts

fonts.register()

# initializing document
doc = master.document()

# setting frame
resume_frame = master.single_frame(doc, id='normal')
from . import section_ids

# setting master
doc.addPageTemplates([PageTemplate(id=section_ids.default, frames=resume_frame, onPage=master.default_master),
                    #   PageTemplate(id=message_section_id, frames=single_frame, onPage=message_master),
                      ])

# Adding elements
from .contents import Elements
# Elements.append(Spacer(1, PAGE_HEIGHT * 0.3))



Elements.append(PageBreak())  # skipping the other side of first title page

# start the construction of the pdf
doc.build(Elements)


