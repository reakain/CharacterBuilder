# Random Generators
Python classes for generation of random literary objects/helpers. (IE characters, countries, etc)

These classes primarily use pycorpora for data generation and inflect for data cleanup.

## Usage Example
```
from CharacterGenerator import Character

newCharacter = Character()
newCharacter.build_character()

print(newCharacter.character_bio())
```


## Resources
- [Corpora Project](https://github.com/dariusk/corpora)