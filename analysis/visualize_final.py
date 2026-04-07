import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches
import numpy as np

matplotlib.rcParams['font.family'] = 'Arial'
matplotlib.rcParams['font.size'] = 11

# Updated participant count: 17 individual (P01-P17) + 5-6 group speakers (G1a-c, G2a-c)
# Total unique: ~23
N_INDIVIDUAL = 17
N_GROUP_SPEAKERS = 6
N_TOTAL = 23

# ============================================================
# FIGURE 1: Gap Analysis + Code Frequency (updated numbering)
# ============================================================
fig1, axes = plt.subplots(1, 2, figsize=(18, 9), gridspec_kw={'width_ratios': [1.1, 1]})
fig1.suptitle('Chinatown ARcade: Grounded Theory Analysis Results (N=23)',
              fontsize=16, fontweight='bold', y=0.98)

# --- Left: Code Frequency ---
ax1 = axes[0]

categories = [
    'Gesture / Interaction',
    'Navigation / Wayfinding',
    'Onboarding / Instructions',
    'Narrative / Story Depth',
    'Pricing / Monetization',
    'Hardware / Comfort',
    'Cultural Heritage Value',
    'Souvenirs / Merch',
    'Business Partnerships',
    'Multiplayer / Social',
    'Safety',
]

# Recounted with new numbering:
# Gesture: P01,P02,P03,P04,P05,P06,P07,P08,P10,P11,P13,P14,P15,P16,P17, G1b,G2a = ~17
# Navigation: P01,P02,P04,P05,P06,P08,P11,P13,P14,P15, G1a,G1c,G2a = ~13
# Onboarding: P01,P03,P05,P06,P07,P08,P11,P14,P15,P16,P17, G1b,G2a = ~13
# Narrative: P02,P03,P06,P08,P11,P14,P15,P17, G1a,G1b,G2b = ~11
# Pricing: P01,P02,P04,P05,P06,P08,P10,P11,P12,P13,P15,P16,P17, G2a,G2b = ~15
# Hardware: P01,P03,P06,P07,P08,P11,P12,P13, G1a,G2a = ~10
# Cultural: P01,P04,P08,P09,P10,P15,P16,P17, G1c,G2b = ~10
# Souvenirs: P08,P14, G1a,G2a,G2b,G2c = ~6
# Business: P04,P08,P10, G2a,G2b = ~5
# Multiplayer: P03,P06, G2a = ~3
# Safety: P01,P14 = ~2

counts = [17, 13, 13, 11, 15, 10, 10, 6, 5, 3, 2]
percentages = [c / N_TOTAL * 100 for c in counts]

colors = [
    '#FF6B6B', '#FF6B6B', '#FF6B6B', '#FFD93D',
    '#4ECDC4', '#FF6B6B', '#4ECDC4', '#4ECDC4',
    '#4ECDC4', '#FFD93D', '#CCCCCC',
]

bars = ax1.barh(range(len(categories)), percentages, color=colors, alpha=0.85,
                edgecolor='white', linewidth=0.5)

for i, (pct, cnt) in enumerate(zip(percentages, counts)):
    ax1.text(pct + 1.5, i, f'{cnt}/23 ({pct:.0f}%)', va='center', fontsize=9)

ax1.set_yticks(range(len(categories)))
ax1.set_yticklabels(categories, fontsize=10)
ax1.set_xlabel('% of Participants Mentioning', fontsize=11)
ax1.set_title('Interview Code Frequency', fontsize=13, fontweight='bold', pad=12)
ax1.set_xlim(0, 100)
ax1.invert_yaxis()
ax1.grid(axis='x', alpha=0.2)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

legend1 = [
    mpatches.Patch(facecolor='#FF6B6B', alpha=0.85, label='Pain Points'),
    mpatches.Patch(facecolor='#FFD93D', alpha=0.85, label='Design Gaps'),
    mpatches.Patch(facecolor='#4ECDC4', alpha=0.85, label='Opportunities'),
]
ax1.legend(handles=legend1, loc='lower right', fontsize=9, framealpha=0.9)

# --- Right: Top Suggested Improvements ---
ax2 = axes[1]

improvements = [
    'Better onboarding /\nin-app instructions',
    'Gesture capture\nfeedback & confirmation',
    'Better navigation /\nwayfinding system',
    'Deeper narrative /\nstoryline continuity',
    'Progressive hint\nsystem (time-based)',
    '3D model placement\nfix (behind photo bug)',
    'Sound / audio\nintegration',
    'Historical visual\noverlay (1900s)',
    'Multiplayer /\nrole intertwining',
    'Restaurant / business\npartnerships',
]

# Recounted mentions
imp_counts = [13, 10, 10, 9, 7, 5, 5, 4, 3, 4]

# Who mentioned (new IDs)
imp_who = [
    'P01,P03,P05,P06,P07,P08,\nP11,P14,P15,P16,P17,G1b,G2a',
    'P01,P02,P05,P06,P08,\nP11,P14,P16,G1b,G2a',
    'P01,P02,P04,P05,P06,P08,\nP13,G1a,G2a,G2b',
    'P02,P03,P06,P08,P14,\nP15,G1a,G1b,G2b',
    'P08,G1a,G2a,P06,P14,P15,G2b',
    'P10,P11,P13,P16,G2a',
    'P06,G1a,G1b,G2a,P15',
    'P15,P17,G2b,G1c',
    'P03,P06,G2a',
    'P04,P08,P10,G2a',
]

bar_colors = plt.cm.RdYlGn_r(np.linspace(0.15, 0.85, len(improvements)))

bars2 = ax2.barh(range(len(improvements)), imp_counts, color=bar_colors, alpha=0.85,
                  edgecolor='white', linewidth=0.5)

for i, cnt in enumerate(imp_counts):
    ax2.text(cnt + 0.2, i, f'{cnt}', va='center', fontsize=10, fontweight='bold')

ax2.set_yticks(range(len(improvements)))
ax2.set_yticklabels(improvements, fontsize=9.5)
ax2.set_xlabel('Number of Mentions', fontsize=11)
ax2.set_title('Top 10 Suggested Improvements (ranked)', fontsize=13, fontweight='bold', pad=12)
ax2.invert_yaxis()
ax2.set_xlim(0, 16)
ax2.grid(axis='x', alpha=0.2)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout(rect=[0, 0.02, 1, 0.95])
plt.savefig('/Users/wu.w4/chinatown-ar-interviews/analysis/fig1_final.png', dpi=200, bbox_inches='tight')
print("Fig 1 saved.")

# ============================================================
# FIGURE 2: Willingness to Pay (updated)
# ============================================================
fig2, ax3 = plt.subplots(figsize=(11, 5.5))

price_ranges = ['$10-15', '$15-20', '$20-25', '$25-30', '$30-40', '$40-50', '$50-100', '$100-200+']
# Recounted with merged participants:
# $10-15: P01, P07 = 2
# $15-20: P04, P05, P11, G2c = 4
# $20-25: P08, P15, P16, G2a, G2b = 5
# $25-30: P02, P17 = 2  (P02 said 25-30 with more content, P17 said $30)
# $30-40: P11 ($30 with more) = 1
# $40-50: P06 (multiplayer $40-50), G2a ($40-50 solid UX) = 2
# $50-100: (none standalone) = 0
# $100-200+: P10 ($150-200 tourism), P17 ($100 combined tour) = 2
# Declined/not asked: P12, P13, P09 = 3

wtp_counts = [2, 4, 5, 2, 1, 2, 0, 2]

bar_colors = ['#BDBDBD', '#BDBDBD', '#4ECDC4', '#4ECDC4', '#FFD93D', '#FFD93D', '#EEEEEE', '#FF6B6B']

bars3 = ax3.bar(price_ranges, wtp_counts, color=bar_colors, alpha=0.85, edgecolor='white', linewidth=1)

for bar, count in zip(bars3, wtp_counts):
    if count > 0:
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
                 str(count), ha='center', va='bottom', fontsize=11, fontweight='bold')

# Who said what (new IDs)
annotations = [
    ('P01, P07', 0),
    ('P04, P05,\nP11, G2c', 1),
    ('P08, P15,\nP16, G2a, G2b', 2),
    ('P02, P17', 3),
    ('P11', 4),
    ('P06, G2a', 5),
    ('', 6),
    ('P10, P17', 7),
]
for text, idx in annotations:
    if text:
        ax3.text(idx, -0.6, text, ha='center', fontsize=7, color='#666', style='italic')

ax3.axvline(x=2.3, color='#D32F2F', linestyle='--', linewidth=1.5, alpha=0.7)
ax3.text(2.5, max(wtp_counts) + 0.3, 'Median: ~$20-25', color='#D32F2F', fontsize=10, fontweight='bold')

ax3.annotate('Current 10-min\nexperience', xy=(1.5, 5.3), fontsize=9, ha='center', color='#555', style='italic')
ax3.annotate('With tour\nintegration', xy=(7, 2.5), fontsize=9, ha='center', color='#555', style='italic')

ax3.set_ylabel('Number of Participants', fontsize=11)
ax3.set_xlabel('Willingness to Pay (USD)', fontsize=11)
ax3.set_title('Willingness to Pay Distribution (N=18 responded out of 23)', fontsize=13, fontweight='bold')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.grid(axis='y', alpha=0.2)
ax3.set_ylim(-1.8, max(wtp_counts) + 1.5)

plt.tight_layout()
plt.savefig('/Users/wu.w4/chinatown-ar-interviews/analysis/fig2_final.png', dpi=200, bbox_inches='tight')
print("Fig 2 saved.")

# ============================================================
# FIGURE 3: Theoretical Model (updated)
# ============================================================
fig3, ax4 = plt.subplots(figsize=(14, 8))
ax4.set_xlim(0, 14)
ax4.set_ylim(0, 10)
ax4.axis('off')
ax4.set_title('Grounded Theory: "Embodied Cultural Discovery Through Augmented Perception" (N=23)',
              fontsize=14, fontweight='bold', pad=20)

def draw_box(ax, x, y, w, h, text, color, fontsize=9, fontweight='normal'):
    rect = matplotlib.patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                                              facecolor=color, edgecolor='#333', linewidth=1.2, alpha=0.9)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize,
            fontweight=fontweight, linespacing=1.3)

def draw_arrow(ax, x1, y1, x2, y2, color='#555'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.8))

# Core category
draw_box(ax4, 3.5, 8.2, 7, 1.2, 'CORE CATEGORY\nEmbodied Cultural Discovery\nThrough Augmented Perception',
         '#5B8DEF', fontsize=11, fontweight='bold')

# Enablers
ax4.text(1.5, 7.5, 'ENABLERS', ha='center', fontsize=11, fontweight='bold', color='#FF6B6B')
draw_box(ax4, 0.2, 6.2, 2.6, 1.1, 'Gesture Reliability\n& Feedback\n(17/23, 74%)', '#FFE0E0')
draw_box(ax4, 0.2, 4.8, 2.6, 1.1, 'Hardware Comfort\n& FOV\n(10/23, 43%)', '#FFE0E0')
draw_box(ax4, 0.2, 3.4, 2.6, 1.1, 'Onboarding\nQuality\n(13/23, 57%)', '#FFE0E0')

# Mediators
ax4.text(7, 7.5, 'MEDIATORS', ha='center', fontsize=11, fontweight='bold', color='#FFB300')
draw_box(ax4, 5.5, 6.2, 3, 1.1, 'Navigation Balance\n(Guided \u2194 Discovery)\n(13/23, 57%)', '#FFF3E0')
draw_box(ax4, 5.5, 4.8, 3, 1.1, 'Narrative Coherence\n(Tasks \u2192 Story Arc)\n(11/23, 48%)', '#FFF3E0')
draw_box(ax4, 5.5, 3.4, 3, 1.1, 'Social-Material\nEcology\n(6/23, 26%)', '#FFF3E0')

# Outcomes
ax4.text(12, 7.5, 'OUTCOMES', ha='center', fontsize=11, fontweight='bold', color='#4ECDC4')
draw_box(ax4, 10.5, 6.2, 3, 1.1, 'Cultural\nUnderstanding\n(10/23, 43%)', '#E0F7FA')
draw_box(ax4, 10.5, 4.8, 3, 1.1, 'Emotional\nConnection\n(10/23, 43%)', '#E0F7FA')
draw_box(ax4, 10.5, 3.4, 3, 1.1, 'Commercial\nViability\n(15/23, 65%)', '#E0F7FA')

# Arrows
draw_arrow(ax4, 2.8, 7.2, 3.5, 8.5, '#FF6B6B')
draw_arrow(ax4, 7, 8.2, 7, 7.5, '#FFB300')
draw_arrow(ax4, 8.5, 6.7, 10.5, 6.7, '#4ECDC4')
draw_arrow(ax4, 8.5, 5.3, 10.5, 5.3, '#4ECDC4')
draw_arrow(ax4, 8.5, 3.9, 10.5, 3.9, '#4ECDC4')
draw_arrow(ax4, 2.8, 5.3, 5.5, 5.3, '#999')
draw_arrow(ax4, 2.8, 3.9, 5.5, 3.9, '#999')

# Propositions
ax4.text(7, 1.8, 'KEY PROPOSITIONS', ha='center', fontsize=11, fontweight='bold')
propositions = [
    'P1: Photography-as-interaction creates embodied agency (but fragile when feedback absent)',
    'P2: Navigation requires progressive disclosure (broad hint \u2192 time delay \u2192 specific cue)',
    'P3: Narrative is the multiplier \u2014 transforms "scavenger hunt" into "City Theater"',
    'P4: Experience extends beyond glasses (video \u2192 onboarding \u2192 play \u2192 souvenir \u2192 dining)',
    'P5: Commercial viability = B2B partnerships (tourism board, local business) > direct B2C',
]
for i, prop in enumerate(propositions):
    ax4.text(7, 1.3 - i * 0.35, prop, ha='center', fontsize=8.5, color='#444')

plt.savefig('/Users/wu.w4/chinatown-ar-interviews/analysis/fig3_final.png', dpi=200, bbox_inches='tight')
print("Fig 3 saved.")

# ============================================================
# FIGURE 4: PDF vs Interviews (updated)
# ============================================================
fig4 = plt.figure(figsize=(20, 14))
gs = fig4.add_gridspec(2, 2, hspace=0.35, wspace=0.3)
fig4.suptitle('PDF Presentation Deck vs. User Interview Reality (N=23)',
              fontsize=17, fontweight='bold', y=0.97)

# --- Panel 1: Merch Gap ---
ax5 = fig4.add_subplot(gs[0, 0])

merch_items = [
    'Real food\n(dumplings, tea)',
    'Vendor discount /\nVIP card',
    'Blind boxes',
    'Keychains of\ncollected items',
    'AR-enabled\npostcard (Web AR)',
    'Digital badge /\nachievement',
    'Plush toys\n(dumpling)',
    'Metal bookmark\n/ magnet',
    'Pop-up book',
]

# Recounted with new IDs
user_demand = [5, 4, 3, 2, 3, 2, 2, 0, 0]
in_pdf = [False, False, True, False, False, False, True, True, True]
bar_colors5 = ['#4ECDC4' if not p else '#FF6B6B' for p in in_pdf]

bars5 = ax5.barh(range(len(merch_items)), user_demand, color=bar_colors5, alpha=0.85,
                  edgecolor='white', linewidth=1)

for i, (demand, pdf) in enumerate(zip(user_demand, in_pdf)):
    label = f'{demand}'
    if pdf:
        label += '  [IN PDF]'
    ax5.text(max(demand, 0) + 0.2, i, label, va='center', fontsize=9,
             fontweight='bold' if pdf else 'normal',
             color='#C62828' if pdf else '#333')

ax5.set_yticks(range(len(merch_items)))
ax5.set_yticklabels(merch_items, fontsize=10)
ax5.set_xlabel('User Demand (# mentions)', fontsize=10)
ax5.set_title('Merchandise: PDF Shows vs. Users Want', fontsize=13, fontweight='bold')
ax5.invert_yaxis()
ax5.set_xlim(0, 8)
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.grid(axis='x', alpha=0.15)

legend5 = [
    mpatches.Patch(color='#4ECDC4', alpha=0.85, label='User wants (NOT in PDF)'),
    mpatches.Patch(color='#FF6B6B', alpha=0.85, label='Shown in PDF deck'),
]
ax5.legend(handles=legend5, loc='lower right', fontsize=9)

# --- Panel 2: Mental Models ---
ax6 = fig4.add_subplot(gs[0, 1])

comparisons = [
    'Scavenger Hunt',
    'Escape Room',
    'Video Game\n(Mario, 1080)',
    'China AR Tourism\n(Xiaohongshu)',
    'Viator City Tour',
    'Tenement Museum',
    'Museum Theater\n/ City Theater',
    'Rock Climbing\nDay Pass',
]
comparison_counts = [5, 3, 3, 2, 2, 1, 1, 1]
# Which who (new IDs)
comp_who = [
    'P01,P08,P15,G1c,G2a',
    'G2a,G2b,P10',
    'G2a,G2b,P14',
    'G1a,G1c',
    'P10',
    'G2b',
    'P03',
    'P15',
]

pdf_aligned = [True, False, False, True, False, False, True, False]
c_colors = ['#5B8DEF' if a else '#BDBDBD' for a in pdf_aligned]

bars6 = ax6.barh(range(len(comparisons)), comparison_counts, color=c_colors, alpha=0.85,
                  edgecolor='white', linewidth=1)

for i, (cnt, who) in enumerate(zip(comparison_counts, comp_who)):
    ax6.text(cnt + 0.15, i, f'{cnt}  ({who})', va='center', fontsize=8)

ax6.set_yticks(range(len(comparisons)))
ax6.set_yticklabels(comparisons, fontsize=10)
ax6.set_xlabel('# Participants Using This Comparison', fontsize=10)
ax6.set_title('User Mental Models: "This is like..."', fontsize=13, fontweight='bold')
ax6.invert_yaxis()
ax6.set_xlim(0, 9)
ax6.spines['top'].set_visible(False)
ax6.spines['right'].set_visible(False)
ax6.grid(axis='x', alpha=0.15)

legend6 = [
    mpatches.Patch(color='#5B8DEF', alpha=0.85, label='Aligns with PDF positioning'),
    mpatches.Patch(color='#BDBDBD', alpha=0.85, label="User's own comparison"),
]
ax6.legend(handles=legend6, loc='lower right', fontsize=9)

ax6.annotate('Users say "scavenger hunt"\nPDF says "City Theater"',
             xy=(5, 0), xytext=(6, 2.5),
             fontsize=9, fontweight='bold', color='#C62828',
             arrowprops=dict(arrowstyle='->', color='#C62828', lw=1.5))

# --- Panel 3: Team Roles vs Pain Points ---
ax7 = fig4.add_subplot(gs[1, 0])

roles = [
    'Developer Lead\n(Hongming Li)',
    'No UX/Onboarding\nrole on team',
    'Narrative Researcher\n(Dei Deng)',
    'Team Lead\n(Zihao Zhang)',
    '3D Designer\n(Zoe Wang)',
    'Marketing Lead\n(Annie Hu)',
]

complaint_counts = [15, 13, 11, 5, 4, 3]
role_colors = ['#FF6B6B', '#E53935', '#FFD54F', '#78909C', '#FFB74D', '#CE93D8']

bars7 = ax7.barh(range(len(roles)), complaint_counts, color=role_colors, alpha=0.85,
                  edgecolor='white', linewidth=1)

for i, cnt in enumerate(complaint_counts):
    ax7.text(cnt + 0.3, i, f'{cnt} mentions', va='center', fontsize=10, fontweight='bold')

ax7.set_yticks(range(len(roles)))
ax7.set_yticklabels(roles, fontsize=10)
ax7.set_xlabel('User Complaints in This Domain', fontsize=10)
ax7.set_title('Team Roles (PDF) vs. User Pain Points', fontsize=13, fontweight='bold')
ax7.invert_yaxis()
ax7.set_xlim(0, 20)
ax7.spines['top'].set_visible(False)
ax7.spines['right'].set_visible(False)
ax7.grid(axis='x', alpha=0.15)

bars7[1].set_edgecolor('#E53935')
bars7[1].set_linewidth(2.5)
ax7.annotate('MISSING ROLE',
             xy=(13, 1), xytext=(17, 0.3),
             fontsize=9, fontweight='bold', color='#C62828',
             arrowprops=dict(arrowstyle='->', color='#C62828', lw=1.5))

# --- Panel 4: Participant Background Distribution ---
ax8 = fig4.add_subplot(gs[1, 1])

bg_labels = [
    'XR Industry\nProfessional',
    'Student /\nAcademic',
    'General\nTech User',
    'Media /\nJournalist',
    'Investor',
]

# Recounted with new IDs:
# XR Pro: P03,P04,P06,P07,P08,P10,P13,P15,G1a = 9
# Student: P02,P05,P11,G1b,G1c = 5
# General: P01,P14,P16,G2a,G2b,G2c = 6
# Media: P09,P17 = 2
# Investor: P12 = 1
bg_counts = [9, 5, 6, 2, 1]
bg_who = [
    'P03,P04,P06,P07,\nP08,P10,P13,P15,G1a',
    'P02,P05,P11,\nG1b,G1c',
    'P01,P14,P16,\nG2a,G2b,G2c',
    'P09,P17',
    'P12',
]

bg_colors = ['#5B8DEF', '#FFD93D', '#4ECDC4', '#CE93D8', '#FF6B6B']

wedges, texts, autotexts = ax8.pie(bg_counts, labels=bg_labels, autopct='%1.0f%%',
                                     colors=bg_colors, startangle=90,
                                     textprops={'fontsize': 10},
                                     pctdistance=0.75)

for t in autotexts:
    t.set_fontweight('bold')
    t.set_fontsize(10)

ax8.set_title('Participant Background Distribution (N=23)', fontsize=13, fontweight='bold')

# Add count text
for i, (count, who) in enumerate(zip(bg_counts, bg_who)):
    pass  # pie chart already has percentages

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig('/Users/wu.w4/chinatown-ar-interviews/analysis/fig4_final.png', dpi=200, bbox_inches='tight')
print("Fig 4 saved.")

print("\nAll final figures saved to ~/chinatown-ar-interviews/analysis/")
