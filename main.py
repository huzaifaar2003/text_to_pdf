import pandas as pd
import fpdf
import glob
import pathlib
import os

filepaths = glob.glob("text_and_files/*.txt")
filenames_list = []
file_contents = []
for filepath in filepaths:
    filenames_list.append(pathlib.Path(filepath).stem)
    with open(filepath, "r") as file:
        file_contents.append(file.read())


print(filenames_list)
print(file_contents)



#for filename in filenames_list:
#    pdf.add_page()
#    pdf.set_font(family="Times", style= "b", size = 20)
#    pdf.cell(w=0, h=20, txt=str(filename).title(), align="L", ln=1)
#    #pdf.cell(w=0, h=60, txt = str())


if os.path.isdir("PDFs") == False:
    os.mkdir("PDFs")

# to create individual PDFs, the pdf initialization and final output have to placed
# in the for loop

pdf = fpdf.FPDF(orientation="P", unit="mm", format="A4")

for i in range(0,4):

    pdf.add_page()
    # header
    pdf.set_font(family="Times", style="b", size=20)
    print(filenames_list[i].title())
    pdf.cell(w=0, h=10, txt=filenames_list[i].title(), align="L", ln=1)

    # content
    pdf.set_font(family="Times", size=12)
    print(file_contents[i])
    pdf.multi_cell(w=0, h=6, txt=file_contents[i], align="L")

pdf.output(f"PDFs/complete.pdf")