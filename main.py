import streamlit as st
import pandas

st.set_page_config(layout='wide')
st.title("The Best Company")
st.write("""Once upon a time, in a land far, far away, there was a company called "Spaghetti Solutions." Their main 
goal was to create a world where spaghetti could be used for anything and everything - from building bridges to 
fueling spaceships. 

Founded by a group of highly intelligent spaghetti enthusiasts, the company quickly gained a reputation for its 
unconventional approach to problem-solving. They believed that any challenge could be overcome with a good serving of 
spaghetti and a healthy dose of imagination. 

Despite the initial skepticism from the rest of the business world, Spaghetti Solutions quickly proved their worth. 
They solved complex engineering problems, invented new materials, and even managed to launch a few successful rockets 
using spaghetti fuel. 

Today, Spaghetti Solutions is a multi-billion dollar company with a worldwide presence. Their team of spaghetti 
experts continues to push the boundaries of what's possible, one noodle at a time. If you're ever in need of a 
creative solution to a problem, just remember - when in doubt, turn to Spaghetti Solutions!""")

st.header("Our Team")

col1, nocol1, col2, nocol2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image(f"images/{row['image']}")
