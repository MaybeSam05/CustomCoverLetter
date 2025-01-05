from pypdf import PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def main():
    companyName = ""
    companyAddress = ""
    companyValue = ""
    positionName = ""
    industry = ""

    templatePath = "/Users/samarthVerma/Documents/Cover Letter/CL_TEMPLATE_2.pdf"
    outputPath = f"/Users/samarthVerma/Documents/Cover Letter/{companyName}.pdf"

    my_vars = {
        "[Position Name]" : positionName,
        "[Company Name]" : companyName,
        "[Specific Company Value]" : companyValue,
        "[Company Address]" : companyAddress,
        "[Industry/Field]" : industry,
    }
    
    # Step 1: Extract text from the existing PDF
    reader = PdfReader(templatePath)
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text()

    # Step 2: Replace all placeholders with corresponding values
    for placeholder, value in my_vars.items():
        extracted_text = extracted_text.replace(placeholder, value)

    # Step 3: Create a new PDF with the updated text
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    text_object = can.beginText(50, 750)
    text_object.setFont("Arial", 10)

    # Add the updated text line by line (handling line breaks)
    for line in extracted_text.split("\n"):
        text_object.textLine(line)

    can.drawText(text_object)
    can.save()

    # Step 4: Save the new PDF
    with open(outputPath, "wb") as output_file:
        output_file.write(packet.getvalue())

if __name__ == "__main__":
    main()