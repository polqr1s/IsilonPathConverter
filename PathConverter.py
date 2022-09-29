import sys


def convert():
    storageServer = input("Enter the storage server this data belongs to:")
    print("Paste in the paths. The paths should have the server name first. ex; \\\\storage\\main\\subfolder")
    print("Press ctrl+d when all paths have been entered.")
    paths = sys.stdin.read()
    if storageServer not in paths:
        print("Warning: " + storageServer + " was not found in one or more paths. Check the paths and try again")
        convert()
    flipSlashes = paths.replace("\\", "/")
    addIfs = flipSlashes.replace(storageServer, "ifs")
    removeDoubleSlashes = addIfs.replace("//", "/")
    addDotArchive = removeDoubleSlashes.replace(".archive", "/.archive")
    #Now I check to make sure ifs starts with a forward slash
    if addDotArchive.startswith("ifs"):
        final = addDotArchive.replace("ifs", "/ifs")
    else:
        final = addDotArchive
    print("\n \n" + final)
    print("Delete this data on " + storageServer)
    convert()

convert()
