all: iptc needs

iptc:
	./pyenv/bin/python iptc.py

needs:
	./pyenv/bin/python user_needs.py
