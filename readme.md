# HessOS

![](https://raw.githubusercontent.com/bowser-2077/HessOS/refs/heads/main/github/V2.png)

HessOS is a lightweight, custom command-line operating system simulator written in Python.  
Designed for learning, tinkering, and fun, HessOS offers a simple shell with essential commands, boot animation, dependency management, and more.

---

## Features

- **Custom Shell Interface** with command prompt and dynamic command handling
- **Boot Sequence** with centered logo and loading animation  
- **First Boot Dependency Installation** with automatic package setup  
- **Command Modules** for easy extensibility (commands live in `cmds/` folder)  
- Common Unix-like commands:  
  - `ls`, `cd`, `mkdir`, `rmdir`, `rm`, `touch`, `cat`, `head`  
  - `clear`, `help`, `ping`, `ssh`, `download`  
- **Logging and Configuration Management** through `logs/` and `config/` folders  
- Shutdown command with fake service loading animation  
- Modular codebase structured with `cmds/`, `startup/`, `utils/`, `config/`, and `logs/`

---

## Getting Started

### Requirements

- Python 3.8 or higher  
- Internet connection for first-time dependency installation

### Installation

Clone the repository:

```bash
git clone https://github.com/bowser-2077/HessOS.git
cd hessos
```

# Run the OS:

```
python main.py
```

On the first run, you will need to install required dependencies by using the 
```
py install-deps.py
``` 
command into HessOS.

# HessOS Usage

### Basic Commands


    help — Show available commands
    ls — List files in current directory
    cd <folder> — Change directory
    mkdir <folder> — Create a new directory
    rmdir <folder> — Remove a directory
    rm <file> — Delete a file
    touch <file> — Create a new empty file
    cat <file> — Display file content
    head <file> — Show first 10 lines of a file
    clear — Clear the screen
    ping <host> — Ping a host to check network connectivity
    ssh <user>@<host> — Connect to a remote host via SSH
    download <url> — Download a file from a URL into downloads/ folder
    showlogs — Display recent logs
    shutdown — Shutdown the OS with animated loading of services
    package — Install package (only git for now)
    update — Update the os (Very Unstable for now!)

## Package Command Usage


  Multiple packages can be installed, here all of the informations that you need to know about


### List of the packages


  - 2048 (Game, indev)
  - Ascii-art (Utility, working)
  - Curl (Utility, working)
  - Download (Utility, working, unstable)
  - Git (Utility, untested, unstable)
  - Qr (Fun, utility, working)
  - Snake (Game, working, a bit bugged)
  - Speedtest (Utility, untested)
  - Stock (Money, Money, Money, working)
  - Sysinfo (No implemented yet but working) -> to install it, you will need to modify the package list at /config/packages.json and add the package name
  - Tetris (Game, indev)


    Note : all indev package are not supposed to work.

### Install a package


  Usage : ```package install <package_name>```

  Make sure to execute : ```reload-cmds``` before executing a package!

### Uninstall a package


  
  Usage : ```package uninstall <package_name>```

  Make sure to execute : ```reload-cmds``` to properly uninstall it.

### Add your own package


  You can code your own package and open a pull request with your package informations, code, and dependencies
  I will review it and add it to the "OS"

  Make sure to code it in python (Python 3 and older only)

  Requirements to add your package

 - -> Your name (Username, not real if you want) need to be somewhere in the code (as a command like "<packagename> about" or a comment on the code "# made by <name>")
 - -> Your code cant be obfuscated
 - -> Your package cannot use any visual ui (PySide6, PyQt5,...) its only cli
 - -> Your package cant be used to track people activity
 - -> Your package need to be usable on Linux and Windows 10/11

Thanks!
    

## Exiting


    Use forceexit command to quit hessos OR use the shutdown command.

## Project Structure


hessos/

├── cmds/          # Command implementations and package python files  
├── config/        # Configuration files and and package list file
├── logs/          # Log files (Not working yet) 
├── startup/       # Boot scripts and animations  
├── utils/         # Utility modules (logger, helpers) -> not working yet  
├── main.py        # Entry point, start the os with this file

## SSH Client

HessOS come with an integrated ssh client, usable with : ```ssh <host> <username> <password>```
Your will need to have paramiko installed to use SSH.

## Updates system

The update command will not work with HessOS V1, please install the V2 of HessOS to be able to use the update command
After the update please manually restart your PC, issue will be fixed in a couple of days

## Contributing

Feel free to open issues or pull requests! Add commands, improve UX, or optimize code.
License

MIT License © 2025 Gaetan LERLEY

## Contact

Hostinfire — hostinfire@gmail.com
GitHub: https://github.com/bowser-2077

# Happy HessIng! 🚀

