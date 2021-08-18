import PyPDF2

template = PyPDF2.PdfFileReader(open(r"File Path", 'rb'))
watermark = PyPDF2.PdfFileReader(open(r"File Path", 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
