# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
Pixels Illuminate 

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| Tashvi Shukla | Coding | Electronics | Previous coding knowledge |

## 1.3 Project Title
IRL Block Blast 

## 1.4 One-Line Pitch
A physical, LED-powered recreation of the Block Blast puzzle game, controlled by real buttons and played on a glowing 8×8 matrix.

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
IRL Block Blast is a tangible, hardware-based reimagining of the popular mobile game Block Blast. The game runs on an ESP32 microcontroller and is displayed on an 8×8 LED matrix, where colourful blocks accumulate as the player places them one by one. A separate 5×5 LED matrix acts as a live preview window, showing the next block in white before it is placed. The player uses a five-button controller for directions (up, down, left, right, place) to position and drop each block onto the board. An LCD screen tracks the score in real time, and a NeoPixel ring lights up green when a line is cleared and red when the game ends.
The experience is satisfying in the same way the original mobile game is. There is a quiet pleasure in slotting a block perfectly into a gap and watching a full row or column vanish in a flash of light. What makes this version special is that it is entirely physical, completely replacing the need for a phone with the glow of the LEDs, the click of the buttons, and the tactile feedback of a real controller. It reactivates nostalgia, reminiscent of the times when video games used to be physical. 

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
The experience is a single-player puzzle game that rewards spatial thinking and forward strategy. The player must look at the incoming block on the preview matrix and decide where it fits best on the board, while also considering what the future turns could look like. The player should feel a sense of focus and flow while playing, punctuated by bursts of satisfaction when a line clears and the board opens up. The visual feedback makes every successful clear feel rewarding rather than silent. The moment the game ends, the red flash and the final score on the LCD create a natural desire to beat the number next time. Someone would want to try it again because puzzle games like this are inherently "one more go" experiences. One always believes they can beat the number the next time they play and the glowing hardware certainly makes it visually appealing to pick up and play again.

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
I am designing this project as if I am a small creative studio making a physical game for mostly teenagers but also mixed audiences.

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| App | Block Blast | Core logic of gameplay of placing blocks, clearing full lines and columns, game over when no space remains |
| Board game/ Toy | Tetris | The idea that a falling-block puzzle can be endlessly replayable and deeply satisfying in a tactile form |
| `[Toy / Board game / App / Video / Website / Object]` | `[Link or title]` | `[What did you learn or borrow?]` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
While Block Blast already exists as a polished mobile app, no one has physically built it as an LED matrix game with real button controls. The aim is to simulate a retro video game controller, to build on the factor of nostalgia and offline connection. The project's originality lies in the translation from screen to hardware with the 5×5 preview matrix as a separate physical display, the NeoPixel ring as an expressive status indicator, and the use of colourful individually-addressable LEDs that make each player's board state look visually unique. It is not just a copy of the game but a reimagining of what that game feels like when you can hold it, press real buttons, and watch light physically change in front of you.

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
preview block → position → place → clear lines → score → repeat → game over

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | Anyone who wants to go back to a simpler time, disconnect from their phone or just enjoy a game of simple strategy |
| Age range | 10 years and above |
| Solo or multiplayer | Solo |
| Expected duration of one round | Anywhere from 3 - 10 minutes on basis of skill |
| What should the player feel? | Focused and competitive while playing, satisfied when game ends |
| Is explanation required before use? | Minimal, most people are aware of the game, and its quite self explanatory otherwise |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `[How does the player first encounter it?]`
2. **Start:** The game is already running in idle/start state. The player presses any button or the Place button to begin.
3. **First Action:** A white block shape appears on the 5×5 preview matrix. The player presses the directional buttons to move the cursor (ghost block) around the 8×8 board to choose a placement position.
4. **Main Interaction:** The player continuously receives new blocks on the preview matrix, decides where they fit best on the board, navigates the cursor, and presses Place to lock them in. The board fills up gradually.
5. **System Response:** Each placed block lights up in a random colour on the 8×8 matrix. When a full row or column is completed, it instantly clears, the NeoPixel ring flashes green, and the LCD score updates. The preview matrix immediately shows the next block.
6. **Win / Lose / End Condition:** The game ends when the current block cannot be placed anywhere on the board. The NeoPixel ring flashes red, the LCD displays the final score on row 2.
7. **Reset:** After a 15-second display of the final score, the board clears and a new game begins automatically.

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- The player must place the block shown on the 5×5 preview matrix somewhere on the 8×8 board — they cannot skip or discard a block.
- Blocks cannot overlap existing placed blocks or go outside the board boundary.
- Placing any block scores 1 point.
- Completing a full row or full column (all 8 cells filled) clears that line and scores 10 points per line cleared.
- Multiple rows and columns can be cleared in a single placement — all are cleared simultaneously and each scores 10 points.
- The game ends when no position on the board can fit the current block.

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `The 8x8 LED matrix correctly displays placed blocks in colour and updates in real time`
- [ ] `The 5×5 preview region on the second matrix correctly shows the upcoming block in white`
- [ ] `All five buttons respond correctly to the input`
- [ ] `Clearing lines works smoothly and in sync with the flash of the green LED`
- [ ] `The game correctly detects when no more placement is possible, triggering the red LED and clearing the whole board`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
A working version where the player can place blocks on the 8×8 matrix using the five buttons, lines clear when completed and the game ends and resets correctly. The 5×5 preview matrix, LCD screen and NeoPixel ring are part of the minimum viable version since they are central to the designed experience.

## 5.3 Stretch Features
What features are nice to have but not essential?

- A high score that persists across resets, stored in the ESP32's non-volatile memory and shown on the LCD at game over
- A difficulty or speed mode where a time limit per placement is enforced, adding pressure
- Sound effects using a small buzzer
  
---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [ ] Electronics-based
- [ ] Mechanical
- [ ] Sensor-based
- [ ] App-connected
- [ ] Motorized
- [ ] Sound-based
- [ ] Light-based
- [ ] Screen/UI-based
- [ ] Fabricated structure
- [ ] Game logic based
- [ ] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
Input: Five tactile buttons for different directions (up, down, left, right and place) are wired to the ESP32 GPIO, using the PULL_DOWN configuration.
Processing: An ESP32 microcontroller running MicroPython executes all game logic including block selection, cursor movement, collision detection, line clearing, score tracking, and game over detection. The board state is stored as an 8×8 Python list where each cell is either empty or filled. 
Output: An 8×8 NeoPixel matrix displays the live game board. A second 8×8 matrix displays the upcoming block in white in its bottom-right 5×5 region only (first 3 rows and columns are unused). A green LED flashes when a line is cleared. A red LED flashes when the game ends.
Physical structure: 
App interaction: NA

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| Up button | Input | Moves cursor up |
| Down button | Input | Moves cursor down |
| Left button | Input | Moves cursor left |
| Right button | Input | Moves cursor right |
| Place button | Input | To place the block on the board in a final position |
| ESP32 | Processing | Controls the whole game, runs the code |
| 8x8 LED Matrix | Output | Displays the board state to play the game on|
| 8x8 LED Matrix | Output | Displays a preview of the next block to come |
| Green LED | Output | Flashes thrice when a line clears |
| Red LED | Output | Flashes thrice when the game is over |
| `[Mechanical Assembly]` | Physical Action | `[Describe]` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[Write here]` |
| Width | `[Write here]` |
| Height | `[Write here]` |
| Estimated weight | `[Write here]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [Not applicable] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
NA

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
NA

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
NA

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
NA

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| ESP32 | 1 | Main controller |
| 8x8 Neopixel Matrix | 2 | One is used for displaying the real game board, while one is used for previewing the upcoming blocks |
| Tactile push buttons | 5 | Up, Down, Left, Right, Place- control the direction of the block on board |
| Green LED | 1 | Indicator of line clearing |
| Red LED | 1 | Indicator of game ending |
| Resistor | 2 | Data line protection for both matrices |
| External 5V power supply | 1 | Powers breadboard |


## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
Both matrices connect to the ESP32 via GPIO 13 and GPIO 32 respectively, each through a Ω resistor on the data line. Both matrices and the ESP32 are powered from an external 5V supply. The ESP32 receives 5V through its VIN pin, and the matrices receive 5V directly through their V+ pins. All grounds are tied together on a common rail. The five buttons connect between their respective GPIO pins and 3.3V, using internal PULL_DOWN in code. The green LED connects to GPIO 27 and GND. The red LED connects to GPIO 4 and GND.

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | External 5V adapter |
| Voltage required |  5V for both matrices and ESP32; ESP32 onboard regulator steps down to 3.3V internally for all GPIO logic |
| Current concerns | Overheating of ESP32 due to connection between VIN and 5V |
| Safety concerns | Overheating of ESP32 due to connection between VIN and 5V |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| MicroPython | Firmware language on ESP32 |
| Thonny IDE | Code upload |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
Startup: Both matrices are cleared. A 1-second delay flushes any startup noise. All debounce timers reset. A random block loads into the preview matrix in white. The game board stays dark.
Input handling: All five buttons are polled every 30ms. Each press is validated against a 250ms debounce timer per button. 
Block pickup: When any directional button is pressed and no block is active, the current block transfers from preview to board at the first valid free position. The next block immediately appears in the preview. The ghost block that appears on the board is in white.
Cursor movement: Directional buttons move the cursor within board boundaries.
Collision detection: The white cursor moves freely over existing coloured blocks visually. The Place button only locks the block in if there is no overlap with existing blocks and no out-of-bounds cells.
Placement: On valid placement, the block appears on the board in a random colour. Score increments by 1. Line clear check runs immediately.
Line clearing: All completed rows and columns are identified and cleared simultaneously as score increments by 10 per line. Green LED flashes thrice.
Game over: After each placement, all 8×8 positions are scanned for any valid placement of the next block. If none exists, red LED flashes thrice, both matrices clear. There is a 3-second pause before game restarts.
Reset: run_game() calls itself recursively, reinitialising all state variables cleanly.

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[Upload image and link here]`

## 10.4 Pseudocode


START
  clear both matrices
  wait 1 second
  reset all debounce timers
  pick random cur_block, next_block
  show cur_block in preview (white)
  block_active = False

LOOP
  IF block_active is False:
    IF any direction button pressed:
      find first free position on board
      IF no free position: GAME OVER
      set cursor to free position
      block_active = True
      show next_block in preview immediately
      draw board with white cursor ghost

  IF block_active is True:
    read buttons
    IF up/down/left/right pressed:
      calculate new cursor position within bounds
      IF position changed: redraw board with cursor
    IF place pressed:
      IF block_fits at cursor:
        write block to board in current colour
        check and clear lines
        IF lines cleared: flash green LED
        load next_block as cur_block
        pick new next_block
        block_active = False
        IF no valid position for cur_block: GAME OVER
        show cur_block in preview
        redraw board

  GAME OVER:
    flash red LED
    clear both matrices
    wait 3 seconds
    restart


---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
NA

## 11.3 App Features

| Feature | Purpose |
|---|---|
NA

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
NA

## 11.5 App Screen Flow

NA

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| ESP32 | 1 | Yes | No | 0 | Spec | Micropython game logic is easier to control |
| LED Matrix | 2 | No | Yes | 299 x 2 | Spec | To create a playing board for the game, as well as a preview board to show upcoming pieces |
| Tactile push buttons | 5 | Yes | No | 0 | Spec | To simulate the nostalgic feeling of playing on old video game consoles |
| Breadboard | 1 | Yes | No | 0 | Spec | Easier connections between power supply, ESP32 and components |
| Red LED | 1 | Yes | No | 0 | Spec | Signal for game ending |
| Green LED | 1 | Yes | No | 0 | Spec | Signals line clearing |
| Resistor | 2 | Yes | No | 0 | Spec | Reduce current flow |
| Jumper wires | Multiple | Yes | No | 0 | Spec | Forming connections between components |
| Power supply | 1 | Yes | No | 0 | Spec | Provide more power to ESP32 connections |
| LCD screen | 1 | No | Yes | 220 | Spec | To display score |
| i2c module | 1 | No | Yes | 150 | Spec | To display score |
| MDF board | 1 | No | No | 0 | Material | To make the physical model viable |
| Cardboard | 1 | No | No | 0 | Material | To make the physical model viable |
| Tape | 1 | No | No | 0 | Material | To make the physical model viable |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
WS2812B matrices were chosen because they are individually addressable, require only a single data wire each, and are available in pre-assembled 8×8 panels — making physical setup clean and reliable. The ESP32 was chosen over Arduino because MicroPython makes the game logic far easier to write and debug, and its processing speed handles real-time LED updates without issue. Tactile buttons were chosen over a joystick module because the game only needs discrete directional inputs and individual coloured buttons better simulate the feel of a retro game controller. Simple green and red LEDs were used for the status indicators because they are simpler to wire and use less current. MDF was chosen over cardboard for the physical base because it is rigid, flat, and will not warp under the weight of the components during a showcase.

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| LED matrix | The board for the whole game | `[Link]` | 13th April | Recieved |
| LCD screen | To display score | `[Link]` | 18th April | Recieved (faulty) |
| I2C module | To display score | `[Link]` | 18th April | Recieved (late) |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | 970 |
| Mechanical parts | 0 |
| Fabrication materials | 0 |
| Purchased extras | 0 |
| Contingency | 100 |
| **Total** | 1070 |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
NA

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
NA - working alone

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
NA

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
NA

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [ ] Idea finalized
- [ ] Core interaction decided
- [ ] Sketches made
- [ ] BOM completed
- [ ] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | Finalise concept, complete BOM, identify purchases| Project concept finalised, all components identified, initial wiring planned | Decided to use two 8×8 matrices| Order parts, begin wiring plan |
| Week 2 | Test all components, resolve any hardware issues | All components individually tested. Power and signal issues discovered and resolved. Matrix orientation confirmed. | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Write here]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Method]` | `[What counts as success?]` |
| `[Mechanism movement]` | `[Method]` | `[What counts as success?]` |
| `[Sensor behavior]` | `[Method]` | `[What counts as success?]` |
| `[App communication]` | `[Method]` | `[What counts as success?]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Method]` |
| Is the interaction satisfying? | `[Method]` |
| Do players want another turn? | `[Method]` |
| Is the challenge balanced? | `[Method]` |
| Is the response clear and immediate? | `[Method]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[Write here]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Date]` | `[Describe]` | `[Reason]` |
| `v2` | `[Date]` | `[Describe]` | `[Reason]` |
| `v3` | `[Date]` | `[Describe]` | `[Reason]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
