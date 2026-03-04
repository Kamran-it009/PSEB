import streamlit as st

st.title(":green[Hello, Streamlit!] :smile:", text_alignment = 'center')

st.header('This is Header')

st.subheader('This is subheader')
st.markdown('# Heading1')
st.markdown('## Heading2')
st.markdown('### Heading3')
st.markdown('#### Heading4')
st.markdown('##### Heading5')

st.text("Hello this is text")

st.success("Admission Successful")
st.info("Information")
st.warning("Warning")
st.error("Error")

st.code("x = 2")

# f st.checkbox("Show/Hide"):
#     st.video('https://www.youtube.com/watch?v=i3z4uhd28gw')

status = st.radio('Select Gender:', ['Male', 'Female'])

if status == 'Male':
    st.write('You are resposible')
else:
    st.write('You must have patience')

st.button('Submit', type = 'primary')


# exp = ZeroDivisionError("Trying to divide by Zero")

# st.exception(exp)

# st.write(range(10))

# st.image('solider.png', width=500)

# st.video('https://www.youtube.com/watch?v=i3z4uhd28gw')



