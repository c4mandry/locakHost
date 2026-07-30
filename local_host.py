#!/usr/bin/env python3
"""
Local Host - a tiny GUI app to host a folder as a local website.

Works on macOS and Linux. Requires Python 3 with tkinter (usually pre-installed
on macOS; on Linux you may need: sudo apt install python3-tk).

Usage:
    python3 local_host.py
"""

import http.server
import socketserver
import threading
import webbrowser
import tkinter as tk
from tkinter import filedialog, messagebox

DEFAULT_PORT = 8080


class Server:
    def __init__(self):
        self.httpd = None
        self.thread = None

    def start(self, folder: str, port: int):
        if self.httpd is not None:
            raise RuntimeError("Server already running")

        handler = lambda *args, **kwargs: http.server.SimpleHTTPRequestHandler(
            *args, directory=folder, **kwargs
        )

        # allow_reuse_address avoids "port already in use" right after stopping
        socketserver.TCPServer.allow_reuse_address = True
        self.httpd = socketserver.TCPServer(("0.0.0.0", port), handler)

        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()

    def stop(self):
        if self.httpd is not None:
            self.httpd.shutdown()
            self.httpd.server_close()
            self.httpd = None
            self.thread = None

    @property
    def running(self):
        return self.httpd is not None


class App:
    def __init__(self, root):
        self.root = root
        self.server = Server()
        self.folder_var = tk.StringVar(value="")
        self.port_var = tk.StringVar(value=str(DEFAULT_PORT))
        self.status_var = tk.StringVar(value="Not running")

        root.title("Local Host")
        root.resizable(False, False)
        pad = {"padx": 10, "pady": 6}

        # Folder row
        tk.Label(root, text="Folder:").grid(row=0, column=0, sticky="w", **pad)
        tk.Entry(root, textvariable=self.folder_var, width=40).grid(
            row=0, column=1, **pad
        )
        tk.Button(root, text="Browse...", command=self.browse).grid(
            row=0, column=2, **pad
        )

        # Port row
        tk.Label(root, text="Port:").grid(row=1, column=0, sticky="w", **pad)
        tk.Entry(root, textvariable=self.port_var, width=10).grid(
            row=1, column=1, sticky="w", **pad
        )

        # Buttons row
        self.host_btn = tk.Button(root, text="Host", width=12, command=self.toggle_host)
        self.host_btn.grid(row=2, column=1, sticky="w", **pad)

        self.open_btn = tk.Button(
            root, text="Open in Browser", command=self.open_browser, state="disabled"
        )
        self.open_btn.grid(row=2, column=2, sticky="w", **pad)

        # Status row
        tk.Label(root, textvariable=self.status_var, fg="gray").grid(
            row=3, column=0, columnspan=3, sticky="w", **pad
        )

        root.protocol("WM_DELETE_WINDOW", self.on_close)

    def browse(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_var.set(folder)

    def toggle_host(self):
        if self.server.running:
            self.server.stop()
            self.host_btn.config(text="Host")
            self.open_btn.config(state="disabled")
            self.status_var.set("Not running")
            return

        folder = self.folder_var.get().strip()
        if not folder:
            messagebox.showerror("Error", "Please choose a folder first.")
            return

        port_str = self.port_var.get().strip() or str(DEFAULT_PORT)
        try:
            port = int(port_str)
        except ValueError:
            messagebox.showerror("Error", "Port must be a number.")
            return

        try:
            self.server.start(folder, port)
        except OSError as e:
            messagebox.showerror("Error", f"Could not start server:\n{e}")
            return

        self.host_btn.config(text="Stop")
        self.open_btn.config(state="normal")
        self.status_var.set(f"Hosting {folder} at http://localhost:{port}")

    def open_browser(self):
        port = self.port_var.get().strip() or str(DEFAULT_PORT)
        webbrowser.open(f"http://localhost:{port}")

    def on_close(self):
        self.server.stop()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
