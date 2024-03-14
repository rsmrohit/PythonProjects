from fpdf import FPDF
import webbrowser
import os


class PdfReport:
    """
    Creates a pdf report containing data about the flatmates' names, period of bill, and pay
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, bill, *flatmates):

        borders = False

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=40)

        # Add some text
        pdf.set_font(family="Arial", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill",
                 border=borders, align="C", ln=1)

        # Add the period
        pdf.cell(w=100, h=40, txt="Period", border=borders)
        pdf.cell(w=150, h=40, txt=bill.period, border=borders, ln=1)

        # Add flatmates
        pdf.set_font(family="Arial", size=12)
        for mate in flatmates:
            pdf.cell(w=100, h=30, txt=mate.name)
            pdf.cell(w=150, h=30, txt=str(mate.pays(bill, flatmates)), ln=1)

        os.chdir("files")

        pdf.output(self.filename)
        webbrowser.open('file://' + os.path.realpath(self.filename))

        pass
