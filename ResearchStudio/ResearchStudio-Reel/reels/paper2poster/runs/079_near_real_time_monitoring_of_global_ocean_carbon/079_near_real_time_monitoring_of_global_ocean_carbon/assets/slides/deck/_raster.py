import asyncio, glob, os
from playwright.async_api import async_playwright
async def main():
    files=sorted(glob.glob("svg_output/*.svg"))
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1280,"height":720},device_scale_factor=1.5)
        for f in files:
            svg=open(f).read()
            await pg.set_content(f'<!doctype html><html><body style="margin:0">{svg}</body></html>')
            await pg.wait_for_timeout(120)
            out=f"_raster/{os.path.splitext(os.path.basename(f))[0]}.png"
            await pg.locator("svg").screenshot(path=out)
            print("rastered",out)
        await b.close()
asyncio.run(main())
