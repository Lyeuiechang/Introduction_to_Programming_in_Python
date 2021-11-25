import re
def dehtml(text):
    # Reture the text that replaced each tag with a blank space
    replaced_text = re.sub(r'<.*?>'," ",text)
    return replaced_text
html_text = input()
print(dehtml(html_text))