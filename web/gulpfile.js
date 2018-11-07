var gulp           = require('gulp'), // Gulp
    sass           = require('gulp-sass'), // SASS,
    changed   = require('gulp-changed'), // Save time on processing unchanged files
    autoprefixer   = require('gulp-autoprefixer'); // Add the desired vendor prefixes and remove unnecessary in SASS-files


//
// SASS
//

// Unify Main
gulp.task('sass', function() {
  return gulp.src('./assets/include/scss/**/*.scss')
    .pipe(changed('./assets/css/'))
    .pipe(sass({outputStyle:'expanded'}))
    .pipe(autoprefixer(['last 3 versions', '> 1%'], { cascade: true }))
    .pipe(gulp.dest('./assets/css/'))
});

// E-commerce
gulp.task('sass-shop', function() {
  return gulp.src('./html/e-commerce/assets/scss/**/*.scss')
    .pipe(changed('./html/e-commerce/assets/css/'))
    .pipe(sass({outputStyle:'expanded'}))
    .pipe(autoprefixer(['last 3 versions', '> 1%'], { cascade: true }))
    .pipe(gulp.dest('./html/e-commerce/assets/css/'))
});

// Blog & Magazine
gulp.task('sass-blog', function() {
  return gulp.src('./html/blog-magazine/classic/assets/scss/**/*.scss')
    .pipe(changed('./html/blog-magazine/classic/assets/css/'))
    .pipe(sass({outputStyle:'expanded'}))
    .pipe(autoprefixer(['last 3 versions', '> 1%'], { cascade: true }))
    .pipe(gulp.dest('./html/blog-magazine/classic/assets/css/'))
});

// Multi Pages (Marketing Demo example, please change this path if you are using other demos)
gulp.task('sass-mp-marketing', function() {
  return gulp.src('./html/multipage/marketing/assets/scss/**/*.scss')
    .pipe(changed('./html/multipage/marketing/assets/css/'))
    .pipe(sass({outputStyle:'expanded'}))
    .pipe(autoprefixer(['last 3 versions', '> 1%'], { cascade: true }))
    .pipe(gulp.dest('./html/multipage/marketing/assets/css/'))
});

// One Page (Accounting Demo example, please change this path if you are using other demos)
gulp.task('sass-op', function() {
  return gulp.src('./assets/scss/**/*.scss')
    .pipe(changed('./assets/css/'))
    .pipe(sass({outputStyle:'expanded'}))
    .pipe(autoprefixer(['last 3 versions', '> 1%'], { cascade: true }))
    .pipe(gulp.dest('./assets/css/'))
});

// Dark Theme
gulp.task('sass-dt', function() {
  return gulp.src('./html/examples/dark-theme/assets/scss/**/*.scss')
    .pipe(changed('./html/examples/dark-theme/assets/css/'))
    .pipe(sass({outputStyle:'expanded'}))
    .pipe(autoprefixer(['last 3 versions', '> 1%'], { cascade: true }))
    .pipe(gulp.dest('./html/examples/dark-theme/assets/css/'))
});


//
// Watch
//

gulp.task('watch', function() {
  gulp.watch('./html/assets/include/scss/**/*.scss', ['sass']);
});


//
// Default
//

gulp.task('default', ['watch', 'sass']);