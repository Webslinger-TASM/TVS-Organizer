# TVS-Organizer
Automatically organizes your TV Shows/Series files into 'Spider' or 'Bat' formats by renaming and converting between them. This tool ensures your media library remains neatly structured.

## Formats
### Spider Format
```
Name (Year) - SXXEXX - EP_Name
```

### Bat Format
```
Name (Year) SXXEXX (EP_Name)
```

## Features

1. **Renames Files to Spider and Bat Formats:**
    - Automatically renames files to Spider or Bat format.
    - Automatically converts files to Spider or Bat format.

2. **Sorts Files:**
    - Organizes files into a structured directory based on the show name, year, and season.

### Output Example

- Example directory structure, season 1 as Spider Format and season 2 as Bat Format:
  - Note that some choices are optional, like: Name and Year in episode's name
    
    ```
    Spider-Man (1994-1998)
    |
    | - Spider-Man (1994) - Season 01
    |   | - Spider-Man (1994) - S01E01 - Night of the Lizard
    |   |   | - Spider-Man (1994) - S01E01 - Night of the Lizard.mp4
    |   |   | - Spider-Man (1994) - S01E01 - Night of the Lizard.srt
    |
    | - Spider-Man (95-96) - Season 02
    |   | - Spider-Man (95-96) S02E01 - Neogenic Nightmare Chapter 1 - The Insidious Six
    |   |   | - Spider-Man (95-96) S01E02 (Neogenic Nightmare Chapter 1 - The Insidious Six).mp4
    |   |   | - Spider-Man (95-96) S01E02 (Neogenic Nightmare Chapter 1 - The Insidious Six).srt
    ```

## Requirements

- Python 3.12
- OS Library
