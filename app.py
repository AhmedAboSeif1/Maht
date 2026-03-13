import streamlit as st
import pandas as pd
import plotly.express as px

# إعدادات الصفحة
st.set_page_config(page_title="مستقبلي الرياضي", page_icon="📈")

# التصميم وتنسيق الواجهة
st.title("🚀 منصة المستثمر الذكي (الرياضيات التفاعلية)")
st.markdown("""
هذا الموقع صُمم لطلاب الصف الثالث المتوسط لتحويل **المتتابعات الحسابية** و**الدوال الخطية** إلى أداة حقيقية للتنبؤ بالأرباح.
""")

# --- الجزء الأول: المدخلات (المتتابعة الحسابية) ---
st.sidebar.header("⚙️ إعدادات المشروع المالي")
a1 = st.sidebar.number_input("الربح الأول (الحد الأول a1)", value=100)
d = st.sidebar.number_input("الزيادة الدورية (أساس المتتابعة d)", value=50)
n_weeks = st.sidebar.slider("عدد أسابيع التوقع (n)", 1, 52, 12)

# --- الجزء الثاني: العمليات الرياضية (Logic) ---
# إنشاء بيانات المتتابعة الحسابية
weeks = list(range(1, n_weeks + 1))
profits = [a1 + (i - 1) * d for i in weeks] # قانون الحد النوني

df = pd.DataFrame({
    "الأسبوع (n)": weeks,
    "الربح المتوقع (an)": profits
})

# --- الجزء الثالث: عرض النتائج التفاعلية ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 جدول التوقعات")
    st.dataframe(df, height=400)

with col2:
    st.subheader("📈 الرسم البياني (الدالة الخطية)")
    fig = px.line(df, x="الأسبوع (n)", y="الربح المتوقع (an)", 
                 markers=True, template="plotly_dark",
                 labels={"الربح المتوقع (an)": "الأرباح (ريال)"})
    st.plotly_chart(fig, use_container_width=True)

# --- الجزء الرابع: شرح الدرس الرياضي ---
st.divider()
st.subheader("📝 كيف فكر الحاسوب؟ (الربط بالمنهج)")

with st.expander("اضغط هنا لرؤية المعادلات المستخدمة"):
    st.write(f"1. **المتتابعة الحسابية:** استخدمنا القانون $a_n = {a1} + (n - 1) \\times {d}$")
    st.write(f"2. **الدالة الخطية:** المعادلة التي رسمت الخط هي: $f(x) = {d}x + {a1 - d}$")
    st.write(f"3. **التنبؤ:** في الأسبوع رقم {n_weeks}، سيكون ربحك هو **{profits[-1]} ريال**.")

# --- الجزء الخامس: تحدي حل المعادلات ---
st.divider()
st.subheader("🎯 تحدي الهدف المالي")
target = st.number_input("أدخل الربح الذي تطمح للوصول إليه:", value=1000)

if st.button("احسب متى سأصل لهذا الهدف؟"):
    # حل المعادلة: target = a1 + (n-1)d
    # n = ((target - a1) / d) + 1
    n_target = ((target - a1) / d) + 1
    if n_target > 0:
        st.success(f"ستصل لهدفك ({target} ريال) في الأسبوع رقم: **{round(n_target, 2)}**")
        st.info("💡 قمنا بحل المعادلة الخطية $a_n = a_1 + (n-1)d$ لإيجاد قيمة $n$.")
    else:
        st.error("الهدف الذي أدخلته أقل من ربحك الحالي!")