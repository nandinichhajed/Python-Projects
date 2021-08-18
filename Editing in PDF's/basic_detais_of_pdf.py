import PyPDF2
with open(r"File Path", 'rb') as file:
    # r = read file
    # b = binary
    print(file)

    reader = PyPDF2.PdfFileReader(file)  # it allows us to read the python file
    print(reader.numPages)

    page = reader.getPage(0)  # get the perticular page

    page.rotateCounterClockwise(90) # rotate the page

    writer = PyPDF2.PdfFileWriter() # writer.addPage(Page)
    
    with open(r'File path', 'wb') as new_file:
        writer.write(new_file)
