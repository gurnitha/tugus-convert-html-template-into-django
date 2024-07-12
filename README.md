# Convert HTML into DJANGO 


#### 1. Initial commit

        new file:   .gitignore
        new file:   README.md


#### 2. Membuat proyek django

        new file:   convert_html/convert_html/__init__.py
        new file:   convert_html/convert_html/asgi.py
        new file:   convert_html/convert_html/settings.py
        new file:   convert_html/convert_html/urls.py
        new file:   convert_html/convert_html/wsgi.py
        new file:   convert_html/manage.py


#### 3. Merubah nama folder proyek bagian dalam dengan nama src

        modified:   README.md
        renamed:    convert_html/convert_html/__init__.py -> src/convert_html/__init__.py
        renamed:    convert_html/convert_html/asgi.py -> src/convert_html/asgi.py
        renamed:    convert_html/convert_html/settings.py -> src/convert_html/settings.py
        renamed:    convert_html/convert_html/urls.py -> src/convert_html/urls.py
        renamed:    convert_html/convert_html/wsgi.py -> src/convert_html/wsgi.py
        renamed:    convert_html/manage.py -> src/manage.py


#### 4. Memodifikasi struktur file

        modified:   README.md
        renamed:    src/convert_html/__init__.py -> convert_html/__init__.py
        renamed:    src/convert_html/asgi.py -> convert_html/asgi.py
        renamed:    src/convert_html/settings.py -> convert_html/settings.py
        renamed:    src/convert_html/urls.py -> convert_html/urls.py
        renamed:    src/convert_html/wsgi.py -> convert_html/wsgi.py
        renamed:    src/manage.py -> manage.py


#### 5. Membuat aplikasi gym

        modified:   .gitignore
        modified:   README.md
        new file:   gym/__init__.py
        new file:   gym/admin.py
        new file:   gym/apps.py
        new file:   gym/migrations/__init__.py
        new file:   gym/models.py
        new file:   gym/tests.py
        new file:   gym/views.py


#### 6. Mendaftarkan app  gem  pada proyek

        modified:   README.md
        modified:   convert_html/settings.py


#### 7. Membuat laman home (urls, views, templates)

        modified:   convert_html/settings.py
        modified:   convert_html/urls.py
        new file:   gym/urls.py
        modified:   gym/views.py
        new file:   templates/gym/index.html


#### 8. Mengisi html template untuk laman home

        modified:   README.md
        modified:   templates/gym/index.html


#### 9. Mengisi static file

        modified:   README.md
        new file:   static/css/bootstrap.css
        new file:   static/css/responsive.css
        new file:   static/css/style.css
        ....
        new file:   static/js/bootstrap.js
        new file:   static/js/jquery-3.4.1.min.js


#### 10. Membuat path untuk static file

        modified:   README.md  
        modified:   convert_html/settings.py


#### 11. Load static file

        modified:   README.md
        modified:   templates/gym/index.html

####  Note: 12. Membuat commit setelah urut 11


#### 13. Membuat laman why

        modified:   README.md
        modified:   gym/urls.py
        modified:   gym/views.py
        new file:   templates/gym/why.html


#### 14. Membuat link untuk laman home dan why

        modified:   README.md
        modified:   templates/gym/index.html