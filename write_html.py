"""
Nick Faber
11/29/2019
This file creates the final html code with the provided variables
"""
from dataclasses import dataclass
from create_txt import make_para, make_img, make_head, make_title
@dataclass
class paragraph:
    heading:str
    txt:str
    img:list

def write_html(Title,style_temp,paras,site_name,links):
    """
    :param Title: The title of the site that is used to create the main heading
    :param style_temp: This is the string that holds the completed style template
    :param paras: A list of paragraphs that will be coded into the site, each paragraph contains a heading,text(body),
                  and a list of image file names
    :param site_name: This is the site name
    :param links: This is a dictionary in which the keys are the site names, and the values are lists with
                  [0] being the name of the sites source file and [1] being the list of paragraphs for that site
    :return: none
    """
    final_html = open(site_name+".html", "a+")
    final_html.write("<!DOCTYPE html>\n")
    final_html.write("<html>\n")
    final_html.write("<head>\n")
    final_html.write("<title>\n")
    final_html.write(Title+"\n")
    final_html.write("</title>\n")
    final_html.write(style_temp)
    final_html.write("</head>\n")
    final_html.write("<body>\n")
    final_html.write(make_title(Title))
    final_html.write("<hr/>\n")
    #This if statement checks the length of the links dict
    #and if it is greater than zero, it will add links to the other sites(as well as itself)
    if len(links)>0:
        final_html.write("<p align=\"center\">\n")
        #This for loop goes through the dictionary links and writes the name and files accordingly
        for lnk in links:
            final_html.write("<a href=\""+str(links[lnk][0])+".html\">"+lnk+"</a>---")
        final_html.write("</p>\n")
    #This for loop goes through the list of paragraphs and writes them into the html file
    for sect in paras:
        final_html.write(make_head(sect.heading))
        final_html.write(make_para(sect.txt))
        #Since each paragraph has a list of images, this loop goes through that list to write the code for each image
        if len(sect.img)>0:
            for img in sect.img:
                final_html.write(make_img(img))
    final_html.write("</body>\n")
    final_html.write("</html>")