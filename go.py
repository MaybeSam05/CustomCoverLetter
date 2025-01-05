from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import pypdf
from pdfminer.high_level import extract_text
import textwrap
import pdfplumber

def main():
    positionName = "Testing Intern"
    companyName = "Nvidia"
    companyValue = "To serve and protect"
    companyAddress = "7 Anna Lane"
    industry = "technology"

    templatePath = "/Users/samarthVerma/Documents/Cover Letter/CL_TEMPLATE_3.pdf"
    #templatePath = "/Users/samarthVerma/Documents/Cover Letter/SamVermaCoverLetter01.pdf"
    
    outputPath = f"/Users/samarthVerma/Documents/Cover Letter/{companyName}.pdf"

    my_vars = {
        "[Position Name]": positionName,
        "[Company Name]": companyName,
        "[Specific Company Value]": companyValue,
        "[Company Address]": companyAddress,
        "[Industry/Field]": industry,
    }

    text = extract_text(templatePath, page_numbers=[0])

    for placeholder, value in my_vars.items():
        text = text.replace(placeholder, value)

    print(text)



if __name__ == "__main__":
    main()
