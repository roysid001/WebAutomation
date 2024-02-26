import webbrowser as wb

def webauto():
    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    URLs = (
        "stackoverflow.com",
        "youtube.com",
        "linkedin.com",
        "google.com",
        "github.com/roysid001"
    )
    wb.register('chrome', None, wb.BackgroundBrowser(chrome_path))
    for url in URLs:
        print("opening: "+url)
        wb.get('chrome').open(url)

webauto()