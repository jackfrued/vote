import hashlib
import random

from rest_framework.authentication import BaseAuthentication

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def gen_md5_digest(content):
    """将字符串处理成MD5摘要"""
    return hashlib.md5(content.encode()).hexdigest()


def gen_sha256_digest(content):
    """将字符串处理成SHA-256摘要"""
    return hashlib.sha256(content.encode()).hexdigest()


def gen_random_code(length=4):
    """生成指定长度的随机验证码"""
    return ''.join(random.choices(ALL_CHARS, k=length))
