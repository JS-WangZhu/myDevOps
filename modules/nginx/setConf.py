import os
import time

class setConf():
    def __init__(self):
        # 数据库获取
        self.raw_conf_path = '/usr/local/etc/nginx'
        self.conf_dir = '/usr/local/etc/nginx/servers'

    def addConf(self):
        f = open('tmp/tmp.txt', 'w+', encoding='utf-8')
        conf_name = ""
        server_name = "www.iwangzhu.cn  iwangzhu.cn 118.195.148.81"
        access_log = "/root/logs/www.access.log"
        error_log = "/root/logs/www.error.log"
        ssl_certificate = "/root/cert/iwangzhu.cn.crt"
        ssl_certificate_key = "/root/cert/iwangzhu.cn.key"
        proxy_pass = "http://localhost:8443"
        template_conf = "server {\n" +\
        "    listen 443 ssl;\n" +\
        "    server_name "+server_name+";\n" +\
        "\n" +\
        "    access_log "+access_log+" main;\n" +\
        "    error_log "+error_log+";\n" +\
        "    root   html;\n" +\
        "    index  index.html index.htm index.php;\n" +\
        "    ssl_certificate "+ssl_certificate+";   #将domain name.pem替换成您证书的文件名。\n" +\
        "    ssl_certificate_key "+ssl_certificate_key+";   #将domain name.key替换成您证书的密钥文件名。\n" +\
        "    ssl_session_timeout 5m;\n" +\
        "    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;  #使用此加密套件。\n" +\
        "    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;   #使用该协议进行配置。\n" +\
        "    ssl_prefer_server_ciphers on;\n" +\
        "    ## send request back to apache ##\n" +\
        "    location / {\n" +\
        "        proxy_pass  "+proxy_pass+";\n" +\
        "        #if  (  $http_frontend_protocol = 'http') {\n" +\
        "         #return 301 https://$host$request_uri;\n" +\
        "        #}\n" +\
        "        #Proxy Settings\n" +\
        "        proxy_redirect     off;\n" +\
        "        proxy_set_header   Host             $host;\n" +\
        "        proxy_set_header   X-Real-IP        $remote_addr;\n" +\
        "        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;\n" +\
        "        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;\n" +\
        "        proxy_max_temp_file_size 0;\n" +\
        "        proxy_connect_timeout      90;\n" +\
        "        proxy_send_timeout         90;\n" +\
        "        proxy_read_timeout         90;\n" +\
        "        proxy_buffer_size          4k;\n" +\
        "        proxy_buffers              4 32k;\n" +\
        "        proxy_busy_buffers_size    64k;\n" +\
        "        proxy_temp_file_write_size 64k;\n" +\
        "   }\n" +\
        "    location /nginx_status{\n" +\
        "        stub_status on;\n" +\
        "        access_log off;\n" +\
        "}\n" +\
        "}\n"

        f.write(template_conf)
        f.close()

    def delConf(self):
        pass

    def modifyConf(self):
        pass