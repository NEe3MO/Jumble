# Guess the Word

A simple web game for guessing words and solving math questions.

## Preview

![Project preview](preview.png)

## Run Locally

1. Open `index.html` in your browser.
2. For reliable JSON loading, run a local server (for example `python3 -m http.server`).

## Structure

- `index.html` - main game page
- `data/` - questions and difficulty sets
- `images/` - background images
- `Roboto/` - fonts
- `background.mp3`, `correct.mp3` - audio files


 ## How the Game Works

  The game loads question sets from JSON files in the `data/` folder and shows them in 3 difficulty levels:

  - Easy
  - Medium
  - Hard


  Each question has this format:

  ```json
  {
    "q": "Question text",
    "a": "Correct answer"
  }

  - q = question shown to the player
  - a = correct answer (string is recommended)

  In word mode, letters are revealed over time.
  In math mode, math expressions are shown and scored with the same system.

  ```

  ## Game Modes

  - Jumble: answer letters are shuffled, and the player must guess the original answer.
  - Math: loads math question files (Math_easy, Math_medium, Math_hard).

  You can switch modes from the Game Modes panel in the UI.

  ## Scoring System

  Score is based on:

  - response speed
  - revealed letters (fewer reveals = more points)
  - current difficulty (higher difficulty = multiplier)
  - combo streak (consecutive correct answers)
  

  Main scoring ideas:

  - faster answer => higher score
  - no revealed letters => perfect bonus
  - wrong/missed question => combo reset

  ## Add Your Own Questions (Custom JSON)

  1. Open the data/ folder.
  2. Create or edit one of these files:
      - Qe_en.json (easy)
      - Qm_en.json (medium)
      - Qh_en.json (hard)
  3. Keep valid JSON array format.
  4. Each item must contain:
      - "q" (question)
      - "a" (answer)
  5. Save and reload the page (use a local server for best results).

  Example:

  [
    { "q": "Capital of France", "a": "Paris" },
    { "q": "Largest planet", "a": "Jupiter" }
  ]

  ## Add Your Own Math Sets

  Math mode loads:

  - Math_easy.json
  - Math_medium.json
  - Math_hard.json

  Use the same object structure:

  [
    { "q": "12 + 7", "a": "19" },
    { "q": "9 * 8", "a": "72" }
  ]

  ## Local Development

  For proper JSON loading, run a local server:

  python3 -m http.server

  Then open:

  - http://localhost:8000

  ## Troubleshooting

  - Questions not loading: check JSON syntax (missing comma/bracket is the most common issue).
  - Wrong answers not accepted: answer matching is exact (case-insensitive in current logic).
  - Assets missing: verify file paths in index.html and make sure files exist.


## Support Development

If you enjoy using EROS VAULT and want to help keep the project going,
you are welcome to support development with a small crypto contribution.

- Bitcoin (BTC): `bc1qfg0w2ujx743k8nrgxux09dt8rpgcketh0h4ryv`
- Ethereum (ETH): `0x128460f95956c755d09695ab5c5d46262f8b2ae6`
- Solana (SOL): `J7GyhqPCuotpw43qLwT832455mJrWgKcAGfh4i8TN2vc`

Every contribution is appreciated, but absolutely optional. Your support helps maintain and improve the vault. Thank you!
