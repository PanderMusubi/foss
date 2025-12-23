"""Generate documentation on selected FOSS software."""

from json import load
from glob import glob
from typing import TextIO

from pycountry import countries

# pylint:disable=unspecified-encoding


def flag(lang: str) -> str:
    """Get flag for language."""
    lang = lang.upper()
    if lang == 'EN':
        lang = 'GB'
    return countries.get(alpha_2=lang).flag


def header(mado: TextIO, references: dict, headers: dict, lang: str) -> None:
    """Write Markdown header."""
    for reference, value in sorted(references.items()):
        if reference != lang:
            mado.write(f'_{flag(reference)} {value}'
                       f' [overview-{reference}.md]'
                       f'(overview-{reference}.md)_\n\n')
    mado.write(f'{headers[lang]}\n\n')


def footer(mado: TextIO, footers: dict, lang: str) -> None:
    """Write Markdown footer."""
    mado.write(f'{footers[lang]}\n\n')


def read_json() -> tuple:
    """Read the JSON file with all the data."""
    with open('data.json') as file:
        data = load(file)
        return (data['references'], data['headers'], data['footers'],
                data['categories'])
    # TODO fennec addons


def generate() -> None:
    """Generate files."""
    references, headers, footers, categories = read_json()
    for lang in sorted(references):
        with open(f'overview-{lang}.md', 'w') as mado:
            header(mado, references, headers, lang)
            mado.write('<table>\n')
            icons = set()
            for category in categories:
                replaces_title = 'Replaces'
                if lang == 'nl':
                    replaces_title = 'Vervangt'
                elif lang == 'es':
                    pass  # TODO
                mado.write(f'<tr><th colspan="2"><br>{category["name"][lang]}'
                           f'</th><th><br>{replaces_title}</th></tr>\n')
                for app in category['apps']:
                    url = ''
                    it = ''
                    if 'id' in app:
                        it = app['id']
                        url = f'https://f-droid.org/en/packages/{it}'
                    else:
                        it = app['name'].lower().replace(' ', '-')
                        url = app['url']
                    icon = f'icons/{it}.png'
                    mado.write(f'<tr id="{it}"><td><a target="_blank"'
                               f' href="{url}"><img alt="icon" width="128px"'
                               f' src="{icon}"></a></td>\n')
                    mado.write('<td valign="top"><a target="_blank"'
                               f' href="{url}"><strong>{app["name"]}'
                               '</strong></a><br>\n')
                    links = []
                    if 'mobile' in app:
                        links.append(f'<a target="_blank" href="https://github.com/PanderMusubi/fdroid/blob/main/overview-{lang}.md#{app["mobile"]}">MB</a>')
                    if 'desktop' in app:
                        links.append(f'<a target="_blank" href="https://github.com/PanderMusubi/foss/blob/main/overview-{lang}.md#{app["desktop"]}">DT</a>')
                    if 'apt' in app:
                        links.append(f'<a target="_blank" href="{app["apt"]}">AP</a>')
                    if 'flathub' in app:
                        links.append(f'<a target="_blank" href="https://flathub.org/apps/{app["flathub"]}">FH</a>')
                    if 'snapcraft' in app:
                        links.append(f'<a target="_blank" href="https://snapcraft.io/{app["snapcraft"]}">SC</a>')
                    if 'alternativeto' in app:
                        links.append(f'<a target="_blank" href="https://alternativeto.net/software/{app["alternativeto"]}/about/">AT</a>')
                    if 'osalternative' in app:
                        links.append(f'<a target="_blank" href="https://osalternative.to/project/{app["alternativeto"]}">OA</a>')
                    mado.write(f'{app["description"][lang]}<br><small>{" ".join(links)}</small></td>\n')
                    if lang == 'en' and icon in icons:
                        print(f'WARNING: Duplicate use if icon {icon}')
                    icons.add(icon)
                    replaces = app.get('replaces', '')
                    mado.write(f'<td valign="top"><font color="red">{replaces}</font></td></tr>\n')
            mado.write('</table>\n\n')
            footer(mado, footers, lang)
    for file in sorted(glob('icons/*')):
        if file not in icons:
            print(f'WARNING: Unused icon file {file}')


if __name__ == '__main__':
    generate()
