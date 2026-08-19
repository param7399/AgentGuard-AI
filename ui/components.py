import streamlit as st


def page_header(title, subtitle=""):
    st.markdown(
        f"""
        <div class="page-title">{title}</div>
        <div class="page-subtitle">{subtitle}</div>
        """,
        unsafe_allow_html=True
    )


def section_title(title):
    st.markdown(
        f"""
        <div class="section-title">{title}</div>
        """,
        unsafe_allow_html=True
    )


def metric_card(label, value, subtitle=""):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-sub">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def status_badge(text, status="success"):
    classes = {
        "success": "badge-green",
        "warning": "badge-yellow",
        "danger": "badge-red"
    }

    css_class = classes.get(status, "badge-green")

    return (
        f'<span class="badge {css_class}">{text}</span>'
    )


def severity_badge(severity):

    severity = str(severity).upper()

    if severity == "CRITICAL":
        css_class = "badge-red"
    elif severity == "HIGH":
        css_class = "badge-red"
    elif severity == "MEDIUM":
        css_class = "badge-yellow"
    else:
        css_class = "badge-green"

    return (
        f'<span class="badge {css_class}">'
        f'{severity}'
        f'</span>'
    )


def test_card(
    test_id,
    category,
    result,
    score,
    failure_type="None"
):

    if result == "PASS":
        icon = "✓"
        badge_class = "badge-green"
    else:
        icon = "!"
        badge_class = "badge-red"

    st.markdown(
        f"""
        <div class="test-row">
            <b>{icon} Test #{test_id} — {category}</b>

            <span
                style="float:right;"
                class="badge {badge_class}">
                {score}/100
            </span>

            <br>

            <span
                style="
                font-size:12px;
                color:#64748b;
                ">
                {failure_type}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(title, value, description=""):

    st.markdown(
        f"""
        <div class="card">
            <div
                style="
                font-size:12px;
                color:#64748b;
                text-transform:uppercase;
                letter-spacing:.08em;
                font-weight:700;
                ">
                {title}
            </div>

            <div
                style="
                font-size:28px;
                font-weight:800;
                color:#f8fafc;
                margin-top:8px;
                ">
                {value}
            </div>

            <div
                style="
                font-size:12px;
                color:#64748b;
                margin-top:5px;
                ">
                {description}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def empty_state(title, description):

    st.markdown(
        f"""
        <div class="card" style="text-align:center;padding:45px;">
            <div style="font-size:36px;">🛡️</div>

            <div
                style="
                font-size:20px;
                font-weight:750;
                color:#f8fafc;
                margin-top:12px;
                ">
                {title}
            </div>

            <div
                style="
                color:#64748b;
                font-size:13px;
                margin-top:8px;
                ">
                {description}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )