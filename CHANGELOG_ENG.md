# Changelog  


## [1.1.0] - 2024-11-07
### Added
* File `CHANGELOG_ENG.md`.
* При створенні екземпляр класу `Fraction` відбувається перевірка типів та значення знаменника, щоби він був більшим за нуль. Якщо неправильний тип аргументів, у знаменнику нуль або від'ємне число, то тоді генерується виняток `ValueError`
* Кнопка "Спробувати ще" за замовчуванням неактивна, якщо користувач правильно порахував, тоді вона стає активною.

### Changed
* Style of changelog.
* Tests.
* Text for some buttons.
* Якщо при виділенні цілої частинин, дріб виноситься повністю до прикладу <sup>4</sup>/<sub>4</sub>, тоді потрібно записати 1<sup>0</sup>/<sub>4</sub>.
* Congratulation window image.
* Program title from "Програма для покращення знань з дробів" to "Тренажер для вивчення звичайних дробів".

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
