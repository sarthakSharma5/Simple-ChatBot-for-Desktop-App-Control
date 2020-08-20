#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pyttsx3


# In[5]:


check="null"
while True:
    if check == "exit":
        break
    else:
        prompt=input("\n\n What would you like to do: \ntype 'exit' to end \n")
        if ("run" in prompt or "launch" in prompt or "open" in prompt) and (("text editor" in prompt) or ("notepad" in prompt)):
            os.system("notepad")
        elif ("run" in prompt or "launch" in prompt or "open" in prompt) and (("browser" in prompt) or ("chrome" in prompt)):
            url=input("have some URL to open, give me: \n - put no if dont : ")
            if url != "no":
                os.system("chrome "+url)
            else:
                os.system("chrome")
        elif ("run" in prompt or "launch" in prompt or "open" in prompt) and ("firefox" in prompt):
            url=input("have some URL to open, give me: \n - put no if dont : ")
            if url != "no":
                os.system("firefox "+url)
            else:
                os.system("firefox")
        elif ("run" in prompt or "launch" in prompt or "open" in prompt) and (("media player" in prompt) or ("windows media player" in prompt) or ("wmplayer" in prompt)):
            os.system("wmplayer")
        elif ("run" in prompt or "launch" in prompt or "open" in prompt) and (("vlc media player" in prompt) or ("vlc" in prompt)):
            os.system("vlc")
        elif ("run" in prompt or "launch" in prompt or "open" in prompt) and (("android studio" in prompt) or ("studio64.exe" in prompt)):
            os.system("studio64.exe")
        elif ("run" in prompt or "launch" in prompt or "open" in prompt) and (("visual studio code" in prompt) or ("vscode" in prompt) or ("code" in prompt)):
            os.system("code")
        elif ("run" in prompt or "launch" in prompt or "open" in prompt or "get" in prompt ) and (("command line" in prompt) or ("cmd" in prompt) or ("start" in prompt)):
            os.system("start")
        elif (prompt == "exit"):
            pyttsx3.speak("Wish to see you again")
            break
        else:
            print("\nNot Supported\n")


# In[ ]:




