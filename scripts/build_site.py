import os
import jinja2

os.makedirs("site", exist_ok=True)

env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

# Render the index.
top_level = env.get_template("index.html.j2")

my_string = "Hello_world"
my_string_es = "Hola_mundo"

top_en = {"language": "en", "my_string": my_string}
top_level.stream(top_en).dump("site/index.html")


top = {"language": "es", "my_string": my_string_es}
top_level.stream(top).dump("site/index.es.html")
