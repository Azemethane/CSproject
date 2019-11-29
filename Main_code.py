import sys
import questions
import create_txt
import create_html
from dataclasses import dataclass
PARAS=[]
SITES={}
@dataclass
class paragraph:
    heading:str
    txt:str
    img:list
def wizard_mode():
    cont="yes"
    while cont=="" or cont=="yes":
        heading=input("Title of your paragraph: ")
        txt=input("Content of your paragraph (single line)")
        img_chk=input("Do you want to add an image?")
        new_para=paragraph(heading,txt,[])
        while img_chk=="" or img_chk=="yes":
            new_img=input("Image file name:")
            new_para.img.append(new_img)
            img_chk=input("Do you want to add another image?")
        PARAS.append(new_para)
        cont=input("Do you want to add another paragraph to your website?")

def site_mode():
    current_paras=[]
    for site in sys.argv[1:]:
        site_paras=sep_paras(site)
        name=site_paras[0][0]
        for txt in site_paras[1:]:
            new_para=paragraph("","",[])
            for string in txt[1:]:
                if string=="":
                    pass
                if "!title" in string:
                    new_para.heading = string.replace("!title","")
                elif "!image" in string:
                    new_para.img.append(string.replace("!image", ""))
                else:
                    new_para.txt+= string.replace("\n", "")
            current_paras.append(new_para)
        temp=[]
        temp.append(site.replace(".txt",""))
        temp.append(current_paras)
        SITES[name]=temp
        current_paras=[]

def sep_paras(file_name):
    fixed_paras = []
    with open(file_name, errors='ignore') as text:
        paras = text.read().split("!new_paragraph")
    for text in paras:
        fixed_paras.append(text.split("\n"))
    return fixed_paras

def main():
    if len(sys.argv)>1:
        back_color = questions.bck_color()
        font = questions.fnt_choice()
        para_color = questions.para_style()
        head_color = questions.head_style()
        style_temp = create_txt.make_style(back_color, head_color, font, para_color)
        site_mode()
        for x in SITES:
            create_html.write_html(x,style_temp,SITES[x][1],SITES[x][0],SITES)
    else:
        title_name = questions.title()
        back_color = questions.bck_color()
        font = questions.fnt_choice()
        para_color = questions.para_style()
        head_color = questions.head_style()
        style_temp = create_txt.make_style(back_color, head_color, font, para_color)
        wizard_mode()
        create_html.write_html(title_name, style_temp, PARAS,"index")

main()