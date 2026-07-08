"""
Shared UI helpers for the System Window theme.
Import these into every page so the look stays consistent.
"""

import streamlit as st
from pathlib import Path

# Path to assets/style.css relative to the project root.
# Adjust if you move this file — it's resolved from this file's own location,
# so it works no matter what folder you run `streamlit run` from.
_STYLE_PATH = Path(__file__).resolve().parent.parent / "assets" / "style.css"


def load_css():
    """Inject the system-window theme. Call this once at the top of every page."""
    with open(_STYLE_PATH, "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def render_splash(title: str = "WELCOME BACK", subtitle: str = "SYSTEM ONLINE"):
    """
    Full-screen 'system window' splash, shown once per session.
    Fades in, holds, fades out automatically (pure CSS, no JS needed).
    Call this near the top of your home page, before your main content.
    """
    if st.session_state.get("_splash_shown"):
        return

    st.session_state["_splash_shown"] = True

    st.markdown(
        f"""
        <div id="system-splash">
            <div class="splash-panel">
                <div class="splash-scanline"></div>
                <p class="splash-title">{title}</p>
                <p class="splash-subtitle">{subtitle}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str | None = None):
    """Consistent 'system window' style header for any page."""
    st.markdown(f"<h1 class='system-title'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(
            f"<p style='color:var(--text-muted); margin-top:-0.8rem;'>{subtitle}</p>",
            unsafe_allow_html=True,
        )