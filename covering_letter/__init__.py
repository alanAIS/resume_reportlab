import time
import os
 
 

 
ParagraphStyle(name='Justify', alignment=TA_JUSTIFY)
 
 
def add_image(img):
    im = Image(img, 2*inch, 2*inch)
    page.append(im)
 
 
def add_space():
    page.append(Spacer(1, 12))
 
 
def add_text(text, space=0):
    if type(text)==list:
        for f in text:
            add_text(f)
    else:
        ptext = f'<font size="12">{text}</font>'
        page.append(Paragraph(ptext, styles["Normal"]))
        if space==1:
            add_space()
        add_space()
 
 
# =============================== The content =======================

 
os.startfile("form_letter.pdf")