
init python:
    galleryCharacter = ""
    galleryPageNumber = 1

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1
        return

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1
        return

    sceneGalleryMenuDict = {
    "galleryMenu": [
    ["All", "/images/35.jpg"],
    ],
    "All": {
    1: [
    ["d2_shower_mast", {"pc":persistent.pc}, "/images/d2/bob-d2-9.jpg"],
    ["d3_shower_mast", {"pc":persistent.pc}, "/images/d2/bob-d2-33.jpg"],
    ["next", {"pc":persistent.pc}, "/images/31a.jpg"],
    ["d2_tpeek1", {"pc":persistent.pc, "x_charm_points":99, "x_dark_points":99}, "/images/d2/bob-d2-248.jpg"],
    ["galleryScene1", {"pc":persistent.pc}, "/images/d2/bob-d2-308.jpg"],
    ["galleryScene2", {"pc":persistent.pc}, "/images/d4/bob-d4-g79.jpg"],
    ["d4_gena_dark_soul", {"pc":persistent.pc}, "/images/d4/bob-d4-g146.jpg"],
    ],
    },
    }

label galleryNameChange:
    default persistent.pc = ""
    default persistent.pc1 = ""
    while persistent.pc == "" or persistent.pcl == "": # or persistent.lana_n == "" or  persistent.anita_n == "" or persistent.harry_n == "":
        $ persistent.pc = renpy.input("Enter your first name: ")
        $ persistent.pcl = renpy.input("Enter your last name: ")
        # show bob-lana-sprite-1
        # $ persistent.lana_n = renpy.input("Enter this young lady's name: ")
        # hide bob-lana-sprite-1
        # show bob-anita-sprite-1 with dissolve
        # $ persistent.anita_n = renpy.input("Enter this god-fearing lady's name: ")
        # hide bob-anita-sprite-1 with dissolve
        # show bob-harry-sprite-1 with dissolve
        # $ persistent.harry_n = renpy.input("Enter this bible-thumping man's name: ")
        # hide bob-harry-sprite-1 with dissolve
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"
    # add "oscarAdditions/images/galleryMenuTemplate.png"
    text "Oscar's Scene Gallery":
        style "galleryHeader"
        xcenter 960
        ycenter 167

    imagebutton:
        action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
        idle "/oscarAdditions/images/button.png"
        hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
        pos(1684, 51)

    text "Back":
        style "galleryBody"
        xcenter 1778
        ycenter 88

    imagebutton:
        action OpenURL("https://www.patreon.com/oscarsix/overview")
        idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
        hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
        pos(1546, 146)

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict["galleryMenu"]:
            vbox:
                imagebutton:
                    action ShowMenu("sceneCharacterMenu"), Hide("sceneGalleryMenu"), SetVariable("galleryCharacter", i[0])
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)

    hbox: # Row 1 Character Names
        ypos 580

        text "Character1" xcenter 310 style "galleryBody"


screen sceneCharacterMenu():
    tag menu
    modal True
    add "#23272a"

    $ galleryCharacter = "All"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "galleryHeader"
        xcenter 960
        ycenter 167

    vbox:
        pos(1684, 51)
        spacing 20

        imagebutton:
            if galleryPageNumber == 1:
                action ShowMenu("main_menu"), Hide("sceneCharacterMenu") # Changed
            else:
                action Function(galleryDecreasePageNumber)
            idle "/oscarAdditions/images/button.png"
            hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))

        if galleryPageNumber < len(sceneGalleryMenuDict[galleryCharacter]):
            imagebutton:
                action Function(galleryIncreasePageNumber)
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))

    text "Back":
        style "galleryBody"
        xcenter 1778
        ycenter 88
    if galleryPageNumber < len(sceneGalleryMenuDict[galleryCharacter]):
        text "Next":
            style "galleryBody"
            xcenter 1775
            ycenter 185

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            imagebutton:
                action Replay(i[0], scope=i[1], locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)
