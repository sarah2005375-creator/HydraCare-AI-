
import streamlit as st

st.set_page_config(page_title="HydraCare AI", page_icon="💧")

st.title("💧 HydraCare AI")
st.subheader("Your Dehydration Assistant")

st.write("Welcome! Ask me about dehydration.")
st.write("مرحباً! اسألني عن الجفاف.")

question = st.chat_input("Ask your question...")

if question:

    st.write("You asked:", question)

    q = question.lower()

    if "prevention" in q or "وقاية" in q:
        st.write("Drink enough water regularly.")
        st.write("اشرب الماء بانتظام لتجنب الجفاف.")

    elif "signs" in q or "علامات" in q:
        st.write("Signs include thirst, dizziness and dark urine.")
        st.write("تشمل العلامات العطش والدوخة والبول الداكن.")

    elif "risk" in q or "خطر" in q:
        st.write("Infants and older adults are at higher risk.")
        st.write("الرضع وكبار السن أكثر عرضة للجفاف.")

    elif "fluid" in q or "سوائل" in q:
        st.write("Fluid balance means replacing lost body fluids.")
        st.write("توازن السوائل يعني تعويض السوائل التي يفقدها الجسم.")

    else:
        st.write("I can answer questions about dehydration only.")
        st.write("أستطيع الإجابة عن الأسئلة المتعلقة بالجفاف فقط.")

