import PyPDF2

pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf']

merger = PyPDF2.PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
