init python:
    cheatMenuDict = {
    "General": [
    ["Charm Points", "x_charm_points", 20],
    ["Dark Ponts", "x_dark_points", 20],
    ["Money", "dollars", 9999],
    ],
    }

screen cheatMenu():
    modal True
    zorder 200
    add "#23272a"

    python:
        cheatMenuList = ["General"]

    default shownCheatMenu = None

    add "/oscarAdditions/images/cheatMenuBackground.png"
    fixed:
        xysize (1877, 99)
        pos (18, 13)

        hbox:
            xcenter 0.5
            ycenter 0.5
            spacing 100
            for i in cheatMenuList:
                textbutton i:
                    action [Function(renpy.retain_after_load), SetScreenVariable("shownCheatMenu", value=i)]
                    text_style "modTextButtonHeader"

    # for i in cheatMenuList:
    #     if shownCheatMenu == i:
    use cheatMenuValues(cheatMenuChar=i)

    imagebutton:
        action Hide("cheatMenu"), Hide("cheatMenuValues"), SetVariable("quick_menu", True)
        idle "/oscarAdditions/images/cheatMenuBackButton.png"
        hover im.MatrixColor("/oscarAdditions/images/cheatMenuBackButton.png", im.matrix.brightness(0.2))
        pos (1666, 50)

screen cheatMenuValues(cheatMenuChar):
    tag cheatmenu
    zorder 199

    vpgrid:
        cols 4
        pos (100, 200)
        spacing 50
        for x in cheatMenuDict[cheatMenuChar]:

            vbox:
                spacing 20
                text "[x[0]]:" style "modTextBody2"
                fixed:
                    xysize (352, 42)

                    bar value VariableValue(x[1], x[2]):
                        left_bar Frame("gui/bar/left.png", 10, 0)
                        right_bar Frame("gui/bar/right.png", 10, 0)
                    text "{:}".format(getattr(store, x[1])) xcenter 0.5 ycenter 0.5
