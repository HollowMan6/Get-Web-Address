# -*- coding:utf-8 -*-
# by 'hollowman6' from Lanzhou University(兰州大学)

import re
from Crypto.Cipher import AES


def encrypUrl(protocol, url):
    port = ""
    segments = ""

    if url[:7] == "http://":
        url = url[7:]
    elif url[:8] == "https://":
        url = url[8:]

    v6 = ""
    match = re.compile("/\[[0-9a-fA-F:]+?\]/").match(url)
    if match:
        v6 = match[0]
        url = url[len(match[0]):]
    segments = url.split("?")[0].split(":")
    if len(segments) > 1:
        port = segments[1].split("/")[0]
        url = url[0:len(segments[0])] + url[len(segments[0]) + len(port) + 1:]

    if protocol != "connection":
        i = url.find('/')
        if i == -1:
            if v6 != "":
                url = v6
            url = encrypt(url, "wrdvpnisthebest!", 'wrdvpnisthebest!')
        else:
            host = url[:i]
            path = url[i:]
            if v6 != "":
                host = v6
            url = encrypt(host, "wrdvpnisthebest!", 'wrdvpnisthebest!') + path
    if port != "":
        url = "/" + protocol + "-" + port + "/" + url
    else:
        url = "/" + protocol + "/" + url
    return url


def encrypt(text, key, iv):
    textLength = len(text)
    text = textRightAppend(text, 'utf8')
    keyBytes = key.encode(encoding='UTF-8')
    ivBytes = iv.encode(encoding='UTF-8')
    textBytes = text.encode(encoding='UTF-8')
    aesCfb = AES.new(keyBytes, AES.MODE_CFB, ivBytes, segment_size=128)
    encryptBytes = aesCfb.encrypt(textBytes)
    return ivBytes.hex() + encryptBytes.hex()[:textLength * 2]


def textRightAppend(text, mode):
    segmentByteSize = 32
    if mode == 'utf8':
        segmentByteSize = 16

    if len(text) % segmentByteSize == 0:
        return text

    appendLength = segmentByteSize - len(text) % segmentByteSize
    for i in range(appendLength):
        text += '0'
    return text


if __name__ == '__main__':
    import webbrowser
    host = "https://vpnx.lzu.edu.cn"
    print("Support HTTPS, HTTP, SSH, RDP, VNC")
    protocol = input("Please enter the protocol:")
    message = "Please enter the address, [ADDR: PORT]，eg：192.168.0.1:22\n"
    while True:
        if protocol.upper() in ["HTTPS", "HTTP", "SSH", "RDP", "VNC"]:
            if protocol.upper() in ["HTTPS", "HTTP"]:
                message = "Please enter the URL:\n"
            break
        else:
            protocol = input("Wrong protocal, please enter the protocol:")
    address = input(message)
    url = encrypUrl(protocol, address)
    print("Address for LZU vpnx:")
    print(url)
    url = host+url
    webbrowser.open(url)
