# jinja2_website_translations
A static simple example website created using jinja2, with support for translations

## Description

I want to help translating https://electioncal.us/ to Spanish. I have worked with jinja2 templates for ansible stuff, but never for making websites.

This is a repo to test how to build a mini site that is simple enough to test the translation integrations for jinja2 under python3.

## Usage

So, this is a blank repo project that does not have any translations **yet**. The following commands, on the root of the project will extract the strings found on the python code and hopefully the jinja2 templates, and create them in text files with extension ``.pot``

```bash
mkdir -pv ./lang/{en_US,es_ES}/LC_MESSAGES/

# Extractor. Finds .py files but not jinja2 o html
# This step will create the file lang/messages.pot
pybabel -v extract  -o ./lang/messages.pot ./

# This is how you create a catalog, in this example for spanish
# You run this only the first time
pybabel init -l es_ES -d ./lang -i ./lang/messages.pot

# The other times, you run this
pybabel update -l es_ES -d ./lang -i ./lang/messages.pot

# Last step, we turn the .pot text files into binary .mo files
pybabel compile -f -d ./lang
```


## Status

- [x] Basic site.
- [x] Translations with gettext.
- [ ] Translations with gettext and jinja2 templates
- [x] Documenation on how to use.
