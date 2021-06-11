import sys


def deletion():
    storageServer = input("Enter the storage server this data belongs to:")
    print("Enter in paths, line by line. Press ctrl+d when all paths have been entered.")
    paths = sys.stdin.read()
    if storageServer not in paths:
        print("Warning: " + storageServer + " was not found in one or more paths.")
    flipSlashes = paths.replace("\\", "/")
    # print(flipSlashes)
    addIfs = flipSlashes.replace(storageServer, "ifs")
    # print(addIfs)
    removeDoubleSlashes = addIfs.replace("//", "/")
    print(removeDoubleSlashes)
    print("Delete this data on " + storageServer)


deletion()
