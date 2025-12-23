# F-Droid

Selection of FOSS for Windows, macOS and Linux

## Overviews

The overviews are:
- [English overview](overview-en.md)
- [Dutch overview](overview-nl.md)
- [Spanish overview](overview-es.md)

## Build

To build the overviews, install

```sh
sudo apt-get -y install python3-pip python3-venv
python3 -m venv .venv
. .venv/bin/activate
pip install -Ur requirements.txt
```

and then run `./build.sh`.

## TODO

https://get.alternative.to/

whatsapp -> telegram / signal

https://desktop.telegram.org/
https://syncthing.net/
https://signal.org/
https://apps.ankiweb.net/
https://mixxx.org/
https://desktop.jitsi.org/
https://mattermost.com/
https://handbrake.fr/
https://matrix.org/ecosystem/clients/ https://element.io/
https://mifi.no/losslesscut/

## Development

Install

```sh
. .venv/bin/activate
pip install -Ur requirements-dev.txt
```

Run the linters with `./lint.sh`.

