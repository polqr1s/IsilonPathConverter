import sys
import tkinter as tk
from tkinter import scrolledtext



def convert():
    storageServer = storageIdentity()
    if len(storageServer) == 0:
        print('No identity was given')
        raise SystemExit(0)
    paths = storagePaths()
    if len(paths) == 0:
        print('No paths were given')
        raise SystemExit(0)
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
    final = convertedPaths(final, storageServer)
    convert()


def next_window(window):
    window.destroy()


def user_close(window):
    print('Window was closed')
    window.destroy()


def storageIdentity():
    window = tk.Tk()
    window.title('Enter Storage Identity')
    window.geometry('400x200')
    window.protocol('WM_DELETE_WINDOW', lambda : user_close(window))
    
    storage_name = tk.StringVar()

    storage_label = tk.Label(window, text = 'Enter the storage server this data belongs to:')
    storage_entry = tk.Entry(window, text = storage_name)

    storage_label.place(relx=0.5, rely=0.4, anchor='center')
    storage_entry.place(relx=0.5, rely=0.5, anchor='center')
    storage_entry.bind('<Return>', lambda e: next_window(window))
    
    storage_entry.focus()
    window.mainloop()

    storage = storage_name.get()
    print ('Storage Server:' + storage)
    return storage


def submit(window, storage_paths):
    global submittedPaths
    submittedPaths = storage_paths.get('1.0', 'end-1c')
    window.destroy()
    return submittedPaths


# https://stackoverflow.com/questions/60014280/tkinter-how-can-you-use-get-to-save-the-input-in-a-scrolled-text-widget-to-a
def storagePaths():
    window = tk.Tk()
    window.title('Enter Storage Paths')
    window.geometry('800x600')
    window.protocol('WM_DELETE_WINDOW', lambda : user_close(window))
    window.attributes('-topmost', True)

    storage_label = tk.Label(window, text = 'Paste in the paths. The paths should have the server name first. ex; \\\\storage\\main\\subfolder')
    storage_paths = scrolledtext.ScrolledText(window, width=60, height=25)
    submit_button = tk.Button(window, text='Submit', width=6, command=lambda : submit(window, storage_paths))

    submit_button.place(relx=0.5, rely=0.9, anchor='center')         
    storage_label.place(relx=0.5, rely=0.1, anchor='center')
    storage_paths.place(relx=0.5, rely=0.5, anchor='center') 

    window.focus_force()
    storage_paths.focus_force()
    window.mainloop()

    return submittedPaths


def convertedPaths(final, storageServer):
    window = tk.Tk()
    window.title('Converted Paths')
    window.geometry('800x600')
    window.protocol('WM_DELETE_WINDOW', lambda : user_close(window))

    converted_label = tk.Label(window, text = ('Delete this data on ' + storageServer))
    converted_paths = scrolledtext.ScrolledText(window, width=60, height=25)

    converted_label.place(relx=0.5, rely=0.1, anchor='center')
    converted_paths.place(relx=0.5, rely=0.5, anchor='center')

    converted_paths.insert(tk.INSERT, final)
    converted_paths.configure(state ='disabled')

    window.mainloop()


convert()

