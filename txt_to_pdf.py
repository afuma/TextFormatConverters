from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # You can add a header if needed
        pass

    def footer(self):
        # You can add a footer if needed
        pass

    def chapter_title(self, title):
        # This method formats the title of each chapter
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'C')
        self.ln(10)

    def chapter_body(self, body):
        # This method formats the body of each chapter
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create instance of FPDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Read text file
with open("reik.txt", "r") as f:
    # Add chapter title
    pdf.chapter_title('Reik Text Content')

    # Add chapter body
    text = f.read()
    pdf.chapter_body(text)

# Output the PDF
pdf.output("reik.pdf")
