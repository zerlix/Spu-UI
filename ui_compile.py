'''
einfaches script um *.ui dateien im Verzeichnis ./ui zu kompilieren 
die kompilierten python datei befinden sich dann im verzeichnis ./src
'''
import os
ui_dir = './ui'
src_dir = './src'

if __name__ == "__main__":
    for filename in os.listdir(ui_dir):
        if filename.endswith('.ui'):
            print('Compiling... '+ui_dir+'/'+filename)
            print('Save...      '+src_dir+'/ui_'+filename[:-3  ]+'.py')
            os.system('pyside6-uic '+ui_dir+'/'+filename+' -o '+src_dir+'/ui_'+filename[:-3]+'.py')
