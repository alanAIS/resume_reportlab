from . import section_ids
from .settings import PAGE_FRAME_WIDTH, PAGE_WIDTH, PAGE_FRAME_HEIGHT, PAGE_HEIGHT, LEFT_MARGIN, RIGHT_MARGIN, BOTTOM_MARGIN

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, NextPageTemplate, Table, TableStyle, Spacer


color_light = colors.Color(0.7, 0.8, 0.9)
color_general = colors.Color(0.2, 0.3, 0.4) 
color_deep_dark = colors.Color(0.2, 0.2, 0.3)
color_extra_light = colors.Color(0.9, 0.94, 0.94)
color_white = colors.Color(1, 1, 1)

from .text import data

def data_scientist_heading(text):
    first_cell = (0, 0)
    last_cell = (-1, -1)
    heading_title_table = Table(
            [[text.upper(),]], 
            colWidths=[PAGE_WIDTH],
            rowHeights=[PAGE_FRAME_HEIGHT/10,]
        )
    heading_title_table.setStyle(
        TableStyle([
            ('BACKGROUND', first_cell, last_cell, color_white),
            ("TEXTCOLOR", first_cell, last_cell, color_deep_dark),
            ('FONTSIZE', first_cell, last_cell, 35),
            ('TEXTFONT', first_cell, last_cell, 'Times-Bold'),
            ('ALIGN', first_cell, last_cell, 'CENTER'),
            ('VALIGN', first_cell, last_cell, 'MIDDLE'),
        ])
    )
    return heading_title_table


def produce_contact_heading_section(text_list):
    first_cell, last_cell = (0, 0), (-1, -1)
    col_widths = [LEFT_MARGIN] + [PAGE_FRAME_WIDTH/len(text_list) for i in range(len(text_list))] + [RIGHT_MARGIN]
    col_data = [""] + text_list + [""]
    heading_title_table = Table([col_data], colWidths=col_widths, rowHeights=[PAGE_FRAME_HEIGHT/36])
    heading_title_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), color_general),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.whitesmoke),
            ('FONTSIZE', first_cell, last_cell, 10),
            ("ALIGN", (1, 0), (-2, -1), "CENTER"),
            ("ALIGN", (1, 0), (1, 0), "LEFT"),
            ("ALIGN", (-2, 0), (-2, 0), "RIGHT"),
            ('VALIGN', first_cell, last_cell, "MIDDLE"),
        ])
    )
    # return [Spacer(width=PAGE_FRAME_WIDTH, height=4, isGlue=True), heading_title_table, Spacer(width=PAGE_FRAME_WIDTH, height=2, isGlue=True)]
    return heading_title_table

def horizontal_row(height=3, width=PAGE_FRAME_WIDTH, color=colors.Color(0.2, 0.3, 0.4)):
    row_table = Table([["",]], colWidths=[width], rowHeights=[height])
    row_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), color),
        ])
    )
    return [Spacer(width=PAGE_FRAME_WIDTH, height=4, isGlue=True), row_table, Spacer(width=PAGE_FRAME_WIDTH, height=2, isGlue=True)]

def ribbon(height=10, width=PAGE_FRAME_WIDTH, color=color_light, space_before=0):
    row_table = Table([["",]], colWidths=[width], rowHeights=[height])
    row_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), color),
        ])
    )
    return row_table
    # return [Spacer(width=PAGE_FRAME_WIDTH, height=space_before, isGlue=True), row_table, Spacer(width=PAGE_FRAME_WIDTH, height=2, isGlue=True)]


Elements = []
from .page_templates import next_page_template as letter_page_next_template
Elements.append(letter_page_next_template)  # marking section id to identify master page and style


# =========================== Header Resume =================================
# adding white space above everything to move the content towards bottom so as to reduce the space in the bottom
heading = data_scientist_heading("data scientist")
text_list = ["santokalayil@gmail.com", "+91 8891960880", "Hennur, Bengaluru"]
heading_contact = produce_contact_heading_section(text_list)

bottom_ribbon = ribbon(height=PAGE_FRAME_HEIGHT/36, width=PAGE_WIDTH, color=color_general, space_before=0)

heading.height = sum(heading._rowHeights)
heading_contact.height = sum(heading_contact._rowHeights)
bottom_ribbon.height = sum(bottom_ribbon._rowHeights)
fill_height = PAGE_FRAME_HEIGHT- (heading.height+heading_contact.height+bottom_ribbon.height+BOTTOM_MARGIN)
fill_spacer = Spacer(width=PAGE_FRAME_WIDTH, height=fill_height, isGlue=True)

Elements.append(heading)
Elements.append(heading_contact)

Elements.append(fill_spacer)
Elements.append(bottom_ribbon) # the line
# ===========================================================================




# Elements += ribbon(color=color_light)

# ===========================================================================



