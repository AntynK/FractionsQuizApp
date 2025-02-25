# Changelog  

## [1.2.2] - 2025-02-25
### Changed
* Reduced the amount of text in messages.

## [1.2.1] - 2025-01-17
### Changed
* The app version has been removed from the window title.
* File `main.pyw` has been renamed to `main.py`.


## [1.2.0] - 2024-11-16
### Fixed
* Error in exersice window.
* Minor errors.

### Added
* Instruction for building program.


## [1.1.0] - 2024-11-08
### Added
* File `CHANGELOG_ENG.md`.
* Type and value check `ValueError`
* Button "Спробувати ще"(Try again) by default is inactive, if user enters right answer button becomes active.

### Changed
* Style of changelog.
* Tests.
* Text for some buttons.
* Congratulation window image.
* Program title from "Програма для покращення знань з дробів"(A program to improve knowledge of fractions) to "Тренажер для вивчення звичайних дробів"(An interactive tool for learning fractions).

### Fixed
* Typos in README files.
* Помилки при скороченні дробів з нульовим чисельником, тепер після скорочення повертається дріб з 0 в чисельнику.
* Issuses with subtopics display.

## [1.0.2] - 2024-02-08
### Changed
* `README.md` file, now Ukrainian version is main, and English is secondary because this app is mainly designed for Ukrainian schools.
* Removed negative fractions in fraction subtraction topic, because the program is designed for pupils in 5th grade who have not yet studied negative fractions.


## [1.0.1] - 2024-01-15
### Fixed
* Congratulation window image.
* Problem when result of operation is zero, now when result of operation is **0** user should pass fraction **0 <sup>0</sup>/<sub>0</sub>**.


## [1.0.0] - 2024-01-07
### Added
* Title window.

### Changed
* The exercise window, now input fields are placed like fraction.


## [0.2.7] - 2023-12-10
### Changed
* Congratulation window.
* Increased size of buttons and labels font size.


## [0.2.6] - 2023-12-03
### Added 
* Congratulation window.
* Capability of entering negative numbers.

### Fixed
* Issues with fraction operations.


## [0.2.5] - 2023-11-25
### Added
* [`CHANGELOG.md`](CHANGELOG.md).

### Changed
* Removed `requirements.txt`, because project don't use any external libraries.

### Fixed
* Issues with fraction appearence.
* Issues with fraction calculation.
