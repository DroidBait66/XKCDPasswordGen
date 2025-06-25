# 🔐 XKCD-Style Password Generator (`xkcdpwgen`)

A secure, memorable password generator that uses the [XKCD method](https://xkcd.com/936/), written in Python. This command-line tool produces passwords consisting of random English words, with optional capitalization, symbols, and numbers to enhance entropy without sacrificing memorability.

---

## 📄 Description

People often choose weak passwords or overly complex ones that are hard to remember. This project aims to strike a balance by generating passwords that are both **secure** and **easy to recall**, using a list of English words and optional modifiers.


The generator supports the following options:
- Specify number of words
- Capitalize the first letter of selected words
- Insert symbols and numbers at random positions

---

## 🛠️ Features

- ✅ Default behavior: generate 4 lowercase words
- ✅ Supports `--words` / `-w` to change word count
- ✅ Supports `--caps` / `-c` to capitalize N random words
- ✅ Supports `--numbers` / `-n` to insert N numbers
- ✅ Supports `--symbols` / `-s` to insert N symbols
- ✅ Help flag `-h` / `--help` shows usage instructions

---

## 💻 Usage

```bash
$ ./xkcdpwgen             # Generates 4-word password
$ ./xkcdpwgen -w 5        # 5 words
$ ./xkcdpwgen -c 2        # Capitalize 2 random words
$ ./xkcdpwgen -n 2 -s 3   # Add 2 numbers and 3 symbols
$ ./xkcdpwgen --help      # Show help message