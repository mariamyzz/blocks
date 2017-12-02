var gulp = require('gulp'),
    sass = require('gulp-sass'),
    watch = require('gulp-watch'),
    concat = require('gulp-concat'),
    prefixer = require('gulp-autoprefixer'),
    cssmin = require('gulp-minify-css'),
    rename = require('gulp-rename'),
    uglify = require('gulp-uglify'),
    rigger = require('gulp-rigger'),
    htmlhint = require("gulp-htmlhint"),
    changed = require('gulp-changed'),
    gpath = require('path'),
    fs = require('fs'),
    fspath = require('path'),
    sourcemaps = require('gulp-sourcemaps');

var path = {
    build: {
        js: 'server/static/js',
        style: 'server/static/css'
    },
    app: {
        js: 'blocks/templates/**/*.js',
        style: 'blocks/templates/**/*.sass'
    },
    watch: {
        js: 'blocks/templates/**/*.js',
        style: 'blocks/templates/**/*.sass',
    }
};

gulp.task('js:build', function () {
    gulp.src(path.app.js)
        .pipe(concat('common.js'))
        .pipe(rigger())
        .pipe(uglify())
        .pipe(rename({ suffix: '.min' }))
        .pipe(gulp.dest(path.build.js));
});

gulp.task('style:build', function () {
    gulp.src(path.app.style)
        .pipe(concat('common.sass'))
        .pipe(sass())
        .pipe(prefixer())
        .pipe(gulp.dest(path.build.style));
});

gulp.task('build', [
    'js:build',
    'style:build'
]);

gulp.task('watch', [], function () {
    watch([path.watch.style], function (event, cb) {
        gulp.start('style:build');
    });
    watch([path.watch.js], function (event, cb) {
        gulp.start('js:build');
    });
});

gulp.task('default', ['build', 'watch']);