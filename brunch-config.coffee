exports.config =
  paths:
    public: 'static'
    watched: ['public', 'vendor']
  files:
    javascripts:
      joinTo:
        'js/bulletin.js': /^public/
        'js/vendor.js': /^vendor|bower_components/
    stylesheets:
      joinTo: 'css/bulletin.css'
    templates:
      joinTo: 'js/bulletin.js'
  plugins:
    sass:
      options:
        allowCache: false
        options: ['--style expanded']
        includePaths: [
          'bower_components/bourbon/app/assets/stylesheets/'
          'bower_components/neat/app/assets/stylesheets/'
        ]
