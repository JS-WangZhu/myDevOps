import re
import time

f = open('secure', 'r', encoding='utf-8')
all_ban_ipd = []
for i in f.readlines():
    if i.find('Failed password')!=-1:
        trueIp = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', i)
        ipduan = str(trueIp[0]).split('.')[0] +'.'+ str(trueIp[0]).split('.')[1] +'.'+ str(trueIp[0]).split('.')[2]+'.*'
        all_ban_ipd.append(ipduan)
f.close()
ban_dic = {}
for i in all_ban_ipd:
    if i in ban_dic:
        ban_dic[i]+=1
    else:
        ban_dic[i]=1
final_ban = []
for i in ban_dic:
    if ban_dic[i]>=10:
        final_ban.append(i)
fr = open('hosts.deny','w',encoding='utf-8')
fr.write('# hosts.deny\n')
fr.write('# 更新时间 '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'\n')
fr.write('# Ban ip段总数：'+str(len(final_ban))+'\n')
for i in final_ban:
    template = 'sshd:'+i+':deny'
    fr.write(template)
    fr.write('\n')
fr.close()