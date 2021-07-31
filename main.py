from fpdf import FPDF
from hentai import Hentai
import os
import time
import shutil

def get_image_list(path):
  page_num = 1
  image_list = []
  while len(image_list) < len(os.listdir(path)):
    for file in os.listdir(path):
      if int(file.rsplit('.', 1)[0]) == page_num:
        image_list.append(fr"{path}\{file}")
        page_num += 1
  return image_list

input_id = input("Code ( ͡° ͜ʖ ͡°): ")

# some error handling
if Hentai.exists(int(input_id)) == False:
  print("bruh give me an id that actually exists smh my head")
  exit()

#download it ( ͡° ͜ʖ ͡°)
doujin = Hentai(int(input_id))
doujin.download(progressbar = True)

#wait for doujin to finish downloading
while len(os.listdir(input_id)) < len(doujin.image_urls):
  time.sleep(1)

print("Almost done ;)")

#pdf creation
doujin_pdf = FPDF()
doujin_pdf.set_auto_page_break(0)        #this is stupid...
doujin_pdf.set_margins(0,0,0)            #this one is kinda dumb but not as bad
for image in get_image_list(input_id):  
  doujin_pdf.add_page()
  doujin_pdf.image(image, 0,0,210,297)
doujin_pdf.output(f"{input_id}.pdf", "F")

print("Aaaand done!")

#cleaning up! deletes the folder made to create pdf
shutil.rmtree(input_id)
