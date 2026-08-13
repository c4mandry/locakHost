# 🌐 LocakHost

> **The zero-terminal, point-and-click local web server for frontend developers.**

LocakHost is a lightweight desktop app built to serve static websites and modern Single Page Applications (SPAs) instantly. No terminal commands, no complex server setups—just select your folder, click start, and preview your work in the browser.

---

## 📸 Overview & Key Features

* 🖱️ **100% Graphical (GUI):** No CLI experience required.
* 🔄 **SPA Route Fallback:** Built-in support for single-page apps (React, Vue, Vite, Svelte) to prevent `404 Not Found` errors when refreshing sub-routes like `/dashboard`.
* 📁 **Smart Folder Detection:** Automatically detects project roots and `index.html` files.
* 🔌 **Port Binding Control:** Easily switch between custom ports or let LocakHost auto-detect an open one.
* 🧹 **Clean System Exit:** Kills background child processes and frees network sockets when closed—no stuck ports!

---

## ⚡ Quick Start

### 1. Prerequisites
LocakHost runs on **Python 3.8+**. It uses standard Python libraries, including `tkinter` for the GUI.

* **Linux (Ubuntu/Debian/Arch/Void):**
  ```bash
  # Debian/Ubuntu
  sudo apt install python3-tk

  # Arch Linux / CachyOS
  sudo pacman -S tk

  # Void Linux
  sudo xbps-install -S tk

### 2. how to run 
   #### macos - "brew install python-tk && python3 your/directory/to/locakhost.py $(: like for example: ~/downloads/locakhost)"
   #### linux - "$(: first install python-tk in your way) python3 your/directory/to/locakhost.py $(: like for example: ~/downloads/locakhost)"
