from PyPDF2 import PdfFileReader, PdfFileMerger


pdf_file1 = PdfFileReader(r"File Path")
pdf_file2 = PdfFileReader(r"File Path")


output = PdfFileMerger()

output.append(pdf_file1)
output.append(pdf_file2)

output.write('super.pdf')
