/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        'Success': 'teal-400',
        'Error': 'red-500',
      },
    },
  },
  plugins: [],
}

