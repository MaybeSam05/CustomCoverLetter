from pdfminer.high_level import extract_text
from fpdf import FPDF
import re

def main():
    positionName = ""
    companyName = ""
    companyValue = ""
    companyAddress = ""
    industry = "Technology"
    hiringManager = "Hiring Manager"
    name = "Samarth Verma"
    email = "samarthverma1108@gmail.com"
    number = "(732)-500-7690"

    templatePath = "/Users/samarthVerma/Documents/Cover Letter/CL_TEMPLATE_3.pdf"
    outputPath = f"/Users/samarthVerma/Documents/Cover Letter/Companies/{companyName}_CoverLetter.pdf"

    my_vars = {
        "[Position Name]": positionName,
        "[Company Name]": companyName,
        "[Specific Company Value]": companyValue,
        "[Company Address]": "\n" + companyAddress,
        "[Industry/Field]": industry,
        "[Hiring Manager]": "" + hiringManager + "\n",
        "[myName]" : "\n" + name,
        "[myEmail]" : "\n" + email,
        "[myNumber]" : "\n" + number,
    }

    text = extract_text(templatePath, page_numbers=[0])

    for placeholder, value in my_vars.items():
        text = text.replace(placeholder, value)

    # Clean up the text: remove unnecessary newlines within paragraphs but preserve paragraph breaks
    text = re.sub(r'\n{2,}', '\n\n', text)  # Keep double newlines as paragraph breaks
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)  # Replace single newlines with spaces

    # Add a newline before each dash followed by a space
    text = re.sub(r'(?<!\n)- ', '\n- ', text)

    pdf = FPDF('P', 'pt', 'Letter')
    pdf.add_page()
    pdf.set_margins(72, 72, 72)  
    pdf.ln(30)
    pdf.set_font("Arial", size=10)

    paragraphs = text.split('\n\n')
    for paragraph in paragraphs:
        pdf.multi_cell(0, 12, txt=paragraph)
        pdf.ln(10)  

    pdf.output(outputPath)

    print("Done")


if __name__ == "__main__":
    main()
