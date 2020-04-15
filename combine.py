
import PyPDF2
import sys
import glob


# it combines the pdfs in list
# create it combines all that is in a folder
inputs = []


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')


for filename in glob.glob(f'combine_me/*.pdf'):  # assuming pdf
    inputs.append(filename)
# print(inputs)
pdf_combiner(inputs)
