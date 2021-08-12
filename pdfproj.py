#Project: Combining selected pages from Many PDFs

import os
from os.path import exists
import PyPDF2
import sys

print("Welcome to PDF combiner")
print("="*20,"\n")

def verifier(msg, numpages, startpage=None):
 'Verifier function will validate the page number input given by user'
 while True:
  try:
   page = int(input(msg))
   if startpage == None:
    if page not in range(1, numpages+1):
     print(f'Exceeding range of total pages. Please select a page number between 1 to {numpages}')
     continue
    else:
     return page
   else:
    if page not in range(1, numpages+1) or page < startpage:
     print(f'to_page cannot be less than from_page. Please provide a page number between {startpage} & {numpages}')
     continue
    else:
     return page
  except:
   print('Please provide an integer for page number (e.g. 1,2,...)') 


def main():
 count = 0
 while True:
  directory = []
  pdfWriter = PyPDF2.PdfFileWriter()
  
  try:
  
   path = input('Enter folder path to fetch pdf Files: ')
   os.chdir(path)
   print(os.getcwd(),'\n')
   
   print('PDF files in this directory are: ')
   for files in os.listdir(path):
    if files.endswith('.pdf'):
     directory.append(files)  
     
  except:
   print('No path found. Try again') 
   count += 1
   if count == 3:
    print('Exceeded Number of tries. Exiting program')
    sys.exit()
   continue
  
  if len(directory) == 0:
   print('No pdf file/s to fetch')
   continue
  else:
   bullet = 0
   for file in directory:
    bullet += 1
    print(bullet, end='.')
    print (file)
   print('='*20,'\n')
  
  count = 0
  while True:
   
   try:
    pdffile = input('Choose a file from the given list to proceed: ')
    pdffile = (pdffile if pdffile.endswith('.pdf') else pdffile+'.pdf')
    pdfReader = PyPDF2.PdfFileReader(open(pdffile,'rb'))
    TotalPages = pdfReader.numPages
    print("Number of pages :", TotalPages)
    startpage = verifier('From Page :', TotalPages)
    endpage = verifier('To Page :', TotalPages, startpage)
    for page in range(startpage-1, endpage):
     pageObj = pdfReader.getPage(page)
     pdfWriter.addPage(pageObj)
   except:
    print('File not found. Please give correct input. Select file from the list provided')
    count += 1
    if count == 3:
     print('Exceeded Number of tries. Exiting program')
     sys.exit()
    continue
          
   file = input("Enter X to cut or merge | Press any key to choose more file to merge " )
   if file=="X":
    print("Processing your request..")
    break
   else:
    continue
      
  while True:
   Outputfile = input('Save as? ')
   outputfile = (Outputfile if Outputfile.endswith('.pdf') else Outputfile+'.pdf')
   if exists('F:\\py_codes\\pdf_project\\'+outputfile):
    print('A file with same name already exists.')
    continue
   else:
    break
  pdfWriter.write(open(outputfile,'wb'))
  print("Merging completed.Output Folder -> F:\py_codes\pdf_project",'\n')
  cont = input('Enter 0 to exit program | Press any key to continue the program ')
  if cont == '0':
   print('===========Exiting program. Thank you==============')
   break
  else:
   continue 

main()