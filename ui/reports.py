import pandas as pd
import streamlit as st

from ui.components import (
    page_header,
    metric_card,
    section_title
)


def render_reports(results):

    page_header(
        "Reliability Reports",
        "Evaluation results, insights, and downloadable reports."
    )

    if not results:

        st.info(
            "Run an evaluation to generate a report."
        )

        return

    df = pd.DataFrame(results)

    total = len(df)

    passed = len(
        df[df["result"] == "PASS"]
    )

    failed = total - passed

    reliability = round(
        float(df["score"].mean()),
        1
    )

    pass_rate = round(
        passed / total * 100,
        1
    )

    # =====================================================
    # SUMMARY
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "RELIABILITY",
            f"{reliability}/100",
            "Overall agent score"
        )

    with c2:
        metric_card(
            "TOTAL TESTS",
            total,
            "Evaluation scenarios"
        )

    with c3:
        metric_card(
            "PASS RATE",
            f"{pass_rate}%",
            f"{passed} successful tests"
        )

    with c4:
        metric_card(
            "FAILURES",
            failed,
            "Tests requiring attention"
        )

    st.write("")

    # =====================================================
    # TABLE
    # =====================================================

    section_title(
        "Complete Evaluation Report"
    )

    columns = [
        "test_id",
        "category",
        "result",
        "failure_type",
        "severity",
        "score"
    ]

    available_columns = [
        col
        for col in columns
        if col in df.columns
    ]

    report_df = df[
        available_columns
    ]

    st.dataframe(
        report_df,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # CSV
    # =====================================================

    csv_data = report_df.to_csv(
        index=False
    )

    st.download_button(
        "⬇ Download Evaluation CSV",
        data=csv_data,
        file_name="agentguard_reliability_report.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # RECOMMENDATIONS
    # =====================================================

    section_title(
        "Key Recommendations"
    )

    if "recommendation" not in df.columns:

        st.info(
            "No recommendations available."
        )

        return

    recommendations = (
        df[
            df["result"] == "FAIL"
        ]["recommendation"]
        .dropna()
        .unique()
    )

    if len(recommendations) == 0:

        st.success(
            "🎉 No major reliability improvements detected."
        )

    else:

        for recommendation in recommendations:

            st.markdown(
                f"""
                <div class="test-row">
                    💡 {recommendation}
                </div>
                """,
                unsafe_allow_html=True
            )