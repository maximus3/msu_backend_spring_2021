echo ------------------------- STATIC TEST -------------------------
ab -c 10 -n 5000 -v 1 http://localhost:80/a.txt

echo ------------------------- GUNICORN TEST -------------------------
ab -c 10 -n 5000 -v 1 http://localhost:8000/

echo ------------------------- GUNICORN PROXY TEST -------------------------
ab -c 10 -n 5000 -v 1 http://localhost:80/api 

echo ------------------------- ERROR TEST -------------------------
ab -c 400 -n 5000 -v 1 http://localhost:80/api 
