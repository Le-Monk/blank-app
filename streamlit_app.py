import streamlit as st
from ai import generate_response, generate_story


def format_style(style):
    return style.capitalize()
image = None
st.header("AI Picture Generator")
col1, col2 = st.columns(2, gap="small", vertical_alignment="top", border=True, width="stretch")

with col1:
    col1b, col2b = st.columns(2, gap="small", vertical_alignment="top", border=True, width="stretch")
    with col1b:
            character_1 = st.text_input("Enter Image of Character 1 URL", "https://example.com/default_image.png")
            st.image(character_1, caption="Character 1", width="stretch")
    with col2b:
            character_2 = st.text_input("Enter Image of Character 2 URL", "https://example.com/default_image.png")
            st.image(character_2, caption="Character 2", width="stretch")
    img_url = st.text_input("Enter Image URL", "https://example.com/default_image.png")
    st.image(img_url, caption="Your Image", width="stretch")

with col2:
    st.subheader("Generate Your Own AI Picture")
    col1a, col2a = st.columns(2, gap="small", vertical_alignment="top", border=True, width="stretch")

    with col1a:
        style_selection = st.radio("Time Period / World Changes", ["Present Day","Future", "Medieval", "Prehistoric", "War time",
                                               "Superheroes", "Fantastical", "Cyberpunk",] , index=0, 
                                               format_func=format_style, key=None, help=None, on_change=None, 
                                               args=None, kwargs=None, disabled=False, horizontal=False, 
                                               captions=None, label_visibility="visible", width="content")
        Other_1 = st.text_input("Other Time Period / World Change")
        if Other_1 != "":
            style_selection = Other_1 


    with col2a:
        twist_selection = st.radio("Twist in the Story", ["No Twist", "Character Changes Personality", "Character Dies", 
                                                          "Sudden Setting Change", "Weather Changes", "Enemy Appears",
                                                          "Problem is Not Solved", "Problem Solved Differently"] , index=0, 
                                    format_func=format_style, key=None, help=None, on_change=None, 
                                    args=None, kwargs=None, disabled=False, horizontal=False, 
                                    captions=None, label_visibility="visible", width="content")
        Other_2 = st.text_input("Other Twist")
        if Other_2 != "":
            twist_selection = Other_2










    # width_by_height_selection =  st.radio("Width", ["1024x1024", "1024x1536", "1536x1024"] , index=0, 
    #                                 format_func=format_style, key=None, help=None, on_change=None, 
    #                                 args=None, kwargs=None, disabled=False, horizontal=False, 
    #                                 captions=None, label_visibility="visible", width="content")

    
    generate_image_button = st.button("Generate Story", key=None, help=None, on_click=None, args=None, kwargs=None, type="primary", width="content")


if generate_image_button:
    analysis = generate_response(img_url)
    character_1_analysis = generate_response(character_1)
    character_2_analysis = generate_response(character_2)
    story_generation = generate_story(character_1_analysis, character_2_analysis, analysis, twist_selection, style_selection)

    st.text_area("Setting Analysis", value = analysis)
    st.text_area("Character 1 Analysis", value = character_1_analysis)
    st.text_area("Character 2 Analysis", value = character_2_analysis)  
    st.text_area("Story Generation", value = story_generation, height=300)


