import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

pickle_inDT = open("ImonDT.pkl","rb")
regressorDT=pickle.load(pickle_inDT)


st.title("Модель кредитного скоринга")
st.caption("Made By Mercurii.ai")
st.sidebar.header("Ввод данных заемщика")

gender = st.sidebar.selectbox("Пол", ["Муж", "Жен"])
marial = st.sidebar.selectbox("Семейное положение", ["Married", "Single", "Divorced", "Widow/Widower"])
person_age = st.sidebar.slider("Возраст", 18, 100, 25)
nationality = st.sidebar.selectbox("Национальность", ["Таджик", "Узбек",  "Другие" , "Русский"])
client = st.sidebar.selectbox("Повторный клиент", ["Старый клиент", "Новый клиент"])
suma = st.sidebar.number_input("Какую денежную сумму вы хотите взять в кредит", min_value=0)
zalog = st.sidebar.selectbox("Тип залога", ["Поручительство", "Не обеспеченный" , "Смешанное обеспечение" , "Движимое имущество" , "Ювелирные изделия"
"Депозит" ,"Недвижимость"])

study = st.sidebar.selectbox("Образование", ["Среднее образование", "Высшее образование" , "Сред.спец.образ-ние" , "Непол Сред.образ" , "Аспирантура","Начал образование" ])

biznes = st.sidebar.selectbox("Тип бизнеса", ["1. Карзи истеъмоли/Потребительский кредит", "3. Хизматрасони/Услуги" , "4. Савдо / Торговля" , "2. Истехсолот/Производство" , "8. Ипотека/Ипотек"
"5. Чорводори / Животноводство" , "6. Хочагии кишлок / Сельское хозяйство"
"7. Тичорати бурунмарзи / Внешняя торговля"])

creditaim =st.sidebar.selectbox("Цель кредита", ["Потребительские цели", "Оборотный капитал" , "Основные средства" , "Строительство жилья" , "Баланд бардоштани сам. эн. манзил"
"Покупка жилья" , "Ремонт жилья" , "Старт-ап"])



X = pd.DataFrame({
    'Пол': [gender],
    'Семейное положение': [marial],
    'Национальность': [nationality],
    'Повторный клиент': [client],
    'Сумма выдачи номинал': [suma],
    'Тип залога': [zalog],
    'Образование': [study],
    'Тип бизнеса': [biznes],
    'Цель кредита': [creditaim],
    'age': [person_age]
})

X = pd.get_dummies(X, columns=['Пол', 'Семейное положение', 'Национальность', 'Повторный клиент', 'Тип залога', 'Образование', 'Тип бизнеса', 'Цель кредита'], drop_first=True)

credit_score = regressorDT.predict(X)[0]
if st.button("Предсказать кредитный скоринг"):        
    if credit_score == 1:
        st.balloons()
        t1 = plt.Polygon([[5, 0.5], [5.5, 0], [4.5, 0]], color='black')
        placeholder.markdown('Your credit score is **GOOD**! Congratulations!')
        st.markdown('This credit score indicates that this person is likely to repay a loan, so the risk of giving them credit is low.')
    elif credit_score == 0:
        t1 = plt.Polygon([[3, 0.5], [3.5, 0], [2.5, 0]], color='black')
        placeholder.markdown('Your credit score is **REGULAR**.')
        st.markdown('This credit score indicates that this person is likely to repay a loan, but can occasionally miss some payments. Meaning that the risk of giving them credit is medium.')
    elif credit_score == -1:
        t1 = plt.Polygon([[1, 0.5], [1.5, 0], [0.5, 0]], color='black')
        placeholder.markdown('Your credit score is **POOR**.')
        st.markdown('This credit score indicates that this person is unlikely to repay a loan, so the risk of lending them credit is high.')        
