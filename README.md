#  LocakHost

> **The zero-terminal, point-and-click local web server for frontend developers.**

easiest way to run complex websites with a gui programm. works with all sorts of websites, so leav the nmp stuff behind and use this.

---

##  Overview & Key Features

*  **100% Graphical (GUI):** No CLI experience required.
*  **SPA Route Fallback:** Built-in support for single-page apps (React, Vue, Vite, Svelte) to prevent `404 Not Found` errors when refreshing sub-routes like `/dashboard`.
*  **Smart Folder Detection:** Automatically detects project roots and `index.html` files.
*  **Port Binding Control:** Easily switch between custom ports or let LocakHost auto-detect an open one.
*  **Clean System Exit:** Kills background child processes and frees network sockets when closed—no stuck ports!
*  **Can open up your website in your browser with just one click

---

##  Quick Start

### 1. how to run 
   #### macos - "brew install python-tk && python3 your/directory/to/locakhost.py $(: like for example: ~/downloads/locakhost)"
   #### linux - "$(: first install python-tk in your way) python3 your/directory/to/locakhost.py $(: like for example: ~/downloads/locakhost)"
   #### windows powershell - "winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements; python C:\path\to\locakhost.py "C:\path\to\your\folder" " dont know if it works i dont have a windows system but mac and linux are tested
