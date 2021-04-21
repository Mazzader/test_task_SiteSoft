upstream django {
    server djangoapp:8000;
}

server {

    listen 80;
    server_name 80.87.96.170;

    location / {
        proxy_pass http://django;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }

    location /static/ {
        root /opt/test_task_SiteSoft;
        expires 30d;
    }
}