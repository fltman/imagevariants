from openai import OpenAI
import base64

# Skapar OpenAI-klient för att kommunicera med API:et
client = OpenAI() 

# Funktion för att konvertera en bildfil till base64-format
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Funktion för att skapa bildvarianter baserat på en originalbild och en prompt
def create_image_variants(image_path, prompt, output_path):
    # Konverterar originalbilden till base64-sträng
    base64_image = encode_image(image_path)

    # Skickar förfrågan till OpenAI API för att generera ny bildvariant
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": prompt },  # Textprompt som beskriver önskad förändring
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",  # Originalbilden i base64-format
                    },
                ],
            }
        ],
        tools=[{"type": "image_generation"}],  # Anger att vi vill generera bilder
    )

    # Extraherar bilddata från API-svaret
    image_data = [
        output.result
        for output in response.output
        if output.type == "image_generation_call"
    ]

    # Sparar den genererade bilden till fil om data finns
    if image_data:
        image_base64 = image_data[0]
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(image_base64))

# Skapar 5 varianter av bilden "mouse.jpg" med olika positioner för mössen
for i in range(5):
    create_image_variants("mouse.jpg", f"put the mouses in new positions", f"mouse_variant_{i}.png")

