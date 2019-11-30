"""
Nicholas Faber
11/29/2019

"""
import sys
import questions
import create_txt
import create_html
from dataclasses import dataclass
#PARAS is used by wizard mode and is a list of paragraphs
PARAS=[]

#SITES is used by website mode and is a dictionary with the keys as site names and the values a list with
#[0] being the name of the sites source file(file.html) and [1] being the list of paragraphs for that site
SITES={}

#This dataclass is used for both wizard and website mode, it is used to represent each paragraph of the sites
@dataclass
class paragraph:
    heading:str
    txt:str
    img:list
    __slots__ = "heading", "txt", "img"
def wizard_mode():
    """
    This function goes through the process of wizard mode, asking and creating the paragraphs for the site
    :return:
    """
    cont=""
    #This while loop continues as long as the user wishes to create more paragraphs
    while cont=="" or cont=="yes":
        heading=input("Title of your paragraph: ")
        txt=input("Content of your paragraph (single line)")
        img_chk=input("Do you want to add an image?")
        new_para=paragraph(heading,txt,[])
        #If the user wishes to add images this loop will start and add the images requested by the user to the image
        #list of the current paragraph
        while img_chk=="" or img_chk=="yes":
            new_img=input("Image file name:")
            new_para.img.append(new_img)
            img_chk=input("Do you want to add another image?")
        #The completed paragraph is added to the list
        PARAS.append(new_para)
        cont=input("Do you want to add another paragraph to your website?")

def site_mode():
    """
    This function goes through the website mode procces by splitting up paragraphs in text files and constructing them
    to properly fit the paragraph dataclass
    :return:
    """
    current_paras=[]
    for site in sys.argv[1:]:
        site_paras=sep_paras(site)
        name=site_paras[0][0]
        #This for loop goes through each paragraph in the returned list
        #And since the first one is always the title we skip it
        for txt in site_paras[1:]:
            new_para=paragraph("","",[])
            #This nested for loop goes through each line (the nested list) of the paragraph
            #And depending on the line it is added to the structure of the current paragraph
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
        #This part is where the dictionary is formed where the title of the file and the list of paragraphs are
        #added to the dictionary with the the name of the site as the key
        temp=[]
        temp.append(site.replace(".txt",""))
        temp.append(current_paras)
        SITES[name]=temp
        current_paras=[]

def sep_paras(file_name):
    """
    This is a helper function for website mode which takes a file and splits it up in paragraphs by using the split
    command on !new_paragraph before splitting it again by line
    :param file_name:
    :return: a list of paragraphs
    """
    fixed_paras = []
    with open(file_name, errors='ignore') as text:
        paras = text.read().split("!new_paragraph")
    #After spliting the paragraphs the next thing this function does is split up each paragraph by line
    #Meaning at each index in fixed_paras there is another list that contains the lines for a paragraph
    for text in paras:
        fixed_paras.append(text.split("\n"))
    return fixed_paras

def main():
    #If the command line contains a txt file run website mode, otherwise start up wizard mode
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
        create_html.write_html(title_name, style_temp, PARAS,"index",[])

main()