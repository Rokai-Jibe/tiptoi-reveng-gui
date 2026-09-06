#!/usr/bin/env python3
"""
tttool GUI - Graphical interface for tttool (Tiptoi Reveng)
A cross-platform GUI wrapper for the tttool command-line utility.
https://github.com/entropia/tip-toi-reveng
"""
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import subprocess
import os
import sys
import shutil
import json
import threading
import platform

# Config file storing the user-selected tttool path
CONFIG_PATH = os.path.expanduser("~/.tttool_gui_config.json")

def get_base_dir():
    """Return the directory where the script or frozen executable lives."""
    if getattr(sys, "frozen", False):
        # Running as a PyInstaller bundle
        # In .app bundles, sys._MEIPASS is the temp extraction dir
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def get_tttool_binary_name():
    return "tttool.exe" if platform.system() == "Windows" else "tttool"

def load_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_config(data):
    try:
        with open(CONFIG_PATH, "w") as f:
            json.dump(data, f)
    except Exception:
        pass

def find_tttool():
    """
    Try to locate the tttool executable, in order:
    1. Next to the script/bundled executable
    2. In the system PATH
    3. In the saved config file
    Returns the path if found, or None.
    """
    binary_name = get_tttool_binary_name()

    # 1. Next to the script/executable
    candidate = os.path.join(get_base_dir(), binary_name)
    if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
        return candidate

    # 2. In system PATH
    found = shutil.which(binary_name) or shutil.which("tttool")
    if found:
        return found

    # 3. Saved config
    config = load_config()
    saved_path = config.get("tttool_path")
    if saved_path and os.path.isfile(saved_path) and os.access(saved_path, os.X_OK):
        return saved_path

    return None

def ask_user_for_tttool(root):
    """Prompt the user to manually locate the tttool executable."""
    messagebox.showwarning(
        "tttool not found",
        "The tttool executable could not be found automatically.\n\n"
        "Please select its location manually in the next dialog."
    )
    binary_name = get_tttool_binary_name()
    filetypes = [("tttool executable", binary_name), ("All files", "*.*")]
    path = filedialog.askopenfilename(
        title="Locate the tttool executable",
        filetypes=filetypes
    )
    if path and os.path.isfile(path):
        config = load_config()
        config["tttool_path"] = path
        save_config(config)
        return path
    return None


class TipToiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tiptoi Reveng - GUI")
        self.root.geometry("700x600")

        self.input_file = tk.StringVar()
        self.output_file = tk.StringVar()

        # Resolve the tttool path (auto-detect, then ask user if needed)
        self.tttool_path = find_tttool()
        if not self.tttool_path:
            self.tttool_path = ask_user_for_tttool(self.root)

        self.build_ui()

        if not self.tttool_path or not os.path.exists(self.tttool_path):
            messagebox.showerror(
                "Error",
                "tttool executable could not be located.\n\n"
                "The application may not work correctly.\n"
                "You can restart it and select the path manually when prompted."
            )

    def build_ui(self):
        pad = {'padx': 10, 'pady': 5}

        # --- tttool path info ---
        frame_path = tk.LabelFrame(self.root, text="tttool executable")
        frame_path.pack(fill="x", **pad)
        self.path_label = tk.Label(
            frame_path,
            text=self.tttool_path or "Not found",
            fg="black", anchor="w"
        )
        self.path_label.pack(side="left", padx=5, pady=5, fill="x", expand=True)
        tk.Button(frame_path, text="Change...", command=self.change_tttool_path).pack(side="left", padx=5)

        # --- Input file ---
        frame_in = tk.LabelFrame(self.root, text="Source GME file")
        frame_in.pack(fill="x", **pad)

        tk.Entry(frame_in, textvariable=self.input_file, width=60).pack(side="left", padx=5, pady=5)
        tk.Button(frame_in, text="Browse...", command=self.browse_input).pack(side="left", padx=5)

        # --- Available commands ---
        frame_cmd = tk.LabelFrame(self.root, text="Action to perform")
        frame_cmd.pack(fill="x", **pad)

        self.command_var = tk.StringVar(value="info")
        commands = [
            ("General information (info)", "info"),
            ("Export to YAML (export)", "export"),
            ("Show scripts (scripts)", "scripts"),
            ("Show games (games)", "games"),
            ("Check for errors (lint)", "lint"),
            ("List segments (segments)", "segments"),
            ("Extract audio (media)", "media"),
            ("Extract binaries (binaries)", "binaries"),
            ("Change language (set-language)", "set-language"),
            ("Change product-id (set-product-id)", "set-product-id"),
            ("Reassemble (assemble)", "assemble"),
        ]

        for i, (label, val) in enumerate(commands):
            tk.Radiobutton(
                frame_cmd, text=label, variable=self.command_var, value=val,
                command=self.update_options
            ).grid(row=i // 2, column=i % 2, sticky="w", padx=10, pady=2)

        # --- Dynamic options ---
        self.frame_opts = tk.LabelFrame(self.root, text="Options")
        self.frame_opts.pack(fill="x", **pad)
        self.opts_widgets = {}
        self.update_options()

        # --- Output folder/file ---
        frame_out = tk.LabelFrame(self.root, text="Output file / folder")
        frame_out.pack(fill="x", **pad)
        tk.Entry(frame_out, textvariable=self.output_file, width=60).pack(side="left", padx=5, pady=5)
        tk.Button(frame_out, text="Choose...", command=self.browse_output).pack(side="left", padx=5)

        # --- Run button ---
        tk.Button(
            self.root, text="Run", bg="#4CAF50", fg="black",
            font=("Arial", 12, "bold"), command=self.run_command
        ).pack(pady=10)

        # --- Log area ---
        frame_log = tk.LabelFrame(self.root, text="Log / Output")
        frame_log.pack(fill="both", expand=True, **pad)
        self.log = scrolledtext.ScrolledText(frame_log, height=15, wrap="word", fg="black", bg="white")
        self.log.pack(fill="both", expand=True)

    def change_tttool_path(self):
        path = filedialog.askopenfilename(
            title="Locate the tttool executable",
            filetypes=[("tttool executable", get_tttool_binary_name()), ("All files", "*.*")]
        )
        if path and os.path.isfile(path):
            self.tttool_path = path
            config = load_config()
            config["tttool_path"] = path
            save_config(config)
            self.path_label.config(text=path)
            self.log_msg(f"tttool path updated: {path}")

    def update_options(self):
        # Clear previous option widgets
        for w in self.frame_opts.winfo_children():
            w.destroy()
        self.opts_widgets.clear()

        cmd = self.command_var.get()

        if cmd == "set-language":
            tk.Label(self.frame_opts, text="Language code (e.g. FR, DE, EN):").pack(side="left", padx=5)
            self.opts_widgets["lang"] = tk.Entry(self.frame_opts, width=10)
            self.opts_widgets["lang"].pack(side="left", padx=5)

        elif cmd == "set-product-id":
            tk.Label(self.frame_opts, text="New Product ID:").pack(side="left", padx=5)
            self.opts_widgets["pid"] = tk.Entry(self.frame_opts, width=10)
            self.opts_widgets["pid"].pack(side="left", padx=5)

        elif cmd == "assemble":
            tk.Label(self.frame_opts, text="Requires a YAML file (select as source file above)").pack(padx=5, pady=5)

        else:
            tk.Label(self.frame_opts, text="No additional options required.").pack(padx=5, pady=5)

    def browse_input(self):
        path = filedialog.askopenfilename(
            title="Select a GME or YAML file",
            filetypes=[("GME/YAML files", "*.gme *.yaml *.yml"), ("All files", "*.*")]
        )
        if path:
            self.input_file.set(path)
            base, _ = os.path.splitext(path)
            self.output_file.set(base + "_modified")

    def browse_output(self):
        cmd = self.command_var.get()
        if cmd in ("media", "binaries", "oid-codes"):
            path = filedialog.askdirectory(title="Choose an output folder")
        else:
            path = filedialog.asksaveasfilename(title="Save as...")
        if path:
            self.output_file.set(path)

    def log_msg(self, msg):
        self.log.insert("end", msg + "\n")
        self.log.see("end")
        self.root.update_idletasks()

    def run_command(self):
        if not self.tttool_path or not os.path.exists(self.tttool_path):
            messagebox.showerror("Error", "tttool executable not found. Please set its path first.")
            return
        thread = threading.Thread(target=self._run_command_thread)
        thread.start()

    def _run_command_thread(self):
        infile = self.input_file.get()
        outfile = self.output_file.get()
        cmd = self.command_var.get()

        if not infile or not os.path.exists(infile):
            messagebox.showerror("Error", "Please select a valid source file.")
            return

        args = [self.tttool_path, cmd]

        if cmd == "set-language":
            lang = self.opts_widgets["lang"].get().strip()
            if not lang:
                messagebox.showerror("Error", "Please enter a language code.")
                return
            args += [lang, infile]

        elif cmd == "set-product-id":
            pid = self.opts_widgets["pid"].get().strip()
            if not pid:
                messagebox.showerror("Error", "Please enter a product-id.")
                return
            args += [pid, infile]

        elif cmd == "assemble":
            args += [infile]
            if outfile:
                args += ["-o", outfile]

        elif cmd in ("media", "binaries"):
            args += [infile]
            if outfile:
                os.makedirs(outfile, exist_ok=True)
                args += ["-d", outfile]

        else:
            args += [infile]

        self.log_msg(f"\n>>> Running command:\n{' '.join(args)}\n")

        try:
            result = subprocess.run(
                args, capture_output=True, text=True, timeout=300
            )
            if result.stdout:
                self.log_msg(result.stdout)
            if result.stderr:
                self.log_msg("[stderr]\n" + result.stderr)

            if result.returncode == 0:
                self.log_msg("\n✅ Command completed successfully.")

                # Special case: set-language / set-product-id modify the file in place
                if cmd in ("set-language", "set-product-id"):
                    messagebox.showinfo("Success", f"File modified in place:\n{infile}")
                elif cmd == "assemble" and outfile:
                    messagebox.showinfo("Success", f"File created:\n{outfile}")
            else:
                self.log_msg(f"\n❌ Error (return code {result.returncode})")

        except subprocess.TimeoutExpired:
            self.log_msg("❌ Timeout: the command took too long to execute.")
        except Exception as e:
            self.log_msg(f"❌ Exception: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TipToiApp(root)
    root.mainloop()
