
username='UserName'
password='Password'

login ()
{
res=`curl -s -X POST ${url} -d "action=login&username=${username}&password=${password}&ac_id=1"`
echo ${res}
}


logout()
{
res=`curl -s -X POST ${url} -d "action=logout"`
echo ${res}
}
md5=$(echo -n ${password} | md5sum | cut -d ' ' -f1)

url='http://net.tsinghua.edu.cn/do_login.php'

check=`curl -X POST -s ${url} -d "action=check_online"`
echo $check

login

