# import streamlit as st
#
# st.title("Welcome to wsube tech")
# st.header("python")
# st.subheader("java")
# st.markdown("I Love Python")
# st.code("""for i in range(1,5,1):
#             print("Hello Riya")
# """)




# import streamlit as st
# import pandas as pd
#
# dataset = pd.read_csv("PythonMP")
#
# st.dataframe(dataset)




# import streamlit as st
# import p

name = st.text_input("Enter your Name")
fname = st.text_input("Enter your Fathor Name")
adr = st.text_area("Enter your Text")
classdata = st.selectbox("Enter your Class :",(1,2,3,4,5,6,7,8,9,10,12))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Fathor Name : {fname}
    address : {adr}
    class : {classdata}""")