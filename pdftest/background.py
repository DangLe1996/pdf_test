from fpdf import FPDF
from PyPDF2 import PdfFileWriter,PdfFileReader
from miner import find_text, get_file_name


from Class_PDF import PDF


#input_file = "mo-1120-sign.pdf"
#input_file = "f1120.pdf"

input_file_list = ["f1120_sign.pdf","mo-1120-sign.pdf"]

signature = '2.png'
location_file = 'locations_data'
data = PDF.import_location(location_file)

def extract_data(input_file_list):
    for input_file in input_file_list:
        name,signature_coor,date_coor = find_text(input_file)
        WIP_file = PDF(name,signature_coor,date_coor)
        data[name] = WIP_file
    
    PDF.export_location(data,location_file)

def sign_document(input_file_path,signature_path):
    output_file_path = "signed" + input_file_path 
    name = get_file_name(input_file_path)
    data[name].create_signature(signature_path)
    data[name].sign_document(input_file_path,output_file_path)

for i in input_file_list:
    sign_document(i,signature)


    ##name = get_file_name(input_file)
    #output_file = PdfFileWriter()
    #input_file = PdfFileReader(open(input_file, "rb"))


    #pdf=FPDF('P','pt',(612 ,792))
    #pdf.add_page()
    #pdf.set_font('Times','',10.0)
    #if len(date_coor.__dict__) > 0:
    #    pdf.set_xy(date_coor.x,792-date_coor.y)
    #    pdf.cell(2.5,0.0,'08/14/2019')

    #pdf.image(signature,signature_coor.x,792-signature_coor.y,90)
    #pdf.output(watermark_file, 'F')


    ## Number of pages in input document
    #page_count = input_file.getNumPages()

    ## Go through all the input file pages to add a watermark to them
    #for page_number in range(page_count):
    #    # merge the watermark with the page
    #    input_page = input_file.getPage(page_number)
    #    if page_number ==   signature_coor.page:
    #        input_page.mergePage(watermark.getPage(0))
    #    # add page from input file to output document
    #    output_file.addPage(input_page)

    ## finally, write "output" to document-output.pdf
    #with open(output_file_path, "wb") as outputStream:
    #    output_file.write(outputStream)