"""
Nick Faber
11/29/2019
This file contains the functions that ask the questions to reduce the line count of the main file
It also opens up a turtle window to display fonts if requested by user
"""
import turtle as t
FONTS={0:"Arial", 1:"Comic Sans MS", 2:"Lucida Grande", 3:"Tahoma", 4:"Verdana", 5:"Helvetica", 6:"Times New Roman"}

def title():
    """
    This function asks for the title of the site
    :return:
    """
    title = input("What is the title of your site?")
    return title

def bck_color():
    """
    This function returns the background color of the whole site
    :return:
    """
    print("Background color")
    background = input("Choose the name of a color, or in format '#XXXXXX'")
    return background

def txt_display():
    """
    This function displays the fonts on a turtle window if requested by user
    :return:
    """
    t.pu()
    t.lt(180)
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.pd()
    for style in FONTS.values():
        t.write(str(style), font=(style, 14, "normal"))
        t.pu()
        t.rt(90)
        t.fd(20)
        t.lt(90)
        t.pd()
    t.exitonclick()

def fnt_choice():
    """
    This function asks for the font that the user wishes to be used for the whole site
    :return:
    """
    t.setup(400, 400)
    print("You will now choose a font.")
    fnt_check = input("Do you want to see what the fonts look like(yes or no)?")
    if fnt_check == "" or fnt_check=="yes":
        txt_display()
    final_fnt = input("Choose a font by its number."
                      "\n0: Arial, size 14"
                      "\n1: Comic Sans MS, size 14"
                      "\n2: Lucida Grande, size 14"
                      "\n3: Tahoma, size 14"
                      "\n4: Verdana, size 14"
                      "\n5: Helvetica, size 14"
                      "\n6: Times New Roman, size 14"
                      "\n>>")
    return FONTS[int(final_fnt)]

def para_style():
    """
    This function asks for the text color of all paragraphs
    :return:
    """
    print("Paragraph Text Color")
    para_color = input("Choose the name of a color, or in format '#XXXXXX':")
    return para_color

def head_style():
    """
    This function asks for the text color of all headings
    :return:
    """
    print("Heading Text Color")
    head_color = input("Choose the name of a color, or in format '#XXXXXX':")
    return head_color