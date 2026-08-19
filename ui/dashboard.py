import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime, timedelta

from ui.components import (
    page_header,
    section_title,
    metric_card,
    test_card
)


def render_dashboard(results):

    page_header(
        "Agent Reliability Overview",
        "Monitor AI agent health, failures, and reliability trends."
    )

    if not results:

        st.info(
            "No evaluation data available yet."
        )
        return

    df = pd.DataFrame(results)

    total_tests = len(df)

    passed = len(
        df[df["result"] == "PASS"]
    )

    failed = total_tests - passed

    reliability = round(
        float(df["score"].mean()),
        1
    )

    critical = len(
        df[df["severity"] == "CRITICAL"]
    )

    # =====================================================
    # METRICS
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "RELIABILITY",
            f"{reliability}/100",
            "Current agent health"
        )

    with c2:
        metric_card(
            "TESTS EXECUTED",
            total_tests,
            "Automated evaluations"
        )

    with c3:
        metric_card(
            "PASSED",
            passed,
            f"{round(passed / total_tests * 100)}% pass rate"
        )

    with c4:
        metric_card(
            "FAILURES",
            failed,
            f"{critical} critical issues"
        )

    st.write("")

    # =====================================================
    # CHARTS
    # =====================================================

    left, right = st.columns([1.7, 1])

    with left:

        section_title("Reliability Trend")

        dates = [
            datetime.now() - timedelta(days=i)
            for i in range(9, -1, -1)
        ]

        trend = [
            74, 76, 75, 79, 78,
            82, 81, 85, 87, reliability
        ]

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=dates,
                y=trend,
                mode="lines+markers",
                line=dict(
                    color="#818cf8",
                    width=3
                ),
                marker=dict(
                    color="#a5b4fc",
                    size=7
                ),
                fill="tozeroy",
                fillcolor="rgba(99,102,241,0.08)"
            )
        )

        fig.update_layout(
            height=340,
            margin=dict(
                l=10,
                r=10,
                t=15,
                b=10
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(
                color="#94a3b8"
            ),
            xaxis=dict(
                showgrid=False
            ),
            yaxis=dict(
                range=[50, 100],
                gridcolor="rgba(148,163,184,0.08)"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        section_title("Agent Health")

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=reliability,
                number={
                    "suffix": "/100",
                    "font": {
                        "size": 32,
                        "color": "#f8fafc"
                    }
                },
                gauge={
                    "axis": {
                        "range": [0, 100],
                        "tickcolor": "#64748b"
                    },
                    "bar": {
                        "color": "#6366f1"
                    },
                    "bgcolor": "#111827",
                    "borderwidth": 0,
                    "steps": [
                        {
                            "range": [0, 50],
                            "color": "#35151b"
                        },
                        {
                            "range": [50, 75],
                            "color": "#302615"
                        },
                        {
                            "range": [75, 100],
                            "color": "#10271e"
                        }
                    ]
                }
            )
        )

        gauge.update_layout(
            height=300,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=10
            ),
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

        status = (
            "HEALTHY"
            if reliability >= 75
            else "NEEDS ATTENTION"
        )

        st.markdown(
            f"""
            <div style="text-align:center;">
                <span class="status-pill">
                    <span class="status-dot"></span>
                    {status}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # =====================================================
    # FAILURE DISTRIBUTION
    # =====================================================

    left, right = st.columns(2)

    with left:

        section_title("Failure Distribution")

        failures = df[
            df["result"] == "FAIL"
        ]

        if not failures.empty:

            counts = (
                failures["failure_type"]
                .value_counts()
                .reset_index()
            )

            counts.columns = [
                "Failure",
                "Count"
            ]

            fig = px.bar(
                counts,
                x="Count",
                y="Failure",
                orientation="h"
            )

            fig.update_traces(
                marker_color="#6366f1"
            )

            fig.update_layout(
                height=280,
                margin=dict(
                    l=10,
                    r=10,
                    t=10,
                    b=10
                ),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(
                    color="#94a3b8"
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:

            st.success(
                "No failures detected."
            )

    # =====================================================
    # RECENT TESTS
    # =====================================================

    with right:

        section_title("Recent Test Executions")

        for _, row in df.tail(5).iterrows():

            test_card(
                row["test_id"],
                row["category"],
                row["result"],
                row["score"],
                row["failure_type"]
            )