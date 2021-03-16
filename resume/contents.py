from . import section_ids

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, NextPageTemplate


para_style = ParagraphStyle(name='Normal', fontName='oswald_light', fontSize=8,)
full_paragraph = Paragraph("HI SANTO HERE", style=para_style)


Elements = []
Elements.append(NextPageTemplate(section_ids.default))
Elements.append(full_paragraph)


from reportlab.platypus import Table as RLTable
from reportlab.platypus import TableStyle
from reportlab.lib import colors

from .text import data

# ===========================  Education table ===============================
edu = data['education']
tab=edu['table']
education_table_data = [tab['columns']] + tab['data']

education_table = RLTable(education_table_data)
education_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.2, 0.2, 0.3)),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                            ("ALIGN", (0,0), (-1, 0), "CENTER"), # align only the header row.. if not end cell shoudl be (-1,-1)
                            ("FONTNAME", (0,0), (-1, 0), "yanone"),  # header font
                            ("FONTSIZE", (0,0), (-1, 0), 9),  # header font size
                            ("FONTNAME", (0, 1), (-1, -1), "oswald_extralight"),  # other row fonts
                            ("FONTSIZE", (0, 1), (-1, -1), 8),  # font size of other rows
                            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                            ("ALIGN", (1, 0), (-1, -1), "CENTER"),  # all columns except name center align
                            ]))

# further customizing
internal_border_color = colors.white
start = 1

# adding horizontal lines as borders and alighning left Institution column of each row
for i in range(start, len(education_table_data)): # 1 because don't want header row to have horizontal line
    table_style = TableStyle([
        # ("LINEABOVE", (0,i), (-1, i), 0.1, internal_border_color),
        ("ALIGN", (1, i), (1, i), "LEFT") ,  # adding left align to institution column
    ])
    education_table.setStyle(table_style)

Elements.append(education_table)
# ===========================================================================





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

