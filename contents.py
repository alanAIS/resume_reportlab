from . import section_ids

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, NextPageTemplate


para_style = ParagraphStyle(name='Normal', fontName='oswald_light', fontSize=8,)
full_paragraph = Paragraph("HI SANTO HERE", style=para_style)


Elements = []
Elements.append(NextPageTemplate(section_ids.default))
Elements.append(full_paragraph)


