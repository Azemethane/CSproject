"""
Nick Faber
11/29/2019
The functions in this file return strings in the form of html code
"""

def make_para(text):
    """
    This function returns the code necessary for a paragraph in html
    :param text: The text in the paragraph
    :return:
    """
    return "<p>"+ text+ "</p>\n"

def make_title(text):
    """
    This function returns the code necessary for the main heading of the site
    :param text: The text in the main heading
    :return:
    """
    return "<h1>"+text+"</h1>\n"

def make_head(text):
    """
    This function returns the code necessary for a paragraph heading
    :param text: The text in the heading
    :return:
    """
    return "<h2>"+text+"</h2>\n"

def make_img(txt):
    """
    This function returns the code necessary for an image
    :param txt: The file name of the image
    :return:
    """
    split_txt=txt.split(" ")
    #An if statement is used here to check if there is a resize request and if so it adds the width command
    if len(split_txt)>2:
        return "<img src=\""+split_txt[1]+"\" width=\""+split_txt[2]+"\" class=\"center\">\n"
    else:
        return "<img src=\""+txt+"\" class=\"center\">\n"

def make_style(Back_color,Head_col,Font_style,Font_color):
    """
    This function goes line by line of the style template provided, replacing variables when needed and adding each line
    to a string before finally returning that string
    :param Back_color: The background color of the site
    :param Head_col: The text color of a heading
    :param Font_style: The font style of the whole site
    :param Font_color: The text color for paragraphs
    :return:str: A fixed and completed style template
    """
    str=""
    file=open("style_template.txt")
    for line in file:
        if "@BACKCOLOR" in line:
            str+=(line.replace("@BACKCOLOR", Back_color))
        elif "@HEADCOLOR" in line:
            str+=(line.replace("@HEADCOLOR", Head_col))
        elif "@FONTSTYLE" in line:
            str+=(line.replace("@FONTSTYLE", Font_style))
        elif "@FONTCOLOR" in line:
            str+=(line.replace("@FONTCOLOR", Font_color))
        else:
            str+=line
    return str