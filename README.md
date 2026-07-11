# Chinatown ARcade — User Research & Analysis
https://chinatown-arcade-research-stxc28bbtyggynvc2p9d53.streamlit.app/
Post-experience interview study for [Chinatown ARcade](https://wanderlenslab.com), an AR location-based experience on Doyers Street and Pell Street, Manhattan's Chinatown, built with Snap Spectacles by WanderLens Lab.

---

## The Project

Chinatown ARcade is a 10-minute scavenger-hunt experience where participants wear AR glasses to walk through real Chinatown streets, capture historical clues via hand-gesture "screenshots," collect 3D virtual artifacts, and piece together stories tied to the neighborhood's history. The project originated from MIT Reality Hack 2024/2025 and has since been shown at ASU ReMIX, StanfordXR Immerse the Bay, GTXR, and Snap AR events.

**Team**: Zihao Zhang (Lead, Columbia GSAPP) · Hongming Li (Dev) · Zoe Wang (3D Design) · Annie Hu (Marketing) · Dei Deng (Narrative Research)

---

## This Repository

This repo contains the interview transcripts, grounded theory analysis, and an interactive Streamlit app for exploring the findings. **Video files and participant identity keys are excluded** for privacy.

### Structure

```
chinatown-arcade-research/
├── transcripts/              # Whisper-transcribed interview texts (anonymized)
│   ├── P01.txt – P17.txt     # Individual participants
│   ├── G1.txt                # Group interview 1 (3 speakers)
│   ├── G2a.txt, G2b.txt      # Group interview 2 (2 speakers)
│   └── *.json                # Timestamped transcripts (same content)
├── analysis/
│   ├── 01_open_coding.md     # Narrative open coding (163 codes, 12 categories)
│   ├── 01_open_coding_table.csv
│   ├── 02_axial_coding.md    # 6 axial categories with paradigm model
│   ├── 03_selective_coding.md # Core category + 5 theoretical propositions
│   ├── 04_code_frequency_table.md
│   ├── 05_project_description.md
│   ├── 06_interview_guide.md
│   ├── 07_chinatown_meaning_analysis.md
│   ├── fig1_final.png        # Code frequency + top improvements
│   ├── fig2_final.png        # Willingness to pay distribution
│   ├── fig3_final.png        # Grounded theory theoretical model
│   └── fig4_final.png        # Presentation deck vs. user reality
├── app.py                    # Streamlit visualization app
├── visualize_final.py        # Script that generated the 4 figures
├── transcribe_all.py         # Whisper transcription script
└── requirements.txt
```

---

## Research Method

**23 participants** across 22 video interviews, conducted on-site in Chinatown immediately after the AR experience (Sep–Nov 2025). Participant backgrounds: XR industry professionals (39%), general tech users (26%), students/academics (22%), media/journalists (9%), investors (4%).

Full **Grounded Theory** analysis (Strauss & Corbin) in three stages:

| Stage | Output | Scale |
|-------|--------|-------|
| Open Coding | 163 initial codes | 12 categories |
| Axial Coding | 6 higher-level categories | Paradigm model (causes → context → strategy → consequences) |
| Selective Coding | 1 core category | 5 theoretical propositions |

**Core Category**: *Embodied Cultural Discovery Through Augmented Perception*

### The 5 Propositions

1. Photography-as-interaction creates embodied agency — but this agency is fragile when gesture feedback is absent
2. Navigation requires progressive disclosure — guided enough to progress, lost enough to discover
3. Narrative is the multiplier that transforms a "scavenger hunt" (user perception) into "City Theater" (design intent)
4. The experience extends beyond the glasses: pre-experience expectations, physical artifacts (postcard, map), and post-experience souvenirs all shape the whole
5. Commercial viability is more likely through B2B (tourism boards, local businesses, schools) than direct B2C ticket sales alone

---

## Key Findings

### Top User Pain Points (by mention frequency)
| Rank | Issue | Mentions |
|------|-------|----------|
| 1 | Onboarding & instructions unclear | 13 |
| 2 | Navigation / light beam guidance | 11 |
| 3 | Gesture recognition inconsistency | 9 |
| 4 | Narrative depth insufficient | 8 |
| 5 | Hardware comfort (weight, FOV) | 6 |

### Willingness to Pay
- Modal range: **$10–20** (most common)
- Upper bound (XR professionals): up to $50
- Median implied price: ~$15

### Deck vs. Reality (4 misalignments)
1. **Merchandise mismatch** — deck shows plush toys; users want functional rewards (discount cards, free food)
2. **Mental model gap** — deck says "City Theater"; users say "scavenger hunt" or "escape room"
3. **Missing role** — the #1 pain point (onboarding/UX) maps to a role that doesn't exist on the current team
4. **Participant bias** — 39% of interviewees are XR professionals whose hardware tolerance is higher than the general public

### What the Project Means to Chinatown (6 dimensions)
| Code | Dimension | Representative Quote |
|------|-----------|----------------------|
| M1 | Making Depth Visible | *"Chinatown has a lot of depth… just walking around you wouldn't be able to notice"* — P01 |
| M2 | Being Seen | *"Really appreciate that people see this and see us"* — P09 |
| M3 | Old Town Rebirth | *"With the new technology, it gives the old town a rebirth chance"* — P17 |
| M4 | Connecting, Not Isolating | *"The right way to let this technology connect people instead of isolating people"* — P15 |
| M5 | Personal Roots | *"I love being in Chinatown, kind of like where my mom grew up"* — P08 |
| M6 | Generational Bridge | *"She started trying out AR at the age of four. I feel like there's a generational gap"* — P17 |

---

## Interactive App

Run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app has 8 pages: Project Overview · Participants · Code Frequency · Willingness to Pay · Theoretical Model · Open Coding Table · Transcript Explorer · Cultural Meaning

---

## Privacy

All participants are anonymized as P01–P17 (individuals) and G1a–c / G2a–b (group sessions). The identity key is excluded from this repository. Video recordings are also excluded.

---

## Citation

If you reference this work:

> Zhang, Z., Li, H., Wang, Z., Hu, A., & Deng, D. (2025–2026). *Chinatown ARcade: Post-Experience Interview Study*. WanderLens Lab. https://github.com/WeiWu0115/chinatown-arcade-research
