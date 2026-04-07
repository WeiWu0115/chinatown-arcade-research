# Chinatown ARcade: Project Description & Research Overview

## Project Background

Chinatown ARcade is an AR (Augmented Reality) location-based experience developed by WanderLens Lab, set in Manhattan's Chinatown, New York City. The project uses Snap Spectacles AR glasses to create an interactive exploration experience on Doyers Street and Pell Street — one of the oldest areas in NYC's Chinatown. Participants wear AR glasses and walk through the real streetscape, using hand gestures to capture visual clues, collect 3D virtual artifacts, and piece together stories tied to the neighborhood's history.

The project originated from a series of XR hackathons, including MIT Reality Hack (2024, 2025), ASU ReMIX, StanfordXR Immerse the Bay, GTXR, and Snap AR events. It was developed by a five-person core team: Zihao Zhang (Team Lead, Columbia University GSAPP), Hongming Li (Developer Lead), Zoe Wang (3D Designer), Annie Hu (Marketing Lead), and Dei Deng (Narrative Researcher). WanderLens Lab operates two product lines: Grand Tour XR (an online guided tour platform) and Chinatown ARcade (the on-site AR experience).

## The Experience

Participants are assigned a character role — such as a reporter, a police officer, a chef, or a gangster — and given a physical postcard and map. Wearing Snap Spectacles, they navigate the Chinatown streets to find specific real-world objects (e.g., a street lamp, a sign, a statue). Using a hand-gesture "screenshot" motion, they capture these objects through the AR glasses, triggering AI-powered responses: 3D models appear and can be placed onto a virtual postcard, Chinese characters are translated in real-time, and contextual information about the location is provided.

The interaction is structured as a scavenger hunt across multiple stops along the street. A light beam system is intended to guide participants between stops. The experience currently lasts approximately 10 minutes, with the team developing a longer version with deeper narrative content.

The team has also developed merchandise tied to the experience, including a dumpling-shaped plush toy (13.5cm, first batch 200-500 units), a Chinatown NYC metal bookmark/light catcher magnet, and a pop-up book featuring stylized Chinatown architecture.

## Research: What We Did

### Data Collection

We conducted semi-structured video interviews with participants immediately after they completed the Chinatown ARcade experience. A total of 22 video recordings were collected across four testing rounds:

| Round | Date | Files |
|-------|------|-------|
| Round 1 | 2025-09-15 | P05a, P05b, P06 |
| Round 2 | 2025-11-07 | P07 |
| Round 3 | 2025-11-12 | P08a, G1 |
| Round 4 | 2025-11-19 | P08b, G2a, G2b |
| Undated | Various | P01, P02, P03, P04, P09, P10, P11, P12, P13, P14, P15, P16, P17 |

Interviews included both individual (17 sessions) and group (2 group sessions with 5-6 speakers) formats, yielding **23 unique participants** in total. Participants ranged from XR industry professionals (39%), students and academics (22%), general tech users (26%), media/journalists (9%), to investors (4%).

Interview questions covered: overall experience feedback, specific likes and dislikes during gameplay, suggestions for improvement, willingness to pay, souvenir preferences, and general comments about the project and the Chinatown neighborhood.

### Data Processing

All 22 video files were transcribed using OpenAI Whisper (medium model) with English language setting. Transcriptions were output in both plain text (.txt) and timestamped JSON (.json) formats. All files were then anonymized (P01-P17 for individuals, G1a-c and G2a-c for group interview speakers), with a confidential key maintained separately. Interviews of the same participant across multiple recordings were merged (P05: two video files; P08: two interviews on different dates).

### Analysis: Grounded Theory Approach

We conducted a full Grounded Theory analysis (Strauss & Corbin) in three stages:

**Stage 1 — Open Coding**: Line-by-line and segment-by-segment coding of all 22 transcripts, generating 163 initial codes across 12 categories. Codes were grounded in participants' own language (in-vivo codes) and tagged with participant identifiers. The 12 categories are: (1) Interaction & Gesture, (2) Navigation & Wayfinding, (3) Onboarding & Instructions, (4) Narrative & Storytelling, (5) Hardware & Comfort, (6) Embodiment & Presence, (7) Safety & Environment, (8) Monetization & Pricing, (9) Souvenirs & Merchandise, (10) Cultural Significance & Community, (11) Expert/Industry Perspectives, (12) Promotional Materials & Perception.

**Stage 2 — Axial Coding**: Open codes were organized into 6 higher-level categories with relationships mapped using Strauss & Corbin's paradigm model (causal conditions → context → strategies → consequences): (A) Embodied Interaction Quality, (B) Spatial Navigation & Discovery, (C) Narrative Depth & Meaning-Making, (D) Social-Material Ecology, (E) Commercial Viability & Scaling, (F) Technology as Cultural Bridge.

**Stage 3 — Selective Coding**: A core category was identified — **"Embodied Cultural Discovery Through Augmented Perception"** — supported by five theoretical propositions:

1. Photography-as-interaction creates embodied agency, but this agency is fragile when gesture feedback is absent.
2. Navigation requires progressive disclosure — a balance between being guided enough to progress and lost enough to discover.
3. Narrative is the multiplier that transforms the experience from a "scavenger hunt" (how users currently perceive it) into a "City Theater" (the design intent).
4. The experience extends beyond the glasses, encompassing pre-experience expectations (video/marketing), physical artifacts (postcard, map), and post-experience engagement (souvenirs, local dining).
5. Commercial viability is more likely through B2B partnerships (tourism boards, local businesses, educational institutions) than direct B2C ticket sales alone.

### Cross-Analysis: Presentation Deck vs. User Reality

We additionally compared the project's presentation deck (presented at Sichuan Fine Arts Academy, April 1, 2026) against the interview data to identify gaps between design intent and user perception. Four key misalignments were identified:

1. **Merchandise mismatch**: The deck features plush toys, metal bookmarks, and pop-up books, but users expressed stronger demand for functional rewards (real food experiences, vendor discount cards) that were not represented in the deck.
2. **Mental model gap**: The deck positions the experience as "City Theater" (immersive dramaturgy), but users overwhelmingly described it as a "scavenger hunt" or "escape room" — the narrative layer has not yet been successfully conveyed.
3. **Missing team role**: The highest-frequency user pain point (onboarding/UX, 13 mentions) maps to a role that does not exist on the current team.
4. **Participant bias**: 39% of interviewees are XR industry professionals, whose tolerance for hardware limitations and technical bugs is likely higher than the general public target market.

### Outputs

| Output | File | Description |
|--------|------|-------------|
| Anonymization Key | 00_anonymization_key.md | Confidential mapping of P01-P17 + G1/G2 to real names |
| Open Coding Table | 01_open_coding_table.csv | 163 codes × 5 columns (Category, Sub-category, Code, Quote, Participant) |
| Open Coding Detail | 01_open_coding.md | Full narrative coding with quotes and context |
| Axial Coding | 02_axial_coding.md | 6 categories with paradigm model relationships |
| Selective Coding | 03_selective_coding.md | Core category, 5 propositions, design implications |
| Code Frequency | 04_code_frequency_table.md | Frequency counts and WTP summary |
| Fig 1 | fig1_final.png | Code frequency + Top 10 improvements |
| Fig 2 | fig2_final.png | Willingness to Pay distribution |
| Fig 3 | fig3_final.png | Grounded Theory theoretical model |
| Fig 4 | fig4_final.png | PDF deck vs. interview reality (4-panel) |
