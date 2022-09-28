import sys
import tkinter as tk
from tkinter import scrolledtext


def convert():
    storageServer = storageIdentity()
    paths = storagePaths()
    if storageServer not in paths:
        print('Warning: ' + storageServer + ' was not found in one or more paths. Check the paths and try again')
        convert()
    flipSlashes = paths.replace('\\', '/')
    addIfs = flipSlashes.replace(storageServer, 'ifs')
    removeDoubleSlashes = addIfs.replace('//', '/')
    addDotArchive = removeDoubleSlashes.replace('.archive', '/.archive')
    # Now I check to make sure ifs starts with a forward slash
    if addDotArchive.startswith('ifs'):
        final = addDotArchive.replace('ifs', '/ifs')
    else:
        final = addDotArchive
    print('\n \n' + final)
    print('Delete this data on ' + storageServer)
    convert()

def closeWindow(window):
    window.destroy()

def storageIdentity():
    identityWindow = tk.Tk()
    identityWindow.title('Enter Storage Identity')
    identityWindow.geometry('400x200')
    
    storage_name = tk.StringVar()

    storage_label = tk.Label(identityWindow, text = 'Enter the storage server this data belongs to:')
    storage_entry = tk.Entry(identityWindow, text = storage_name)

    storage_label.place(relx=0.5, rely=0.4, anchor='center')
    storage_entry.place(relx=0.5, rely=0.5, anchor='center')
    storage_entry.bind('<Return>', lambda e: closeWindow(identityWindow))
    
    storage_entry.focus()
    identityWindow.mainloop()

    storage = storage_name.get()
    print ('Storage Server:' + storage)
    return storage

def submit(pathWindow, storage_paths):
    global submittedPaths
    submittedPaths = storage_paths.get('1.0', 'end-1c')
    pathWindow.destroy()

# https://stackoverflow.com/questions/60014280/tkinter-how-can-you-use-get-to-save-the-input-in-a-scrolled-text-widget-to-a
def storagePaths():
    pathWindow = tk.Tk()
    pathWindow.title('Enter Storage Paths')
    pathWindow.geometry('800x600')

    storage_label = tk.Label(pathWindow, text = 'Paste in the paths. The paths should have the server name first. ex; \\\\storage\\main\\subfolder')
    storage_paths = scrolledtext.ScrolledText(pathWindow, width=60, height=25)
    submit_button = tk.Button(pathWindow, text='Submit', width=6, command=lambda : submit(pathWindow, storage_paths))

    submit_button.place(relx=0.5, rely=0.9, anchor='center')         
    storage_label.place(relx=0.5, rely=0.1, anchor='center')
    storage_paths.place(relx=0.5, rely=0.5, anchor='center') 

    pathWindow.focus_force()
    storage_paths.focus()
    pathWindow.mainloop()
    
    return submittedPaths


convert()

