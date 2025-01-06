from reportlab.pdfgen import canvas
from pdfminer.high_level import extract_text
from fpdf import FPDF

def main():
    positionName = "Testing Intern"
    companyName = "Nvidia"
    companyValue = "To serve and protect"
    companyAddress = "7 Anna Lane"
    industry = "technology"

    templatePath = "/Users/samarthVerma/Documents/Cover Letter/CL_TEMPLATE_3.pdf"
    outputPath = f"/Users/samarthVerma/Documents/Cover Letter/{companyName}.pdf"

    # Variables to replace in the template
    my_vars = {
        "[Position Name]": positionName,
        "[Company Name]": companyName,
        "[Specific Company Value]": companyValue,
        "[Company Address]": companyAddress,
        "[Industry/Field]": industry,
    }

    # Extract text from the template PDF
    text = extract_text(templatePath, page_numbers=[0])
   
    # Replace placeholders with actual values
    for placeholder, value in my_vars.items():
        text = text.replace(placeholder, value)

    
    print(text)

    # Create a new PDF with FPDF
    pdf = FPDF('P', 'pt', 'Letter')
    pdf.add_page()
    pdf.set_margins(72, 72, 72)  # 1-inch margins
    pdf.set_font("Arial", size=10)

    # Split the text by newlines and write each line separately
    lines = text.split('\n')
    for line in lines:
        pdf.multi_cell(0, 12, txt=line)

    # Save the generated PDF
    pdf.output(outputPath)

    print("Done")


if __name__ == "__main__":
    main()
