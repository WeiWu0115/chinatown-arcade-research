import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
import os
import glob

# ─── Page config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Chinatown ARcade — Research",
    page_icon="🏮",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE = os.path.dirname(__file__)
TRANSCRIPT_DIR = os.path.join(BASE, "transcripts")
ANALYSIS_DIR = os.path.join(BASE, "analysis")

# ─── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://i.imgur.com/placeholder.png", width=60) if False else None
    st.title("🏮 Chinatown ARcade")
    st.caption("Grounded Theory Research · N=23")
    st.divider()
    page = st.radio(
        "Navigate",
        ["Project Overview", "Participants", "Code Frequency", "Willingness to Pay",
         "Theoretical Model", "Open Coding Table", "Transcript Explorer", "Cultural Meaning"],
        label_visibility="collapsed"
    )

# ─── Data ───────────────────────────────────────────────────────────────────

@st.cache_data
def load_transcripts():
    data = {}
    for path in sorted(glob.glob(os.path.join(TRANSCRIPT_DIR, "*.txt"))):
        pid = os.path.splitext(os.path.basename(path))[0]
        with open(path) as f:
            data[pid] = f.read().strip()
    return data

@st.cache_data
def load_coding_table():
    path = os.path.join(ANALYSIS_DIR, "01_open_coding_table.csv")
    return pd.read_csv(path)

TRANSCRIPTS = load_transcripts()
CODING_DF = load_coding_table()

PARTICIPANT_INFO = {
    "P01": {"background": "XR Industry", "role": "Software Engineer, Google"},
    "P02": {"background": "General Tech User", "role": "Participant (police role)"},
    "P03": {"background": "XR Industry", "role": "Product Designer, MIT Reality Hack organizer"},
    "P04": {"background": "XR Industry", "role": "CTO, CustomerXR"},
    "P05a": {"background": "Student / Academic", "role": "Urban Science student, WIU"},
    "P05b": {"background": "Student / Academic", "role": "Urban Science student, WIU (cont.)"},
    "P06": {"background": "XR Industry", "role": "XR Developer, Supernatural"},
    "P07": {"background": "XR Industry", "role": "AR/VR enthusiast"},
    "P08a": {"background": "XR Industry", "role": "XR Professional (Interview 1)"},
    "P08b": {"background": "XR Industry", "role": "XR Professional (Interview 2)"},
    "P09": {"background": "Media / Journalist", "role": "PR & Journalist, NYC"},
    "P10": {"background": "XR Industry", "role": "XR Professional, ex-Meta Reality Labs"},
    "P11": {"background": "Student / Academic", "role": "Architecture Student, Columbia University"},
    "P12": {"background": "Investor", "role": "Investment Industry, researching Snap"},
    "P13": {"background": "General Tech User", "role": "Technology Professional"},
    "P14": {"background": "General Tech User", "role": "UX Designer & Artist"},
    "P15": {"background": "XR Industry", "role": "AR/VR Specialist & Researcher"},
    "P16": {"background": "General Tech User", "role": "Marketing & Consulting, Welcome Chinatown Ambassador"},
    "P17": {"background": "Media / Journalist", "role": "Chinatown Correspondent / Reporter"},
    "G1":  {"background": "XR Industry", "role": "Group: Belgian AR dev + 2 users (2025-11-12)"},
    "G2a": {"background": "General Tech User", "role": "Group: Nov 19 session, part 1"},
    "G2b": {"background": "General Tech User", "role": "Group: Nov 19 session, part 2"},
}

BG_COLORS = {
    "XR Industry": "#5B8DEF",
    "Student / Academic": "#FFD93D",
    "General Tech User": "#4ECDC4",
    "Media / Journalist": "#CE93D8",
    "Investor": "#FF6B6B",
}

# ════════════════════════════════════════════════════════════════════════════
# PAGE: Project Overview
# ════════════════════════════════════════════════════════════════════════════
if page == "Project Overview":
    st.title("🏮 Chinatown ARcade — Research Dashboard")
    st.markdown("""
    **Chinatown ARcade** is an AR location-based experience developed by [WanderLens Lab](https://github.com/WeiWu0115/chinatown-arcade-research),
    set in Manhattan's Chinatown. Using **Snap Spectacles**, participants walk through Doyers Street
    and Pell Street, using hand gestures to capture visual clues, collect 3D virtual artifacts,
    and uncover stories tied to the neighborhood's 1900s history.
    """)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Participants", "23", "P01–P17 + G1/G2")
    col2.metric("Interviews", "22 videos", "4 testing rounds")
    col3.metric("Open Codes", "163", "12 categories")
    col4.metric("Median WTP", "$20–25", "per 10-min session")

    st.divider()

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Core Theory")
        st.info(
            '**"Embodied Cultural Discovery Through Augmented Perception"**\n\n'
            'AR technology, when deployed in a culturally rich urban environment, '
            'transforms passive spectatorship into embodied cultural investigation — '
            'but this transformation is fragile, mediated by interaction quality, '
            'narrative coherence, and social-material conditions.'
        )

        st.subheader("5 Key Propositions")
        propositions = [
            ("P1", "Photography-as-interaction creates embodied agency (but fragile when feedback is absent)"),
            ("P2", "Navigation requires progressive disclosure — broad hint → time delay → specific cue"),
            ("P3", "Narrative is the multiplier — transforms 'scavenger hunt' into 'City Theater'"),
            ("P4", "Experience extends beyond glasses: video → onboarding → play → souvenir → dining"),
            ("P5", "Commercial viability = B2B partnerships (tourism/local business) > direct B2C"),
        ]
        for code, text in propositions:
            st.markdown(f"**{code}** — {text}")

    with col_b:
        st.subheader("Testing Timeline")
        timeline_data = pd.DataFrame([
            dict(Task="Round 1 (P05, P06)", Start="2025-09-15", Finish="2025-09-15", Resource="Testing"),
            dict(Task="Round 2 (P07)", Start="2025-11-07", Finish="2025-11-07", Resource="Testing"),
            dict(Task="Round 3 (P08, G1)", Start="2025-11-12", Finish="2025-11-12", Resource="Testing"),
            dict(Task="Round 4 (P08b, G2)", Start="2025-11-19", Finish="2025-11-19", Resource="Testing"),
            dict(Task="Undated interviews (P01–P04, P09–P17)", Start="2025-09-01", Finish="2025-11-30", Resource="Undated"),
            dict(Task="Grounded Theory Analysis", Start="2026-04-06", Finish="2026-04-07", Resource="Analysis"),
        ])
        fig_tl = px.timeline(timeline_data, x_start="Start", x_end="Finish", y="Task",
                             color="Resource",
                             color_discrete_map={"Testing": "#FF6B6B", "Undated": "#BDBDBD", "Analysis": "#4ECDC4"})
        fig_tl.update_layout(height=280, margin=dict(l=0, r=0, t=10, b=0),
                              showlegend=False, yaxis_title="")
        st.plotly_chart(fig_tl, use_container_width=True)

        st.subheader("Participant Background")
        bg_counts = {"XR Industry": 9, "General Tech User": 6, "Student / Academic": 5,
                     "Media / Journalist": 2, "Investor": 1}
        fig_pie = go.Figure(go.Pie(
            labels=list(bg_counts.keys()),
            values=list(bg_counts.values()),
            marker_colors=[BG_COLORS[k] for k in bg_counts],
            textinfo="label+percent",
            hole=0.35,
        ))
        fig_pie.update_layout(height=260, margin=dict(l=0, r=0, t=10, b=0), showlegend=False)
        st.plotly_chart(fig_pie, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════════
# PAGE: Participants
# ════════════════════════════════════════════════════════════════════════════
elif page == "Participants":
    st.title("👥 Participants (N=23)")
    st.caption("All identities anonymized. Anonymization key kept offline.")

    filter_bg = st.multiselect(
        "Filter by background",
        options=list(BG_COLORS.keys()),
        default=list(BG_COLORS.keys()),
    )

    cols = st.columns(3)
    col_idx = 0
    for pid, info in PARTICIPANT_INFO.items():
        if info["background"] not in filter_bg:
            continue
        color = BG_COLORS.get(info["background"], "#CCCCCC")
        with cols[col_idx % 3]:
            st.markdown(
                f"""<div style="border-left: 4px solid {color}; padding: 8px 12px;
                margin-bottom: 10px; border-radius: 4px; background: #fafafa;">
                <b>{pid}</b><br/>
                <span style="font-size:13px; color:#555">{info['role']}</span><br/>
                <span style="font-size:11px; background:{color}22; color:{color};
                padding:1px 6px; border-radius:10px;">{info['background']}</span>
                </div>""",
                unsafe_allow_html=True
            )
        col_idx += 1

# ════════════════════════════════════════════════════════════════════════════
# PAGE: Code Frequency
# ════════════════════════════════════════════════════════════════════════════
elif page == "Code Frequency":
    st.title("📊 Interview Code Frequency")
    st.caption("Percentage of all 23 participants who mentioned each theme")

    N = 23
    data = {
        "Category": ["Gesture / Interaction", "Pricing / Monetization", "Navigation / Wayfinding",
                      "Onboarding / Instructions", "Narrative / Story Depth", "Hardware / Comfort",
                      "Cultural Heritage Value", "Souvenirs / Merch", "Business Partnerships",
                      "Multiplayer / Social", "Safety"],
        "Count": [17, 15, 13, 13, 11, 10, 10, 6, 5, 3, 2],
        "Type": ["Pain Point", "Opportunity", "Pain Point", "Pain Point", "Design Gap",
                 "Pain Point", "Opportunity", "Opportunity", "Opportunity", "Design Gap", "Minor"],
    }
    df = pd.DataFrame(data)
    df["Pct"] = (df["Count"] / N * 100).round(1)
    df = df.sort_values("Count", ascending=True)

    color_map = {"Pain Point": "#FF6B6B", "Opportunity": "#4ECDC4",
                 "Design Gap": "#FFD93D", "Minor": "#CCCCCC"}

    fig = go.Figure()
    for t, grp in df.groupby("Type"):
        fig.add_trace(go.Bar(
            x=grp["Pct"], y=grp["Category"], orientation="h",
            name=t, marker_color=color_map[t],
            text=[f"{c}/23 ({p}%)" for c, p in zip(grp["Count"], grp["Pct"])],
            textposition="outside",
        ))

    fig.update_layout(
        barmode="stack", height=420,
        xaxis=dict(title="% of Participants", range=[0, 100]),
        yaxis=dict(title=""),
        legend=dict(orientation="h", y=-0.15),
        margin=dict(l=0, r=120, t=20, b=40),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("Top 10 Suggested Improvements")

    imp_data = {
        "Improvement": [
            "Better onboarding / in-app instructions",
            "Gesture capture feedback & confirmation",
            "Better navigation / wayfinding system",
            "Deeper narrative / storyline continuity",
            "Progressive hint system (time-based)",
            "3D model placement fix (behind photo bug)",
            "Sound / audio integration",
            "Historical visual overlay (1900s)",
            "Restaurant / business partnerships",
            "Multiplayer / role intertwining",
        ],
        "Mentions": [13, 10, 10, 9, 7, 5, 5, 4, 4, 3],
        "Participants": [
            "P01,P03,P05,P06,P07,P08,P11,P14,P15,P16,P17,G1b,G2a",
            "P01,P02,P05,P06,P08,P11,P14,P16,G1b,G2a",
            "P01,P02,P04,P05,P06,P08,P13,G1a,G2a,G2b",
            "P02,P03,P06,P08,P14,P15,G1a,G1b,G2b",
            "P08,P06,P14,P15,G1a,G2a,G2b",
            "P10,P11,P13,P16,G2a",
            "P06,P15,G1a,G1b,G2a",
            "P15,P17,G2b,G1c",
            "P04,P08,P10,G2a",
            "P03,P06,G2a",
        ]
    }
    imp_df = pd.DataFrame(imp_data).sort_values("Mentions", ascending=True)

    fig2 = px.bar(imp_df, x="Mentions", y="Improvement", orientation="h",
                  color="Mentions", color_continuous_scale="RdYlGn_r",
                  text="Mentions", hover_data={"Participants": True})
    fig2.update_traces(textposition="outside")
    fig2.update_layout(height=380, coloraxis_showscale=False,
                       margin=dict(l=0, r=60, t=10, b=10),
                       xaxis=dict(title="Number of Mentions", range=[0, 16]),
                       yaxis=dict(title=""))
    st.plotly_chart(fig2, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════════
# PAGE: Willingness to Pay
# ════════════════════════════════════════════════════════════════════════════
elif page == "Willingness to Pay":
    st.title("💰 Willingness to Pay")
    st.caption("18 out of 23 participants gave a price estimate")

    wtp = {
        "$10–15": {"count": 2, "who": "P01, P07"},
        "$15–20": {"count": 4, "who": "P04, P05, P11, G2c"},
        "$20–25": {"count": 5, "who": "P08, P15, P16, G2a, G2b"},
        "$25–30": {"count": 2, "who": "P02, P17"},
        "$30–40": {"count": 1, "who": "P11"},
        "$40–50": {"count": 2, "who": "P06, G2a"},
        "$50–100": {"count": 0, "who": "—"},
        "$100–200+": {"count": 2, "who": "P10, P17 (with full tour)"},
    }

    labels = list(wtp.keys())
    counts = [v["count"] for v in wtp.values()]
    whos = [v["who"] for v in wtp.values()]
    bar_colors = ["#BDBDBD", "#BDBDBD", "#4ECDC4", "#4ECDC4",
                  "#FFD93D", "#FFD93D", "#EEEEEE", "#FF6B6B"]

    fig = go.Figure(go.Bar(
        x=labels, y=counts, marker_color=bar_colors,
        text=counts, textposition="outside",
        customdata=whos,
        hovertemplate="<b>%{x}</b><br>Count: %{y}<br>Who: %{customdata}<extra></extra>",
    ))
    fig.add_vline(x=2.5, line_dash="dash", line_color="#D32F2F",
                  annotation_text="Median: ~$20–25", annotation_position="top right")
    fig.update_layout(
        height=380, yaxis=dict(title="Number of Participants", range=[0, 7]),
        xaxis=dict(title="Willingness to Pay (USD)"),
        margin=dict(l=0, r=0, t=20, b=10),
    )
    st.plotly_chart(fig, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Current 10-min experience", "~$20–25", "Median WTP")
    col2.metric("Polished 30-min version", "~$40–50", "with multiplayer")
    col3.metric("Full tour integration", "$100–200+", "tourist package")

    st.divider()
    st.subheader("What Drives Higher WTP?")
    drivers = [
        ("⏱ Duration", "Longer experience = higher willingness to pay"),
        ("📖 Content depth", "More storyline and objects = more perceived value"),
        ("👥 Multiplayer", "Group play with intertwining roles significantly raises WTP"),
        ("🏆 Uniqueness", '"First AR experience in NYC" — no price reference point'),
        ("🔗 Tour integration", "Bundled with walking tour doubles perceived value"),
    ]
    for icon_label, desc in drivers:
        st.markdown(f"- **{icon_label}**: {desc}")

# ════════════════════════════════════════════════════════════════════════════
# PAGE: Theoretical Model
# ════════════════════════════════════════════════════════════════════════════
elif page == "Theoretical Model":
    st.title("🧩 Grounded Theory: Theoretical Model")
    st.markdown(
        '**Core Category**: *"Embodied Cultural Discovery Through Augmented Perception"*'
    )

    fig = go.Figure()
    fig.update_layout(
        width=900, height=520,
        xaxis=dict(range=[0, 14], showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(range=[0, 10], showgrid=False, zeroline=False, showticklabels=False),
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="white",
    )

    def add_box(fig, x, y, w, h, text, color, textcolor="#333", fontsize=11):
        fig.add_shape(type="rect", x0=x, y0=y, x1=x+w, y1=y+h,
                      fillcolor=color, line=dict(color="#888", width=1.2),
                      opacity=0.88)
        fig.add_annotation(x=x+w/2, y=y+h/2, text=text, showarrow=False,
                           font=dict(size=fontsize, color=textcolor), align="center")

    def add_arrow(fig, x0, y0, x1, y1, color="#999"):
        fig.add_annotation(x=x1, y=y1, ax=x0, ay=y0,
                           xref="x", yref="y", axref="x", ayref="y",
                           showarrow=True, arrowhead=2, arrowsize=1.2,
                           arrowcolor=color, arrowwidth=2)

    # Core
    add_box(fig, 3.5, 8.1, 7, 1.3,
            "<b>CORE CATEGORY</b><br>Embodied Cultural Discovery<br>Through Augmented Perception",
            "#5B8DEF", "#fff", 12)

    # Enablers
    fig.add_annotation(x=1.4, y=7.4, text="<b>ENABLERS</b>", showarrow=False,
                       font=dict(size=11, color="#FF6B6B"))
    for i, (label, pct) in enumerate([
        ("Gesture Reliability<br>& Feedback", "74%"),
        ("Hardware Comfort<br>& FOV", "43%"),
        ("Onboarding<br>Quality", "57%"),
    ]):
        add_box(fig, 0.2, 6.1 - i*1.4, 2.6, 1.1,
                f"{label}<br><span style='color:#888'>{pct}</span>", "#FFE8E8")

    # Mediators
    fig.add_annotation(x=7, y=7.4, text="<b>MEDIATORS</b>", showarrow=False,
                       font=dict(size=11, color="#FFB300"))
    for i, (label, pct) in enumerate([
        ("Navigation Balance<br>(Guided ↔ Discovery)", "57%"),
        ("Narrative Coherence<br>(Tasks → Story Arc)", "48%"),
        ("Social-Material<br>Ecology", "26%"),
    ]):
        add_box(fig, 5.5, 6.1 - i*1.4, 3, 1.1,
                f"{label}<br><span style='color:#888'>{pct}</span>", "#FFF8E1")

    # Outcomes
    fig.add_annotation(x=12, y=7.4, text="<b>OUTCOMES</b>", showarrow=False,
                       font=dict(size=11, color="#4ECDC4"))
    for i, (label, pct) in enumerate([
        ("Cultural<br>Understanding", "43%"),
        ("Emotional<br>Connection", "43%"),
        ("Commercial<br>Viability", "65%"),
    ]):
        add_box(fig, 10.5, 6.1 - i*1.4, 3, 1.1,
                f"{label}<br><span style='color:#888'>{pct}</span>", "#E0F7FA")

    # Arrows
    add_arrow(fig, 2.8, 7.0, 3.5, 8.5, "#FF6B6B")
    add_arrow(fig, 7, 8.1, 7, 7.4, "#FFB300")
    for i in range(3):
        add_arrow(fig, 8.5, 6.55 - i*1.4, 10.5, 6.55 - i*1.4, "#4ECDC4")
    add_arrow(fig, 2.8, 5.15, 5.5, 5.15, "#aaa")
    add_arrow(fig, 2.8, 3.75, 5.5, 3.75, "#aaa")

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("5 Key Propositions")
    props = [
        ("P1", "🤌", "Photography-as-interaction creates embodied agency",
         "But this agency is fragile when gesture feedback is absent. Every participant commented on gesture interaction — it is the single most critical factor."),
        ("P2", "🧭", "Navigation requires progressive disclosure",
         "Broad hint → time delay → specific cue. Too much guidance removes discovery joy; too little causes abandonment. The sweet spot is a 'phone a friend' system."),
        ("P3", "📖", "Narrative is the multiplier",
         "Users currently perceive a 'scavenger hunt'; the design intends a 'City Theater'. Narrative coherence is the bridge. Without it, the experience is a tech demo. With it, it becomes a cultural product."),
        ("P4", "🔄", "Experience extends beyond the glasses",
         "Before (video expectations) → onboarding → play → souvenir → local dining. Each phase amplifies or diminishes the whole."),
        ("P5", "💼", "B2B partnerships > direct B2C",
         "Tourism boards, local businesses, and education institutions are more viable monetization channels than direct ticket sales at current experience maturity."),
    ]
    for code, icon, title, desc in props:
        with st.expander(f"**{code}** {icon} {title}"):
            st.write(desc)

# ════════════════════════════════════════════════════════════════════════════
# PAGE: Open Coding Table
# ════════════════════════════════════════════════════════════════════════════
elif page == "Open Coding Table":
    st.title("🏷️ Open Coding Table")
    st.caption(f"{len(CODING_DF)} codes across 12 categories")

    col1, col2 = st.columns(2)
    with col1:
        cats = ["All"] + sorted(CODING_DF["Category"].unique().tolist())
        selected_cat = st.selectbox("Filter by Category", cats)
    with col2:
        search = st.text_input("Search codes or quotes", placeholder="e.g. gesture, navigation, story...")

    df_view = CODING_DF.copy()
    if selected_cat != "All":
        df_view = df_view[df_view["Category"] == selected_cat]
    if search:
        mask = (
            df_view["Code"].str.contains(search, case=False, na=False) |
            df_view["Representative Quote"].str.contains(search, case=False, na=False) |
            df_view["Sub-category"].str.contains(search, case=False, na=False)
        )
        df_view = df_view[mask]

    st.caption(f"Showing {len(df_view)} codes")
    st.dataframe(
        df_view,
        use_container_width=True,
        height=500,
        column_config={
            "Category": st.column_config.TextColumn("Category", width=160),
            "Sub-category": st.column_config.TextColumn("Sub-category", width=160),
            "Code": st.column_config.TextColumn("Code", width=200),
            "Representative Quote": st.column_config.TextColumn("Quote", width=350),
            "Participant(s)": st.column_config.TextColumn("Participant(s)", width=120),
        },
        hide_index=True,
    )

# ════════════════════════════════════════════════════════════════════════════
# PAGE: Transcript Explorer
# ════════════════════════════════════════════════════════════════════════════
elif page == "Transcript Explorer":
    st.title("📄 Transcript Explorer")

    col1, col2 = st.columns([1, 2])
    with col1:
        selected = st.selectbox(
            "Select Participant",
            options=sorted(TRANSCRIPTS.keys()),
            format_func=lambda p: f"{p} — {PARTICIPANT_INFO.get(p, {}).get('role', '')[:40]}"
        )
        info = PARTICIPANT_INFO.get(selected, {})
        color = BG_COLORS.get(info.get("background", ""), "#ccc")
        st.markdown(
            f"""<div style="border-left:4px solid {color}; padding:8px 12px;
            border-radius:4px; background:#fafafa; margin-top:8px;">
            <b>{selected}</b><br/>
            <span style="font-size:13px">{info.get('role','—')}</span><br/>
            <span style="font-size:11px; background:{color}22; color:{color};
            padding:1px 6px; border-radius:10px">{info.get('background','—')}</span>
            </div>""",
            unsafe_allow_html=True
        )

        search_term = st.text_input("Highlight keyword", placeholder="e.g. narrative, pay, gesture")

    with col2:
        text = TRANSCRIPTS.get(selected, "Transcript not found.")
        word_count = len(text.split())
        st.caption(f"~{word_count} words")

        if search_term and search_term.lower() in text.lower():
            import re
            highlighted = re.sub(
                f"({re.escape(search_term)})",
                r'<mark style="background:#FFD93D; padding:1px 3px; border-radius:3px">\1</mark>',
                text, flags=re.IGNORECASE
            )
            st.markdown(
                f'<div style="height:520px; overflow-y:auto; font-size:14px; '
                f'line-height:1.7; padding:12px; border:1px solid #eee; border-radius:8px; '
                f'background:#fff">{highlighted}</div>',
                unsafe_allow_html=True
            )
        else:
            st.text_area("", text, height=520, label_visibility="collapsed")

# ════════════════════════════════════════════════════════════════════════════
# PAGE: Cultural Meaning
# ════════════════════════════════════════════════════════════════════════════
elif page == "Cultural Meaning":
    st.title("🏮 What Does This Project Mean to Chinatown?")
    st.markdown(
        "15 out of 23 participants spontaneously commented on the project's cultural or "
        "community significance. The following 6 dimensions emerged from their responses."
    )

    dimensions = [
        {
            "code": "M1", "icon": "🔍", "label": "Making Depth Visible",
            "desc": "The project makes visible what is otherwise invisible to casual visitors — the historical and cultural layers hidden beneath the contemporary streetscape.",
            "quotes": [
                ("P01", "Chinatown has a lot of depth to it that just walking around you wouldn't be able to notice, but this kind of immersive experiences really can help you get deeper into the community."),
                ("G2b", "I wanna feel what it was like to be on this street 100 years ago."),
                ("P10", "I got to experience parts of the street that I probably would not have experienced before."),
            ],
            "who": "Non-Chinese participants", "color": "#5B8DEF",
        },
        {
            "code": "M2", "icon": "👁️", "label": "Being Seen",
            "desc": "The project helps Chinese culture be visible and appreciated by outsiders. P09's phrase 'see us' signals that this is about cultural recognition, not just tourism.",
            "quotes": [
                ("P09", "Really appreciate that people see this and see us and help to promote Chinese culture."),
                ("P09", "A really good way to bring the technology in and bring the culture out to the world."),
            ],
            "who": "Chinese-American participants", "color": "#FF6B6B",
        },
        {
            "code": "M3", "icon": "🌱", "label": "Old Town Rebirth",
            "desc": "New technology gives the historic neighborhood renewed relevance. AR is framed not as disruption but as revitalization — culturally respectful rather than extractive.",
            "quotes": [
                ("P17", "It's an old town, but with the new technology, it gives the old town a rebirth chance, like a new potential."),
                ("P17", "Chinatown now thrives on tourism and whatever new experience will be an add-on."),
            ],
            "who": "P17 (Chinatown correspondent)", "color": "#4ECDC4",
        },
        {
            "code": "M4", "icon": "🤝", "label": "Connecting, Not Isolating",
            "desc": "Multiple participants explicitly contrast this outdoor, place-based AR experience with the isolating nature of VR. AR in a real street setting is seen as a philosophical statement.",
            "quotes": [
                ("P15", "It's the right way to let this technology connect people instead of isolating people in their bubbles."),
                ("P03", "Leverage technology in a way that helps people build deeper relationships to the physical world."),
            ],
            "who": "XR industry professionals", "color": "#FFD93D",
        },
        {
            "code": "M5", "icon": "❤️", "label": "Personal & Emotional Roots",
            "desc": "For Chinese-American participants, the project activates personal and family histories. AR transforms a casual neighborhood visit into an emotional homecoming.",
            "quotes": [
                ("P08", "I love being in Chinatown, kind of like where my mom grew up."),
                ("P16", "Great community building and team bonding... contributing this to the community."),
            ],
            "who": "Chinese-American participants", "color": "#CE93D8",
        },
        {
            "code": "M6", "icon": "🌉", "label": "Generational Bridge",
            "desc": "The AR experience becomes a site where older cultural knowledge and newer technological fluency meet. Gen Z participants feel prompted to 'catch up' across the generational gap.",
            "quotes": [
                ("P17", "I met a little girl who's 10. She started trying out AR at the age of four. I feel like there's a generational gap and I should try the best to catch up."),
            ],
            "who": "P17 (Gen Z reporter)", "color": "#FF8C42",
        },
    ]

    for dim in dimensions:
        with st.expander(f"**{dim['code']}** {dim['icon']} **{dim['label']}** — *{dim['who']}*",
                         expanded=dim['code'] in ("M1", "M2")):
            st.markdown(f"> {dim['desc']}")
            for pid, quote in dim["quotes"]:
                st.markdown(
                    f"""<div style="border-left:3px solid {dim['color']}; padding:6px 12px;
                    margin:6px 0; border-radius:4px; background:#fafafa; font-size:13px;">
                    <b>{pid}</b> — "{quote}"
                    </div>""",
                    unsafe_allow_html=True
                )

    st.divider()
    st.subheader("Key Conclusion")
    st.success(
        "The project's cultural meaning operates on **three levels simultaneously**:\n\n"
        "- 🔵 **Micro** (individual): Reveals hidden heritage (M1) and activates personal roots (M5)\n"
        "- 🟡 **Meso** (social): Creates cross-cultural encounter (M2), connects rather than isolates (M4), bridges generations (M6)\n"
        "- 🟢 **Macro** (community): Positions AR as a tool for culturally-grounded neighborhood revitalization (M3)\n\n"
        "**Chinatown ARcade is not technology applied to a place — it is a community using technology to tell its own story.**"
    )
