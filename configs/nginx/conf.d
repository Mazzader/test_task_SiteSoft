upstream django {
    server djangoapp:8800;
}

server {

    listen 80;
    server_name _;

    location / {
        proxy_pass http://django;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }