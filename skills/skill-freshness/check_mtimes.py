import os, time
now = time.time()
dirs = [('articles', '.md'), ('.outputs', '.md'), ('memory/topics', None), ('memory/state', '.json')]
for d, ext in dirs:
    print('===', d, '===')
    if not os.path.exists(d):
        print('MISSING')
        continue
    for f in sorted(os.listdir(d)):
        if ext and not f.endswith(ext):
            continue
        p = d + '/' + f
        h = (now - os.path.getmtime(p)) / 3600
        print(round(h,1), p)
