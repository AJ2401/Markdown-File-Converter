# Pdf content extraction
# Md to Pdf Converter
# Md to Html Converter
# Details of the Text.
# Pdf to Html and Pdf to md file.
import markdown_it
import pdfkit 
import html2text
import re
import os
from pdfminer.high_level import extract_text
from os import path
from dotenv import load_dotenv

load_dotenv()
folderAddress = str(os.getenv('FOLDER'))
filename = str(os.getenv('FILE'))
 
def mdToHtml(mdFile):
   md = markdown_it.MarkdownIt()
   html_content = md.render(mdFile.read())
   cssFile = open("/Users/abhishekjhawar/Desktop/Project/Winter_Vacation/Md_File_Converter/Styles.css", 'r') 
   cssContent = cssFile.read()
   Html_content= f"<html><head><style>{cssContent}</style></head><body>{html_content}</body></html>"
   Htmlfile = open(folderAddress + "/" + filename + ".html", "w+")
   Htmlfile.write(Html_content)
   Htmlfile.close()

def mdToPdf():
   if path.exists(folderAddress + "/" + filename + ".html") == False:
      address = folderAddress + "/" + filename + ".md"
      mdFile = open(address, "r")
      mdToHtml(mdFile)
   else:
      pass
   config = pdfkit.configuration(wkhtmltopdf ="/usr/local/bin/wkhtmltopdf")
   options = {
      'enable-local-file-access': True,
      'encoding': 'UTF-8'
    }
   try:
      pdfkit.from_file(
         folderAddress + "/" + filename + ".html",
         folderAddress + "/" + filename + ".pdf",
         configuration = config,
         options = options
      )
   except Exception as e:
      print("Error Encountered : ", str(e))

def pdfToMd():
   text = extract_text(folderAddress + "/" + filename + ".pdf")
   text = pdfTo_markdown_format(text)
   if  path.exists(folderAddress + "/" + filename + ".md") == True:
      mdFile = open(folderAddress + "/" + filename + "_New.md", "w+")
   else:
      mdFile = open(folderAddress + "/" + filename + ".md", "w+")
   mdFile.write(text)
   mdFile.close()

def pdfTo_markdown_format(text):
   lines = text.split('\n')
   formatted_text = []
   if not lines:
       return ""
   formatted_text.append(f'# {lines[0].strip()}\n')
   for line in lines[1:]:
       line = line.strip()
       if line.endswith(':'):
           formatted_text.append(f'\n## {line[:-1]}\n')
       elif '**' in line:
           formatted_text.append(f'\n**{line.replace("**", "")}**\n')
       elif line.startswith('- ') or line.startswith('* '):
           formatted_text.append(f'- {line[2:]}\n')
       elif re.match(r'^\d+\.', line):
           formatted_text.append(f'{line}\n')
       elif line:
           formatted_text.append(f'\n{line}\n')
   return ''.join(formatted_text)

def deatilsOfFile(Fileaddress):
   file = open(Fileaddress,"r",encoding='utf-8', errors='replace')
   file_Content = file.read()
   rendered_Content = html2text.html2text(file_Content)
   words = len(re.findall(r'\b\w+\b',rendered_Content))
   characters = len(re.findall(r'.',rendered_Content))
   tab_spaces = len(re.findall(r'\b',rendered_Content))
   line_breaks = len(re.findall(r'\n',rendered_Content))
   file.close()
   return [words,characters,tab_spaces,line_breaks]
   
def main():
   n = 1
   while n == 1:
      Option = int(input("\n\nChoose Your Option : \n\n1.) mdToHtml\n2.) mdToPdf\n3.) pdfToMd\n4.) deatilsOfFile\n5.) EXIT\n\n"))
      if Option == 1:
         address = folderAddress + "/" + filename + ".md"
         mdFile = open(address, "r")
         mdToHtml(mdFile)
         
      elif Option == 2:
         mdToPdf()
         Htmladdress = folderAddress + "/" + filename + ".html"
         os.remove(Htmladdress)
      
      elif Option == 3:
         pdfToMd()
         
      elif Option == 4:
         Fileaddress = input("Enter the File Address to Get the Insights of : ")
         while os.path.exists(Fileaddress) == False:
            Fileaddress = input("Enter the File Address to Get the Insights of : ")
         Result = deatilsOfFile(Fileaddress)
         newfilename, _ = os.path.splitext(Fileaddress)
         print(f"\n\n\t--- Insights of {newfilename} File is ---\t\n\n")
         print(f"\n\nNumber of Words in the {newfilename} is : {Result[0]}\n\nNumber of Characters in the {Fileaddress} is : {Result[1]}\n\nNumber of Tab-Spaces in {Fileaddress} is : {Result[2]}\n\nThe Number of Line-Breaks in the {Fileaddress} is : {Result[3]}\n\n")
         
      elif Option == 5:
         n = 0
         return
            
main()

