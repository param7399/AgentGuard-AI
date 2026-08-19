import pandas as pd
import streamlit as st

from ui.components import (
    page_header,
    section_title,
    severity_badge,
    metric_card,
)


def render_failure_analysis(results):

    page_header(
        "Failure Analysis",
        "Understand why your AI agent failed and how to improve it.",
    )

    if not results:
        st.info(
            "No evaluation failures available."
        )
        return

    df = pd.DataFrame(results)

    failures = df[
        df["result"].astype(str).str.upper() == "FAIL"
    ]

    if failures.empty:
        st.success(
            "🎉 No failures detected in the current evaluation."
        )
        return

    # =====================================================
    # FAILURE SUMMARY
    # =====================================================

    metric_card(
        "DETECTED FAILURES",
        len(failures),
        "Requiring developer attention",
    )

    st.write("")

    # =====================================================
    # FAILURE CARDS
    # =====================================================

    for _, row in failures.iterrows():

        severity = str(
            row.get(
                "severity",
                "MEDIUM",
            )
        ).upper()

        if severity == "CRITICAL":
            icon = "🔴"
        elif severity == "HIGH":
            icon = "🟠"
        else:
            icon = "🟡"

        test_id = row.get(
            "test_id",
            "N/A",
        )

        failure_type = row.get(
            "failure_type",
            "Unknown Failure",
        )

        with st.expander(
            f"{icon} Test #{test_id} — {failure_type}",
            expanded=True,
        ):

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Score",
                    f"{row.get('score', 0)}/100",
                )

            with c2:
                st.metric(
                    "Severity",
                    severity,
                )

            with c3:
                st.metric(
                    "Category",
                    row.get(
                        "category",
                        "Unknown",
                    ),
                )

            st.divider()

            # =================================================
            # SCENARIO
            # =================================================

            section_title("Scenario")

            st.info(
                row.get(
                    "scenario",
                    "No scenario available.",
                )
            )

            # =================================================
            # AGENT RESPONSE
            # =================================================

            section_title("Agent Response")

            st.code(
                row.get(
                    "agent_response",
                    "No response available.",
                ),
                language="text",
            )

            # =================================================
            # FAILURE REASON
            # =================================================

            section_title("Why It Failed")

            st.warning(
                row.get(
                    "reason",
                    "No failure reason available.",
                )
            )

            # =================================================
            # RECOMMENDATION
            # =================================================

            section_title("Recommended Fix")

            st.success(
                row.get(
                    "recommendation",
                    "No recommendation available.",
                )
            )