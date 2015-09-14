exports.config =
  paths:
    public: 'static'
    watched: ['public']
  files:
    javascripts:
      joinTo: 'js/bulletin.js'
    stylesheets:
      joinTo: 'css/bulletin.css'
    templates:
      joinTo: 'js/bulletin.js'
  plugins:
    sass:
      options:
        allowCache: false
        options: ['--style expanded']
