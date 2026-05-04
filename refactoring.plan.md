# Light Refactoring Plan for Moving Squares

## Overview
The project is a single-file Pygame application that creates moving squares on the screen and updates their behavior in a game loop. It uses a `Square` dataclass, initializes Pygame, creates square objects, handles events, updates square positions and velocities, draws squares, and quits cleanly.

The code works correctly, but it can be improved by making responsibilities clearer, reducing duplicated logic, and making the game loop structure easier to follow for beginner readers.

## Refactoring Goals
- Improve readability by clarifying function responsibilities.
- Reduce duplicated logic in movement and collision handling.
- Strengthen naming for important concepts like velocity, wall collision, and neighbor search.
- Keep the single-file structure intact while making each block easier to understand.
- Preserve behavior exactly while adding helpful comments for learners.

## Step-by-Step Refactoring Plan

1. Separate creation of squares from the main loop.
   - Keep `create_squares()` as the single function responsible for initial square setup.
   - Ensure the function returns a list of `Square` objects and does not manage any game loop state.
   - Add an inline comment in the final code explaining that this isolates initialization logic from runtime updates.

2. Rename `handle_events()` to `check_quit_event()` or similar if needed.
   - The current return value is a boolean that only signals quit.
   - Update the name and add a small comment explaining that the function scans events and returns whether the user closed the window.
   - This makes the function purpose explicit for students.

3. Extract wall collision logic into a helper function.
   - Create a new function like `handle_wall_collision(square: Square) -> None` that contains left/right and top/bottom bounce rules.
   - In `update_squares()`, call this helper after position updates.
   - Add inline comments in the final code explaining why moving wall collision to a separate helper improves clarity and avoids repeated logic.

4. Extract fleeing behavior into a helper function.
   - Create a helper like `update_fleeing_behavior(square: Square, squares: List[Square]) -> None` that finds the closest larger square and updates velocity.
   - Keep the logic for distance calculation and direction normalization inside that function.
   - Add comments in the final code explaining that this isolates the emergent behavior from the generic update loop.

5. Simplify `update_squares()` by moving specific concerns to helpers.
   - After extracting wall collision and fleeing behavior, the `update_squares()` function should read as: determine fleeing behavior, apply velocity, add jitter, then resolve collisions.
   - Keep the function body short and sequential.
   - Add a comment describing the update sequence in plain language.

6. Add a small helper for random jitter.
   - Create a helper named `apply_random_jitter(square: Square) -> None` or inline a comment explaining the jitter step.
   - This makes the intent of `random.randint(-1, 1)` obvious to a beginner.

7. Add a top-level comment block or brief docstring for the main game loop.
   - In the `main()` function, add a short comment that explains the four stages of each loop iteration: event handling, update, draw, tick.
   - This reinforces the standard game loop pattern for students.

8. Check naming and constants.
   - Ensure constant names like `SQUARE_COUNT`, `MIN_SQUARE_SIZE`, `MAX_SQUARE_SIZE`, `FPS`, `SCREEN_WIDTH`, and `SCREEN_HEIGHT` are grouped and easy to read.
   - If any constant names should be split into a small block with a comment, do so.
   - Keep any final comments concise and beginner-friendly.

## Final Output Requirements (Mandatory)
- The final output must contain only the refactored code.
- The final code must preserve the current behavior exactly.
- Inline comments must explain:
  - What changed in each extracted helper or renamed function.
  - Why the change improves readability or maintainability.
  - Relevant beginner-friendly programming concepts such as separation of concerns and function responsibility.
- Keep comments concise and directly tied to the code around them.

## Key Concepts for Students
- Separation of concerns: one function does one job.
- Helper functions: break complex logic into named pieces.
- Code readability: short, clear functions are easier to understand than long blocks.
- Game loop structure: handle input, update state, draw frame, control timing.
- Collision and movement logic: update position, then correct boundaries.

## Safety Notes
- Do not change the game behavior or output style.
- Test the application after each small refactoring step if possible.
- Preserve the order of update steps so position, jitter, and collision handling behave the same.
- Keep the single-file structure rather than splitting into new modules for this light refactoring.
