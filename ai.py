from openai import OpenAI
import base64

SYSTEM_PROMPT = """
Your job is to take an image URL and analyze it, describing key details from the image. 
"""



CLIENT = OpenAI(
    api_key = "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"
)
chat_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

# Character 1


def generate_response(character_1):
    PROMPT = f"""
       Analyze the image of a character in the URL given. Do not include any additional questions or requests for more information or descriptions of the background. 
        """
    


    print(PROMPT)
    result = CLIENT.responses.create(
        model="gpt-4o",
        input=[
            {"role": "user", "content": [
                {"type": "input_image", "image_url": character_1},
                {"type": "input_text", "text": PROMPT}
            ] }
        ]   
    )
    return result.output_text


# Character 2


def generate_response(character_2):
    PROMPT = f"""
       Analyze the image of a character in the URL given. Do not include any additional questions or requests for more information or descriptions of the background.
        """
    


    print(PROMPT)
    result = CLIENT.responses.create(
        model="gpt-4o",
        input=[
            {"role": "user", "content": [
                {"type": "input_image", "image_url": character_2},
                {"type": "input_text", "text": PROMPT}
            ] }
        ]   
    )
    return result.output_text


# Setting


def generate_response(img_url):
    PROMPT = f"""
       Analyze the image of a setting in the URL given. do not include any additional questions or requests for more information.
        """
    


    print(PROMPT)
    result = CLIENT.responses.create(
        model="gpt-4o",
        input=[
            {"role": "user", "content": [
                {"type": "input_image", "image_url": img_url},
                {"type": "input_text", "text": PROMPT}
            ] }
        ]   
    )
    return result.output_text


#Story Generation w/ Other 3 Analysis

def generate_story(character_1_analysis, character_2_analysis, analysis, twist_selection, style_selection):
    PROMPT = f"""
       Generate a 3 paragraphstory based on the following character and setting analyses. 
       Use the twist and style selections to create a unique story. 
       Do not include any additional questions or requests for more information.
       If in the other twist box or other style box
       Character 1 Analysis: {character_1_analysis}
       Character 2 Analysis: {character_2_analysis}
       Setting Analysis: {analysis}
       Twist: {twist_selection}
       Style: {style_selection}
        """
    


    print(PROMPT)
    result = CLIENT.responses.create(
        model="gpt-4o",
        input=[
            {"role": "user", "content": [
                {"type": "input_text", "text": PROMPT}
            ] }
        ]   
    )
    return result.output_text




# def generate_image(style_selection, color_selection, width_by_height_selection, analysis):
#     PROMPT_2 = f"""
#          Generate an image based on the analysis provided.
#          The style of the image should be {style_selection} and the dominant color should be {color_selection}.
#             Analysis: {analysis}
#         """
#     result = CLIENT.images.generate(
#         model="gpt-image-1",
#         prompt=PROMPT_2,
#         size = width_by_height_selection
#     )


    # image_base64 = result.data[0]['image_base64']
    # return base64.b64decode(image_base64)

