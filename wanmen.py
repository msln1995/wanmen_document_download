from urllib import response
import requests
import json
import js2py
import sys
from turtle import width

from time import time
from multiprocessing.pool import ThreadPool
 
if len(sys.argv) < 2:
    print("参数错误");
    exit();
coursesId = str(sys.argv[1])
f = open('./Authorization.ini', 'r')
Authorization = f.read()

tokenKey = "****请自己获取****"

context = js2py.EvalJs()
js = '''
//定义x-token
function antitoken(e) {
    var a12 = {
        utf8: {
			stringToBytes: function(e) {
				return a12.bin.stringToBytes(unescape(encodeURIComponent(e)))
			},
			bytesToString: function(e) {
				return decodeURIComponent(escape(r.bin.bytesToString(e)))
			}
		},
		bin: {
			stringToBytes: function(e) {
				for (var t = [], r = 0; r < e.length; r++) t.push(255 & e.charCodeAt(r));
				return t
			},
			bytesToString: function(e) {
				for (var t = [], r = 0; r < e.length; r++) t.push(String.fromCharCode(e[r]));
				return t.join("")
			}
		}
    };
    var t = null;
    var n, i, o, s, r;
	r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", 
    n = {
		rotl: function(e, t) {
			return e << t | e >>> 32 - t
		},
		rotr: function(e, t) {
			return e << 32 - t | e >>> t
		},
		endian: function(e) {
			if (e.constructor == Number) return 16711935 & n.rotl(e, 8) | 4278255360 & n.rotl(e, 24);
			for (var t = 0; t < e.length; t++) e[t] = n.endian(e[t]);
			return e
		},
		randomBytes: function(e) {
			for (var t = []; e > 0; e--) t.push(Math.floor(256 * Math.random()));
			return t
		},
		bytesToWords: function(e) {
			for (var t = [], r = 0, n = 0; r < e.length; r++, n += 8) t[n >>> 5] |= e[r] << 24 - n % 32;
			return t
		},
		wordsToBytes: function(e) {
			for (var t = [], r = 0; r < 32 * e.length; r += 8) t.push(e[r >>> 5] >>> 24 - r % 32 & 255);
			return t
		},
		bytesToHex: function(e) {
			for (var t = [], r = 0; r < e.length; r++) t.push((e[r] >>> 4)
				.toString(16)), t.push((15 & e[r])
				.toString(16));
			return t.join("")
		},
		hexToBytes: function(e) {
			for (var t = [], r = 0; r < e.length; r += 2) t.push(parseInt(e.substr(r, 2), 16));
			return t
		},
		bytesToBase64: function(e) {
			for (var t = [], n = 0; n < e.length; n += 3)
				for (var i = e[n] << 16 | e[n + 1] << 8 | e[n + 2], a = 0; a < 4; a++) 8 * n + 6 * a <= 8 * e.length ? t.push(r.charAt(i >>> 6 * (3 - a) & 63)) : t.push("=");
			return t.join("")
		},
		base64ToBytes: function(e) {
			e = e.replace(/[^A-Z0-9+\/]/gi, "");
			for (var t = [], n = 0, i = 0; n < e.length; i = ++n % 4) 0 != i && t.push((r.indexOf(e.charAt(n - 1)) & Math.pow(2, -2 * i + 8) - 1) << 2 * i | r.indexOf(e.charAt(n)) >>> 6 - 2 * i);
			return t
		}
    }, i = a12.utf8, a = null, o = a12.bin, (s = function(e, t) {
        e.constructor == String ? e = t && "binary" === t.encoding ? o.stringToBytes(e) : i.stringToBytes(e) : a(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || e.constructor === Uint8Array || (e = e.toString());
			for (var r = n.bytesToWords(e), c = 8 * e.length, l = 1732584193, u = -271733879, d = -1732584194, _ = 271733878, p = 0; p < r.length; p++) r[p] = 16711935 & (r[p] << 8 | r[p] >>> 24) | 4278255360 & (r[p] << 24 | r[p] >>> 8);
			r[c >>> 5] |= 128 << c % 32, r[14 + (c + 64 >>> 9 << 4)] = c;
			var f = s._ff,
				h = s._gg,
				m = s._hh,
				g = s._ii;
			for (p = 0; p < r.length; p += 16) {
				var v = l,
					b = u,
					y = d,
					E = _;
				u = g(u = g(u = g(u = g(u = m(u = m(u = m(u = m(u = h(u = h(u = h(u = h(u = f(u = f(u = f(u = f(u, d = f(d, _ = f(_, l = f(l, u, d, _, r[p + 0], 7, -680876936), u, d, r[p + 1], 12, -389564586), l, u, r[p + 2], 17, 606105819), _, l, r[p + 3], 22, -1044525330), d = f(d, _ = f(_, l = f(l, u, d, _, r[p + 4], 7, -176418897), u, d, r[p + 5], 12, 1200080426), l, u, r[p + 6], 17, -1473231341), _, l, r[p + 7], 22, -45705983), d = f(d, _ = f(_, l = f(l, u, d, _, r[p + 8], 7, 1770035416), u, d, r[p + 9], 12, -1958414417), l, u, r[p + 10], 17, -42063), _, l, r[p + 11], 22, -1990404162), d = f(d, _ = f(_, l = f(l, u, d, _, r[p + 12], 7, 1804603682), u, d, r[p + 13], 12, -40341101), l, u, r[p + 14], 17, -1502002290), _, l, r[p + 15], 22, 1236535329), d = h(d, _ = h(_, l = h(l, u, d, _, r[p + 1], 5, -165796510), u, d, r[p + 6], 9, -1069501632), l, u, r[p + 11], 14, 643717713), _, l, r[p + 0], 20, -373897302), d = h(d, _ = h(_, l = h(l, u, d, _, r[p + 5], 5, -701558691), u, d, r[p + 10], 9, 38016083), l, u, r[p + 15], 14, -660478335), _, l, r[p + 4], 20, -405537848), d = h(d, _ = h(_, l = h(l, u, d, _, r[p + 9], 5, 568446438), u, d, r[p + 14], 9, -1019803690), l, u, r[p + 3], 14, -187363961), _, l, r[p + 8], 20, 1163531501), d = h(d, _ = h(_, l = h(l, u, d, _, r[p + 13], 5, -1444681467), u, d, r[p + 2], 9, -51403784), l, u, r[p + 7], 14, 1735328473), _, l, r[p + 12], 20, -1926607734), d = m(d, _ = m(_, l = m(l, u, d, _, r[p + 5], 4, -378558), u, d, r[p + 8], 11, -2022574463), l, u, r[p + 11], 16, 1839030562), _, l, r[p + 14], 23, -35309556), d = m(d, _ = m(_, l = m(l, u, d, _, r[p + 1], 4, -1530992060), u, d, r[p + 4], 11, 1272893353), l, u, r[p + 7], 16, -155497632), _, l, r[p + 10], 23, -1094730640), d = m(d, _ = m(_, l = m(l, u, d, _, r[p + 13], 4, 681279174), u, d, r[p + 0], 11, -358537222), l, u, r[p + 3], 16, -722521979), _, l, r[p + 6], 23, 76029189), d = m(d, _ = m(_, l = m(l, u, d, _, r[p + 9], 4, -640364487), u, d, r[p + 12], 11, -421815835), l, u, r[p + 15], 16, 530742520), _, l, r[p + 2], 23, -995338651), d = g(d, _ = g(_, l = g(l, u, d, _, r[p + 0], 6, -198630844), u, d, r[p + 7], 10, 1126891415), l, u, r[p + 14], 15, -1416354905), _, l, r[p + 5], 21, -57434055), d = g(d, _ = g(_, l = g(l, u, d, _, r[p + 12], 6, 1700485571), u, d, r[p + 3], 10, -1894986606), l, u, r[p + 10], 15, -1051523), _, l, r[p + 1], 21, -2054922799), d = g(d, _ = g(_, l = g(l, u, d, _, r[p + 8], 6, 1873313359), u, d, r[p + 15], 10, -30611744), l, u, r[p + 6], 15, -1560198380), _, l, r[p + 13], 21, 1309151649), d = g(d, _ = g(_, l = g(l, u, d, _, r[p + 4], 6, -145523070), u, d, r[p + 11], 10, -1120210379), l, u, r[p + 2], 15, 718787259), _, l, r[p + 9], 21, -343485551), l = l + v >>> 0, u = u + b >>> 0, d = d + y >>> 0, _ = _ + E >>> 0
			}
			return n.endian([l, u, d, _])
    })._ff = function(e, t, r, n, i, a, o) {
        var s = e + (t & r | ~t & n) + (i >>> 0) + o;
        return (s << a | s >>> 32 - a) + t
    }, s._gg = function(e, t, r, n, i, a, o) {
        var s = e + (t & n | r & ~n) + (i >>> 0) + o;
        return (s << a | s >>> 32 - a) + t
    }, s._hh = function(e, t, r, n, i, a, o) {
        var s = e + (t ^ r ^ n) + (i >>> 0) + o;
        return (s << a | s >>> 32 - a) + t
    }, s._ii = function(e, t, r, n, i, a, o) {
        var s = e + (r ^ (t | ~n)) + (i >>> 0) + o;
        return (s << a | s >>> 32 - a) + t
    };
    s._blocksize = 16;
    s._digestsize = 16;
    var a = n.wordsToBytes(s(e, t));
    return t && t.asBytes ? a : t && t.asString ? s.bytesToString(a) : n.bytesToHex(a);
}
'''

xtime = '''
 var x_time = Math.round((new Date).getTime() / 1e3).toString(16);
'''
context.execute(xtime)
x_time = context.x_time

xtoken = "xtoken = antitoken('"+ tokenKey + x_time + "')"
context.execute(js + xtoken)
xtoken = context.xtoken

session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type":"application/json; charset=utf-8",
    "x-sa":"9e2fc61b78106962a1fa5c5ba6874acaaf0cabfecb6f85ae2d4a082b672b9139f1466529572da95c36dd39a7cf9c8444",
    "x-platform":"web",
    "x-app":"uni",
    "x-time":x_time,
    "x-token":xtoken,
    "Authorization":"Bearer " + Authorization
}
# 设置session的请求头信息
session.headers = headers
response = session.get("https://api.wanmen.org/4.0/content/v2/courses/" + coursesId)
res = response.content;
课程列表 = json.loads(res) 
arrData = []
for item in 课程列表["documents"]:
    if "." in item["name"]:
        arrData.append((item["name"], item["url"]))
    else:
        pos = item["url"].rfind(".")
        file_type = item["url"][pos:]
        arrData.append((item["name"] + file_type, item["url"]))

def url_response(url):
    path,url = url
    r = requests.get(url, stream=True, headers=headers)

    path = "./Download/" + path
    with open(path, "wb") as f:
        for ch in r:
            f.write(ch)

start = time()
for x in arrData:
    url_response(x)
print(f"Time to dowmload: {time() - start}")
ThreadPool(len(课程列表["documents"])).imap_unordered(url_response, arrData)
