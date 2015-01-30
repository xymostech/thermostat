.PHONY: static/build/bundle.js
static/build/bundle.js:
	./node_modules/.bin/browserify -t reactify js/main.jsx -o $@
