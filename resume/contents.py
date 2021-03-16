from . import section_ids

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, NextPageTemplate


para_style = ParagraphStyle(name='Normal', fontName='oswald_light', fontSize=8,)
full_paragraph = Paragraph("HI SANTO HERE", style=para_style)


Elements = []
Elements.append(NextPageTemplate(section_ids.default))
Elements.append(full_paragraph)


from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
style = styles["Normal"]
t = ListFlowable([
    Paragraph("Item no.1", style),
    ListItem(Paragraph("Item no. 2", style),bulletColor="green",value=7),
    ListFlowable(
        [
        Paragraph("sublist item 1", style),
        ListItem(Paragraph('sublist item 2', style),bulletColor='red',value='square')
        ], bulletType='bullet', start='square',),
    Paragraph("Item no.4", style)],
bulletType='i'
)
Elements.append(t)

