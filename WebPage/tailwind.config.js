/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/public/main.html", "./templates/public/tinnydev.html", "./static/src/script.js"],
  theme: {
    extend: {},
  },
  plugins: [],
  "scripts": {

    "build-css": "tailwindcss build -i ./static/src/input.css -o ./static/styles.css --watch"

  },

}
