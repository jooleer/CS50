from fpdf import FPDF


class PDF(FPDF):
    # declare PDF header content
    def header(self):
        self.set_font("helvetica", "B", 50)
        self.cell(80)
        self.cell(30, 50, "CS50 Shirtificate", border=0, align="C")
        self.ln(5)


def main():
    # ask user for name
    name = input("Name: ")

    # create new object from PDF class
    pdf = PDF()

    # add new page to document
    pdf.add_page()

    # import shirt image, resize and center it
    pdf.image("shirtificate.png", 10, 70, 210-20, 297-100)

    # set shirt text parameters
    pdf.set_font("Times", "B", size=25)
    pdf.set_text_color(255, 255, 255)

    # output text centered on the tshirt
    pdf.cell(50)
    pdf.cell(95, 250, f"{name} took CS50", align="C")

    # export document to shirtificate.pdf
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
