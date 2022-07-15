server{
    listen 80;
    server_name pe-weel1-demo.duckdns.org;

    if ($host = pe-week1-demo.duckdns.org){
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name pe-week1-demo.duckdns.org;

    location / {
        proxy_pass http://localhost:5000;
    }
    
    # Load the certificate files.
    ssl_certificates /etc/letsencrypt/live/myportfolio/fullchain.pem;
    ssl_certificate_key
/etc/letsencrypt/live/myportfolio/privkey.pem;
    ssl_trusted_certificate
/etc/letsencrypt/live/myportfolio/chain.pem;
}
