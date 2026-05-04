# Architecture Documentation

This document provides an overview of the architecture of the Moving Squares Pygame application.

## Dependency Graph of Modules

The application consists of a single Python file `main.py` that depends on several external libraries and standard modules.

```mermaid
graph TD;
    A["main.py"] --> B["pygame"]
    A --> C["random"]
    A --> D["math"]
    A --> E["dataclasses"]
    A --> F["typing"]
```

## High-Level System/Runtime Flow Graph

The application follows a standard game loop structure: initialization, main loop with event handling, updates, and rendering, followed by cleanup.

```mermaid
flowchart TD;
    A["Start"] --> B["Initialize Pygame"]
    B --> C["Create Squares"]
    C --> D["Game Loop"]
    D --> E["Handle Events"]
    E --> F["Update Squares"]
    F --> G["Draw Squares"]
    G --> H["Tick Clock"]
    H --> D
    E --> I["Quit"]
    I --> J["End"]
```

## Function-Level Call Graph

The main function orchestrates the application by calling initialization and loop functions. Update and draw functions handle the core logic.

```mermaid
graph TD;
    A["main()"] --> B["initialize_pygame()"]
    A --> C["create_squares()"]
    A --> D["handle_events()"]
    A --> E["update_squares()"]
    A --> F["draw_squares()"]
    E --> G["math.hypot()"]
    E --> H["random.randint()"]
```

## Full Sequence Diagram for Primary Execution Path

The sequence diagram shows the flow from startup through the game loop until termination.

```mermaid
sequenceDiagram
    participant M as "Main"
    participant P as "Pygame"
    participant S as "Squares"

    M->>P: initialize_pygame()
    M->>S: create_squares()
    loop Game Loop
        M->>M: handle_events()
        alt Quit Event
            M->>P: pygame.quit()
        else Continue
            M->>S: update_squares()
            M->>P: draw_squares()
            M->>P: clock.tick()
        end
    end
```</content>
<parameter name="filePath">/Users/saintangegirija/Documents/lab8-pygame/docs/architecture.md