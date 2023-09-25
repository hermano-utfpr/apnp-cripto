import sys
import datetime
import hmac
import hashlib

document = nome = sys.argv[1];
today = datetime.datetime.today().day

keys = { 1:'uEArdG',
         2:'BP6OIs',
         3:'ufzns2',
         4:'7QUmdh',
         5:'WSKc7W',
         6:'jqZqFB',
         7:'o2YiIF',
         8:'PqkzPQ',
         9:'ByrQb7',
        10:'irrvuI',
        11:'FyFGzk',
        12:'pWmCWD',
        13:'0j8s8J',
        14:'y6gro1',
        15:'DgaeRt',
        16:'3K6mVF',
        17:'ztt9HN',
        18:'8LoKcx',
        19:'C1Jtkx',
        20:'pPQORe',
        21:'TRISb5',
        22:'Xe49gH',
        23:'3LY62E',
        24:'JgLdxE',
        25:'K70osr',
        26:'GIc5ai',
        27:'9AGbkl',
        28:'2yWckN',
        29:'zO4frs',
        30:'YmMKFn',
        31:'SG7FWA'}

digest_maker = hmac.new(b''+keys[today].encode(),b'',hashlib.sha256)

with open(document, 'rb') as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()

print(digest)

