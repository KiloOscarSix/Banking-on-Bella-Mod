init python:
    galleryCharacter = "All"
    galleryPageNumber = 1

    sceneGalleryMenuDict = {
    "galleryMenu": [
    ["All", "/images/35.jpg"],
    ],
    "All": {
    1: [
    ["d2_shower_mast", {}, "/images/d2/bob-d2-9.jpg"],
    ["d3_shower_mast", {}, "/images/d2/bob-d2-33.jpg"],
    ["next", {}, "/images/31a.jpg"],
    ["d2_tpeek1", {"x_charm_points":99, "x_dark_points":99}, "/images/d2/bob-d2-248.jpg"],
    ["galleryScene1", {}, "/images/d2/bob-d2-308.jpg"],
    ["galleryScene2", {}, "/images/d4/bob-d4-g79.jpg"],
    ["d4_gena_dark_soul", {}, "/images/d4/bob-d4-g146.jpg"],
    ["d5_morning_shower", {"TatiSofiass":True, "d4_gg_dark_sex":True}, "/images/D5/bob-d5-8.jpg"],
    ],
    2: [
    ["d5_stacy_cab_hj", {}, "/images/D5/bob-d5-496.jpg"],
    ["d5_hotel_threesome", {}, "/images/D5/bob-d5-674.jpg"],
    ],
    },
    }

label galleryNameChange:
    default persistent.pc = ""
    default persistent.pc1 = ""
    default persistent.lana_n = ""
    default persistent.anita_n = ""
    default persistent.harry_n = ""
    if persistent.pc == "":
        $ persistent.pc = renpy.input("What's your first name?", default="Peter")
    if persistent.pcl == "":
        $ persistent.pcl = renpy.input("Your last name is?", default="Dick")
    if persistent.lana_n == "":
        show bob-lana-sprite-1
        $ persistent.lana_n = renpy.input("This sweet, innocent, beautiful, young girl's name is?", default="Lana")
        hide bob-lana-sprite-1
    if persistent.anita_n == "":
        show bob-anita-sprite-1 with dissolve
        $ persistent.anita_n = renpy.input("This lovely, church-going, god-fearing, lady's name is?")
        if not persistent.patch_enabled:
            $ persistent.anita_name2 = persistent.anita_n
        hide bob-anita-sprite-1 with dissolve
    if persistent.harry_n == "":
        show bob-harry-sprite-1 with dissolve
        $ persistent.harry_n = renpy.input("This stern, judgmental, bible-thumping, religious gentleman's name is?", default="Harry")
        if not persistent.patch_enabled:
            $ persistent.harry_name2 = persistent.harry_n
        hide bob-harry-sprite-1 with dissolve
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/oscarAdditions/images/button.png"
                hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in sceneGalleryMenuDict["galleryMenu"]:
            vbox:
                imagebutton:
                    action ShowMenu("sceneCharacterMenu"), Hide("sceneGalleryMenu"), SetVariable("galleryCharacter", i[0])
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu():
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Hide("sceneCharacterMenu"), ShowMenu("main_menu")
                else:
                    action SetVariable("galleryPageNumber", galleryPageNumber - 1)
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action SetVariable("galleryPageNumber", galleryPageNumber + 1)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"pc":persistent.pc, "pc1":persistent.pc1, "lana_n":persistent.lana_n, "anita_n":persistent.anita_n, "harry_n":persistent.harry_n, "anita_name2":persistent.anita_name2, "harry_name2":persistent.harry_name2}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)
