init python:
    try:
        import requests
        import hashlib
        import logging
    else:
        def isUpToDate(fileName, url):
            f = open(fileName, "r")
            file = f.read()
            f.close()
            hash = hashlib.sha256((file).encode('utf-8')).hexdigest()

            urlcode = requests.get(url).text
            urlhash = hashlib.sha256((urlcode).encode('utf-8')).hexdigest()

            if hash == urlhash:
                return True
            else:
                return False

        if renpy.variant("mobile"):
            modConfigPath = None
        else:
            modConfigPath = os.path.join(os.getcwd(), "game", "oscarAdditions", "modConfig.txt")

        def updateChecker():
            if renpy.variant("mobile"):
                return False
            if not isUpToDate(modConfigPath, "https://raw.githubusercontent.com/KiloOscarSix/Banking-on-Bella-OscarSix-s-Mod/master/game/oscarAdditions/modConfig.txt"):
                return True
