screen cheatMenu():
    tag cheatMenu
    modal True
    add "#23272a"

    text "Oscar's Cheat Menu":
        style "galleryHeader"
        xcenter 960
        ycenter 167

    imagebutton:
        action [Hide("cheatMenu"), SetVariable("quick_menu", True)]
        idle "/oscarAdditions/images/button.png"
        hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
        pos(1684, 51)

    text "Back":
        style "galleryBody"
        xcenter 1778
        ycenter 88

    hbox:
        pos (200, 300)
        spacing 100

        vbox:
            spacing 20

            text "Charm Points:":
                style "galleryBody"

            bar value VariableValue("x_charm_points",50,offset=-25):
                xmaximum 350
                ymaximum 5
                # left_bar Frame("gui/bar/left.png", 10, 0)
                # right_bar Frame("gui/bar/right.png", 10, 0)

        vbox:
            spacing 20

            text "Dark Points:":
                style "galleryBody"

            bar value VariableValue("x_dark_points",50,offset=-25):
                xmaximum 350
                ymaximum 5

    # Bar Values
    text "{=bar_text} [x_charm_points]" xcenter 370 ycenter 398 # Charm Points
    text "{=bar_text} [x_charm_points]" xcenter 820 ycenter 398 # Charm Points
