from pathlib import Path
from datetime import date
import random

from fpdf import FPDF
from faker import Faker
from autoscab.constants.resume import degrees, unis

faker = Faker()

def make_resume(name:str, email:str, suffix:str = 'resume', prefix:str='', uni=None, degree=None) -> Path:
    year = date.today().year
    if uni is None:
        uni = random.choice(unis)
    if degree is None:
        degree = random.choice(degrees)

    font_face = random.choice(['Helvetica', 'Times'])

    pdf = FPDF()
    pdf.add_page()

    # Header
    header_alignment = random.choice(['L','C','R'])
    header_bigfont = random.choice([24,28,32])
    ## Name
    pdf.set_font(font_face, random.choice(['','B']), header_bigfont)
    pdf.cell(w=0, txt=name, align=header_alignment)
    pdf.ln(int(header_bigfont*0.3))
    ## Email 
    pdf.set_font(font_face, random.choice(['','I']), int(header_bigfont*0.5))
    pdf.cell(w=0, txt=email, align=header_alignment)
    pdf.ln(20)

    # Body
    section_style = random.choice(['B','U'])
    grad_year = random.randrange(1990,year-10)

    ## Education
    pdf.set_font(font_face, section_style, int(header_bigfont*0.65))
    pdf.cell(w=0, txt='Education', align='L')
    pdf.ln(int(header_bigfont*0.25))

    pdf.set_font(font_face, '', int(header_bigfont*0.55))
    pdf.cell(w=0, txt=uni, align='L')
    pdf.cell(w=0, txt=str(grad_year-4)+' - '+str(grad_year), align='R')
    pdf.ln(int(header_bigfont*0.25))

    pdf.set_font(font_face, 'I', int(header_bigfont*0.55))
    pdf.cell(w=0, txt=degree, align='L')
    pdf.ln(int(header_bigfont*0.5))

    ## Experience
    midyear = int(grad_year + (year-grad_year)*0.1*random.randrange(3,7))

    pdf.set_font(font_face, section_style, int(header_bigfont*0.65))
    pdf.cell(w=0, txt='Experience', align='L')
    pdf.ln(int(header_bigfont*0.25))

    for i in range(0,2):
        pdf.set_font(font_face, '', int(header_bigfont*0.55))
        pdf.cell(w=0, txt=faker.company(), align='L')
        pdf.cell(w=0, txt=str(grad_year if i else midyear)+' - '+str(midyear if i else year), align='R')
        pdf.ln(int(header_bigfont*0.25))

        pdf.set_font(font_face, 'I', int(header_bigfont*0.55))
        pdf.cell(w=0, txt=faker.job(), align='L')
        pdf.ln(int(header_bigfont*0.2))

        for _ in range(0, random.randint(3,7)):
            pdf.set_font(font_face, '', int(header_bigfont*0.5))
            pdf.cell(w=0, txt='- '+faker.bs(), align='L')
            pdf.ln(int(header_bigfont*0.2))
        
        pdf.ln(int(header_bigfont*0.2))
    pdf.ln(int(header_bigfont*0.1))
    
    ## Skills
    pdf.set_font(font_face, section_style, int(header_bigfont*0.65))
    pdf.cell(w=0, txt='Skills', align='L')
    pdf.ln(int(header_bigfont*0.25))

    for j in range(0, random.randint(6,11)):
        pdf.set_font(font_face, '', int(header_bigfont*0.55))
        pdf.cell(w=0, txt='- '+faker.bs(), align='L')
        pdf.ln(int(header_bigfont*0.2))

    # Print
    filename = Path(f"{prefix}{name}_{email}_{suffix}.pdf").resolve()
    pdf.output(str(filename), 'F')

    return filename
