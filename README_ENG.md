# Program for studying fractions

> [!NOTE]
> Цей документ має переклад [українською](README.md).


This program is designed to teach and improve understanding of fractions. The program contains interactive exercises that will help users improve their skills in working with fractions.

The program consists of 4 topics, each of which has several subtopics:
* Adding fractions
     * Adding fractions with like denominator
     * Adding fractions with unlike denominators
     * Adding mixed numbers
* Subtracting fractions
     * Subtracting fractions with like denominator
     * Subtracting fractions with unlike denominators
     * Subtracting mixed numbers
* Multiplying fractions
     * Multiplying fraction by a natural number
     * Multiplying fractions with unlike denominators
     * Multiplying mixed numbers
* Dividing fractions
     * Dividing fraction by a natural number
     * Dividing natural number by a fraction
     * Dividing fractions with unlike denominators
     * Dividing mixed numbers

![Exercise Window](assets/exercise_window_ua.png)

## Features
* Exercises are randomly generated, but with restrictions so that fractions are always proper. When subtracting, there were no negative fractions (the program is designed for pupils in 5–6 grades who don't study negative fractions).
* If the calculation result is an integer, the user can hide the fraction part by pressing the button "Приховати" values entered earlier will be saved. 
* If the user correctly calculated result, the congratulation window will be opened:
![Congratulation window](assets/congratulation.png)


## Available languages
* Ukrainian

## Available platforms
This program is written in [Python 3.9.7](https://www.python.org/downloads/release/python-397/) using the built-in module [tkinter](https://docs.python.org/3/library/tkinter.html) and module [pillow](https://pypi.org/project/pillow/).

If you have found mistake or problem, please report them on the [Issues](https://github.com/AntynK/FractionsQuizApp/issues) page.

> [!IMPORTANT]
> Python 3.9 or later is required.


## How to get started

### Method 1: Download the source code
> [!IMPORTANT]
> You must have the [Python interpreter](https://www.python.org/downloads/release/python-397/) installed.
    
> [!IMPORTANT]
> To run the source code, install dependencies with the command: `pip install -r requirements.txt`

1. Open the [releases](https://github.com/AntynK/FractionsQuizApp/releases/latest) page.
2. Download the SourceCode.zip archive.
3. Unzip it.
4. Run the main.py file by double-clicking on it or via the command:

#### Windows:
```bash
python main.py
```
#### Linux and MacOS:
```bash
python3 main.py
```

> [!IMPORTANT]
> Some Linux distributions do not include `tkinter` package. If you receive `ImportError` try to install `python-tk` package via package manager for example `apt`.


### Method 2: Download the executable file
> [!WARNING]
> Windows Antivirus may recognize the executable file as a potential malware. If you are worried, you could try to run the source code(Method 1).

1. Open the [releases](https://github.com/AntynK/FractionsQuizApp/releases/latest) page.
2. Download the FractionsQuizApp.exe file.
3. Run it.

## Contributors
If you have ideas for improvement or want to contribute to the development of the project, please submit your contribution. See [CONTRIBUTING.md](CONTRIBUTING.md).

### Building (Windows only)
[Pyinstaller](https://pyinstaller.org/en/stable/) is used for building the program. It can be installed using the following command:

#### Windows
```bash 
pip install -U pyinstaller
```
To build the app, use the following command:

#### Windows
```bash 
pyinstaller build.spec
```

After building, a `dist` folder will be created, which contains the executable file.

> [!NOTE]
> `exe_file_version` file must be in the same directory as `build.spec` file.
