import os
import subprocess
import time

class setConf():
    def __init__(self):
        # 数据库获取
        self.raw_conf_path = '/usr/local/etc/nginx'
        self.conf_dir = '/usr/local/etc/nginx/servers'
        self.conf_name = ''
        self.ssl_certificate = '.crt'
        self.ssl_certificate_key = '.key'


    def addConf(self):
        f = open('tmp/tmp.txt', 'w+', encoding='utf-8')
        server_name = "www.iwangzhu.cn  iwangzhu.cn 118.195.148.81"
        access_log = self.conf_name+"_acc.log"
        error_log = self.conf_name+"_err.log"
        # 创建日志文件
        cmd = 'mkdir -p '+self.conf_dir+'/'+self.conf_name+'/logs '+'& clear'+'& touch '+\
                  self.conf_dir+'/'+self.conf_name+'/logs/'+access_log\
                  +' & touch '+self.conf_dir+'/'+self.conf_name+'/logs/'+error_log
        # print(cmd)
        os.system(cmd)
        ssl_certificate = self.conf_dir+'/'+self.conf_name+'/'+self.conf_name+self.ssl_certificate
        ssl_certificate_key = self.conf_dir+'/'+self.conf_name+'/'+self.conf_name+self.ssl_certificate_key
        proxy_pass = "http://localhost:8443"
        template_conf = "server {\n" +\
        "    listen 443 ssl;\n" +\
        "    server_name "+server_name+";\n" +\
        "    access_log "+self.conf_dir+'/'+self.conf_name+'/logs/'+access_log+" main;\n" +\
        "    error_log "+self.conf_dir+'/'+self.conf_name+'/logs/'+error_log+";\n" +\
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
        # 上传证书


        f.write(template_conf)
        f.close()
        # 移动文件
        os.system("mv tmp/tmp.txt " + self.conf_dir + "/" + self.conf_name + '/' + self.conf_name + '.conf')
        # 检查文件
        r = self.checkConf()
        print(r)
        if r['status']==True:
            return {'status': True, 'msg': '添加成功'}
        else:
            return {'status': False, 'msg': '添加失败'}


    def delConf(self):
        a = os.listdir(self.conf_dir)
        print(a)
        pass


    def modifyConf(self):
        pass


    def checkConf(self):
        f = subprocess.Popen('nginx -t', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        m = f.stderr.readlines()
        msg = ''
        for x in m:
            tmp = str(x)[2:-1]
            msg += tmp
        if msg.find('failed') > -1:
            status = False
        else:
            status = True
        return {'status': status, 'msg': msg}

    def reloadConf(self):
        os.system('nginx -s reload')

if __name__ == '__main__':
    c = setConf()
    # c.conf_name = 'test2'
    # aa = c.addConf()
    # print(aa)
    # # a = c.checkConf()
    # # print(a)
    c.delConf()