# Age of Dragons

A collection of Object-Oriented Python exercises exploring classes, inheritance, encapsulation, operator overloading, and more -- all themed around a medieval fantasy world of soldiers, dragons, and siege warfare.

> This repository is a learning/coursework project for an OOP Python bootcamp. Each file is a self-contained exercise demonstrating specific Python class concepts. The files are **not** part of a single runnable game.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Project Structure](#project-structure)
- [OOP Concepts Covered](#oop-concepts-covered)
- [Getting Started](#getting-started)
- [Running the Exercises](#running-the-exercises)
- [Running the Tests](#running-the-tests)
- [Exercise Reference](#exercise-reference)
- [Contributing](#contributing)

---

## About the Project

**Age of Dragons** is an educational repository containing ~15 standalone Python scripts, each demonstrating one or more Object-Oriented Programming principles using a fantasy/combat theme. Topics range from basic class definitions and `__init__` constructors to advanced name-mangling, abstract methods, and operator overloading.

There is no game engine, GUI, or networking -- just pure Python classes and logic.

---

## Project Structure

```
age_of_dragons/
├── main.py                 # Multi-exercise file: Soldier, Archer, Wall, Wizard, Dragon, Brawler, Human
├── main_test.py            # Tests for the Wizard class (from main.py)
├── script.py               # Minimal Point class demo (__str__)
├── practice.py             # Card comparison system (Card, Round, HighCardRound, LowCardRound)
├── card_game_plus.py       # Identical copy of practice.py (course platform artifact)
├── practice_test.py        # Tests for Card/Round classes (from card_game_plus.py)
├── card-game.py            # Standalone DeckOfCards implementation
├── army_form.py            # Rectangle / Square inheritance demo
├── crossbowman_unit.py     # Three-level inheritance: Human → Archer → Crossbowman
├── dragon_fight.py         # Unit/Dragon positional combat with fire breath areas
├── dragons_announce.py     # Simple Dragon class with __str__
├── hero_childs.py          # Hero inheritance hierarchy: Hero → Archer / Wizard
├── hit_box.py              # Rectangle collision detection for dragon fire breath
├── library_system.py       # Book and Library management classes
├── siege_weapons.py        # Siege → BatteringRam / Catapult inheritance with super()
├── craft_weapons.py        # Sword class with operator overloading (__add__) for crafting
├── .env                    # Environment variable placeholders (unused)
├── .gitignore              # Ignores .env and __pycache__
└── .vscode/                # VS Code workspace settings
```

### File Dependency Map

```
main.py          ◄─── main_test.py       (from main import *)
card_game_plus.py ◄─── practice_test.py  (from card_game_plus import *)
practice.py      ════ card_game_plus.py  (identical files)
```

All other `.py` files are fully standalone with no cross-file dependencies.

---

## OOP Concepts Covered

| Concept | Files |
|---|---|
| **Classes & `__init__`** | `main.py` (Soldier, Dragon), `script.py` (Point), `library_system.py` (Book) |
| **Instance Methods & Attributes** | All files |
| **Encapsulation / Name Mangling** | `main.py` (Wizard, Human), `hit_box.py` (Rectangle) |
| **Inheritance** | `army_form.py`, `crossbowman_unit.py`, `hero_childs.py`, `siege_weapons.py`, `dragon_fight.py`, `hit_box.py` |
| **Method Overriding** | `siege_weapons.py`, `hit_box.py` |
| **`super()` usage** | `army_form.py`, `crossbowman_unit.py`, `hero_childs.py`, `siege_weapons.py` |
| **Abstract Methods** | `practice.py` / `card_game_plus.py` (Round.resolve_round) |
| **Operator Overloading** | `craft_weapons.py` (`__add__`), `practice.py` (`__eq__`, `__gt__`, `__lt__`), `script.py` / `dragons_announce.py` (`__str__`), `hit_box.py` / `craft_weapons.py` (`__repr__`) |
| **Class Composition** | `hit_box.py` (Dragon has-a Rectangle), `library_system.py` (Library has-many Books) |
| **Collision / Position** | `dragon_fight.py`, `hit_box.py` |

---

## Getting Started

### Prerequisites

- **Python 3.10+** (the project was developed across Python 3.12 and 3.14)
- No third-party packages are required. The only standard library import is `random` in `card-game.py`.

### Installation

```bash
git clone https://github.com/YitbarekEnd/age_of_dragons.git
cd age_of_dragons
```

No virtual environment or `pip install` step is needed -- there are no external dependencies.

---

## Running the Exercises

Each file is an independent exercise. Run any file directly:

```bash
# Main multi-exercise file (Brawlers, Dragons, fights)
python main.py

# Dragon positional combat
python dragon_fight.py

# Card deck demo
python card-game.py

# Rectangle / Square inheritance
python army_form.py

# Three-level inheritance chain
python crossbowman_unit.py

# Sword crafting with operator overloading
python craft_weapons.py

# Hero hierarchy
python hero_childs.py

# Hit box collision detection
python hit_box.py

# Siege weapon inheritance
python siege_weapons.py

# Library management
python library_system.py
```

Files like `script.py`, `dragons_announce.py`, `practice.py`, and `card_game_plus.py` define classes but do not have a `main()` call, so they produce no output when run directly -- they are designed to be imported or tested.

---

## Running the Tests

There are two test files using a bootcamp-style testing framework with `run_cases`/`submit_cases` toggles.

### Wizard tests (from main.py)

```bash
python main_test.py
```

Tests the `Wizard` class's `get_fireballed()` and `drink_mana_potion()` methods with three wizard configurations.

### Card game tests (from card_game_plus.py)

```bash
python practice_test.py
```

Tests `Card` comparison operators and `HighCardRound`/`LowCardRound` resolution with 7 test cases.

> **Note**: Both test files use `from <module> import *`, which will execute any top-level code in the imported module. For example, `main_test.py` will trigger the `main()` function in `main.py` as a side effect.

---

## Exercise Reference

### `main.py` -- Multi-Exercise File

The largest file in the project (225 lines), containing seven classes:

| Class | Description | Key Methods |
|---|---|---|
| **Soldier** | Basic unit with health, armor, weapons | `get_speed()`, `take_damage(damage, multiplier)` |
| **Archer** | Ranged unit with arrows | `shoot(target)`, `get_status()` |
| **Wall** | Defensive structure | `fortify()`, `get_cost()` |
| **Wizard** | Encapsulated magic user (name-mangled `__stamina`, `__intelligence`) | `get_fireballed(damage)`, `drink_mana_potion(potion_mana)` |
| **Dragon** | Element-based damage dealer | `get_breath_damage()` |
| **Brawler** | Fighter with computed `power` attribute | Used with `fight()` function |
| **Human** | Fully encapsulated unit with positional movement | `move_right/left/up/down()`, `sprint_right/left/up/down()` |

### `hero_childs.py` -- Hero Hierarchy

```
Hero (base: __name, __health)
├── Archer (adds __num_arrows, shoot)
└── Wizard (adds __mana, cast)
```

### `crossbowman_unit.py` -- Three-Level Inheritance

```
Human (base: __name)
└── Archer (adds __num_arrows, use_arrows)
    └── Crossbowman (adds triple_shot)
```

### `hit_box.py` -- Collision Detection

```
Unit (base: name, pos_x, pos_y, in_area)
├── Dragon (adds fire_range, hit_box Rectangle, overrides in_area)
└── Rectangle (x1, y1, x2, y2, overlaps)
```

### `siege_weapons.py` -- Method Overriding

```
Siege (base: max_speed, efficiency, get_trip_cost, get_cargo_volume)
├── BatteringRam (overrides both methods, adds load_weight, bed_area)
└── Catapult (overrides get_cargo_volume)
```

### `craft_weapons.py` -- Crafting System

```
Bronze + Bronze = Iron
Iron   + Iron   = Steel
All others     → ValueError("cannot craft")
```

### `card_game_plus.py` / `practice.py` -- Card Comparison

```
Card (rank, suit, comparison operators)
Round (abstract base)
├── HighCardRound (higher card wins)
└── LowCardRound (lower card wins)
```

### `library_system.py` -- Book Management

```
Book (title, author)
Library (name, books[])
  ├── add_book(book)
  ├── remove_book(book)
  └── search_books(search_string)  # case-insensitive
```

---

## Known Issues

- `main.py` contains incomplete class instantiations (`Soldier()`, `Wall()`, `Soldier.take_damage(2)`) at module level that will raise `TypeError` at runtime. These appear to be leftover code from incremental development.
- `practice.py` and `card_game_plus.py` are identical files -- likely a duplication artifact from the course platform.
- `dragon_fight.py` and `hit_box.py` have inconsistent `in_area` parameter ordering (`x1, x2, y1, y2` vs `x1, y1, x2, y2`).

---

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m "Add amazing feature"`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

When adding new exercises, keep each file self-contained and follow the existing naming convention (snake_case with a descriptive name).


