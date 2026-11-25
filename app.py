import streamlit as st
from dotenv import load_dotenv
from modules.nutrition_calculator import calculate_targets
from modules.meal_planner import build_meal_plan
from modules.supplement_advisor import get_supplement_info
from modules.chatbot import ask_nutrition_question
from database.database import init_db, save_profile, get_recent_profiles

load_dotenv()
init_db()

st.set_page_config(page_title="NutriFit AI Advisor", page_icon="🥗", layout="wide")

st.title("🥗 NutriFit AI — Nutrition & Supplement Advisor")
st.caption("Personalized nutrition education, meal ideas, and supplement information.")
st.warning("This app provides general educational information only. It is not medical advice or a substitute for a registered dietitian or healthcare professional.")

with st.sidebar:
    st.header("Your profile")
    name = st.text_input("Name (optional)")
    age = st.number_input("Age", min_value=16, max_value=100, value=25)
    sex = st.selectbox("Sex used for equation", ["Male", "Female"])
    height_cm = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0, step=1.0)
    weight_kg = st.number_input("Weight (kg)", min_value=30.0, max_value=300.0, value=70.0, step=0.5)
    activity = st.selectbox(
        "Activity level",
        ["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"]
    )
    goal = st.selectbox("Goal", ["Maintain weight", "Lose weight", "Gain weight"])
    dietary = st.selectbox("Diet preference", ["No preference", "Vegetarian", "Vegan", "Eggetarian"])
    calculate = st.button("Calculate my targets", type="primary", use_container_width=True)

tab1, tab2, tab3, tab4 = st.tabs(["📊 Nutrition targets", "🍽️ Meal planner", "💊 Supplement guide", "🤖 AI chatbot"])

if "targets" not in st.session_state:
    st.session_state.targets = None
if "profile" not in st.session_state:
    st.session_state.profile = None

if calculate:
    profile = {
        "name": name.strip() or "Guest",
        "age": int(age),
        "sex": sex,
        "height_cm": float(height_cm),
        "weight_kg": float(weight_kg),
        "activity": activity,
        "goal": goal,
        "dietary": dietary,
    }
    targets = calculate_targets(profile)
    st.session_state.profile = profile
    st.session_state.targets = targets
    save_profile(profile, targets)

with tab1:
    st.subheader("Your estimated daily targets")
    if st.session_state.targets:
        t = st.session_state.targets
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Calories", f"{t['calories']:,} kcal")
        c2.metric("Protein", f"{t['protein_g']} g")
        c3.metric("Carbohydrates", f"{t['carbs_g']} g")
        c4.metric("Fat", f"{t['fat_g']} g")
        st.info(f"Estimated maintenance calories: {t['maintenance_calories']:,} kcal/day")
        st.write("These are estimates based on a standard equation and your selected activity level. Actual needs vary.")
        st.button("Save profile", on_click=save_profile, args=(st.session_state.profile, t), key="save_profile_btn")
    else:
        st.write("Enter your details in the sidebar and click **Calculate my targets**.")

with tab2:
    st.subheader("Simple meal plan")
    if st.session_state.targets:
        plan = build_meal_plan(st.session_state.targets["calories"], st.session_state.profile["dietary"])
        for meal, items in plan.items():
            with st.expander(meal, expanded=True):
                st.write(" • ".join(items))
        st.caption("Meal ideas are illustrative. Adjust portions, allergies, culture, budget, and preferences.")
    else:
        st.write("Calculate your nutrition targets first to create a meal plan.")

with tab3:
    st.subheader("Supplement information")
    supplement = st.selectbox("Choose a supplement", [
        "Protein powder", "Creatine monohydrate", "Vitamin D", "Vitamin B12",
        "Omega-3", "Electrolytes", "Caffeine", "Iron"
    ])
    if st.button("Show supplement guide"):
        info = get_supplement_info(supplement)
        st.markdown(info["summary"])
        st.markdown("**Important considerations**")
        st.write(info["cautions"])
        st.caption("Check with a qualified healthcare professional before starting supplements, especially if pregnant, under 18, taking medication, or managing a medical condition.")

with tab4:
    st.subheader("Ask the AI nutrition assistant")
    st.write("Ask general questions about food, fitness nutrition, meal planning, or supplement basics.")
    question = st.text_area("Your question", placeholder="Example: What are some vegetarian protein sources?")
    if st.button("Ask Gemini", type="primary"):
        if not question.strip():
            st.warning("Please type a question first.")
        else:
            with st.spinner("Thinking..."):
                answer = ask_nutrition_question(question)
            st.markdown(answer)

with st.expander("Recent saved profiles"):
    rows = get_recent_profiles()
    if rows:
        st.dataframe(rows, use_container_width=True, hide_index=True)
    else:
        st.write("No profiles saved yet.")
