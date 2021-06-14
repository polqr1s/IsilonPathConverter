import sys


def deletion():
    storageServer = input("Enter the storage server this data belongs to:")
    print("Enter in paths, line by line. The paths should have the server name first. ex; \\\\storage\\main\\subfolder")
    print("Press ctrl+d when all paths have been entered.")
    paths = sys.stdin.read()
    if storageServer not in paths:
        print("Warning: " + storageServer + " was not found in one or more paths.")
    flipSlashes = paths.replace("\\", "/")
    # print(flipSlashes)
    addIfs = flipSlashes.replace(storageServer, "ifs")
    # print(addIfs)
    removeDoubleSlashes = addIfs.replace("//", "/")
    print("\n \n" + removeDoubleSlashes)
    print("Delete this data on " + storageServer)


deletion()
