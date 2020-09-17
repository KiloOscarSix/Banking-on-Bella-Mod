init python:
    cheatMenuDict = {
    "[player_name]": [
    ["Corruption", "Corruption", 25],
    ["Focus", "Focus", 10],
    ["Prowess", "Prowess", 10],
    ["Energy", "Energy", 25],
    ["Blue Ball", "BlueBall", 3],
    ],
    "Mary": [
    ["Lust", "MomLust", 60],
    ["Trust", "MomTrust", 60],
    ],
    "Nathalie": [
    ["Lust", "NatLust", 60],
    ["Trust", "NatTrust", 60],
    ],
    "Jocelyn": [
    ["Lust", "JoLust", 60],
    ["Trust", "JoTrust", 60],
    ],
    }

screen cheatMenu():
    modal True
    zorder 200

    python:
        cheatMenuList = ["[player_name]", "Mary", "Nathalie", "Jocelyn"]

    default shownCheatMenu = None

    # add "/oscarAdditions/images/OscarCheatMenuMockup.png"
    add "/oscarAdditions/images/cheatMenuBackground.png"
    fixed:
        xysize (2505, 133)
        pos (23, 16)

        hbox:
            xcenter 0.5
            ycenter 0.5
            spacing 100
            for i in cheatMenuList:
                textbutton i:
                    action [Function(renpy.retain_after_load), SetScreenVariable("shownCheatMenu", value=i)]
                    text_style "modTextButtonHeader"

    for i in cheatMenuList:
        if shownCheatMenu == i:
            use cheatMenuValues(cheatMenuChar=i)

    imagebutton:
        action Hide("cheatMenu"), Hide("cheatMenuValues")
        idle "/oscarAdditions/images/cheatMenuBackButton.png"
        hover im.MatrixColor("/oscarAdditions/images/cheatMenuBackButton.png", im.matrix.brightness(0.2))
        pos (2222, 67)

screen cheatMenuValues(cheatMenuChar):
    tag cheatmenu
    zorder 199

    vpgrid:
        cols 4
        pos (140, 256)
        spacing 50
        for x in cheatMenuDict[cheatMenuChar]:

            vbox:
                spacing 20
                text "[x[0]] Points:" style "modTextBody2"
                fixed:
                    xysize (468, 55)

                    bar value VariableValue(x[1], x[2]):
                        left_bar Frame("gui/bar/left.png", 10, 0)
                        right_bar Frame("gui/bar/right.png", 10, 0)
                    text "{:}".format(getattr(store, x[1])) xcenter 0.5 ycenter 0.5
