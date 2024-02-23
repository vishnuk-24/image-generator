import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SECRET_KEY = os.getenv("OPEN_API_SECRET_KEY")


def image_generator(image_text: str, image_size: str):
    """Generate an image based on text using the GPT-3 API."""
    try:
        client = OpenAI(api_key=SECRET_KEY)

        image_generate = client.images.generate(
            model="dall-e-3",
            prompt=image_text,
            size=image_size,
            quality="standard",
            n=2,  # Fix the number of generated images to 2
        )

        image_urls = [image.data.url for image in image_generate.data]
        return {"images": image_urls}
    except Exception as e:
        print(f"Error while connecting to Open AI API. Error: {str(e)}")
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    result = image_generator("A cute baby sea otter", "1024x1024")
    print(result["Image 1"])
