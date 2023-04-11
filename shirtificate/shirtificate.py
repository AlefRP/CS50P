from fpdf import FPDF, XPos, YPos

class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Printing title:
        self.cell(0, 10, "CS50 shirtificate", border=0, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

name = input("Name: ")

# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)

# Calculate the center position for the image
img_width = 593 / 5  # Scale down image width
img_height = 592 / 5  # Scale down image height
img_x = (pdf.w - img_width) / 2
img_y = (pdf.h - img_height) / 2

# Rendering the shirt image centered
pdf.image("shirtificate.png", x=img_x, y=img_y, w=img_width, h=img_height)

# Setting font and printing the name centered in the middle of the shirt image
pdf.set_font("helvetica", "B", 20)
pdf.set_text_color(255, 255, 255) # Set text color to white
name = name + " took CS50" # Concatenate name and text
name_width = pdf.get_string_width(name) + 6
name_x = (pdf.w - name_width) / 2
name_y = img_y + (img_height / 2) - 10  # Adjust '-10' to position the name vertically within the image
pdf.text(x=name_x, y=name_y, txt=name)

pdf.output("shirtificate.pdf")