Automation Tool to create cover letters for companies I'm applying to quickly

Libaries Required:
 - pip install pdfminer.six
 - pip install fpdf

 # 📝 Cover Letter Generator

This project automates the generation of personalized cover letters by filling in a customizable PDF template with job-specific information.

## 📌 Features

- Extracts text from a PDF cover letter template
- Replaces placeholder variables with user-defined values
- Cleans and formats the resulting text
- Exports the final version as a new PDF

## 📂 File Structure

```text
.
├── main.py               # Main script to generate cover letters
├── CL_TEMPLATE_3.pdf     # Your cover letter template (edit path in code)
├── /Companies/           # Folder where output PDFs are saved
```

## 🔧 Technologies Used

- **Python 3**
- [pdfminer.six](https://github.com/pdfminer/pdfminer.six) — for extracting text from PDF
- [fpdf](https://py-pdf.github.io/fpdf2/) — for writing the final PDF
- `re` — for text formatting and cleanup

## 🛠️ How It Works

1. Define the job-specific variables in the `main()` function.
2. Extract the template text from `CL_TEMPLATE_3.pdf`.
3. Replace placeholders (e.g., `[Company Name]`, `[Position Name]`, etc.) with the actual values.
4. Clean the text formatting and structure.
5. Generate a new PDF and save it to a `Companies` directory with a company-specific filename.

## ✍️ Placeholders Supported

These must exist in your PDF template:
- `[Position Name]`
- `[Company Name]`
- `[Specific Company Value]`
- `[Company Address]`
- `[Industry/Field]`
- `[Hiring Manager]`
- `[myName]`
- `[myEmail]`
- `[myNumber]`

## 🚀 How to Run

1. Install dependencies:
    ```bash
    pip install pdfminer.six
    pip install fpdf
    ```

2. Adjust the variables and file paths in `main.py`:
    - Make sure `templatePath` points to your PDF template.
    - Make sure `outputPath` points to a valid save location.

3. Run the script:
    ```bash
    python main.py
    ```

4. The output PDF will be saved in the `Companies/` folder with a filename like `Google ._CoverLetter.pdf`.

## 📌 Example Use Case

This tool is great for students or professionals who are applying to multiple companies and want to speed up the process of customizing cover letters.
