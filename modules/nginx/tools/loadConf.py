import os
import subprocess
import json


def exec_cmd(cmd):
    out_result = []
    err_result = []
    res = subprocess.Popen(cmd + ' ;echo $?', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for i in res.stdout.readlines():
        out_result.append(i.decode().replace('\n', ''))
    for i in res.stderr.readlines():
        err_result.append(i.decode().replace('\n', ''))
    return json.dumps({'return_code': int(out_result[-1]), 'stdout': out_result[:-1], 'stderr': err_result})


def search_conf(filepath='/usr/local'):
    cmd = 'find ' + filepath + ' -name nginx.conf'
    a = exec_cmd(cmd)
    return json.loads(a)['stdout']




search_conf()
