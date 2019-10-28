#!/usr/bin/env python
#remove public read right for all keys within a directory

#usage: remove_public.py bucketName folderName

import sys
import boto

# bucketname = sys.argv[1]
# dirname = sys.argv[2]
bucketname = 'e-smartprocess'
dirname = 'api-project'
s3 = boto.connect_s3()
bucket = s3.get_bucket(bucketname)

keys = bucket.list(dirname)
icont = 0
for k in keys:
    # options are 'private', 'public-read'
    # 'public-read-write', 'authenticated-read'
    icont += 1
    print(k)
    k.set_acl('private')
print('Number of Files:')
print(icont)