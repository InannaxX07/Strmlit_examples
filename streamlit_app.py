import streamlit as st

# Set the title of the app
st.title("Streamlit App with Button, Slider, and Image")

# Create a slider with a descriptive label
image_scale = st.slider("Adjust Image Scale", min_value=0.5, max_value=2.0, step=0.1, value=1.0)

# Define the image path (replace with your image path)
image_path = "https://i.shgcdn.com/d4d32e40-f454-4eee-b0ee-43a03f927768/-/format/auto/-/preview/3000x3000/-/quality/lighter/"

# Load the image
image = st.cache(lambda path: open(path, "rb").read())(image_path)

# Display the image with caption using HTML
st.markdown(f"""<center><img src="data:image/jpg;base64,{image.decode('utf-8')}" 
style="width: {image_scale}*{100}px;" alt="Image"></center>""", unsafe_allow_html=True)

# Add a button (optional functionality can be added here)
if st.button("Click Me!"):
    st.write("Button Clicked!")

