import streamlit as st
import time
import random

# --- Page Config ---
st.set_page_config(
    page_title="Multi-Tool Agentic RAG",
    page_icon="🔧",
    layout="wide"
)

# --- Custom CSS for Agentic/Tech Look ---
st.markdown("""
<style>
    .main { background-color: #05070a; }
    .stApp { background: radial-gradient(circle at bottom left, #0f172a, #05070a); }
    
    /* Neon Glow Title */
    .agent-title {
        font-family: 'Courier New', Courier, monospace;
        font-size: 3rem;
        font-weight: bold;
        color: #60a5fa;
        text-shadow: 0 0 10px rgba(96, 165, 250, 0.5);
        margin-bottom: 5px;
    }
    
    .agent-subtitle {
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }

    /* Tool Call Cards */
    .tool-box {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid #1e293b;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        transition: all 0.3s ease;
    }
    .tool-box:hover {
        border-color: #60a5fa;
        background: rgba(30, 41, 59, 1);
    }
    
    .tool-badge {
        font-size: 0.7rem;
        padding: 2px 8px;
        border-radius: 5px;
        background: #1e293b;
        color: #60a5fa;
        font-weight: bold;
        margin-bottom: 10px;
        display: inline-block;
    }

    /* Terminal Simulation */
    .terminal-window {
        background: #000;
        color: #10b981;
        font-family: 'Consolas', monospace;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #064e3b;
        height: 350px;
        overflow-y: auto;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://img.icons8.com/nolan/128/bot.png", width=80)
    st.markdown("### Agent Architecture")
    st.info("ReAct (Reason + Act) Pattern")
    st.info("Model: GPT-4o / Claude 3.5")
    st.divider()
    st.markdown("#### Available Tools")
    st.write("🕒 **CurrentTime**")
    st.write("➕ **Calculator**")
    st.write("🌤️ **WeatherAPI**")
    st.write("🔍 **GoogleSearch**")
    st.write("📂 **PDF_Retriever**")
    st.write("🐍 **Python_Interpreter**")
    st.write("🗄️ **SQL_Database**")
    st.write("💱 **Currency_Converter**")
    st.write("📧 **EmailSender**")

# --- Header ---
st.markdown('<div class="agent-title">AGENTIC RAG SYSTEM</div>', unsafe_allow_html=True)
st.markdown('<div class="agent-subtitle">Multi-Tool Orchestration & Knowledge retrieval</div>', unsafe_allow_html=True)

# --- Layout ---
col_in, col_out = st.columns([3, 2])

with col_in:
    st.markdown("### 🗣️ User Query")
    query = st.text_area(
        "Ask the agent anything (Multi-step query):",
        value="What is the weather in London? I have 5000 USD, convert it to PKR. Then, subtract 150,000 PKR for travel expenses. Find if any flights are delayed via Google, and email the remaining balance to travel@agency.com.",
        height=150
    )
    
    run_btn = st.button("🏁 Execute Agentic Pipeline", use_container_width=True)

with col_out:
    st.markdown("### ⛓️ Tool Execution Chain")
    chain_container = st.container()

if run_btn:
    # --- PHASE 1: Execution Simulation ---
    with st.status("🤖 Agent is thinking...", expanded=True) as status:
        
        # 1. Thought Process
        st.write("🤔 **Thought:** This request requires weather data, currency conversion, financial calculation, web search, and notification.")
        time.sleep(1)
        
        # 2. Weather Tool
        with chain_container:
            st.markdown("""<div class="tool-box"><span class="tool-badge">CALLING TOOL</span><br><b>🌤️ WeatherAPI</b><br><small>Params: {'location': 'London'}</small></div>""", unsafe_allow_html=True)
        st.write("📡 Calling `WeatherAPI`...")
        time.sleep(1)
        st.write("✅ **Result:** London: 12°C, Light Drizzle.")
        
        # 3. Currency Tool
        with chain_container:
            st.markdown("""<div class="tool-box"><span class="tool-badge">CALLING TOOL</span><br><b>💱 Currency_Converter</b><br><small>Convert: 5000 USD to PKR</small></div>""", unsafe_allow_html=True)
        st.write("📡 Fetching Live Exchange Rates...")
        time.sleep(1.2)
        st.write("✅ **Result:** 1,390,000 PKR (Rate: 278.0)")

        # 4. Calculator Tool
        with chain_container:
            st.markdown("""<div class="tool-box"><span class="tool-badge">CALLING TOOL</span><br><b>➕ Calculator</b><br><small>Input: 1390000 - 150000</small></div>""", unsafe_allow_html=True)
        st.write("📡 Running financial calculation...")
        time.sleep(0.7)
        st.write("✅ **Result:** 1,240,000 PKR")

        # 5. Google Search
        with chain_container:
            st.markdown("""<div class="tool-box"><span class="tool-badge">CALLING TOOL</span><br><b>🔍 GoogleSearch</b><br><small>Query: 'London Heathrow flight delays today'</small></div>""", unsafe_allow_html=True)
        st.write("📡 Searching `Google`...")
        time.sleep(1.2)
        st.write("✅ **Result:** No major delays reported at LHR currently.")

        # 6. Email Sender
        with chain_container:
            st.markdown("""<div class="tool-box"><span class="tool-badge">CALLING TOOL</span><br><b>📧 EmailSender</b><br><small>To: travel@agency.com</small></div>""", unsafe_allow_html=True)
        st.write("📡 Dispatching itinerary summary...")
        time.sleep(1)
        st.write("✅ **Result:** Email sent successfully.")
        
        # Final Summary
        st.write("✨ **Finalizing Answer...**")
        time.sleep(1)
        status.update(label="🚀 Mission Accomplished!", state="complete", expanded=False)

    # --- FINAL RESULT ---
    st.write("")
    st.markdown("### 📝 Agent Final Response")
    st.markdown(f"""
    <div style="background: rgba(96, 165, 250, 0.1); padding: 25px; border-radius: 12px; border: 1px solid #1e40af;">
        Your travel request has been processed:
        <br><br>
        1. <b>Weather:</b> London is currently 12°C with light drizzle.
        2. <b>Currency:</b> $5,000 USD has been converted to <b>1,390,000 PKR</b>.
        3. <b>Budget:</b> After subtracting 150,000 PKR for expenses, your remaining balance is <b>1,240,000 PKR</b>.
        4. <b>Flights:</b> Google Search confirms no major delays for London flights.
        5. <b>Notification:</b> A detailed report has been sent to <b>travel@agency.com</b>.
    </div>
    """, unsafe_allow_html=True)
    st.balloons()

# Footer
st.divider()
st.markdown("<p style='text-align: center; color: #475569;'>Agentic RAG | Multi-Tool Execution Portfolio Demo</p>", unsafe_allow_html=True)
