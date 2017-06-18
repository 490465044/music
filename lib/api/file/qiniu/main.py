#  _*_coding:utf-8 _*_
# NAME = 'main'  
# USER = 'W.Tj'
# EMAIL = 'wangtengjiao1@gmail.com'
# TIME = '2017/2/15 17:34'
# ____________________分割线___________________
from qiniu import Auth
from qiniu import Auth, put_file, etag, urlsafe_base64_encode


#需要填写你的 Access Key 和 Secret Key
access_key = 'QLeHr8OXAYzqIRQH586nH67qbKJTwSrW9doGh_oX'
secret_key = '99xDDboAOueGyOw7vkD459hBbrMIEPDSltHlQ9sH'

# 构造上传函数
def token(access_key, secret_key, bucket_name, key):
    '''
    :param access_key: 七牛账户的key默认为系统设置key如果不是可以重设！
    :param secret_key:七牛账户的secret_key默认为系统值
    :param bucket_name: 要上传的空间
    :param key: 上传到七牛后保存的文件名
    '''
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    t = q.upload_token(bucket_name, key, 3600)
    return

    policy = {
        'callbackUrl': 'http://your.domain.com/callback.php',
        'callbackBody': 'filename=$(fname)&filesize=$(fsize)'
    }
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket=bucket_name, expires=3600, policy=policy)
    ret, info = put_file(token, key, file)
    print token
    print info
    assert ret['key'] == key
    assert ret['hash'] == etag(file)
    return 'http://7xiie2.com1.z0.glb.clouddn.com/'+ key


