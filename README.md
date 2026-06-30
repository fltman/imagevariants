# Image Variants

[![Support me on Patreon](https://img.shields.io/badge/Patreon-Support%20my%20work-FF424D?style=flat&logo=patreon&logoColor=white)](https://www.patreon.com/AndersBjarby)

Ett litet Python-skript som skapar flera varianter av en bild med OpenAI:s bildgenerering. Det läser en originalbild, skickar den tillsammans med en textprompt till modellen och sparar de genererade varianterna som PNG-filer.

## Så funkar det

- Läser en originalbild och kodar den till base64
- Anropar `gpt-4.1` med `image_generation`-verktyget och din prompt
- Sparar varje variant till disk (skriptet skapar 5 varianter av `mouse.jpg` som exempel)

## Kom igång

```bash
pip install openai
export OPENAI_API_KEY=sk-...
python create_image_variants.py
```

Justera bildfil, prompt och antal varianter direkt i `create_image_variants.py`.

## Teknik

Python, OpenAI Python SDK (Responses API med image generation).
