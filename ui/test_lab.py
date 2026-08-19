import streamlit as st

from ui.components import (
    page_header,
    section_title,
    severity_badge
)


def render_test_lab(
    generate_callback=None,
    evaluate_callback=None
):

    page_header(
        "Test Lab",
        "Generate realistic and adversarial scenarios for your AI agent."
    )

    left, right = st.columns(2)

    # =====================================================
    # AGENT CONFIGURATION
    # =====================================================

    with left:

        section_title("Agent Configuration")

        agent_name = st.text_input(
            "Agent Name",
            value="Travel Booking Agent",
            key="lab_agent_name"
        )

        task = st.text_area(
            "Agent Objective",
            value=(
                "Book flights based on customer requirements."
            ),
            height=110,
            key="lab_agent_task"
        )

        system_prompt = st.text_area(
            "System Prompt",
            value=(
                "You are a helpful travel booking assistant. "
                "Collect all required information before booking."
            ),
            height=160,
            key="lab_system_prompt"
        )

    # =====================================================
    # TEST CONFIGURATION
    # =====================================================

    with right:

        section_title("Test Configuration")

        tools = st.text_area(
            "Available Tools",
            value=(
                "search_flights\n"
                "book_flight\n"
                "cancel_booking"
            ),
            height=110,
            key="lab_tools"
        )

        categories = st.multiselect(
            "Test Categories",
            [
                "Normal",
                "Adversarial",
                "Safety",
                "Tool Failure",
                "Goal Drift",
                "Hallucination"
            ],
            default=[
                "Normal",
                "Adversarial",
                "Safety",
                "Tool Failure"
            ]
        )

        count = st.slider(
            "Number of Test Scenarios",
            3,
            15,
            6
        )

    st.write("")

    # =====================================================
    # GENERATE
    # =====================================================

    if st.button(
        "⚡ Generate Reliability Tests",
        type="primary",
        use_container_width=True
    ):

        if generate_callback:

            with st.spinner(
                "Generating intelligent test scenarios..."
            ):

                scenarios = generate_callback(
                    agent_name,
                    task,
                    system_prompt,
                    tools,
                    categories,
                    count
                )

            st.session_state.scenarios = scenarios

            st.success(
                f"{len(scenarios)} test scenarios generated."
            )

        else:

            st.warning(
                "Scenario generator is not connected yet."
            )

    # =====================================================
    # SCENARIOS
    # =====================================================

    scenarios = st.session_state.get(
        "scenarios",
        []
    )

    if scenarios:

        st.divider()

        section_title(
            f"Generated Scenarios ({len(scenarios)})"
        )

        for scenario in scenarios:

            severity = scenario.get(
                "severity",
                "MEDIUM"
            )

            with st.expander(
                f"Test #{scenario.get('id')} — "
                f"{scenario.get('category')}"
            ):

                st.markdown(
                    severity_badge(severity),
                    unsafe_allow_html=True
                )

                st.write("")

                st.write(
                    "**Scenario:**"
                )

                st.write(
                    scenario.get(
                        "scenario",
                        ""
                    )
                )

                st.write(
                    "**Expected Behavior:**"
                )

                st.write(
                    scenario.get(
                        "expected_behavior",
                        ""
                    )
                )

        st.write("")

        if st.button(
            "▶ Run Full Evaluation",
            type="primary",
            use_container_width=True
        ):

            if evaluate_callback:

                evaluate_callback(
                    agent_name,
                    task,
                    system_prompt,
                    tools,
                    scenarios
                )

            else:

                st.warning(
                    "Evaluation engine is not connected yet."
                )

    return {
        "agent_name": agent_name,
        "task": task,
        "system_prompt": system_prompt,
        "tools": tools,
        "categories": categories,
        "count": count
    }